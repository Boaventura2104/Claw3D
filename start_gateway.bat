@echo off
cd /d "%~dp0"
npx openclaw gateway run --bind loopback --port 18789 --verbose
