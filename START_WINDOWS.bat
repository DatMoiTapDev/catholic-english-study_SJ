@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 tools/package_downloads.py
  start "" http://localhost:8000
  py -3 -m http.server 8000 --directory dist --bind 127.0.0.1
) else (
  where python >nul 2>nul
  if errorlevel 1 (
    echo Please install Python 3, then run this file again.
    pause
    exit /b 1
  )
  start "" http://localhost:8000
  python tools/package_downloads.py
  python -m http.server 8000 --directory dist --bind 127.0.0.1
)
pause
