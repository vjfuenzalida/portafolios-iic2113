# Resumen Midterm - Diseño Detallado de Software

## Patrones de Diseño

### Creacionales

#### 1. Abstract Factory

> Contexto: Crear objetos pertenecientes a una misma familia.  
> Provee una interfaz que delega las invocaciones de creación a una o más clases concretas para así retornar objetos específicos.  
Se compone de una factory abstracta (factory OS, provee métodos como crear botón, crear ventana), factories concretas (factory de productos Windows y Linux), productos abstractos (botones, ventanas, etc) y productos concretos (botón windows, ventana linux, etc).

#### 2. Constructor/Builder

> Permite la creación dinámica de objetos basada en algoritmos fácilmente intercambiables.
> Director (usa un builder concreto con la interfaz del abstracto, construye productos), builder abstracto (provee interfaz común para builders), builders concretos (provee métodos del abstracto con valores específicos) y producto (objeto creado por constructor, dependiente de los parámetros del builder usado).  
> Ejemplo: Cocina (director) utiliza un Builder de pizzas hawaianas (builder concreto) mediante la interfaz de un builder de pizzas (builder abstracto) para construir una pizza (producto). La cocina puede tener un método `construir pizza` que use la interfaz del builder (crear pizza, build masa, build salsa, etc) para efectivamente construir y retornar el objeto.

#### 3. Factory Method

> Clase expone un método para crear objetos, permitiendo que subclases controlen el proceso de creación real.  
> Las subclases utilizan el método de creación que quieran.  
> Ejemplo: Clase Tablero (abstracta) con método CrearPieza (factory method). Pueden existir subclases concretas TableroAjedrez y TableroDamas, donde cada una tiene su propia función concreta CrearPieza (CrearPiezaAjedrez, CrearPiezaDamas).

#### 4. Prototype	

> Permite crear objetos basado en un template (prototipo) de objetos existentes mediante clonación.  
> La interfaz abstracta de una clase (prototipo abstracto) declara una operación para clonarse a si misma. El prototipo concreto implementa la operación de clonarse a sí mismo.  
> Permite mantener el estado del objeto y no quedar con los defaults impuestos al crear un nuevo objeto (como método new).


#### 5. Singleton

> Asegura que solo una instancia de una clase sea permitida en un sistema.
> La clase es responsable de la creación e inicialización (lo hace una sola vez, luego retorna la misma instancia siempre).
Ejemplo: se puede aplicar en una *factory* que genera objetos, para que ésta sea única.

### Estructurales

#### 1. Adaptador
> Convertir la interfaz de una clase en otra interfaz, que es la que los clientes esperan. Permite que distintas clases/módulos trabajen juntos cuando por si solos no podrían (interfaces incompatibles).
> Se compone de una interfaz (lo que el cliente ve/usa), el adaptador concreto o wrapper (mapea la operación de la interfaz a la del componente adaptado) y el componente adaptado (realiza su propia operación, llamada desde el adaptador).

#### 2. Bridge
> Desacoplar una abstracción de su implementación de modo que ambas puedan variar independientemente (que sean extensibles mediante subclases).  
> Ejemplo: Thread Scheduler (abstracta) que puede ser de tipo Preemptive y TimeSliced, y puede estar implementado en distintas plataformas (Windows y Linux). Para **evitar armar todas las combinaciones**, se separa la abstracción de ThreadScheduler y de Plataforma, de modo que ambas puedan ser extendidas independientemente (por ejemplo si aparece un nuevo tipo de scheduler u otra plataforma). Finalmente, cuando se instancie un thread scheduler concreto, se le  *pasa* una plataforma para que opere (con una interfaz común).

#### 3. Composite
> Componer objetos en estructuras de árbol para representar sus **jerarquías**. Permite que los clientes traten a los objetos individuales ("primitivos") y a composiciones de objetos de la misma forma.  
> Se define una **clase común "Componente"**, que especifica el comportamiento uniforme que tendrán todos los objetos primitivos y compuestos. En general también se añaden métodos para manejar a los "hijos" de un objeto compuesto (en los objetos primitivos no se implementan estos métodos).
> Ejemplo: Un directorio contiene entradas, y cada entrada puede ser a su vez un directorio. Contenedores que contienen elementos, que a su vez puede ser contenedores.

#### 4. Decorador
> Añadir responsabilidades adicionales a un objeto dinámicamente (individualmente, no a su clase completa). Proveen una alternativa flexible a las subclases, que permite extender funcionalidad.  
> Funciona 'encadenando' características nuevas para producir un objeto personalizado. Se envuelve al objeto en un wrapper que provee la misma interfaz del objeto (*mínimo común denominador* de todos los objetos de la clase) y añade alguna nueva característica.
> Ejemplo: interfaz LCD provee método `draw`, y utiliza una clase Window que provee el mismo método. A su vez, utiliza un wrapper/decorador que *envuelve* a un objeto Window, también provee el método `draw`, y además le añade una característica nueva (borde, sidebar, etc). Así, una Window envuelta en cualquier wrapper también responderá a la interfaz de LCD, pero puede tener características específicas.

#### 5. Fachada
> Provee una interfaz unificada para un set de interfaces en un subsistema. La fachada define una interfaz de alto nivel que hace a un subsistema más fácil de usar. *Envuelve* a un subsistema en una **interfaz más simple**.
> Ejemplo: Se tienen componentes de un computador (complejos): CPU, RAM y Disco Duro. Se puede crear una interfaz llamada Computador que provea un método `start` (prender el computador), y que internamente ésta realice las acciones complejas de cada componente.

#### 6. Flyweight
> Facilita el reuso de muchos objetos livianos, haciendo que el uso de grandes cantidades de estos sea más eficiente.  
> Estos objetos se componen de un estado intrínseco y uno extrínseco (dependen de un cliente externo que les provee un estado). Deben ser instanciados desde una *Factory*, que se encarga de cachear o reusar instancias existentes.  
> Ejemplo: los browsers, para evitar cargar una imagen varias veces la guardan en una caché interna. Cuando se requiere ubicar un objeto en la vista, se crea un objeto flyweight que posee datos propios como su posición, pero el resto de los datos se referencian de una versión cacheada.

#### 7. Proxy
> Permite regular el control de acceso de objetos funcionando como una entidad intermediaria (proxy, sustituto). Provee un nivel de indirección extra para proteger o controlar el acceso a un objeto. Existen proxys: virtuales (reemplaza al objeto real hasta que se requiere acceder o usar el mismo -> es muy *caro* tener instanciado el objeto desde antes), remotos (representación local de un objeto que se encuentra en otro lugar), y de protección (controla acceso al objeto, revisa permisos, etc).
> Ejemplo: un cheque es un proxy para reemplazar los fondos de una cuenta (controla acceso al efectivo en la cuenta).

### De Comportamiento

#### 1. Cadena de Responsabilidades
> Evita acoplamiento del emisor de una request con su receptor dando la oportunidad a más de un objeto para encargarse de la request. Encadena los objetos receptores y pasa la request a lo largo de la cadena hasta que uno de los objetos la procese (debería haber un control para capturar requests no manejadas). 

#### 2. Comando
> Encapsula una request permitiendo que sea tratada como un objeto. Esto permite que la request sea manejada mediante relaciones tradicionales de objetos como queuing y callbacks.  
> Desacopla el objeto que invoca la operación (comando) del que sabe cómo ejecutarla (receptor). La clase base contiene un método `execute()` que simplemente llama a la acción en el objeto receptor. Los usuarios de objetos *comando* tratan a cada objeto como una *caja negra* y sólo invocan al método `execute()` cuando requieren el servicio del objeto.
> Se crea un comando concreto que implementa el método `execute()` y está conectado a un receptor que ejecuta la acción. Luego, cuando un invocador toma el comando, puede utilizar la interfaz `execute()` para que se realice la acción.

#### 3. Intérprete
> Dado un lenguaje, define una representación para su *gramática* junto a un intérprete que usa la representación para interpretar frases en ese lenguaje.
Ejemplo: parser de operaciones aritméticas ("1 + 2 + 3 - 4").
> Se mapea cada símbolo (terminal o no-terminal) de la gramática a una clase y se organizan mediante el patrón Composite. Finalmente se itera sobre los elementos del input, avanzando y almacenando el nuevo estado a medida que se va formando el output.

#### 4. Iterador
> Provee una forma secuencial de acceder a elementos de un objeto agregado, sin exponer cómo están almacenados internamente (representación interna).
> Ejemplo: Control remoto para cambiar canales de TV. 

#### 5. Mediador
> Define un objeto que encapsula cómo un set de otros objetos interactúan. Promueve el acoplamiento débil al quitar las referencias directas a objetos (pasan por el mediador).  
> Actúa como un Hub de comunicación, y es responsable de controlar y coordinar las interacciones de sus clientes (Observación: no es un objeto controlador/*dios*).  
> Ejemplo: Torre de control en aeropuerto. Los aviones no se comunican entre ellos, toda comunicación es mediada por la torre (definir quién despega y quién aterriza). 

#### 6. Memento
> Capturar y externalizar el estado interno de un objeto (sin violar encapsulación) para que pueda ser retornado a ese estado en otro momento.  
> El patrón se compone de 3 roles: el Originador (objeto que sabe guardar su estado), el *Caretaker* (objeto que sabe por qué y cuándo el Originador necesitará guardar y restaurar su estado), y el Memento (objeto cerrado escrito y leído por el Originador, almacenado por el *Caretaker*).

#### 7. Estado
> Permite a un objeto alterar su comportamiento cuando su estado interno cambia. Parecerá que el objeto cambió su clase. Los estados por lo general son singletons.  
> Se crea una máquina de estados, que actúa como wrapper, provee una interfaz (genérica, que será sobreescrita por los estados) y contiene al estado actual.  
> Existe una clase base Estado, que implementa todos los métodos de la interfaz del wrapper y recibe al wrapper como parámetro. Los estados derivados de Estado, sobreescriben solo los métodos que necesitan (dependiendo de cada estado). Todas las llamadas a la interfaz del wrapper se delegan al estado actual que éste mantenga y al ejecutarse, el estado es el encargado de cambiar el estado actual de la máquina por el siguiente que corresponda.  

#### 8. Estrategia
>  Define una **familia de algoritmos**, encapsula cada uno, y los hace **intercambiables** (deben cumplir la misma interfaz pero se comportan distinto). Permite que el algoritmo cambie en tiempo de ejecución independientemente de quien lo usa.  
> Captura la abstracción en una interfaz, y esconde la implementación en clases derivadas (algoritmos/estrategias).
> Se compone de abstracción que provee una interfaz general (por ejemplo un método `doSomething()`), y esta abstracción (Strategy) puede escoger entre distintos algoritmos según el contexto (que también implementan `doSomething()`).  
> Ejemplo: Sistema de cobro en un bar: se define la clase abstracta BillingStrategy que declara el método `getPrice()`, y las estrategias concretas NormalStrategy y HappyHourStrategy, que implementan el método getPrice distinto (happy hour calcula a mitad de precio). Luego, el programa principal escoge entre usar NormalStrategy y HappyHourStrategy según la hora del día.


#### 9. Template Method
> Define el esqueleto de un algoritmo en una operación, y aplaza la definición de algunos pasos a las subclases del cliente. Permite que las subclases redefinan ciertos pasos de un algoritmo sin cambiar la estructura del mismo (es un *molde*).  
> Se define qué pasos de un algoritmo son invariantes y estos se implementan en una clase base abstracta. Los pasos customizables (variantes) pueden ser dejados con una implementación por defecto, o sin implementación. Las clases concretas derivadas pueden proveer dichos pasos o modificar los existentes, pero sin cambiar el orden ni los pasos requeridos (fijado por la clase base).  
> Ejemplo: Trabajador (clase abstracta) tiene una rutina diaria (despertarse, desayuno, trabajar, volver a casa y dormir), y sus subclases concretas sobreescriben el método `trabajar()` dependiendo del caso (constructor, cartero, etc).  
> Nota: Se parece a Strategy pero difieren en su granularidad (strategy pasa algoritmos completos mediante delegación, y template method usa herencia para variar una parte de un algoritmo).

#### 10. Visitor
> Representa una operación a ser realizada sobre los elementos de una estructura de objeto. El Visitor permite definir una nueva operación sin cambiar las clases de los elementos sobre los que opera.  
> Se definen objetos que hereden de la clase Element, que declara el método `accept()`. Cada subclase ("visitable") debe definir `accept()` que reciba como parámetro a un Visitante genérico e invoque su método `visit()` pasándole como parámetro el Element mismo. Cuando el Visitante ejecuta el método `visit()`, elegirá la implementación adecuada según el tipo/clase del Element entregado, y realizará una operación utilizando al objeto.  
> Resumen: Visitable acepta a visitante, y visitante visita a visitable (opera sobre él). Son dos dispatches.
 
#### 11. Observador
>  Define una dependencia one-to-many entre objetos para que cuando un objeto cambie de estado, todos sus dependientes sean notificados y actualizados automáticamente.  
>  Se define un objeto Subject que 'posee' el modelo de datos y/o la lógica de negocios. Delega otras funciones (como vista o representación de los datos) a objetos Observadores que se registran al Subject. Cuando el Subject cambia, transmite a todos sus observadores avisando que ha cambiado, para que estos pidan el nuevo estado del Subject o parte de él.  
>  Si el protocolo de interacción es *pull*, el Subject debe tener un método para registrar/remover Observadores (`attach()`/`detach()`), un método `getState()` para consultar su estado, y otro método `setState()` que llamará al método `update()` de cada Observador suscrito (que a su vez usa `getState()` del Subject)

## Principios de Diseño

### 1. Abstracción

#### Concepto:
> Abstracción es el proceso de extraer o remover características de algo, con el fin de reducirlo a un conjunto de características esenciales.

#### Principio:
> La interfaz de un componente debería ser independiente de su implementación.

#### Recomendación:
> Cada pieza significativa de funcionalidad en un programa debería ser implementada en un solo lugar dentro del código. Cuando hay funciones similares en distintas partes del código, generalmente es beneicioso combinarlas en una función, abstrayendo las partes que varían.  

> Las decisiones de diseño susceptibles de cambio deben ocultarse detrás de interfaces abstractas.


### 2. Ocultamiento

#### Concepto:
> Ocultamiento (de información) hace referencia a la habilidad para prevenir que ciertos aspectos de una clase o componente de software sean accesibles por sus usuarios.  

> *The basic idea is that if code chunk A doesn't really need to know something about how code chunk B (which it calls) does its job, don't make it know it. 
Then, when that part of B changes, you don't have to go back and change A.*

#### Principio (basado en definición de David Parnas):
> Cada Módulo se caracteriza por su conocimiento sobre una decisión de diseño, la cual oculta de los demás módulos. Su interfaz o definición se elige de modo tal que revele lo menos posible acerca de su funcionamiento interno.

#### Recomendación:
> La idea es que al diseñar la solución a un problema, se busquen las decisiones de diseño más propensas a cambiar en el tiempo. Cada módulo se debe diseñar de forma que oculte una de estas decisiones de los demás módulos.

> Se puede lograr utilizando features propias de los lenguajes de programación (ej: variables privadas) o normas explícitas de exportación.  

> Ejemplos: encapsulamiento (técnica que aplica principio des ocultamiento), patrón Bridge (desacoplar una abstracción de su implementación), interfaces para clases.

### 3. Acoplamiento

#### Concepto:
> Es el grado de interdependencia entre dos módulos de software. Es una medida de qué tan conectadas (relacionadas) están dos rutinas/clases/módulos/componentes.

#### Tipos (de mayor a menor):  
> *  de Contenido: un módulo modifica o **se apoya en el funcionamiento interno de otro módulo** (cambiar el funcionamiento del segundo módulo implica cambiar el primero).  

> *  Común: dos módulos comparten las mismos **datos globales** (cambiar el recurso compartido implica cambiar todos los módulos que lo usen).

> *  Externo: dos módulos comparten un formato de datos impuesto externamente, protocolo de comunicación, o **interfaz de dispositivo** (relacionado con la comunicación a **herramientas externas** y dispositivos).

> *  de Control: un módulo **controla el flujo de otro**, mediante el paso de información sobre lo que debe hacer (**flags**).

> *  Sellado: módulos **comparten una estructura** de datos compuesta y **usan solo una parte** de ella (por ejemplo, pasando un registro completo a una función que solo necesita un cambio de dicho registro).

> *  de Datos: módulos **comparten datos** entre ellos (por ejemplo, **parámetros**). Cada dato es una pieza elemental y dicho parámetro es la única data compartida (por ejemplo, pasar un entero a una función que calcula una raíz cuadrada).

> *  de Mensajes: la comunicación entre componentes se realiza mediante parámetros o **paso de mensajes**. El **receptor selecciona e invoca al método adecuado** al recibir el mensaje.

#### Principio:
>Un módulo debería depender de la menor cantidad posible de módulos (**bajo acoplamiento**).

#### Ventajas:

> El bajo acoplamiento **mejora la comprensibilidad** aislada de cada componente (sin necesidad del contexto), **reduce el costo de realizar cambios** (se necesita poco conocimiento del contexto) y **mejora el reuso de componentes** (menos dependencias, más fáciles de adaptar a nuevos contextos).

### 4. Cohesión

#### Concepto:
> El grado en que los elementos de un módulo permanecen juntos. Mide de la fuerza de la relación entre las piezas de funcionalidad dentro de un módulo dado. 

#### Tipos (de menor a mayor):  

> *  Coincidental: las partes de un módulo están **agrupadas arbitrariamente**. Su única relación es que fueron agrupadas juntas.

> *  Lógica: las partes de un módulo están agrupadas porque están categorizadas lógicamente para hacer lo mismo aun cuando son diferentes por naturaleza (por ejemplo: agrupar rutinas de manejo de input de teclado y mouse).

> *  Temporal: las partes de un módulo están agrupadas según cuándo serán procesadas (por ejemplo: una función que es llamada después de atrapar una excepción y que crea un log de error o notifica a un usuario).

> *  Procedural: las partes de un módulo están agrupadas porque siempre siguen una misma secuencia de ejecución (por ejemplo: una función que revisa los permisos de un archivo y que luego abre el archivo).

> *  Comunicacional: las partes de un módulo están agrupadas porque operan obre los mismos datos (por ejemplo: un módulo que opera sobre el mismo registro de información).

> *  Secuencial: las partes de un módulo están agrupadas porque el output de una parte es el input de otra parte, como en una *linea de ensamblaje* (por ejemplo: una función que lee datos de un archivo y luego procesa los datos).

> *  Funcional: las partes de un módulo están agrupadas porque todas ellas contribuyen a una única tarea bien definida del módulo (por ejemplo: análisis léxico de un string de XML).

#### Principio:
> Mientras más cohesionados estén los elementos agrupados en módulos, clases o funciones, mejor (**alta cohesión**).

#### Ventajas:
> La alta cohesión **reduce la complejidad** de los módulos (más simples, con menos operaciones), **incrementa la mantenibilidad** del sistema (cambios afectan a menos módulos), e **incremenenta la reutilización de módulos** (una funcionalidad particular puede ya estar implementada en el código, y al ser cohesiva permite su reuso).

### 5. Otros conceptos

####   Encapsulamiento
> Técnica de ocultamiento. Es el proceso de combinar los elementos de una abstracción que constituyen su estructura y comportamiento en una nueva entidad, restringiendo el acceso directo a los mismos.  
>Se refiere a la agrupación de los datos junto a los métodos que operan sobre dichos datos.

####   Interfaz
>Conexión funcional entre dos componentes de cualquier tipo, que proporciona una comunicación de distintos niveles permitiendo el intercambio de información.
Son puntos de entrada bien definidos, que proveen firmas de métodos (nombre de la función y el número, tipo y orden de los parámetros), constantes, tipos de datos, tipos de procedimientos y espeficicaciones de errores.

####   Separación de Intereses (*concerns*)
>Principio de diseño que consiste en separar un programa en distintas secciones, donde cada una se enfoca en un interés/preocupación (conjunto de información que afecta al código de un programa) delimitado.  
>La modularidad y separación de intereses se logra mediante la encapsulación de información, que provee una interfaz bien definida.  
> Por ejemplo: separación de front-end y back-end, o el patrón de arquitectura MVC.

####   DRY (Don't repeat yourself)
> Cada pieza significativa de funcionalidad en un programa debería ser implementada en un solo lugar en el código fuente.

####   KISS (Keep it simple, stupid!) 
> La mayoría de los sistemas funcionan mejor si se mantienen simples que complejos.  
> *"Perfection is reached not when there is nothing left to add, but when there is nothing left to take away".*

####   Avoid creating a YAGNI (You aren't gonna need it)
> No implementar algo hasta que sea necesario.

####   Do the simplest thing that could possibly work
> Implementar una nueva funcionalidad de la forma más simple que se te ocurra tal que "podría funcionar". No construir una *super-estructura*, no es necesario algo elegante, sólo que funcione y pase sus tests (Es **crítico realizar refactoring** para garantizar código limpio). 
	
####   Don't make me think
> El código debería ser fácil de leer y entender requiriendo mínimo esfuerzo. Si el código requiere que el observador piense mucho para entenderlo, probablemente puede ser simplificado.

####   Write code for the mantainer
> Escribir el código pensando en quién lo mantendrá.  
> "Siempre escribe código pensando en que el mantenedor será un psicópata que sabe dónde vives".

####   Principle of least astonishment
> Un componente debería comportarse de una forma consistente con cómo sus usuarios esperan que se comporte (los usuarios no deberían sorprenderse por como funciona).  
> El componente debe hacer lo que su nombre y los comentarios señalan que hace, sin tener *efectos secundarios*.

####   Law of Demeter
> Cada unidad debería tener conocimiento limitado acerca de otras unidades (solo aquellas cercanamente relacionadas a la unidad en cuestión). *Don't talk to strangers*.

####   Avoid premature optimization
> No gastar preocupación y tiempo pensando en la velocidad de **partes no críticas** de los programas. Estos esfuerzos deberían concentrarse en los cuellos de botella del sistema (cuando sean conocidos).  
> Es fundamental **entender qué es prematuro** y qué no.  
> **Observación:** Optimizar [**si** es bueno](http://ubiquity.acm.org/article.cfm?id=1513451), pero enfocar todo el tiempo en *micro-optimizaciones* en sectores no críticos puede no ser ventajoso para el desarrollo.

####   Boy-Scout Rule
> Siempre deberíamos dejar el código en mejor estado que como lo encontramos (aunque sea en detalles pequeños, el código mejorará gradualmente). Basta con mejorar el nombre de una variable, o separar una función en dos.

####   Command Query Separation
> Un método debería ser o un comando que realiza una acción, o una consula que returna datos a quien lo invoca pero no ambas. Hacer una consulta no debería modificar la respuesta (los métodos de consulta se podrán utilizar en cualquier orden ya que no mutan el estado a diferencia de los comandos). 
 

## Code Smells

## Refactoring

## Modelo 4 + 1

## Principios SOLID (Diseño de Componentes)

### 1. Single Responsability

**Una clase o módulo debería tener una única razón para cambiar**, es decir, debe estar encargada de una sola cosa, y no aglomerar muchas responsabilidades. El motivo detrás de esto es que al fallar una funcionalidad de dicha clase/módulo, queremos que el resto del software siga funcionando, y si la clase sólo encapsula una función, no perderemos nada adicional (otros métodos, por ejemplo).

Ejemplo:

Antes (OxygenMeter con responsabilidades múltiples)

```java

public class OxygenMeter {
    public double OxygenSaturation { get; set; }
 
    public void ReadOxygenLevel() {
        using (MeterStream ms = new MeterStream("O2")) {
            int raw = ms.ReadByte();
            OxygenSaturation = (double)raw / 255 * 100;
        }
    }
 
    public bool OxygenLow() {
        return OxygenSaturation <= 75;
    }
 
    public void ShowLowOxygenAlert() {
        Console.WriteLine("Oxygen low ({0:F1}%)", OxygenSaturation);
    }
}
```
Después (múltiples clases con responsabilidad única)

```java
// SOLO SE ENCARGA DE LEER EL NIVEL DE OXÍGENO
public class OxygenMeter {
    public double OxygenSaturation { get; set; } 
    public void ReadOxygenLevel() {
        using (MeterStream ms = new MeterStream("O2")) {
            int raw = ms.ReadByte();
            OxygenSaturation = (double)raw / 255 * 100;
        }
    }
}

// SOLO SE ENCARGA DE REVISAR SI EL NIVEL ESTÁ BAJO UN VALOR
public class OxygenSaturationChecker {
    public bool OxygenLow(OxygenMeter meter) {
        return meter.OxygenSaturation <= 75;
    }
}

// SOLO SE ENCARGA DE MOSTRAR UNA ALERTA 
public class OxygenAlerter {
    public void ShowLowOxygenAlert(OxygenMeter meter) {
        Console.WriteLine("Oxygen low ({0:F1}%)", meter.OxygenSaturation);
    }
}
```

### 2. Open-Closed

Las entidades de código deben estar abiertas para extensión pero cerradas para modificación. **Se debe escribir clases que cumplan con lo que deben hacer perfectamente, sin asumir que alguien las modificará después** (extensibles).
Así, uno debería construir una clase de modo tal que el procedimiento que sigue para proveer una funcionalidad no sea ambiguo y sea **independiente del formato del input**, al mismo tiempo que permita ser extensible (por medio de herencia, por ejemplo).  

Ejemplo:

Antes (Tipos de loggers hard-coded en el enum y el switch)

```java
public class Logger {
	 // MÉTODO DISEÑADO PARA MANEJAR SOLO 2 TIPOS DE LOGS
    public void Log(string message, LogType logType) {
        switch (logType) {
        	  // HABRÍA QUE AÑADIR CASES PARA NUEVOS TIPOS
            case LogType.Console:
                Console.WriteLine(message);
                break;
 
            case LogType.File:
                // Code to send message to printer
                break;
        }
    }
}
// ESTRUCTURA RÍGIDA, CADA VEZ QUE SE DESEE UN NUEVO TIPO HAY QUE MODIFICARLA
public enum LogType { Console, File }
```
Después (utilizando una interfaz genérica para los tipos de loggers)

```java
// NO ES NECESARIO MODIFICAR LA CLASE LOGGER PARA EXTENDER SU FUNCIONALIDAD
public class Logger {
    MessageLogger _messageLogger;
 
    public Logger(MessageLogger messageLogger) {
        _messageLogger = messageLogger;
    }
    
    public void Log(string message) {
        _messageLogger.Log(message);
    }
}
// BASTA CON CREAR NUEVAS CLASES QUE IMPLEMENTEN ESTA INTERFAZ
public interface MessageLogger {
    void Log(string message);
}
 
public class ConsoleLogger : MessageLogger {
    public void Log(string message) {
        Console.WriteLine(message);
    }
}

public class PrinterLogger : IMessageLogger {
    public void Log(string message) {
        // Code to send message to printer
    }
}
```

### 3. Liskov's Substitution

Si hay herencia, **las clases hijas deben responder como la clase padre sin fallar, es decir, deben ser intercambiables**. Así, si hay una funcionalidad de la clase padre que no será usada por la clase hija (o devolverá error), es mejor evitar el uso de herencia. Las subclases deberían operar de la misma forma que la clase padre, es decir, los parámetros de las subclases deben ser del mismo tipo o menos restrictivos que los de la clase padre, y los retornos de las subclases deben ser de igual tipo o más restrictivos que la clase padre (hay más [condiciones/reglas](https://en.wikipedia.org/wiki/Liskov_substitution_principle#Principle) para garantizar un *behavioural subtype*).
Ejemplos típicos: Elipse/círculo, rectángulo/cuadrado (métodos para calcular áreas entre otros).

### 4. Interface Segregation

Plantea que **se deben favorecer las interfaces sencillas y específicas para cada cliente, es decir, solo proveer lo que sea necesario**.   
Las clases y sus dependencias se comunican usando interfaces específicas, minimizando las dependencias en miembros no usados y reduciendo el acoplamiento. Interfaces más sencillas son más flexibles y reutilizables, y entre menos clases compartan interfaces, se requieren menos cambios para responder a una modificación en la interfaz (mayor robustez).  
**Con interfaces más pequeñas, es más fácil introducir nuevas clases que las implementen.**      
Por ejemplo: en un menú de un restaurant se señala la *sopa del día* en vez de imprimir todos los días un menú especificando qué sopa hay. En este caso, el objetivo es simplemente que el cliente conozca el precio, y si necesita saber qué sopa específica hay, puede utilizar la *interfaz* de preguntarle al mesero.

### 5. Dependancy Inversion

Llama a **escribir código que dependa de abstracciones y no de detalles concretos**, y para reconocerlo se puede observar el *input* que recibe un método y pensar en qué tan genérico (abstracto) es.   
Módulos de alto nivel (con más funcionalidades, lógica de negocios) no deberían depender de módulos de bajo nivel (operaciones detalladas/específicas), sino que ambos deben depender de abstracciones. Esto permite sustituir dependencias por otras nuevas (que implementen la misma interfaz) sin generar impactos negativos.  
Por ejemplo: para las tarjetas de crédito, la máquina que las opera no pregunta si es una Visa o de otro tipo, y simplemente pide que se deslice la tarjeta (abstracción de los distintos tipos de tarjeta que puedan haber).  
Otro ejemplo: clase PasswordReminder utiliza un objeto MySQLConnection para conectarse a la base de datos y obtener información. Si la base de datos fuese otra, habría que entrar a modificar PasswordReminder (viola este principio, y también open-closed). Por lo tanto, la solución es utilizar una interfaz DBConnectionInterface (abstracción) que contenga un método `connect()`, y esto permitirá intercambiar de base de datos fácilmente.


## Diagramas UML

## Diseño en Web