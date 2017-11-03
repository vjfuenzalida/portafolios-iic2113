
# Portafolio Semana 8

Autor: Vicente Fuenzalida Marín  
Fecha de Entrega: 29 de septiembre de 2017  
Tema: Uso de comentarios dentro del código

## Uso de comentarios (en código)

### Artefacto

El artefacto que escogí esta semana es una [entrada de *The Practical Dev*](https://www.quora.com/Do-prestigious-software-companies-regularly-use-UML) donde un desarrollador entrega sus consejos sobre el uso de comentarios como complemento al código escrito.
  
En resumidas cuentas, Andreas Klinger (autor) señala que el objetivo de los comentarios no es explicar *qué* es un determinado fragemento de código, sino *para qué* sirve dicho código.
  
En principio, plante que es responsabilidad del mismo código ser autoexplicativo, es decir, debe poder responder al *qué es* por si solo. La labor de los comentarios es explicar por qué dicho código existe, y por qué realiza una acción (debe explicar lo que no es *obvio*).  

A modo de ejemplo entrega el siguiente extracto:

Mal uso de comentarios: 

```ruby
class Newsletter
  # removes stuff from newsletter
  def remove(stuff)
  …
  end
end
```

Buen uso de comentarios:

```ruby
class Newsletter
  # Note(andreasklinger): In case we run into XYZ we need to remove the user to avoid
  #   problems w/ ABC and DEFG's API. Read more here: https://.....
  def remove(stuff)
  …
  end
end
```
Para utilizar los comentarios correctamente entrega los siguientes consejos:

* Explicar el *por qué* y no el *qué* de un código.

* Dejar por escrito quién escribió el comentario (git blame podría no servir si se edita muchas veces un código)

* Ser minucioso: en este aspecto se hace énfasis, ya que es muy probable que el código que un desarrollador genera pase a manos de otro desarrollador, al menos para ser invervenido un poco. Por lo mismo, llama a ponerse en el lugar del otro, y señala que lo que alguna vez fue obvio para uno, después no lo será para el próximo desarrollador que lo lea, y quizas tampoco para uno mismo (ya que se pierde el contexto en el que se estaba trabajando).

Del último punto, Andreas se extiende señalando información que es útil dejar en los comentarios para preservar un contexto y ayudar a que el código sea más entendible: 

* explicar sin asumir que los demás saben cómo funciona el sistema.
* explicar las particularidades que se deben considerar de los sistemas internos y externos.
* explicar qué partes son código legado.
* explicar cuándo un código legado podrá ser removido.
* explicar interdependencias no explícitas.
* extenderse si se requiere escribir un parrafo más largo.
* pedir que los demás desarrolladores que dejen notas grandes (al igual que uno).

A modo de resumen, aconseja que después de escribir un comentario uno lo vuelva a leer y revise si hay algo que pueda ser removido o resumido/simplificado.

> 	If you can't explain it simply, you don't understand it well enough.   
>  -- Albert Einstein

### Reflexión

