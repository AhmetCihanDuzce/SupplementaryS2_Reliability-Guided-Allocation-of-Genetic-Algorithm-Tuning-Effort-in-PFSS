@echo off
set ROOT=%~dp0
set PKG=%ROOT%..
python "%ROOT%scripts\verify_all.py"
if errorlevel 1 exit /b 1
python "%ROOT%scripts\verify_prospective_matrices_exact.py"
if errorlevel 1 exit /b 1
python "%ROOT%scripts\verify_recommended_operational_policy_validation.py" --s2 "%PKG%"
if errorlevel 1 exit /b 1
pause
