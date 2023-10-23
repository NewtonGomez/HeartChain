# Clonar un Proyecto de GitHub y Configurar DFINITY Internet Computer (DFX)

A continuación, se describen los pasos para clonar un proyecto de GitHub y configurar DFINITY Internet Computer (DFX) en tu entorno.
## 1. Clonar el Proyecto de GitHub

Primero, asegúrate de tener Git instalado en tu sistema. Si no lo tienes, puedes descargarlo e instalarlo desde [Git](https://git-scm.com/).

Una vez que Git esté instalado, puedes clonar un proyecto de GitHub con el siguiente comando:

```bash
git clone https://github.com/NewtonGomez/HeartChain.git
```

## 2. Instalar DFX

DFX es una herramienta que se utiliza para desarrollar y desplegar aplicaciones en Internet Computer. Para instalar DFX, sigue estos pasos:

### Instalación en Linux y macOS

1. Abre una terminal.

2. Ejecuta el siguiente comando para descargar e instalar DFX utilizando "sh":

```bash
sh -ci "$(curl -fsSL https://sdk.dfinity.org/install.sh)"
```

3. Sigue las instrucciones en la terminal para completar la instalación.

### Instalación en Windows

1. Descarga el archivo ejecutable de DFX desde [DFX Releases](https://github.com/dfinity/dfinity/releases).

2. Ejecuta el archivo descargado y sigue las instrucciones del instalador.

3. Abre una nueva terminal o línea de comandos y verifica la instalación ejecutando:

```bash
dfx --version
```

Si todo se ha configurado correctamente, verás la versión de DFX instalada.

## 3. Configurar el Entorno de Desarrollo

### Instalación de Virtualenv y Flask en un Entorno Virtual

#### Paso 1: Instalación de `virtualenv`

Antes de comenzar, asegúrate de tener Python instalado en tu sistema. `virtualenv` es una herramienta que te permite crear entornos virtuales aislados para tus proyectos. Sigue estos pasos para instalar `virtualenv`:

#### Instalación Global (opcional pero recomendada)

Para instalar `virtualenv` de manera global, ejecuta el siguiente comando:

```bash
pip install virtualenv
```

#### Crear un Entorno Virtual

1. Navega hasta la ubicación de tu proyecto o el directorio donde deseas crear el entorno virtual.

2. Ejecuta el siguiente comando para crear un entorno virtual. Puedes reemplazar `myenv` con el nombre que desees para tu entorno virtual:

```bash
virtualenv myenv
```

3. Activa el entorno virtual con el siguiente comando:

**En Windows:**

```bash
myenv\Scripts\activate
```

**En Linux/macOS:**

```bash
source myenv/bin/activate
```

### Paso 2: Instalación de Flask en el Entorno Virtual

Una vez que has activado el entorno virtual, puedes instalar Flask y cualquier otra dependencia específica de tu proyecto. Ejecuta el siguiente comando para instalar Flask:

```bash
pip install Flask
```

¡Ahora tienes Flask instalado en tu entorno virtual! Puedes comenzar a desarrollar tu aplicación web con Flask sin afectar otros proyectos de Python en tu sistema.

### Paso 3: Desactivar el Entorno Virtual

Cuando hayas terminado de trabajar en tu proyecto y desees desactivar el entorno virtual, simplemente ejecuta el siguiente comando:

```bash
deactivate
```
