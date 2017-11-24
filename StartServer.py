import os

os.system("@echo off")
os.system('echo import os > %tmp%\open_localhost.py')
os.system("echo os.system('start http://localhost:8000/') >> %tmp%\open_localhost.py")
os.system("start %tmp%\open_localhost.py")
os.system('python -m http.server 8000')
	