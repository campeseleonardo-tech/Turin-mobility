# Esito L22 (25/10/2026): numeri e gruppi nuovi, home e risultati in due gruppi, grafici tolti, scheda dei costi con due casi

Un commit per punto, tutti su `prova`; `main` aggiornato solo se le prove sono verdi (vedi in fondo).

## Numeri e gruppi
- `NUMERO_PUBBLICO` in `scripts/schede_risultati.py`: costi (id 12) = 1, bus contro auto (8) = 2, dove lasciare l'auto (6) = 3 | fragilità e servizi (10) = 4, ritardi (4) = 5, città dei 15 minuti (1) = 6. Campo nuovo `gruppo` ("decidere" per 1-3, "dati" per 4-6).
- Ogni ricerca per numero pubblico ora usa l'id interno (campo `risultato`): `assets/progetto.js` (`scheda(id)`, e i bottoni «Risultato N» di `progetto.html` leggono il numero dai dati), `scripts/prova_pagine.py` (`#r12`, `#r6`, id nelle prove). Gli indirizzi `#rN` sono invariati; `r/N.html`, anteprime e README seguono i numeri nuovi.

## Home e risultati.html
- Home: eroe com'era, poi due gruppi («Per decidere» – «Risultati che aiutano il Comune e chi si muove a scegliere»; «Cosa dicono i dati» – «Come funziona la città, misurato»), in inglese «To decide» e «What the data show». Ogni riquadro: anteprima animata, nome breve (campo nuovo `titolo_breve`, al massimo 4 parole), numero grande, testo breve. Il codice dei gruppi è in `assets/sito.js` (`Sito.perGruppi`), lo stesso per home e `risultati.html`.
- Tolti dalla home «In breve» (e il campo `chiave` delle schede, che non serviva più) e la fascia «Il progetto»; in fondo c'è il link «Perché questo progetto →» a `progetto.html`; la barra porta a `progetto.html`. CSS e script della fascia tolti dalla home (`progetto.js` e `progetto.css` restano per `progetto.html`).
- `risultati.html`: elenco diviso nei due gruppi, resto uguale. Descrizioni e `og:description` di home e risultati riscritte (sei risultati).
- `progetto.html`: testo visibile IT ed EN identico a prima, salvo i due numeri delle schede citate («Risultato 5 → 4», «Risultato 4 → 2»). Prova: `scripts/prove/progetto_testo_prima_L22.json` (testo di prima, numeri sostituiti da «#») confrontato dentro `design_l22`.

## Prima e dopo, scheda per scheda
| Scheda | Prima | Dopo |
|---|---|---|
| Costi (id 12) | numero 6; grafici: mese dai 12 punti, tempo contro soldi, mese per distanza, commissione | numero 1; grafici: commissione (principale), mese di lavoro in centro (nuovo), mese per distanza; titolo «Con la sosta pagata, andare al lavoro in centro in auto costa circa 270 euro al mese più dei mezzi»; punti: il parcheggio pesa più di tutto, parcheggio gratis → ~35 euro di carburante contro 26-38 dell'abbonamento, ~11 minuti in più a viaggio; nessun «12 punti» fuori dalla parte chiusa |
| Bus contro auto (8) | numero 4; 5 grafici | numero 2; tolto «I tragitti dove coi mezzi pubblici si impiega più del doppio dell'auto» (dati restano in `r8`/rapporti) |
| Dove lasciare l'auto (6) | numero 3 | numero 3, invariata |
| Fragilità e servizi (10) | numero 5; punti sul prezzo: «il legame prezzo-servizi quasi sparisce» e «reggono fragilità-servizi e prezzo-fragilità» | numero 4; punto 1 «Le case costano meno dove la fragilità è alta (−0,69 a parità di distanza dal centro)»; punto 3 «Con i servizi il legame col prezzo quasi sparisce (0,21); resta quello fra fragilità e servizi (−0,48)»; grafici invariati |
| Ritardi (4) | numero 2; 3 grafici in «altri» | numero 5; tolto «GPS e dato ufficiale GTT»; il confronto con GTT resta nei testi chiusi e nei rapporti |
| Città dei 15 minuti (1) | numero 1 | numero 6, invariata |

## Cosa è stato tolto (e dove restano i dati)
- Grafico dei tragitti oltre il doppio (scheda bus contro auto): i dati restano in `data/processed/tp_contro_auto.json`, `r6_bus_contro_auto.json` e nel rapporto del traffico.
- Grafico GPS e dato ufficiale GTT (ritardi): i numeri restano in `data/processed/risultato4_riepilogo_mappa.json` (`confronto_gtt`) e in `docs/R4_puntualita.md`; la riga sul confronto resta nel calcolo.
- Grafici dei costi «mese dai 12 punti» e «tempo contro soldi»: i dati per punto restano in `data/processed/costo_del_viaggio.json` e nel rapporto.
- Non servono più le righe di `testi.json` dei grafici tolti (cancellate le tre esatte); le altre righe inutilizzate restano, innocue.

## Scheda dei costi: tariffe trovate (solo pagine ufficiali GTT, consultate il 24/10/2026)
Le pagine non riportano la data delle tariffe; quella Under 26 cita la campagna 2024-2025. Fonti in `data/ref/costi.json` (`gtt.agevolati`, con indirizzi):
- Under 26 (`gtt.to.it/cms/biglietti-abbonamenti/7326-abbonamenti-under-26`): mensile 25 euro; annuale ordinario 258; annuale con ISEE: fino a 12.000 euro 158, da 12.000 a 20.000 178, da 20.000 a 50.000 208 (residenti o domiciliati a Torino con contratto registrato, o residenze universitarie del Comune).
- Over 65 (`gtt.to.it/cms/biglietti-abbonamenti/7327-abbonamenti-over-65`): mensile 20 euro (residenti a Torino, ISEE sotto 50.000, non in vendita online); annuale con ISEE: fino a 7.000 gratuito (3 euro di pratica), da 7.000 a 12.000 118, da 12.000 a 20.000 155, da 20.000 a 50.000 188.
- Già presenti: biglietto 2,00, mensile 38, annuale 310.
- Nel grafico del mese: Under 26 mensile (25), Under 26 annuale ISEE fino a 12.000 (158/12 = 13), Over 65 mensile (20), Over 65 annuale ISEE 20.000-50.000 (188/12 = 16). Tutte le fasce sono nella riga «Tariffe agevolate» del calcolo.
- Valori nuovi nello script 103 (`riepilogo.mese`): due casi per l'auto (sosta pagata 307 euro, di cui carburante 35 e sosta 272; parcheggio gratis 35 euro di solo carburante, costo pieno 132), mezzi (40 biglietti 80, mensile 38, annuale diviso 12 = 26), agevolati. Rilancio completo di 103: gli altri numeri uguali; le lunghezze fuori ±10% dal servizio di navigazione passano da 11 a 12 su 17 (il servizio risponde con piccole differenze), nessun effetto sui costi.

## Controlli
- `python scripts\04_genera_mappa.py` (5.960.871 byte, come prima), `python scripts\schede_risultati.py` (nessuna ATTENZIONE), `python -m pyflakes scripts` zero, `node --check assets\*.js` zero.
- `python scripts\prova_pagine.py --playwright`: 0 errori su 21 pagine; prove L15-L22 tutte OK; anteprime `assets/anteprime/r1,r2,r4,r5,r6.jpg` e immagini del README rifatte.
- Prove nuove o cambiate: `design_l17` (due gruppi in home e in risultati con i numeri giusti IT ed EN, nessuna fascia «Il progetto», nessun «In breve», link a `progetto.html`), `design_l22` (progetto.html invariata e senza cifre mancanti, nessun «12 punti» nel testo visibile dei costi, grafico del mese con Under 26 e Over 65, fonte GTT e data nella parte chiusa, `r/N.html` e `#rN` coi numeri nuovi), `design_l16` e `design_l21` passate agli id interni.

## Da guardare (Leo)
Home con i due gruppi, `risultati.html`, scheda dei costi (grafico del mese, titolo), `progetto.html` (bottoni «Risultato 4» e «Risultato 2»). Fuori da L22: gerarchia dei riquadri, ISEE e requisiti delle tariffe agevolate da riconfermare sul sito GTT.
