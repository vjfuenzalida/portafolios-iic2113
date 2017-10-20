# Portafolio Semana 11

Autor: Vicente Fuenzalida Marín  
Fecha de Entrega: 20 de octubre de 2017  
Tema: Buenas prácticas para escribir código

## Coding Best Practices

### Artefacto

El artefacto que escogí esta semana es una [entrada](https://dev.to/mohitrajput987/importance-of-writing-clean-code) del sitio [The Practical Dev](dev.to) donde se comenta sobre la importancia de escribir *código limpio*.

#### Las ventajas que se mencionan son las siguientes:

1. *Tu código es tu responsabilidad*: Si no hay preocupación por la calidad del código, más adelante será difícil para uno mismo poder comprender qué hace éste o por qué se realiza determinada instrucción.

2. *Trabajas con un equipo*: Hay que considerar que otros leerán y/o modificarán el código escrito por uno. Se puede perder mucho tiempo en resolver conflictos y comprender la lógica detrás de un código si este no está bien estructurado.

3. *Fácil de mantener y extender*: Muchas veces los clientes piden incoorporar nuevas propiedades/funcionalidades a un proyecto, y esta tarea se vuelve muy complicada si por ejemplo, el código está muy acoplado. Seguir patrones facilita la posterior intervención al código.

4. *Debugging más fácil*: Cuando surge un problema/error en una feature determinada, si se tienen clases/métodos separados, resulta mucho más fácil hacer *logging* paso a paso para encontrar el problema exácto (si el código está muy acoplado se hace difícil localizar dichos errores).

5. *No eres el dueño del producto*: El código fuente resultante de un proyecto se paga, y el cliente (u otro tercero) debería ser capaz de modificarlo posteriormente con facilidad.

#### Las buenas prácticas que se mencionan son:

*   Convenciones de nombres: Nombres claros y estandarizados (variables, clases y funciones cada una con su convención para diferenciarlas), y que sean sencillos de entender a la primera lectura (tanto su función como su tipo).

*   Modularización: Escribir código reusable, en un solo lugar (evitar repeticiones), y que se pueda reutilizar dentro de todo el programa. Esto minimiza la posibilidad de errores, permite extensión y ahorra líneas de código.

*   *Crear un mapa de la casa*: Previo a escribir código, realizar diagramas Entidad-Relación, de Casos de Uso, etc. para tener claridad de la estructura que deberá seguir el código.

*   *Keep it Simple and Small*: Preocuparse de que cada sección de código tenga una única responsabilidad. Ej: la función `getSalary()` sólo debería calcular un salario, **nada más**.

*   Elegir las herramientas adecuadas: Esto es en relación a los IDEs utilizados y herramientas que facilitan la escritura y revisión del código, manejo de directorios y otras funcionalidades (debugging, compilación, linters, etc).

*   *Ser el mejor artista*: Buscar cada día escribir código más limpio, elegante, y conciso. Encontrar motivación en generar un producto de calidad.

### Reflexión



