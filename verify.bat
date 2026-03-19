@echo off
echo =========================================
echo  Project Assignment 1 Verification Script
echo =========================================
echo.

echo 1. Inspecting Custom IPvlan Network:
echo -----------------------------------------
docker network inspect custom_ipvlan
echo.
pause

echo 2. Displaying Container IPs on 'custom_ipvlan':
echo -----------------------------------------
echo Backend IP:
docker inspect -f "{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" comp_backend
echo Database IP:
docker inspect -f "{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" comp_database
echo.
pause

echo 3. Testing API connectivity and Database persistence:
echo -----------------------------------------
echo  - Fetching initial DB status...
curl -s http://localhost:3000/db-status
echo.
echo  - Inserting dummy data via API...
curl -s -X POST -H "Content-Type: application/json" -d "{\"content\":\"Test Proof Data\"}" http://localhost:3000/data
echo.
echo  - Fetching inserted data...
curl -s http://localhost:3000/data
echo.
echo  - Restarting database container to test volume persistence...
docker-compose restart database
echo  - Waiting 5 seconds for DB to align...
timeout /t 5 /nobreak >nul
echo  - Fetching data again (Should still have the inserted data)...
curl -s http://localhost:3000/data
echo.
pause

echo 4. Showing Multi-Stage Docker Image Size comparison:
echo -----------------------------------------
docker images | findstr "comp_backend"
echo.
echo Verification complete. You can use the terminal output above to grab screenshots for your report.
pause
