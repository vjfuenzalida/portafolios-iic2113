
# Portafolio Semana 4

Autor: Vicente Fuenzalida Marín  
Fecha de Entrega: 1 de septiembre de 2017  
Tema: Principios S.O.L.I.D.

## Explicación de los principios SOLID

El artefacto que escogí esta semana es una [publicación del sitio DZone](https://dzone.com/articles/the-solid-principles-in-real-life) en la que se explica brevemente los principios SOLID, planteados por [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_Cecil_Martin).  
Hablaré de la utilidad que presentan los principios mencionados para el desarrollo de software.  
Se adjunta una [copia](https://github.com/vjfuenzalida/portafolios-iic2113/blob/master/semana4/artefacto_semana_4.pdf) del artefacto en formato PDF en el repositorio de Git.  

En primer lugar, cabe mencionar que los principios SOLID están más bien enfocados en la programación orientada a objetos (OOP), pero que su esencia es válida para el código en general.  

En la publicación que escogí como artefacto, se listan los 5 principios que un programador debiese seguir para producir software limpio y mantenible, y son:

*   *Single responsability*
*   *Open/Closed*
*   *Liskov Substitution*
*   *Interface Segregation*
*   *Dependency Inversion*

A continuación rescato lo que me pareció más explicativo de cada uno:

*   Del principio de Responsabilidad Única se dice que **una clase o módulo debería tener una única razón para cambiar**, es decir, debe estar encargada de una sola cosa, y no aglomerar muchas responsabilidades. El motivo detrás de esto es que al fallar una funcionalidad de dicha clase/módulo, queremos que el resto del software siga funcionando, y si la clase sólo encapsula una función, no perderemos nada adicional (otros métodos, por ejemplo).

*   El principio *Open/Closed* plantea que las entidades de código deben estar abiertas para extensión pero cerradas para modificación, y que **se debe escribir clases que cumplan con lo que deben hacer perfectamente sin asumir que alguien las modificará**. Así, uno debería construir una clase de modo tal que el procedimiento que sigue para proveer una funcionalidad no sea ambiguo y sea independiente del formato del input, al mismo tiempo que permita ser extensible (por medio de herencia, por ejemplo).

*   El principio de Liskov se explica de forma simple, planteando que si hay herencia, **las clases hijas deben responder como la clase padre sin fallar, es decir, deben ser intercambiables**. Así, si hay una funcionalidad de la clase padre que no será usada por la clase hija (o devolverá error), es mejor evitar el uso de herencia.

*   El principio de segregación de la interfaz plantea que **se deben favorecer las interfaces sencillas y específicas para cada cliente, es decir, solo proveer lo que sea necesario**. En la publicación, se da un ejemplo de un menú de un restaurant, en que se señala la *sopa del día* en vez de imprimir todos los días un menú especificando qué sopa hay. En este caso, el objetivo es simplemente señalar el precio, y si algún cliente necesita saber qué sopa hay, puede utilizar la *interfaz* de preguntarle al mesero.

*  Por último, el principio de inversión de dependencias llama a **escribir código que dependa de abstracciones y no de detalles concretos**, y para reconocerlo se puede observar el *input* que recibe un método y pensar en qué tan genérico (abstracto) es. El ejemplo dado es el de las tarjetas de crédito, ya que la máquina que las opera no pregunta si es una Visa u otra, y simplemente pide que se deslice una tarjeta (abstracción de los distintos tipos de tarjeta que puedan haber).  


Dadas estas explicaciones se puede intuir rápidamente hacia dónde apuntan los principios, esto es, hacia clases, métodos y módulos que sean fácilmente extensibles, que funcionen en base a abstracciones y no tipos concretos de datos, y que prevengan el acoplamiento excesivo entre ellos.

Lo que encuentro más útil de estos principios es que no son tan complejos o "rebuscados", sino que son recomendaciones que pueden facilitar el desarrollo de software a largo plazo y generar código más limpio y ordenado favoreciendo así su uso y mantención entre los miembros de un equipo de desarrollado.
Además, son principios que no solo conciernen a la OOP, sino que pueden ser reinterpretados y usados en programación funcional con la misma efectividad.
