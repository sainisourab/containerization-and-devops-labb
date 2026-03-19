const express = require('express');
const { Pool } = require('pg');

const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

const pool = new Pool({
  user: process.env.DB_USER || 'admin',
  host: process.env.DB_HOST || 'database',
  database: process.env.DB_NAME || 'project1',
  password: process.env.DB_PASSWORD || 'password',
  port: process.env.DB_PORT || 5432,
});

app.get('/', (req, res) => {
  res.json({ message: 'Welcome to the Backend API. Connectivity looks good!' });
});

// Create data point
app.post('/data', async (req, res) => {
  const { content } = req.body;
  try {
    const result = await pool.query(
      'INSERT INTO AppData(content) VALUES($1) RETURNING *',
      [content || 'Sample Data']
    );
    res.status(201).json(result.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Database error' });
  }
});

// Retrieve data points
app.get('/data', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM AppData');
    res.status(200).json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Database error' });
  }
});

// Test connection endpoint
app.get('/db-status', async (req, res) => {
  try {
    const result = await pool.query('SELECT NOW()');
    res.status(200).json({ status: 'connected', time: result.rows[0].now });
  } catch (err) {
    console.error(err);
    res.status(500).json({ status: 'error', details: err.message });
  }
});

app.listen(port, () => {
  console.log(`Backend API listening on port ${port}`);
});
