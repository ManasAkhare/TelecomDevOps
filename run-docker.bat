@echo off
title Launch Telecom Outage Dashboard in Docker
echo ==============================================================================
echo  BUILDING & RUNNING TELECOM OUTAGE DASHBOARD IN DOCKER
echo  Student: Manas Akhare ^| Roll No: 23102C0017 ^| BE CMPN C
echo ==============================================================================
echo.

echo 1. Checking Docker Engine status...
docker info >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Docker Desktop is not running or not in PATH!
    echo Please make sure Docker Desktop is launched and the Docker engine has started.
    pause
    exit /b 1
)

echo 2. Building Multi-Stage Docker Image (telecom/outage-dashboard:1.0.0)...
docker build -f docker/Dockerfile -t telecom/outage-dashboard:1.0.0 -t telecom/outage-dashboard:latest .

echo.
echo 3. Cleaning up any previous container instance...
docker stop telecom-outage-dashboard >nul 2>&1
docker rm telecom-outage-dashboard >nul 2>&1

echo.
echo 4. Running container mapped to port 8085...
docker run -d --name telecom-outage-dashboard -p 8085:8080 telecom/outage-dashboard:1.0.0

echo.
echo ==============================================================================
echo  SUCCESS! Container is running.
echo  Now open DOCKER DESKTOP to show your examiner!
echo  URL: http://localhost:8085/
echo ==============================================================================
pause
