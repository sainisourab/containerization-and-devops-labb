@echo off
echo Creating custom IPvlan network (L2 mode) to fulfill assignment requirements...

:: For Docker Desktop environments on Windows (using Hyper-V or WSL 2), 
:: Macvlan and Ipvlan tend to connect to the internal virtual switch.
:: The parent interface is usually 'eth0'. It might need adjustment if using physical adapters.
:: We will create it with a 172.x.y.z subnet for local routing test.

docker network rm custom_ipvlan 2>nul

docker network create -d ipvlan ^
  --subnet=172.25.0.0/16 ^
  --gateway=172.25.0.1 ^
  -o ipvlan_mode=l2 ^
  -o parent=eth0 ^
  custom_ipvlan

echo.
echo Network 'custom_ipvlan' created successfully.
echo You can now run: docker-compose up -d --build
pause
