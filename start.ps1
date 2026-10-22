# ==============================================================================
# Telecom Service Outage Dashboard Launcher
# Student: Manas Akhare | Roll No: 23102C0017 | BE CMPN C
# ==============================================================================

Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host " TELECOM SERVICE OUTAGE DASHBOARD (NOC PULSE)" -ForegroundColor Yellow
Write-Host " Student: Manas Akhare | Roll No: 23102C0017 | BE CMPN C" -ForegroundColor Green
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host ""

$javaPath = if ($env:JAVA_HOME) { Join-Path $env:JAVA_HOME "bin\java.exe" } else { "java" }

if (!(Test-Path $javaPath)) {
    if (Test-Path "C:\Program Files\Android\Android Studio\jbr\bin\java.exe") {
        $javaPath = "C:\Program Files\Android\Android Studio\jbr\bin\java.exe"
    }
}

$port = 8085
Write-Host "Starting Dashboard on port $port (Jenkins is currently active on port 8080)..." -ForegroundColor Cyan
Write-Host "Opening browser at: http://localhost:$port/" -ForegroundColor Yellow
Write-Host ""

Start-Process "http://localhost:$port/"

& $javaPath -jar target/telecom-service-outage-dashboard.jar --server.port=$port
