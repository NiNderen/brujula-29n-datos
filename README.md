# Brújula 29N · datos

Archivo público que lee la app Brújula 29N (elecciones generales del 29 de noviembre de 2026).

- `feed.json`: noticias por partido, cambios de posición de los partidos y textos de "Datos y hechos".

## Formato

- `updated`: fecha (AAAA-MM-DD) de la última actualización.
- `banner`: mensaje opcional que se muestra sobre las noticias.
- `news[]`: `id`, `party` (psoe, pp, vox, sumar, podemos, erc, junts, bildu, pnv, bng, cc, upn o `all`), `date`, `topic`, `title`, `summary`, `source`, `url`.
- `positions`: `{ "<id de tema>": [12 valores de -2 a 2 o null] }` en el orden PSOE, PP, VOX, SUMAR, PODEMOS, ERC, JUNTS, EH BILDU, PNV, BNG, CC, UPN.
- `facts`: `{ "<id de tema>": "texto" }` que sustituye a "Datos y hechos".

Las posiciones son estimaciones a partir de propuestas y votaciones públicas. No es una recomendación de voto.
