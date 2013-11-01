call %~dp0setenv.bat

projectloading_log.txt 2>&1

python projectloading\canvas.py %~dp0data\project.qgs

pause