# Esito del giro L21 (25/10/2026, sul PC di Leo)

Decisione di Leo (25/10): permesso speciale per TomTom; il nome sparisce dal testo e resta solo nelle fonti. Nessun controllo grafico, niente telefono.

## 1. TomTom fuori dal testo visibile
- Testi cambiati in `scripts/schede/comune.py`, `r6.py`, `r8.py`, `r12.py`, `testi.json` (IT e EN, chiavi e valori) e `assets/progetto.js`; i commenti del codice, i nomi di variabili e le chiavi JSON (`tomtom`, `limite_basso`) non sono stati toccati. `area.js`, `gara.js` e `mappa_template.html` avevano il nome solo nei commenti: invariati. README e `r/N.html` vengono dalle schede.
- Formule: «tempi di percorrenza in auto con il traffico tipico» (EN: car travel times with typical traffic); «fattore TomTom» -> «fattore di traffico»; «stima TomTom» -> «stima col traffico tipico»; nella scheda 6 «controllato con un servizio di navigazione su 17 percorsi»; «Dati di traffico: TomTom.» tolto dal calcolo.
- Campo nuovo `fonti` in ogni scheda (`FONTI_NOMI` e `FONTI_SCHEDA` in `comune.py`, IT ed EN), mostrato in `risultati.html` come ultima riga della parte chiusa («Fonti: ...»). Il nome TomTom compare solo lì, nelle schede 3, 4 e 6: «TomTom (tempi di percorrenza in auto, uso autorizzato)». Le schede 1, 2 e 5 citano GTT, Comune di Torino, ISTAT, 5T, agenzia della mobilità piemontese, Agenzia delle Entrate, OpenStreetMap; la 6 anche carburanti e ACI; la 4 anche Google Maps (3 percorsi a mano).
- Prima/dopo (menzioni di TomTom fuori dalla riga Fonti nella forma IT / EN): scheda 3: 8 / 8 -> 1 / 1 (resta la chiave `pareggio.tomtom`, non visibile); scheda 4: 12 / 12 -> 0 / 0; scheda 6: 3 / 3 -> 0 / 0; schede 1, 2, 5: 0.
- `docs/FONTI_DATI.md`: «uso con permesso di TomTom (Leo, 25/10/2026)». Memoria: condizione per `main` chiusa (le note tecniche in `docs/R*.md` e `docs/rapporti/` mantengono il nome). Nota: nel giro L20 le due modifiche alla memoria sul punto TomTom non erano state scritte; rifatte ora.
- `git grep -i tomtom` su `*.html`, `assets/`, `testi.json`, `README.md`, `r/`: restano solo commenti del codice, la chiave `pareggio.tomtom` e la voce «TomTom (...)» di `FONTI_NOMI` (la riga Fonti).

## 2. Prova nuova
`design_l21` in `prova_pagine.py` (dentro `prova_design`): nessun «TomTom» nel testo di home, progetto e schede 1-6, IT ed EN, parte chiusa compresa, fuori dalla riga Fonti; la riga Fonti c'è in ogni scheda ed è l'ultima della parte chiusa; nelle schede 3, 4 e 6 cita il fornitore dei tempi in auto. OK.

## 3. Rilancio e prove
`04_genera_mappa.py` (0), `schede_risultati.py` (nessuna ATTENZIONE), `pyflakes scripts` (zero), `node --check assets\*.js` (zero errori), `prova_pagine.py --playwright`: 0 errori su 21 pagine, prove L15-L18, L20, L21 OK; anteprime e immagini del README rifatte.

## 4. Prova da zero con la Release `dati-2026-11`
Ora è **pubblicata** (5 file). Clone di `prova` in una cartella temporanea, `scarica_dati.py` (3 zip, hash OK, 220 file scritti), `rifai_tutto.py --solo schede`: `data/schede_risultati.js` e `r/*.html` **identici** a quelli di prova, salvo «generato». Cartella cancellata.

## 5. Pages
`https://campeseleonardo-tech.github.io/Turin-mobility/` risponde 200; `r/1.html`-`r/5.html` 200; `r/6.html` 404 finché `main` non è aggiornato.
