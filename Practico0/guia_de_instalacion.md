# Practicos IA

## Guía de instalación

### Instalar Python 3.10

https://www.python.org/downloads/

--> Bruno: Instalé desde Microsoft Store. Para saber donde se encuentra ubicado, ejecutar:

```bash
>>> import os, sys
>>> os.path.dirname(sys.executable)
```

### Instalar Poetry

#### Linux / MacOS

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

#### Windows

```Powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### Configurar poetry para que instale el .venv junto con el proyecto

```bash
poetry config virtualenvs.in-project true
```

--> Bruno: Si poetry no funciona. Verificar en el comando de instalación la ubicación correcta (Actual location) y agregarla al PATH.
--> Bruno: Importante que el PATH donde se ejecuta la consola no tenga espacios. Puede provocar que no se encuentre poetry.