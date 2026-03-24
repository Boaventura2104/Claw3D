$output = @()
$output += "==== PM2 LIST ===="
$pm2_out = pm2 list | Out-String
$output += $pm2_out

$output += "`n==== TAILSCALE STATUS ===="
$tailscale_out = tailscale status | Out-String
$output += $tailscale_out

$output += "`n==== NETSTAT 18789 (OpenClaw) ===="
$netstat_out = netstat -ano | findstr 18789 | Out-String
$output += $netstat_out

$output += "`n==== NETSTAT 3000 (Claw3D) ===="
$netstat_3000_out = netstat -ano | findstr 3000 | Out-String
$output += $netstat_3000_out

$output | Out-File -Encoding utf8 all_statuses.txt
