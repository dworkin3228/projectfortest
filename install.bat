@echo off
rem --Install python
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1


rem --Refresh Environmental Variables
call RefreshEnv.cmd

rem --Use python, pip
py -m ensurepip --upgrade
py -m pip install --upgrade pip
py -m pip install -r requirements.txt

