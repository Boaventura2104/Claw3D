$out = ""
try {
    $r1 = Invoke-WebRequest -UseBasicParsing http://127.0.0.1:3000
    $out += "Claw3D (3000): $($r1.StatusCode)`n"
} catch {
    $out += "Claw3D Error: $($_.Exception.Message)`n"
}

try {
    $r2 = Invoke-WebRequest -UseBasicParsing http://127.0.0.1:18789
    $out += "OpenClaw (18789): $($r2.StatusCode)`n"
} catch {
    $out += "OpenClaw Error: $($_.Exception.Message)`n"
}
$out | Out-File -Encoding utf8 test_responses.txt
