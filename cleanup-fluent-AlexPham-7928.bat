echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\ANSYSS~1\v232\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\ANSYSS~1\v232\fluent\ntbin\win64\tell.exe" AlexPham 58691 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\ANSYSS~1\v232\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="AlexPham" (%KILL_CMD% 31076) 
if /i "%LOCALHOST%"=="AlexPham" (%KILL_CMD% 7928) 
if /i "%LOCALHOST%"=="AlexPham" (%KILL_CMD% 25800)
del "C:\Users\hieup\Documents\my-repo-gihub\ansys-pyfluent-tutorial\cleanup-fluent-AlexPham-7928.bat"
