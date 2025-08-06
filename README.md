# Content Marketing Project Manager

Un sistema de gestión de proyectos de marketing de contenido desarrollado con CrewAI que automatiza la planificación, estimación y asignación de recursos para campañas de marketing multi-canal.

## 🚀 Características

- **Planificación Automatizada**: Descompone automáticamente los objetivos del proyecto en tareas específicas
- **Estimación Inteligente**: Calcula tiempo y recursos necesarios para cada tarea
- **Asignación de Recursos**: Distribuye tareas entre miembros del equipo según sus especialidades
- **Calendario de Contenido**: Genera cronogramas detallados con hitos y entregas
- **Exportación a Jupyter**: Crea notebooks interactivos con tablas y visualizaciones

## 📋 Requisitos

- Python 3.12.2
- Microsoft Visual C++ Build Tools 14.0+ (para compilar dependencias nativas)
- uv (gestor de paquetes Python)

## ⚠️ Problema Conocido - Compilación en Windows

CrewAI requiere `chroma-hnswlib` que necesita compilación C++. Si encuentras el error:

```
error: Microsoft Visual C++ 14.0 or greater is required
```

### Solución Rápida
Ejecuta el script de instalación incluido:
```bash
install_build_tools.bat
```

### Solución Manual
1. Instala Visual Studio Build Tools 2022 desde: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Durante la instalación, selecciona:
   - ✅ Herramientas de compilación de MSVC v143
   - ✅ Windows 11 SDK (10.0.22000.0 o superior)
   - ✅ CMake tools for Visual Studio
3. Reinicia tu terminal

### Alternativa Temporal
Mientras tanto, puedes usar la versión alternativa con datos simulados:
```bash
python alternative_main.py
```

## 🛠️ Instalación

1. Clona el repositorio:
```bash
git clone <repository-url>
cd content_marketing_project_manager
```

2. Instala las dependencias:
```bash
uv sync
```

3. Si encuentras problemas de compilación, ejecuta:
```bash
install_build_tools.bat
```

## 🎯 Uso

### Ejecución Principal (CrewAI Real)
```bash
# Usando uv
uv run python src/content_marketing_project_manager/main.py

# O usando el comando personalizado
uv run --active run_crew
```

### Versión Alternativa (Datos Simulados)
```bash
python alternative_main.py
```

### Comandos Adicionales
```bash
# Entrenamiento del modelo
uv run --active train <iterations> <model_name>

# Reproducir ejecución específica
uv run --active replay <task_id>

# Testing
uv run --active test <iterations> <model_name>
```

## 📊 Salida del Sistema

El sistema genera:

1. **Reporte en Terminal**: Muestra tareas, asignaciones, hitos y calendario
2. **Notebook Jupyter** (`crew_output.ipynb`): Contiene tablas interactivas y visualizaciones
3. **Métricas de Uso**: Tokens utilizados y costos estimados

### Ejemplo de Salida

```
--- 📝 Content Tasks ---
- TASK-001: Develop Blog Series Strategy (16h)
- TASK-002: Create Lead Magnet Content (20h)
- TASK-003: Email Nurture Sequence (12h)

--- 👥 Assignments ---
- Sarah Lee: TASK-001, TASK-002 (36h total)
- Mark Johnson: TASK-001, TASK-003 (28h total)

--- 🎯 Milestones ---
- Week 2: Content Strategy Complete
- Week 4: Content Creation Phase 1
- Week 6: Video and Webinar Ready
```

## 🏗️ Estructura del Proyecto

```
content_marketing_project_manager/
├── src/content_marketing_project_manager/
│   ├── main.py              # Punto de entrada principal
│   ├── crew.py              # Definición de agentes y tareas
│   ├── types.py             # Modelos de datos Pydantic
│   └── config/
│       ├── agents.yaml      # Configuración de agentes
│       └── tasks.yaml       # Configuración de tareas
├── alternative_main.py      # Versión alternativa con datos simulados
├── install_build_tools.bat  # Script de instalación de Build Tools
├── crew_output.ipynb        # Notebook generado (después de ejecución)
└── knowledge/
    └── user_preference.txt  # Preferencias del usuario
```

## 🔧 Configuración

### Variables de Entorno
Crea un archivo `.env` con:
```
OPENAI_API_KEY=tu_api_key_aqui
```

### Personalización
- Modifica `config/agents.yaml` para ajustar los agentes
- Edita `config/tasks.yaml` para personalizar las tareas
- Actualiza `knowledge/user_preference.txt` con tus preferencias

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

## 🆘 Soporte

Si encuentras problemas:

1. **Error de compilación**: Ejecuta `install_build_tools.bat`
2. **Problemas con uv**: Asegúrate de tener la versión más reciente
3. **API Key**: Verifica que tu `OPENAI_API_KEY` esté configurada correctamente

Para más ayuda, abre un issue en el repositorio.

---

**Nota**: Este proyecto utiliza CrewAI para la gestión inteligente de proyectos de marketing de contenido. La versión alternativa (`alternative_main.py`) proporciona datos simulados para demonstrar la funcionalidad mientras se resuelven los problemas de compilación.
