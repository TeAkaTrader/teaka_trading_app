# Set PostgreSQL credentials
$env:PGPASSWORD = "EVBot-80"
$psqlPath = "C:\Program Files\PostgreSQL\15\bin\psql.exe"  # Adjust if different
$dbName = "teaka_trading"
$dbUser = "postgres"
$sqlFolder = "E:\EV_Files\teaka.trading app\sql_teaka_dashboard"

# Import all SQL files
Get-ChildItem -Path $sqlFolder -Filter *.sql | ForEach-Object {
    Write-Host "`n📥 Importing $($_.Name)..." -ForegroundColor Cyan
    & "$psqlPath" -U $dbUser -d $dbName -f $_.FullName
}
Write-Host "`n✅ All SQL files imported successfully." -ForegroundColor Green
