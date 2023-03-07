# M04uf1
CyberSeguretat M04 Llenguatge de marques. UF1

## APUNTS DE XML
**XML** Significa extended Markup language i és un llenguatge de marques. Aquests tipus de llenguatges serveixen per transportar i gestionar dades entre aplicacións.
Els llenguatges d'aquest tipus funcionen per etiquetes. Smgl és com la versió antiga (versió mare)  i primera de la que després sortiría HTML i XML i les etiquetes es definien de la següent manera:

Sgml → <I>hola</I> → cursiva
Hyper text → text normal però afegeix una nova dimensió → els enllaços entre pàgines web, que canvien el món de forma espectacular. 
HTML és sgml però amb aquesta nova dimensió.

Mosaic→ el primer browser
XML → Llenguatge més definit que html4 però suficientment lliure per fer el que et doni la gana.

La capçalera que es posa al principi de tots els programes fets amb **XML** és la següent:
<\?xml version="1.0" encoding="UTF-8" ?>
Utf 8 és la codificación de caràcteres. S’especifica per temes de compatibilitat i perquè quan posis el codi en un altre idioma, es mostrin els mateixos caràcters.

Quan el que volem escriure pot ser molt variable, hem d’obrirlo i tancar-lo d'aquesta manera: 
```XML
<nom>Pepsol45</nom>
```

 En canvi si sabem que sempre serà un tipus de dada, (int,float, etc…) utilitzem la següent estructura:
 ```XML
 <age value="234">
 ```

```XML

<?xml version="1.0" encoding="UTF-8" ?>
<character>
	<name>Eustaquio</name>
	<surname>Mendoza</surname>
	<!-- COMENTARIO -->
	<age value="197" />
</character>
```

Nosaltres podem crear les etiquetes que vulguem i perquè tot tingui sentit hem de crear un document XSD per validar la estructura del que hem creat. Per definir que tot allò que hem escrit té un sentit i una direcció funcional.
Per això aquest esquema representa el que són els diferents formats:

* XML --> Crea Etiquetes
* XSD --> Valida les estructures
* DTD --> Com XSD però més antic

En XML (també ho pots aplicar al XSD) hi ha un bocabulari particular que a priori no s'endevina intuitivament:

\* significa 0 o més cops repetits
\? significa 0 o 1 cops
\+ significa 1 o més cops
Si no hi ha res significa 1 cop només

![ADSF](https://i.ytimg.com/vi/cfQN7SqJihk/maxresdefault.jpg)

![eLCHATERO](https://images.cdn3.buscalibre.com/fit-in/360x360/c1/77/c17783c27067d6dca1f2e88def3a6f7e.jpg)

![LKSADFJ](https://sidoxia.files.wordpress.com/2009/10/muscle-man.jpg)


### APUNTES MARKDOWN
A partir d'aquí hi han apunts sobre markdown que és el llenguatge amb el que estic documentant aquest projecte. Per consequència és recomanable la visualització d'auqest text en els seu format "codi" perquè sinó es farà més feixuc el procés d'entendre el que està documentat. Gràcies
#Título1
####Título2
* algo → per fer llistes
_algo_ → cursiva
> algo → per destacar algo “normalment codi”


#### DTD
Aquí irán los apuntes de DTD

> Un gran poder conlleva 
> una gran responsabilidad
>
> -Heràclit d'Hefest

>**Esto es una cita**
>>Ma cagun tot aixo és una cita dintre d'una cita.
>
>Seguim

[CondorChem](https://condorchem.com)

Y [Esto](http://enti.cat) es un enlace a una web muuuy sospechosa

**Brownie de xocolata amb grumolls**



## Ejemplo de código sintáctico interpretado

```kotlin
val range5 = 0..10
fun main() {
	for (n in range5) {
		println(n)
	}
	if (7 in range5) {
		println("yes")
	}
	if (12 !in range5) {
		println("no")
	}
}
```

### Listas de tareas

- [ ] Primera tarea
- [x] Segunda tarea	
- [ ] Tercera tarea

### Carácters extendidos

:poop: :alien: :cry:  :imp: :eggplant: 

### Estilo de carácteres

*cursiva* _cursiva_

**negrita** _negrita_

~~TACHAO~~

~~***TACHAO, negrita y cursiva***~~

### Tablas 

| id_character | name | age | level |
| ---: | --- | --- | --- |
| 1 | Eustaquio | 197 | 99 |
| 2 | Mariana | 20 | 100 |
| 3 | Mortadelo | 100 | 1 |
| 4 | Messi | 44 | 32 |