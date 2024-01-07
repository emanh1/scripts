@echo off
setlocal enabledelayedexpansion

set "exiftoolPath="exiftool(-k).exe""
set "targetFolder="

for %%F in ("%targetFolder%\*.jpg" "%targetFolder%\*.jpeg" "%targetFolder%\*.png" "%targetFolder%\*.gif" "%targetFolder%\*.bmp") do (
    echo Removing metadata from: %%F
    "%exiftoolPath%" -all= "%%F"
)

echo Metadata removal completed.
pause
