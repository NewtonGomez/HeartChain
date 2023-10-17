# Crear una nueva rama en Git, hacer cambios y enviar un Pull Request

En el desarrollo de software, es una buena práctica trabajar en ramas separadas para implementar nuevas características, correcciones de errores o mejoras en el código. Esto ayuda a mantener un historial de cambios limpio y facilita la colaboración. En este tutorial, aprenderás cómo crear una nueva rama en Git, hacer cambios en ella y enviar un Pull Request para fusionar esos cambios con la rama principal. 

## Paso 1: Crear una nueva rama

Antes de hacer cualquier cambio en el código, debes crear una nueva rama. Puedes hacerlo con el siguiente comando:

```bash
git checkout -b nombre-de-la-rama
```

Reemplaza `nombre-de-la-rama` con un nombre descriptivo que refleje la naturaleza de los cambios que realizarás. Por ejemplo:

```bash
git checkout -b nueva-funcionalidad
```

## Paso 2: Realizar cambios

Ahora que te encuentras en tu nueva rama, puedes hacer los cambios necesarios en el código. Puedes agregar, modificar o eliminar archivos según sea necesario. Una vez que hayas completado tus cambios, asegúrate de hacer commits regulares para registrar tus modificaciones:

Si tienes duda sobre como nombrar tus commits, entra a este [archivo](howtocommit.md)

```bash
git add .
git commit -m "Mensaje descriptivo de los cambios realizados"
```

## Paso 3: Enviar la rama y crear un Pull Request

Una vez que hayas realizado tus cambios en la rama y estés satisfecho con ellos, debes enviar la rama al repositorio remoto y crear un Pull Request. Sigue estos pasos:

1. Primero, asegúrate de que estás en la rama que deseas enviar al repositorio remoto.

```bash
git checkout nombre-de-la-rama
```

2. Luego, envía la rama al repositorio remoto:

```bash
git push origin nombre-de-la-rama
```

3. Finalmente, ve al repositorio en la plataforma en la que trabajas (como GitHub o GitLab) y crea un Pull Request. Proporciona información detallada sobre los cambios que realizaste y por qué son importantes.

4. Los colaboradores revisarán tus cambios y, si son aceptados, fusionarán tu rama con la rama principal.

Recuerda que trabajar en ramas separadas es una buena práctica para mantener un historial de cambios limpio y permitir la colaboración sin interferir con el código en producción. También es importante comunicar claramente tus cambios y por qué son necesarios en el Pull Request.