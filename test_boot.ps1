Start-Sleep -Seconds 10
try {
    $r = Invoke-WebRequest -UseBasicParsing http://127.0.0.1:18789
    echo "OpenClaw is UP: $($r.StatusCode)" | Out-File boot_status.txt
} catch {
    echo "OpenClaw is DOWN: $($_.Exception.Message)" | Out-File boot_status.txt
}
pm2 logs openclaw-gateway --lines 50 --nostream | Out-File boot_logs.txt
