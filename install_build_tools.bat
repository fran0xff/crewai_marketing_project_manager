@echo off
echo ============================================
echo   Instalador de Visual Studio Build Tools
echo ============================================
echo.
echo Este script instalará Microsoft Visual Studio Build Tools 2022
echo con los componentes necesarios para compilar paquetes de Python
echo que requieren C++ (como chroma-hnswlib).
echo.
pause

echo Instalando Visual Studio Build Tools 2022...
winget install Microsoft.VisualStudio.2022.BuildTools --override "--quiet --wait --add Microsoft.VisualStudio.Workload.VCTools --add Microsoft.VisualStudio.Component.VC.Tools.x86.x64 --add Microsoft.VisualStudio.Component.Windows11SDK.22000"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ Instalación completada exitosamente!
    echo.
    echo Ahora puedes ejecutar:
    echo   uv run python src/content_marketing_project_manager/main.py
    echo.
    echo O usar el comando personalizado:
    echo   uv run --active run_crew
    echo.
) else (
    echo.
    echo ❌ Error durante la instalación.
    echo.
    echo Como alternativa, puedes:
    echo 1. Descargar manualmente Visual Studio Build Tools desde:
    echo    https://visualstudio.microsoft.com/visual-cpp-build-tools/
    echo.
    echo 2. Durante la instalación, asegúrate de seleccionar:
    echo    - Herramientas de compilación de MSVC v143
    echo    - Windows 11 SDK (10.0.22000.0 o superior)
    echo    - CMake tools for Visual Studio
    echo.
    echo 3. Reinicia tu terminal después de la instalación
    echo.
    echo Mientras tanto, puedes usar la versión alternativa:
    echo   python alternative_main.py
    echo.
)

pause
