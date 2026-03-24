$pm2_path = "C:\Users\alyss\.pm2\logs"
$out_file = "c:\Users\alyss\Documents\claw3d\Claw3D\openclaw_pm2_logs.txt"

if (Test-Path $pm2_path) {
    "=== OUT LOG ===" | Out-File $out_file -Append -Encoding utf8
    $latest_out = Get-ChildItem "$pm2_path\openclaw-gateway-out*.log" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if ($latest_out) {
        Get-Content $latest_out.FullName -Tail 50 | Out-File $out_file -Append -Encoding utf8
    }

    "`n=== ERR LOG ===" | Out-File $out_file -Append -Encoding utf8
    $latest_err = Get-ChildItem "$pm2_path\openclaw-gateway-error*.log" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if ($latest_err) {
        Get-Content $latest_err.FullName -Tail 50 | Out-File $out_file -Append -Encoding utf8
    }
} else {
    "PM2 logs dir not found at $pm2_path" | Out-File $out_file -Encoding utf8
}
