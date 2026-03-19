from typing import Any

import asyncpg

from .config import settings


class Database:
    def __init__(self) -> None:
        self.pool: asyncpg.Pool | None = None

    async def connect(self) -> None:
        self.pool = await asyncpg.create_pool(
            dsn=settings.database_url,
            min_size=1,
            max_size=10,
        )
        await self.create_tables()

    async def disconnect(self) -> None:
        if self.pool:
            await self.pool.close()
            self.pool = None

    async def create_tables(self) -> None:
        if not self.pool:
            raise RuntimeError("Database pool is not initialized.")

        query = """
        CREATE TABLE IF NOT EXISTS image_records (
            id SERIAL PRIMARY KEY,
            input_source TEXT NOT NULL CHECK (input_source IN ('url', 'base64')),
            image_url TEXT,
            reference_text TEXT,
            analysis JSONB NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );
        """
        async with self.pool.acquire() as connection:
            await connection.execute(query)

    async def insert_record(
        self,
        input_source: str,
        image_url: str | None,
        reference_text: str | None,
        analysis: dict[str, Any],
    ) -> dict[str, Any]:
        if not self.pool:
            raise RuntimeError("Database pool is not initialized.")

        query = """
        INSERT INTO image_records (input_source, image_url, reference_text, analysis)
        VALUES ($1, $2, $3, $4)
        RETURNING id, input_source, image_url, reference_text, analysis, created_at;
        """
        async with self.pool.acquire() as connection:
            row = await connection.fetchrow(
                query,
                input_source,
                image_url,
                reference_text,
                analysis,
            )
        return dict(row) if row else {}

    async def list_records(self, limit: int = 50) -> list[dict[str, Any]]:
        if not self.pool:
            raise RuntimeError("Database pool is not initialized.")

        query = """
        SELECT id, input_source, image_url, reference_text, analysis, created_at
        FROM image_records
        ORDER BY created_at DESC
        LIMIT $1;
        """
        async with self.pool.acquire() as connection:
            rows = await connection.fetch(query, limit)
        return [dict(row) for row in rows]

    async def ping(self) -> bool:
        if not self.pool:
            return False
        async with self.pool.acquire() as connection:
            await connection.fetchval("SELECT 1;")
        return True


db = Database()
