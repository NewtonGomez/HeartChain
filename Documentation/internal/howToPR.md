# Cómo hacer un Pull Request en GitHub

Un Pull Request (PR) es una forma común de colaborar en proyectos de código abierto y compartir tus contribuciones con otros desarrolladores. A continuación, se describe el proceso para crear un PR en GitHub, desde el `git add` hasta la solicitud en GitHub.

## 1. Preparar tu entorno de desarrollo

Asegúrate de tener Git instalado y configurado en tu sistema. También necesitas una cuenta en GitHub.

## 2. Clonar el repositorio

Clona el repositorio del proyecto en tu máquina local usando el comando `git clone`:

```bash
git clone <URL_del_repositorio>
```

## 3. Crear una rama

Es importante trabajar en una rama separada para tu contribución. Esto ayuda a mantener la rama principal (generalmente "main" o "master") limpia y estable.

```bash
git checkout -b mi-nueva-funcionalidad
```

## 4. Realizar cambios y hacer `git add`

Haz los cambios necesarios en tus archivos. Una vez que hayas terminado, utiliza `git add` para preparar tus cambios para la confirmación.

```bash
git add <archivos_modificados>
```

## 5. Confirmar los cambios

Confirma tus cambios con un mensaje descriptivo. Esto guarda tus cambios localmente.

Si tienes duda sobre como nombrar tus commits, entra a este [archivo](howtocommit.md)
```bash
git commit -m "Añadida una nueva funcionalidad"
```

## 6. Sincronizar con el repositorio remoto

Antes de crear un PR, asegúrate de que tu rama esté sincronizada con la rama principal del repositorio remoto.

```bash
git fetch origin
git rebase origin/main
```

## 7. Crear el Pull Request

Ve a la página de tu repositorio en GitHub y selecciona la pestaña "Pull Requests." Luego, haz clic en "New Pull Request."

1. Elige la rama que quieres fusionar en el menú desplegable "base branch." Generalmente, esto será la rama principal del proyecto.
2. Selecciona tu rama en el menú desplegable "compare branch."
3. Proporciona un título y una descripción detallada para tu PR.
4. Haz clic en "Create Pull Request."

## 8. Revisar y discutir

Los colaboradores revisarán tu PR y pueden sugerir cambios o hacer preguntas. Asegúrate de estar disponible para responder y hacer las modificaciones necesarias.

## 9. Fusionar el Pull Request

Una vez que tu PR sea aprobado y revisado, un colaborador con permisos apropiados podrá fusionarlo en la rama principal.

## 10. Actualiza tu rama

Después de que tu PR se haya fusionado, es una buena práctica mantener tu rama actualizada.

```bash
git checkout main
git pull origin main
git branch -d mi-nueva-funcionalidad
```

¡Y eso es todo! Has completado con éxito el proceso de crear un Pull Request en GitHub. La colaboración en proyectos de código abierto es una forma valiosa de aprender y contribuir a la comunidad de desarrollo.