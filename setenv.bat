@ECHO OFF
set OSGEO4W_ROOT=C:\OSGeo4W
set PATH=%OSGEO4W_ROOT%\bin;%OSGEO4W_ROOT%\apps\qgis-dev\bin;%PATH%
SET PYTHONHOME=%OSGEO4W_ROOT%\apps\Python27
set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis-dev\python
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis-dev\
set QGIS_DEBUG=0
REM set QGIS_LOG_FILE=%~dp0\qgis.log
REM set QGIS_DEBUG_FILE=%~dp0\qgis-debug.log