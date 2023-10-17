# Convenciones para Nombrar Commits

La forma en que nombras tus commits en un repositorio de control de versiones, como Git, es fundamental para mantener un historial de cambios organizado y comprensible. Las convenciones de nomenclatura de commits ayudan a ti y a otros desarrolladores a entender rápidamente el propósito de cada cambio. Aquí te presento algunas convenciones populares para nombrar commits en Git:

## 1. Mensajes Claros y Concisos

Los mensajes de commit deben ser claros y concisos, proporcionando información relevante sobre el cambio. Los mensajes deben responder a la pregunta: "¿Qué hace este commit?".

## 2. Tense Presente y en Imperativo

Usa el tiempo presente y el modo imperativo en tus mensajes de commit. Por ejemplo, en lugar de "Corregí el error en el archivo X," usa "Corrige el error en el archivo X." Esto hace que los mensajes de commit sean más legibles y orientados a la acción.

## 3. Categorías

Algunas convenciones utilizan categorías en el mensaje del commit para clasificar los cambios. Por ejemplo:

- **[feat]**: Para nuevas características o adiciones.
- **[fix]**: Para corrección de errores.
- **[refactor]**: Para mejoras de código que no afectan la funcionalidad.
- **[docs]**: Para cambios en la documentación.
- **[chore]**: Para tareas de mantenimiento, como actualizaciones de dependencias.
- **[style]**: Para cambios en la apariencia y estilo del código, sin cambios funcionales.
- **[test]**: Para adiciones o modificaciones de pruebas.

Por ejemplo:

```
[feat]: Agregar autenticación de usuarios
[fix]: Corregir error en la validación de formularios
[docs]: Actualizar documentación de la API
```

## 4. Prefijo con Número de Issue

Si estás utilizando un sistema de seguimiento de problemas, como GitHub Issues o JIRA, es común prefijar los mensajes de commit con el número de issue correspondiente. Esto vincula el commit con un problema específico y facilita la trazabilidad. Por ejemplo:

```
[Fix #123]: Corregir error en el inicio de sesión
```

## 5. Máxima Longitud de Línea

Es recomendable que la longitud de línea de un mensaje de commit no supere los 72-76 caracteres. Esto asegura que los mensajes sean legibles en la mayoría de las interfaces y herramientas.

## 6. Descripción Detallada (Opcional)

Si es necesario, puedes proporcionar una descripción más detallada en el cuerpo del mensaje de commit. Esto es útil cuando se requiere explicar con más detalle el cambio. A menudo, se separa del título por una línea en blanco.

## Ejemplos de Convenciones de Commits

A continuación, se presentan algunos ejemplos siguiendo las convenciones mencionadas:

```
feat: Agregar función de autenticación
```

```
fix: Corregir error en el cálculo de impuestos

El cálculo de impuestos no se realizaba correctamente para transacciones internacionales.
```

```
refactor: Simplificar el código de la vista de perfil
```

## Conclusión

La elección de una convención para nombrar commits es importante para mantener la coherencia en tu equipo y facilitar la gestión de cambios en un proyecto. Asegúrate de seguir una convención que se adapte a las necesidades de tu equipo y proyecto, y sé consistente en su aplicación.