# Evidencia-Generacion-y-Limpieza-de-Gramatica

## Contexto de la gramática 

El lenguaje que escogí para poder generar la gramática que se pedia en este proyecto fue el Coreano.

El coreano es un idioma que se habla por más de 75 millones de personas, principalmente en Corea del Norte y Corea del Sur, además de en algunas lugares fuera de estos países como Japón,China y Estados Unidos. Este es el idioma oficial tanto de Corea del Sur (República de Corea) como de Corea del Norte (República Popular Democrática de Corea), sin embargo tienen diferencias menores en cuanto a ortografía, orden alfabético y vocabulario.

En la actualidad, el coreano se escribe utilizando el sistema **"hangul"**, el cual fue creado en el siglo XV por el rey Sejong y consta de 24 letras básicas: 14 consonantes y 10 vocales. Este sistema fue diseñado para ser más sencillo y accesible para la población, ya que anteriormente se utilizaban caracteres chinos, que eran mucho más complejos de aprender, de hecho, el hangul es considerado uno de los sistemas de escritura más eficientes, ya que su diseño sigue una lógica clara facilitando su aprendizaje.

El idioma también da mucha importancia a la cortesía y a las jerarquías sociales, para remarcar esto utilizan formas honoríficas, conocidas como **"jondaetmal"**, las cuales permiten expresar respeto hacia personas mayores, de mayor estatus social o con una posición profesional más alta, estas formas son fundamentales en la comunicación cotidiana, ya que ayudan a reflejar respeto y a mantener buenas relaciones sociales.
(Guasti, 2023; Martin, 2025).


**CÓMO FUNCIONA LA GRAMÁTICA**

De acuerdo con Linz y Rodger (2022), una gramática para un lenguaje, como por ejemplo el inglés, nos permite determinar si una oración está bien formada o no. Una de las reglas más básicas establece que una oración puede construirse a partir de una frase nominal seguida de un predicado, lo cual se puede representar formalmente como:

 <img width="300" height="22" alt="image" src="https://github.com/user-attachments/assets/6ef8dd62-5a55-4381-a6fb-9760b68c16e9" />

Sin embargo, esta regla por sí sola no es suficiente para describir completamente la estructura de las oraciones, por lo que es necesario definir los elementos que la componen, en este caso, la frase nominal y el predicado también se pueden descomponer mediante reglas más específicas, como:

<img width="280" height="50" alt="image" src="https://github.com/user-attachments/assets/27e76bf1-f7c4-4879-b190-c760cb14d913" />

De acuerdo con estos autores, al asociar palabras concretas a cada categoría (por ejemplo, artículos como “a” o “the”, sustantivos como “boy” o “dog”, y verbos como “runs” o “walks”), la gramática permite generar oraciones correctas dentro del lenguaje, como “a boy runs” o “the dog walks”.

Asimismo, Linz y Rodger (2022) explican que, en teoría, una gramática completa permitiría describir cualquier oración válida del idioma mediante este proceso. Este enfoque consiste en partir de una estructura general y descomponerla progresivamente en componentes más simples, lo que da lugar a lo que se conoce como gramáticas formales.

Una gramática formal se define como una estructura compuesta por cuatro elementos, representada como:

**G = (V, T, S, P)**

- **V** corresponde a las variables o símbolos no terminales, es decir, aquellos que pueden seguir siendo reemplazados durante el proceso de derivación.
- **T** representa el conjunto de símbolos terminales, que son los elementos finales de la cadena y que no pueden ser sustituidos.
- **S** es un símbolo especial perteneciente a V, conocido como el símbolo inicial, a partir del cual se comienza a generar cualquier cadena del lenguaje.
- **P** es el conjunto de producciones,las reglas que indican cómo pueden transformarse los símbolos dentro de la gramática.

Además, los autores señalan que los conjuntos de variables (V) y terminales (T) son finitos, no están vacíos y no comparten elementos entre sí.

**Estructura**

La gramática básica coreana utiliza el siguiente orden:

***SUJETO (S) + OBJETO (O) + VERBO (V)*** 

También es conocida como estructura SOV, la cual puede resultar un poco confusa al inicio debido a que es muy diferente a la que usan idiomas como el español y el inglés, los cuales se estructuran con Sujeto + Verbo + Objeto (SVO).

Esto quiere decir que una oración en Coreano traducida al español sería de la siguiente manera: 

Yo + naranja + comí

**Particulas**

La mayoría de las palabras en coreano tienen añadida una partícula, estas partículas lo que van a hacer es indicar el rol de las palabras en la oración, es decir, cuál palabra es el sujeto y cuál el objeto. El español no tiene esto o algo parecido, por lo que no tienen traducción.

*SUJETO*

Se coloca al final de una palabra para indicar que es el sujeto de la oración.
- Se usa **는** cuando la última letra de la última sílaba del sujeto es una **vocal**.
- Se usa **은** cuando la última letra de la última sílaba del sujeto es una **consonante**.

Para facilitar la creación de la gramática se limito el vocabulario para solamente crear palabras que usen **는**, es decir solo utilicé sujetos que terminen con vocal.

*OBJETO*

Se coloca al final de una palabra para indicar que es el objeto de la oración.
- Se usa **를** cuando la última letra de la última sílaba del objeto es una **vocal**.
- Se usa **을** cuando la última letra de la última sílaba del objeto es una **consonante**

Aquí también limité el vocabulario usado para que la creación de oraciones fuera simplemente con **를**, en otras palabras, solo se van a utilizar objetos que terminen en vocal.

*EJEMPLOS*

Usando estas reglas las oraciones se verian de la siguiente manera:
 
1). Yo hablo coreano = Yo는 coreano를 hablo

- 는 va unido a “Yo” (el sujeto)
- 를 va unido a “coreano” (el objeto)

2.) Tú comes chocolate = Tú는 chocolate를 comes

- 는 va unido a “Tú” (el sujeto)
- 를 va unido a “chocolate” (el sujeto)

**Conjunciones**

Para poder realizar oraciones más complejas y con mayor contexto añadí el uso de 3 conjunciones, las cuales son las siguientes: 

- 그리고 (y)
- 또는 (o)
- 하지만 (pero)

Ahora con esta nueva adición, podemos formar oraciones como las siguientes:

- 나(yo)는  피자(pizza)를  먹다(comer)  그리고(y)  그(él)는  커피(café)를  마시다(beber)  그리고(y)  우리(nosotros)는  음악(música)를  듣다(escuchar).
- 그(él)는  영화(película)를  보다(ver) 그리고(y) 그녀(ella)는 음악(música)를 듣다(escuchar).

## MODELOS

### Gramática base

La primera gramática creada, con todas las reglas previamente explicadas, quedo así:

<img width="450" height="image" alt="image" src="https://github.com/user-attachments/assets/724f5e3c-2b11-4636-b768-59a86ca3bfd1" />


Sin embargo esta tiene dos problemas: que es ambigua y cuenta con recursividad izquierda, lo cual solucionaremos a continuación.

### Elimininación de Ambigüedad

De acuerdo con Linz y Rodger (2022), una gramática libre de contexto se considera ambigua cuando existe al menos una cadena **w** ∈ L(G) que puede generarse mediante dos o más árboles de derivación diferentes, esto quiere decir que una misma cadena puede obtenerse a través de múltiples derivaciones, ya sean por la izquierda (leftmost) o por la derecha (rightmost).

Lo cual se veria de esta manera:

<img width="400" height="image" alt="image" src="https://github.com/user-attachments/assets/f14f78d0-f80b-44b7-a2c1-4f29d0cec6a1" />

En el caso de mi gramática, podemos saber que esta es ambigua porque al probar la cadena "나(yo) 는 피자(pizza) 를 먹다(comer) 그리고(y) 그(él) 는 커피(café) 를 마시다(beber) 그리고(y) 우리(nosotros) 는 음악(música) 를 듣다(escuchar)" con el código "gramatica_ambigua.py" podemos observar que el output es el siguiente:

<img width="1200" height="image" alt="Screenshot 2026-04-23 at 12 43 01 p m" src="https://github.com/user-attachments/assets/131263ed-2d40-4c17-89aa-5e4ebbf2c866" />

El output muestra dos árboles, lo cual quiere decir que hay dos maneras diferentes de crear esa string, debido a esto se debe cambiar la gramática de manera que solo exista una sola posibilidad de crear esta y otras strings similares.


### Elimininación de Recursividad Izquierda

## IMPLEMENTACIÓN

## PRUEBAS

## ANÁLISIS

## REFERENCIAS 
- Linz, P., & Rodger, S. H. (2022). An introduction to formal languages and automata. Jones & Bartlett Learning.
- Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2008). Teoría de autómatas, lenguajes y computación (3.ª ed.). Pearson Addison-Wesley.
- Toyryla, L. (2026, March 17). Korean Grammar - a Beginner’s Guide. 90 Day Korean. https://www.90daykorean.com/korean-grammar/
- Guasti, C. (2023, September 6). Interesting facts about the Korean language. https://www.citylit.ac.uk/blog/interesting-facts-about-the-korean-language
- Martin, SE (2025, Aprill 23). Idioma coreano . Enciclopedia Británica . https://www.britannica.com/topic/Korean-language
