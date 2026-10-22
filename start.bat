@echo off
title Telecom Service Outage Dashboard - Manas Akhare (23102C0017)
echo ==============================================================================
echo  TELECOM SERVICE OUTAGE DASHBOARD (NOC PULSE)
echo  Student: Manas Akhare ^| Roll No: 23102C0017 ^| BE CMPN C
echo ==============================================================================
echo.

if not "%JAVA_HOME%"=="" (
    set "JAVA_EXE=%JAVA_HOME%\bin\java.exe"
) else (
    set "JAVA_EXE=java"
)

if not exist "%JAVA_EXE%" (
    if exist "C:\Program Files\Android\Android Studio\jbr\bin\java.exe" (
        set "JAVA_EXE=C:\Program Files\Android\Android Studio\jbr\bin\java.exe"
    )
)

echo Starting application on port 8085 (to avoid conflict with Jenkins on 8080)...
echo Dashboard URL: http://localhost:8085/
echo.

"%JAVA_EXE%" -jar target\telecom-service-outage-dashboard.jar --server.port=8085

pause
