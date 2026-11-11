@echo off
cd /d "%~dp0"

echo Starting NEXORA PHP app on http://localhost:8000...
start "NEXORA PHP" "C:\xampp\php\php.exe" -S localhost:8000

rem Give the PHP server a moment to start
ping -n 3 127.0.0.1 > nul

echo Starting HTTPS proxy on https://localhost:8443...
npx --yes local-ssl-proxy -s 8443 -t 8000
