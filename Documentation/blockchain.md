# ¿Cómo funciona el blockchain?
* [Funciones Hash](#hash)

<a id="hash"></a>
# Funciones Hash: Conceptos Fundamentales

Las funciones hash son un componente fundamental en el campo de la informática y la seguridad de la información. Se trata de algoritmos matemáticos que toman una entrada (un conjunto de datos) y generan un valor hash único, que es una cadena de caracteres de longitud fija. Estas funciones son ampliamente utilizadas en diversas aplicaciones debido a sus características clave y su versatilidad.

## Propiedades de las Funciones Hash

### **Determinismo**:
Una función hash es determinista, lo que significa que dada la misma entrada, siempre producirá el mismo valor hash. Esta propiedad es crucial para garantizar la consistencia en diversas aplicaciones, como la verificación de integridad de datos.

### **Eficiencia**:
Las funciones hash deben ser eficientes en términos de recursos computacionales. Deben calcular el hash de manera rápida y no consumir una cantidad excesiva de memoria o capacidad de procesamiento.

### **Preimagen Resistente**:
Dado un valor hash, debe ser computacionalmente difícil (prácticamente imposible) encontrar la entrada original que generó ese hash. Esta propiedad es fundamental en aplicaciones de seguridad, como el almacenamiento seguro de contraseñas.

### **Propagación de Cambios**:
Un cambio menor en la entrada debe producir un hash completamente diferente. Esto garantiza que incluso una pequeña alteración en los datos se reflejará en un valor hash completamente distinto.

### **Distribución Uniforme**:
Los valores hash deben distribuirse uniformemente en el espacio de hash. Esto asegura que no haya colisiones frecuentes, es decir, dos entradas diferentes que generen el mismo valor hash.

## Aplicaciones de las Funciones Hash

Las funciones hash se utilizan en una amplia gama de aplicaciones:

1. **Verificación de Integridad**: Son esenciales para verificar si los datos no han sido modificados durante la transmisión o el almacenamiento. Si los datos se alteran, el valor hash asociado cambiará, lo que indica una posible corrupción de datos.

2. **Almacenamiento de Contraseñas**: En lugar de almacenar contraseñas en texto claro, los sistemas almacenan los hashes de las contraseñas. Cuando un usuario ingresa su contraseña, se calcula el hash y se compara con el hash almacenado para la autenticación.

3. **Tablas Hash**: Las funciones hash se utilizan en estructuras de datos como tablas hash para buscar y recuperar datos de manera eficiente, lo que es fundamental en bases de datos y sistemas de búsqueda.

4. **Criptografía**: En la criptografía, las funciones hash se emplean para garantizar la seguridad de las comunicaciones y se utilizan en la creación de firmas digitales y la autenticación de datos.

## Ejemplos de Funciones Hash

Existen varias funciones hash ampliamente utilizadas:

1. **MD5 (Message Digest 5)**: Fue popular en el pasado, pero hoy se considera obsoleto debido a vulnerabilidades conocidas.

2. **SHA-1 (Secure Hash Algorithm 1)**: También se considera obsoleto debido a vulnerabilidades. Su uso no se recomienda en aplicaciones críticas de seguridad.

3. **SHA-256 (Secure Hash Algorithm 256)**: Este es un algoritmo de hash ampliamente utilizado en aplicaciones de seguridad y criptografía. Proporciona una mayor seguridad en comparación con MD5 y SHA-1.

4. **bcrypt**: Aunque no es estrictamente una función hash, se utiliza comúnmente para el almacenamiento seguro de contraseñas. Utiliza técnicas de "salting" para aumentar la seguridad.

## Seguridad y Vulnerabilidades

No todas las funciones hash son igualmente seguras. Algunas pueden ser vulnerables a ataques de fuerza bruta, colisiones y otras técnicas maliciosas. Por lo tanto, es crucial seleccionar una función hash adecuada para la aplicación específica y mantenerse actualizado con las mejores prácticas en seguridad de la información.

En conclusión, las funciones hash son un componente esencial en la informática y la seguridad, brindando un mecanismo eficiente para transformar datos y verificar la integridad. Comprender sus propiedades y aplicaciones es fundamental para utilizarlas de manera efectiva y segura en proyectos y sistemas. La selección adecuada de funciones hash es crucial para garantizar la seguridad y la integridad de los datos en diversas aplicaciones.