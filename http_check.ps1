try {
    $res = Invoke-WebRequest -UseBasicParsing http://localhost:3000
    echo "Claw3D: $($res.StatusCode)"
} catch {
    echo "Claw3D Error: $_"
}

try {
    $res = Invoke-WebRequest -UseBasicParsing http://localhost:18789
    echo "OpenClaw: $($res.StatusCode)"
} catch {
    echo "OpenClaw Error: $_"
}
