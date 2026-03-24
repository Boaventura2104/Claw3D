$pm2_path = "C:\Users\alyss\.pm2\logs"
if (Test-Path $pm2_path) {
    echo "Logs Dir Exists"
    Get-ChildItem $pm2_path | Out-File logs_list.txt
    # Read the latest logs for openclaw-gateway
    $latest_out = Get-ChildItem "$pm2_path\openclaw-gateway-out*.log" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    $latest_err = Get-ChildItem "$pm2_path\openclaw-gateway-error*.log" | Sort-Object LastWriteTime -Descending | Select-Object -First 1

    if ($latest_out) {
        echo "=== OUT LOG ===" | Out-File openclaw_pm2_logs.txt -Append
        Get-Content $latest_out.FullName -Tail 50 | Out-File openclaw_pm2_logs.txt -Append
    }
    if ($latest_err) {
        echo "`n=== ERR LOG ===" | Out-File openclaw_pm2_logs.txt -Append
        Get-Content $latest_err.FullName -Tail 50 | Out-File openclaw_pm2_logs.txt -Append
    }
} else {
    echo "PM2 logs dir not found at $pm2_path" | Out-File openclaw_pm2_logs.txt
}
