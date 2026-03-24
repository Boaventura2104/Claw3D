module.exports = {
  apps: [
    {
      name: "claw3d",
      script: "cmd.exe",
      args: "/c npm run dev",
      cwd: __dirname,
      windowsHide: true,
    },
    {
      name: "openclaw-gateway",
      script: "cmd.exe",
      args: "/c npx -y openclaw gateway run --bind loopback --port 18789 --verbose",
      cwd: __dirname,
      windowsHide: true,
    }
  ]
};
