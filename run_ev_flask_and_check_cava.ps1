# === CONFIG ===
$flaskPath = "E:\EchoVault\FlaskLaunchers\ev_flask_server_fixed-launcher.ps1"
$cavaLogPath = "E:\EV_Files\Logs\cava_loop_manifest_patch.json"
$loopManifest = "E:\EV_Files\Logs\loop_manifest.json"
$port = 5050
$url = "http://localhost:$port"

# === 1. Launch Flask Server ===
if (Test-Path $flaskPath) {
    Write-Host "🚀 Launching EV Flask UI..." -ForegroundColor Cyan
    Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -File `"$flaskPath`"" -WindowStyle Hidden
    Start-Sleep -Seconds 5
} else {
    Write-Host "❌ Launcher not found: $flaskPath" -ForegroundColor Red
    exit
}

# === 2. Check if Flask is Live ===
try {
    $response = Invoke-WebRequest -Uri "$url/status?key=forgekeeper" -TimeoutSec 3
    if ($response.StatusCode -eq 200) {
        Write-Host "✅ Flask server is LIVE on port $port." -ForegroundColor Green
    } else {
        Write-Host "⚠️ Flask server returned unexpected response." -ForegroundColor Yellow
    }
} catch {
    Write-Host "❌ Flask server not responding on port $port." -ForegroundColor Red
}

# === 3. Load CAVA + EVBC Manifest Info ===
if (Test-Path $loopManifest) {
    Write-Host "`n🧠 CAVA Registered Loop Entries:" -ForegroundColor Magenta
    (Get-Content $loopManifest -Raw | ConvertFrom-Json) | ForEach-Object {
        Write-Host " - Loop: $($_.loop_id) | Source: $($_.source) | Status: $($_.status)"
    }
} else {
    Write-Host "⚠️ loop_manifest.json not found." -ForegroundColor Yellow
}

if (Test-Path $cavaLogPath) {
    Write-Host "`n📓 CAVA Patch Log Entries:" -ForegroundColor DarkCyan
    Get-Content $cavaLogPath
} else {
    Write-Host "⚠️ cava_loop_manifest_patch.json not found." -ForegroundColor Yellow
}
