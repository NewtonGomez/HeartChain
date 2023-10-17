# Proceso de Creación de Documentación: Crear una Rama y Enviar un Pull Request en GitHub

Cuando se trata de escribir nueva documentación para un proyecto alojado en GitHub, es importante seguir un proceso que permita una colaboración efectiva y un control de versiones adecuado. En este documento, te explicaremos cómo crear una rama y enviar un Pull Request (PR) para contribuir con nueva documentación en GitHub.

## Paso 1: Clonar el Repositorio

Antes de comenzar, asegúrate de tener una copia del repositorio en tu máquina local. Puedes clonar el repositorio utilizando el siguiente comando:

```bash
git clone https://github.com/nombre-usuario/nombre-repositorio.git
```

Reemplaza `nombre-usuario` con el nombre de usuario del propietario del repositorio y `nombre-repositorio` con el nombre del repositorio.

## Paso 2: Crear una Rama Nueva

Es importante que todos los cambios en la documentación se realicen en una rama separada. Esto ayuda a mantener un historial de cambios limpio y evita conflictos con la rama principal. Crea una nueva rama con un nombre descriptivo utilizando el siguiente comando:

```bash
git checkout -b nombre-de-la-rama-documentacion
```

Sustituye `nombre-de-la-rama-documentacion` con un nombre que describa claramente el propósito de la rama.

## Paso 3: Escribir y Editar la Documentación

Ahora puedes crear o editar la documentación en tu rama. Utiliza un editor de texto o una herramienta de edición de documentos según las preferencias y necesidades del proyecto.

## Paso 4: Hacer Commits

Realiza commits periódicos a medida que avances en la creación de la documentación. Utiliza los siguientes comandos para hacer commits:

Si tienes duda sobre como nombrar tus commits, entra a este [archivo](howtocommit.md)

```bash
git add nombre-del-archivo-modificado
git commit -m "Descripción del cambio realizado"
```

Reemplaza `nombre-del-archivo-modificado` con el nombre del archivo que modificaste y proporciona una descripción clara del cambio realizado en el mensaje del commit.

## Paso 5: Enviar la Rama al Repositorio Remoto

Una vez que hayas completado la documentación y realizado los commits necesarios, envía la rama al repositorio remoto en GitHub:

```bash
git push origin nombre-de-la-rama-documentacion
```

## Paso 6: Crear un Pull Request

Dirígete a la página del repositorio en GitHub y selecciona la rama que creaste. A continuación, haz clic en el botón "New Pull Request". Proporciona información detallada sobre los cambios realizados en la documentación y por qué son necesarios. Asigna revisores si es necesario.

## Paso 7: Revisión y Fusión

Los colaboradores del proyecto revisarán tu Pull Request y, si los cambios son aceptados, se fusionarán con la rama principal. Asegúrate de estar disponible para responder a cualquier comentario o pregunta que los revisores puedan tener.

Siguiendo este proceso, podrás contribuir de manera efectiva a la documentación de proyectos en GitHub, manteniendo un flujo de trabajo organizado y facilitando la colaboración con otros desarrolladores.