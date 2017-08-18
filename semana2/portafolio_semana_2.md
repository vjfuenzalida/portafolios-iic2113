Portafolio Semana 2
===================

Autor: Vicente Fuenzalida Marín  
Fecha de Entrega: 18 de agosto de 2017  
Tema: Principios Fundamentales de Diseño de Software

*Code Smells* en el desarrollo de software
-----

El artefacto que escogí esta semana, es un breve [artículo](https://8thlight.com/blog/georgina-mcfadyen/2017/01/19/common-code-smells.html) donde se habla acerca del *code smell* como síntoma de código con potencialidad de contener problemas.  
Se adjunta una [copia]() en formato PDF en el repositorio.

### Artefacto
Escogí este artefacto debido a que no me quedó muy claro a qué se refería el término *code smell*, y si era o no distinto a los llamados *anti-patrones* mencionados también en clases.  

Un [anti-patrón](https://en.wikipedia.org/wiki/Anti-pattern) consiste en un patrón que lleva a desarrollar **malas soluciones** para resolver prolemas, o dicho de forma más sencilla, son 'malas ideas'.  
Por otra parte, el *code smell* hace referencia a un **síntoma** en el código fuente de un software, que posiblemente señala un problema más complejo. Son estructuras que pueden estar violando los *principios fundamentales de diseño de software* (abstracción, ocultamiento, cohesión y acoplamiento). En [StackExchange](https://softwareengineering.stackexchange.com/questions/350085/what-is-the-difference-between-code-smells-and-anti-patterns) se puede encontrar un comentario similar con las diferencias entre ambos términos.  

En el artículo observado se mencionan varios *code smells* como por ejemplo: 
  * *long methods* (demasiadas responsabilidades y difíciles de mantener).
  * *refuse bequests* (herencia de clases con poca/nula utilización de los métodos de la superclase).
  * *data clumps* (muchos métodos utilizan los mismos parámetros).
  * *duplicate code*
  * *middle man* (clases intermedias que solo sirven para delegar a otra).
  * *primitive obsession* (usar tipos primitivos para valores que pueden tener un significado más complejo).
  * *comments* (comentarios no actualizados o que no aportan información para los desarrolladores).

### Reflexión

A partir de la información que entrega el artículo se puede ver la utilidad que brinda conocer estos *smells* y saber identificarlos, ya que permiten ahorrarse muchos problemas al mismo tiempo que hacen el código mantenible y legible por otros desarrolladores.

Lo interesante de los *code smells* es que están directamente relacionados a los *principios de diseño de software*, y si estos principios se aplican al desarrollo del software, permiten **prevenir** y/o **mitigar** los errores detectados mediante *code smells*.

Me parece particularmente útil estar al tanto de la "lista completa" de *code smells*, ya que resumen el aprendizaje de otros programadores y de este modo se puede evitar una equivocación innecesaria.
