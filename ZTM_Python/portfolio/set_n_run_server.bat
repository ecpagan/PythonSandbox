start /b /wait python -m venv venv
start /b /wait .\venv\Scripts\pip.exe install Flask
start .\venv\Scripts\activate.bat

set FLASK_APP=server.py
set FLASK_DEBUG=1
start /b .\venv\Scripts\flask.exe run
brave "http://127.0.0.1:5000"
pause
