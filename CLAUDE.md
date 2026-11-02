# Cuentos de J.A. — contexto del proyecto (traspaso)

Webapp de cuentos para dormir para J.A. (3 años). Producción: https://cuentos-ja.vercel.app
Repo: github.com/jjsuarez14/cuentos-ja (público) → Vercel publica solo en cada push a `main` (~1 min).
Usuario: Jofre (papá). Responder siempre en español latinoamericano, tratamiento de "usted".

## Cómo funciona
- `cuentos/*.txt`: un archivo por bloque. Cabecera de cada cuento:
  `=== id | semana | dia | momento | tipo | titulo | tema | fuente`
  - semana: 1 = semana del lunes 21/09/2026. `0` = sin fecha (se asigna en `ajustes.json`).
  - dia: lun…dom · momento: siesta | noche · tipo: ja | clasico | original | en | spidey
  - Párrafos separados por línea en blanco. Bloque final opcional `@@ Para papá` (una nota por línea) → recuadro en el lector.
- `cuentos/ajustes.json`: asigna cuentos a fechas concretas (lo que desplaza va al banco).
- `cuentos/festivos.json`: festivos escolares (rangos `AAAA-MM-DD..AAAA-MM-DD`).
- `python3 scripts/build.py` → genera `public/cuentos.json` (cuentos + agenda por fecha + festivos + banco) y VALIDA: noche todos los días, siesta en fines de semana/festivos, sin repetidos, largos dentro de tolerancia. Si falla, no publicar.
- `public/index.html`: app (un solo archivo). Agenda por fecha, festivos marcados, modo nocturno, tamaño de letra, "leído" en localStorage (por teléfono), recuadro "Para papá".
- Publicar: `python3 scripts/build.py && git add -A && git commit && git push`. Probar en producción con Playwright (iPhone 14, Europe/Madrid, fijando fecha con `page.clock.setFixedTime`).

## Reglas editoriales (acordadas con Jofre)
- Largo: siesta 750 palabras, noche 1.200 (±10 %). Inglés ~350 (±15 %). Ojo: los borradores suelen quedar 15-30 % cortos; contar con el script y ampliar con escenas reales.
- Siesta SOLO sábados, domingos y festivos escolares de Valencia (desde 07/10/2026). Noche todos los días.
- Cuentos de vida diaria (Simón de protagonista): solo en siesta, nunca de noche (no sobreexcitar). Objetivo ≤25 %.
- Noches: final lento y calmado, imágenes de sueño, cierre "Y colorín colorado…".
- Inglés: martes y jueves por la noche, ~400 palabras, historia narrada y fluida (poco diálogo), recuadro "Para papá" (vocabulario, pronunciación aproximada, consejo de lectura).
- Spidey y sus sorprendentes amigos (Spidey, Ghost-Spider, Spin, TRACE-E, Hulk, Duende Verde): 1 por semana, historias ORIGINALES, solo app, `imprimible: false` (no van a los libros impresos por derechos de autor). No reproducir tramas de Disney/Marvel.
- Temas prioritarios: compartir, portarse bien, "Todavía no puedo… ¡pero lo voy a intentar!" + "¿Me ayudas?" (no prohibir "no puedo": completar la frase). También: amigos nuevos, esperar turno, saber perder, miedos con enfoque de valentía (oscuridad, monstruos, perderse, tormentas, médico).
- NO: princesas, temas de niñas, LGBTQ/inclusión. Sí: deportes (baloncesto), música, aventuras, clásicos de dominio público.
- Idioma: español LATINOAMERICANO (carro, lentes, cobija, durazno, media, papa, torta, colegio, manejar, estacionar, monopatín, enojarse, acostarse). Prohibido: vosotros, coger, vale, enfadar, tumbar, gafas, coche, manta, tarta, zumo, patata, tirita, pegatina, lobezno, cole.
- Sin meta-comentarios del autor dentro del texto ("perdón, quise decir…").

## Familia y personajes recurrentes
- J.A. (Joffre Alejandro, "Jota A"), 3 años, pelo rizado, ama el baloncesto (pelota naranja), la música, Disney, Spidey. Nació en Chile; padres venezolanos; viven en Valencia (España). Colegio a tiempo completo.
- Mamá y Papá · Abuela y Abuelo (en Venezuela; videollamadas los domingos; abuelo toca el cuatro, abuela hace arepas).
- Maestra Inés · amigos del colegio/parque: Sergio, Diego, Martín (llegó nuevo), Leo (empujaba; ya amigos), Pau (habla valenciano), Lucía, Marcos (mayor, máscara) · Eder (amigo de la familia, alto y chistoso).
- Frases/recursos ya usados con J.A.: "regla de la mano en alto" (¡Para! ¡No me gusta!), respirar "como oler una flor / soplar una vela", "Campeonato de Ordenar", "los buenos jugadores miran a todo el equipo".

## Estado al 02/11/2026
- Agenda completa hasta el lunes 30/11/2026. 97 cuentos. Banco vacío.
- DESPERSONALIZACIÓN (pedido de Jofre, 02/11): los nombres reales lo activan en vez de dormirlo. NUNCA usar J.A., Inés, Sergio, Diego, Martín, Leo, Pau, Lucía, Marcos ni Eder en los textos. Personajes ficticios: Simón (protagonista "vida diaria", tipo ja), maestra Rosa, Rodrigo, Joaquín, Gabriel, Óscar, Toni, Clara, Raúl, Félix. Mamá, Papá, Abuela y Abuelo se mantienen genéricos. En la app, el tipo ja se muestra como "Vida diaria".
- INGLÉS desde en-06: "historias" narradas en pasado, fluidas, poco diálogo, ~400 palabras (±15 %). en-01..en-05 siguen en el estilo antiguo (frases cortas y repetitivas): candidatas a reescribir.
- Noviembre: noches n-01..n-16 (noviembre1/2.txt), inglés en-06..en-13 (ingles2.txt), siestas sp-03..sp-06 y s-01, s-02 (noviembre3.txt), más las 7 piezas del banco.
- Próximo: diciembre (01/12 → 31/12). Festivos escolares: 8/12 y 22/12..6/1 → siesta también esos días. Aprox.: 31 noches (9 en inglés), 4-5 Spidey, siestas de fines de semana + ~13 de festivos.
- Festivos pendientes de confirmar: días no lectivos de València ciudad (Fallas 15-18/03/2027 es propuesta).
- Libro impreso (fase posterior): 4 tomos de 14 cuentos, 8×10", 1 ilustración por cuento, KDP color estándar (~2,90 EUR/tomo). Excluir cuentos `imprimible: false`. Antes de maquetar: cerrar textos y aprobar un cuento de muestra.
- Fase 2 opcional: Supabase para compartir las marcas de "leído" entre los dos teléfonos.

## Títulos ya usados (no repetir)
- J.A.: el amigo que hablaba distinto · el campeonato de ordenar · el cumpleaños de Sergio · el día que Diego no quería jugar · el niño nuevo · el partido en el parque · el turno del tobogán · la fiesta de disfraces · la llamada de los abuelos · la paella del domingo · la regla de la mano en alto · la visita a la doctora
- Clásicos: Aladino · Alicia · El gato con botas · El gigante egoísta · El león y el ratón · El ratón de campo y el de ciudad · El ruiseñor del emperador · El sastrecillo valiente · El traje nuevo del emperador · Gulliver · Juan y las semillas mágicas · La cigarra y la hormiga · La liebre y la tortuga · Los duendes y el zapatero · Los músicos de Bremen · Los siete cabritillos · Los tres cerditos · Los tres chivitos · Mowgli y Baloo · Pinocho · Pulgarcito · Robin Hood · Robinson Crusoe · Simbad · Tío Tigre y Tío Conejo
- Originales: Bongo y su tambor · Coco el loro · El autobús de la noche · El balón que quería ver el mar · El barquito de papel · El cohete de cartón · El dragón que tenía miedo de la oscuridad · El faro · El oso que no podía dormir · El pingüino y el sol · El tren de los sueños · Hugo y el camión de la basura · La Luna que quería jugar al baloncesto · La cobija de los abrazos · La estrella que se cayó del cielo · La orquesta de los grillos · Nico el pulpo · Nilo y la luciérnaga · Pincho y las hojas de otoño · Pipo el canguro · Rulo y su trompeta · Tito el delfín y la tormenta · Tomi y el monstruo del armario
- Inglés: Little Bear Can Try · Max Shares His Bananas · Ten Little Stars · The Big Orange Ball · The Magic Words
- Spidey: el nuevo truco de Spin · el parque para todos · el robot de juguete · la carrera de telarañas · la gran pelota de Hulk · el día de lluvia
- Vida diaria (Simón): la torre que se caía · el día de traer un juguete
- Clásicos (nov.): La gallinita roja · Pedro y el lobo · Nils y el viaje con los gansos · Cómo le salió la trompa al elefante · Don Quijote y los gigantes del molino · La zorra y la cigüeña · El viento y el sol
- Originales (nov.): El robot que aprendió a decir gracias · La semilla que quería ser árbol · El castor que construyó la presa · La ballena que cantaba nanas · El erizo que aprendió a abrazar · El viaje de la gotita de lluvia · La ardilla que quería encestar · El jardinero de las estrellas · Rayo, el perro bombero
- Inglés (nov.): The Elephant Who Shared the Water · The Little Train on the Big Hill · The Cat Who Lived in the Lighthouse · The Turtle Who Learned to Swim · The Bear's Long Winter Sleep · The Owl and the Stormy Night · The Garden of Kind Words · The Moon's Night Walk
