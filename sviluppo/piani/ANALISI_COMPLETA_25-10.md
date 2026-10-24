# Analisi completa del progetto (25/10/2026, dopo L22)

Fatta da zero su `origin/prova` = `main` (b4de3f3), nel cloud. Ho letto il sito com'è oggi (testi delle 6 schede, home, risultati, progetto, mappa) e il codice e i dati che lo producono.
Ho rifatto le schede, che escono identiche, e ho lanciato le prove delle pagine e il controllo automatico di GitHub.
Niente giudizi sulla grafica vista (li fa Leo): solo struttura, testi, numeri, metodi.
Ogni punto ha la sua prova (file, riga, numero). Gravità: **alta** = può far perdere credibilità o dare un'informazione sbagliata; **media** = indebolisce; **bassa** = rifinitura.

## In breve

**Cosa funziona.**
- Il sito è online, rifacibile da zero (Release `dati-2026-11`, prova del 25/10: schede identiche), con 6 risultati, una mappa, una storia (`progetto.html`) e una raccolta vera e continua (Raspberry Pi, GPS ogni minuto).
- Le regole dei calcoli sono scritte prima dei numeri e rispettate anche quando danno «non valutabile» (L13): è raro e vale molto.
- Testi chiari, numeri sempre scritti, fonti in ogni scheda.

**Le 5 criticità più importanti.**
1. **Il controllo automatico su GitHub è rosso da 25 commit** (dal 23/10 sera, L9b), e il badge rosso è in cima al README. Tre cause, tutte piccole.
2. **Il numero grande dei costi (269 euro) è quasi tutto un'ipotesi:** 272 euro su 307 sono 8 ore di sosta in strada × 1,70 euro × 20 giorni. Il dato raccolto (carburante, chilometri) pesa 35 euro. In più la destinazione, Piazza Castello, sta nella ZTL, dove in auto non si entra.
3. **Il gruppo «Per decidere» è quello con i numeri meno solidi:** modelli, stime e campioni piccoli. Il gruppo «Cosa dicono i dati» è quello misurato. Dopo L15 i margini d'incertezza si vedono solo nella parte chiusa.
4. **I tempi coi mezzi pubblici delle schede 2 e 3 usano l'orario programmato,** mentre la scheda 5 misura che il 16% dei passaggi arriva oltre 5 minuti tardi. L'obiettivo scritto del progetto («i dati misurati devono calibrare quelli simulati») non è applicato proprio dove servirebbe: il rapporto 1,9 è ottimista per i mezzi.
5. **Il 35% dei passaggi «in anticipo di oltre 1 minuto»** è nel grafico principale della scheda 5 senza spiegazione. Se è vero è un risultato forte (un bus in anticipo fa perdere la corsa); se è un effetto della misura, è un errore in vista.

**Le priorità che suggerisco** (dettagli nel § 9):
1. controllo automatico verde;
2. scheda dei costi onesta (numero grande sul caso senza sosta o con una forbice, destinazione fuori ZTL);
3. tempi dei mezzi corretti coi ritardi misurati;
4. spiegare l'anticipo;
5. poi LinkedIn.

---

## 1. Obiettivi: cosa si voleva e cosa c'è

Obiettivo scritto (memoria, § 1): «capire come funziona la città (chi va dove, dove mancano servizi, dove sono le criticità) + pochi scenari "cosa succede se"»; «i dati MISURATI devono calibrare quelli simulati»; racconto «la tesi era la promessa, il progetto è la verifica».

| Obiettivo | Dove sta oggi | Giudizio |
|---|---|---|
| Chi va dove | Solo nella mappa (tema «Spostamenti», indagine 2022); nessuna scheda | **manca un risultato**: il «chi va dove» è il primo obiettivo ed è il meno visibile |
| Dove mancano servizi | Schede 6 (15 minuti) e 4 (fragilità), mappa | c'è, ma la scheda 6 dice soprattutto che i servizi non mancano (99,2%) |
| Criticità del trasporto | Schede 5 (ritardi), 2 (bus contro auto), 3 (parcheggi) | c'è |
| Scenari «cosa succede se» | Solo i «punti nuovi» della mappa (scheda 6, «fino a 5») | **quasi assente**: l'obiettivo dice «pochi scenari», sul sito non se ne vede nessuno come risultato |
| Misurato che calibra il simulato | Il GPS misura ritardi e velocità (scheda 5), ma i tempi dei mezzi delle schede 2 e 3 restano da orario | **non fatto** (vedi § 3.2) |
| Tesi → verifica | `progetto.html`, tappa «I dati ci sono, ma vanno controllati» | c'è, ma la prova più forte (feed GTT contro GPS) è stata tolta dalla scheda 5 in L22 e resta solo nel testo chiuso |

---

## 2. Stato tecnico

| # | Cosa | Prova | Gravità |
|---|---|---|---|
| 2.1 | **Controllo automatico rosso** su `prova` e `main` dal commit L9b (23/10 sera, 25 esecuzioni rosse di fila). Il badge in cima al README è rosso. | Azioni GitHub, esecuzioni 26-57. Rifatto nel cloud: (a) `prova_traduzione.py`: «PROBLEMA: R12: numero in formato italiano in "petrol 2.004, diesel 2.249 euros per litre"» (in inglese 2.004 è giusto, ma la prova lo legge come «duemilaquattro»: scrivere 2.00 / 2.25 o insegnare alla prova i prezzi); (b) `prova_funzioni_comuni.py`: «24_importanza_vie.py: non importa più da comuni.py» (L9b ha cambiato lo script 24); (c) `99_area_tempi.py --finto`: «manca imq_zone_geo.json» (L12 l'ha tolto da git, la prova finta lo cerca ancora). | **alta** (si vede subito, per un selezionatore vuol dire «non mantenuto») |
| 2.2 | I giri lanciavano `prova_pagine.py` ma non i passi del controllo di GitHub: nessuno se n'è accorto per 25 commit. | `ESITO_L20`, `L21`, `L22`: «prove verdi», ma solo pagine e pyflakes | media (di metodo) |
| 2.3 | `prova_pagine.py` riscrive ogni volta immagini in git (`assets/anteprime/`, `assets/readme/`): dopo una prova il repository risulta cambiato anche se niente è cambiato. | prove del 25/10 nel cloud: 5 anteprime e 3 immagini cambiate | bassa |
| 2.4 | Righe inutili in `scripts/schede/testi.json` (dei grafici tolti), lasciate «innocue». | `ESITO_L22` | bassa |
| 2.5 | 6 rami `claude/*` già uniti, ancora su GitHub. | `git branch -r` | bassa |
| 2.6 | Peso: mappa 5,96 MB (2,3 compressa), home 0,57 MB, repository 146,6 MB, 478 file. | `prova_pagine.py` | ok |

---

## 3. Risultati, uno per uno

### 3.1 Scheda 1 — «Quanto costa muoversi» (gruppo Per decidere)
| # | Problema | Prova | Gravità |
|---|---|---|---|
| a | **Il numero grande è un'ipotesi, non una scoperta.** 307 euro al mese in auto = 35 di carburante + 272 di sosta (8 h × 1,70 euro × 20 giorni). Il risultato è quasi tutto la moltiplicazione di una tariffa. | `costo_del_viaggio.json`, `ESITO_L22` («sosta pagata 307, di cui carburante 35 e sosta 272») | **alta** |
| b | **Chi va al lavoro in auto raramente paga 8 ore di strisce blu** (garage, parcheggio aziendale, abbonamenti alla sosta, che la scheda esclude). Il caso «parcheggio gratis» è nei punti, ma il titolo e il numero grande prendono il caso più caro. | limiti della scheda: «gli abbonamenti alla sosta non contano» | **alta** |
| c | **La destinazione è Piazza Castello, dentro la ZTL centrale**, dove senza permesso non si entra in auto nelle ore di lavoro; la tariffa usata (1,70) è quella fuori ZTL (dentro: 2,80). La scelta è scritta in `costi.json`, ma chi legge pensa «parcheggio in centro». | `data/ref/costi.json`, `sosta.scelta` | media |
| d | **Il risultato vero, che ora sta in un grafico secondario, è più interessante:** senza sosta l'auto costa meno dell'abbonamento sotto i 6 km (14 e 25 euro contro 38) e di più oltre i 6 km; col costo pieno l'auto perde sempre. È «il parcheggio decide», con una soglia di distanza. | grafico «tra due zone di Torino, per distanza» | opportunità |
| e | Tariffe agevolate scelte in modo diseguale: Under 26 alla fascia ISEE più bassa (13 euro), Over 65 alla più alta (16). | grafico del mese | bassa |
| f | Carburante di un solo giorno (24/10) invece della media di 4 settimane (sito del Ministero irraggiungibile). Lunghezze dei percorsi: 12 su 17 fuori ±10% dal servizio di navigazione (la nostra rete è più corta fino al 40%). Pesa poco sul costo, ma la stessa rete dà i tempi «a flusso libero» delle schede 2 e 3. | limiti; `ESITO_L20` § 2 | media (per le schede 2-3, § 3.2 d) |

### 3.2 Scheda 2 — «Bus contro auto» (Per decidere)
| # | Problema | Prova | Gravità |
|---|---|---|---|
| a | **Mezzi da orario programmato:** a piedi + bus/tram/metro con l'orario ufficiale, partenza 7:45-8:15. La scheda 5 dice che il 16% dei passaggi arriva oltre 5 minuti tardi e che alla fermata si aspetta ~1,5 minuti più del promesso. Il 1,9 è quindi **ottimista per i mezzi**. È l'obiettivo «il misurato calibra il simulato» non applicato. | calcolo della scheda 2; scheda 5 | **alta** (di metodo, ed è il risultato che i lettori di trasporti guardano per primo) |
| b | **Il numero vale per il 47% delle auto del mattino** (mancano i viaggi dentro una zona e fra comuni della cintura). È scritto solo nella parte chiusa; il titolo dice «al mattino» in generale. | calcolo, riga 6 | media |
| c | Il controllo con Google è su 2 percorsi (31 contro 30-35, 33 contro 30-35): utile ma piccolo. | calcolo | bassa |
| d | Tempo in auto = flusso libero sulla nostra rete × fattore di traffico + 5 min. Il fattore è misurato su una parte delle coppie; le altre prendono la mediana della fascia. Se la rete è più corta del vero (§ 3.1 f), il fattore lo compensa solo dove è stato misurato. | calcolo, criteri | media |
| e | Nei limiti c'è «Prova sulla scelta del mezzo senza esito» (L13): per chi legge è rumore, una prova fallita detta come limite. | limiti, riga 4 | bassa |
| f | «Vedi sulla mappa» porta al tema «Spostamenti» (quanti viaggi da ogni zona), che non mostra il rapporto bus/auto. | `mappa: imq` | bassa |

### 3.3 Scheda 3 — «Dove lasciare l'auto» (Per decidere)
| # | Problema | Prova | Gravità |
|---|---|---|---|
| a | **Il titolo è netto («2 su 3»), il dato no:** con metà o il doppio di chi lascia l'auto, le fermate senza posti vanno da 135 a 212 su 274 (da 1 su 2 a 3 su 4). Le auto che passano vengono da un modello che per luogo va d'accordo coi sensori solo in modo debole (0,60); la quota del 5,8% viene da 64 interviste. | limiti; memoria § 7 | **alta** (risultato da decisione, numero da modello) |
| b | **La scoperta più utile per decidere è nascosta in un grafico secondario:** i parcheggi di scambio che ci sono già sono pieni dove il bus è competitivo (Stura 39 contro 30, Venchi 28 contro 29) e vuoti dove non lo è (Sofia 33 contro 22, Caio Mario 38 contro 30). Cioè: **un parcheggio serve se il bus dopo è veloce**. È una regola di decisione e lega le schede 2 e 3. | grafico «I parcheggi di scambio che ci sono già» | opportunità |
| c | Due definizioni di «fermata importante»: nel calcolo «metro, stazione o capolinea, oppure 10 corse all'ora»; nei criteri «10 corse all'ora o metro, e 1.000 auto che passano». | calcolo riga 1, criteri riga 1 | media |
| d | «Pareggio: con 16 minuti persi a parcheggiare in centro» è un numero difficile da credere e da capire. | calcolo | bassa |

### 3.4 Scheda 4 — «Fragilità e servizi» (Cosa dicono i dati)
| # | Problema | Prova | Gravità |
|---|---|---|---|
| a | **Due coppie di soglie diverse:** numero grande per sezioni (fragilità sopra 57,7, servizi fino a 34,4) e analisi per zone OMI (49,8 e 33,4, «fissate prima dei numeri»). Si legge come un'incoerenza. | criteri | media |
| b | «Il 20% più alto» di fragilità per sezioni corrisponde al 26% dei residenti (sezioni non pesate per abitanti); il «1,7 volte il caso» è giusto: ricalcolato 9,48% osservato contro 5,7% atteso = 1,67. | barre della scheda | bassa (numeri giusti, da spiegare) |
| c | Due punti su tre parlano di prezzi delle case, che non sono nella domanda («Chi vive dove…»). Scelta di Leo (L22: «lascia tutto»): segnalo solo che il lettore si chiede perché. | punti | bassa |
| d | Numero esatto («79.598») per una stima che dipende da due soglie: «~80 mila» sarebbe più onesto. | numero grande | bassa |

### 3.5 Scheda 5 — «Ritardi dei mezzi» (Cosa dicono i dati)
| # | Problema | Prova | Gravità |
|---|---|---|---|
| a | **35% dei passaggi in anticipo di oltre 1 minuto** (feriale), nel grafico principale, senza una parola. Il passaggio è l'istante più vicino alla fermata (interpolato, entro 60 m), mentre l'orario GTT di solito indica la **partenza**: il tempo di sosta alla fermata spinge verso l'«anticipo». Va capito se è reale (orari larghi, cosa da dire) o della misura (da correggere). | `27_risultato4_regolarita.py:319-333`; grafico principale | **alta** |
| b | **GPS 6,4% contro GTT 2,3% oltre 10 minuti:** la spiegazione «stagione e metodo» è debole e il grafico del confronto è stato tolto in L22. Eppure è la prova più forte del racconto «i dati vanno controllati». | confronto nella parte chiusa | media |
| c | Pochi giorni: 7 feriali, 2 sabati, 1 domenica (P8 a metà novembre lo allunga). | limiti | media (programmato) |
| d | La velocità dei bus (~13 km/h alle 8) è un buon numero. Si potrebbe usare anche per correggere i tempi della scheda 2 (§ 3.2 a). | punto 1 | opportunità |

### 3.6 Scheda 6 — «Servizi a piedi» (Cosa dicono i dati)
| # | Problema | Prova | Gravità |
|---|---|---|---|
| a | **Il numero grande (99,2%) non distingue niente:** fermate e verde ci sono quasi ovunque (verde: 0 residenti senza; fermate: 100). Il dato informativo è quello a 5 minuti (68%) e chi è senza salute (5.340) o scuole (2.529) a 15 minuti. Il titolo «città dei 15 minuti» promette più di quello che si misura: nella definizione corrente ci sono anche lavoro e cultura. | barre della scheda | media (titolo scelto da Leo il 24/10) |
| b | **La domanda mischia due temi:** servizi a piedi e strade trafficate (222 mila residenti, da un modello con errore ±28%). | domanda, punto 2 | media |
| c | Soglia «strada molto trafficata: almeno 10.677 veicoli al giorno»: un numero troppo preciso per una soglia (è un percentile del modello). | nota del grafico | bassa |

---

## 4. Dati

| # | Cosa | Gravità |
|---|---|---|
| 4.1 | Periodi corti e diversi: GPS 10-22/10 (7 feriali), sensori 9-22/10, parcheggi 15-22/10, carburante 1 giorno, indagine spostamenti 2022, censimento 2021, OMI 2025/2. Ogni scheda lo dice, ma nessun risultato è «stagionale» né confrontato nel tempo. | media (P8 aiuta) |
| 4.2 | **TomTom:** permesso di Leo, scritto in `docs/FONTI_DATI.md`. In git e nella Release ci sono file con i risultati delle richieste (`tempi_traffico*.json`, fattori per percorso). Conviene conservare il permesso scritto (email) e controllare che copra anche la **ripubblicazione** di questi numeri in un repository pubblico, non solo l'uso. | media |
| 4.3 | IMQ e OMI fuori da git (L12): giusto. La prova finta dello script 99 li cerca ancora (§ 2.1 c). | — |
| 4.4 | Raccolta sul Pi: storico in crescita (~190 MB al giorno), copia intera ogni giorno sempre più lunga; decisione rinviata a novembre. Il GTFS statico GTT scade il 31/01/2027: l'archivio c'è (L4), ma il rilancio va pianificato. | media (con data) |
| 4.5 | Mancano per sempre (dati aperti): passeggeri e affollamento, treni SFM, bus extraurbani. Va bene dirlo; è già nei limiti. | — |

---

## 5. Metodi

- **Forti:** regole fissate prima dei numeri e rispettate (L13 «non valutabile»); intervalli per ricampionamento e confronto col caso (scheda 4); controlli a mano con Google (pochi); prova da zero riuscita; periodo fisso e numeri riproducibili.
- **Deboli:**
  - modello del traffico usato in 3 schede (1, 3 e strade trafficate della 6) con accordo debole per luogo (0,60);
  - mezzi solo da orario (§ 3.2 a);
  - stime in auto tutte da un solo servizio;
  - la scheda 3 regge su 64 interviste;
  - nessun risultato dice quanto cambia se cambia la regola più importante: ce l'hanno solo la 3 (135-212) e la 2 (sensori, nella parte chiusa).
- **Coerenza fra schede:** il tempo «a flusso libero» e il fattore di traffico sono gli stessi in 1, 2 e 3 (bene). I minuti in più coi mezzi sono ~11 nella 1 e 1,5 volte nella 3: compatibili ma raccontati diversamente.

---

## 6. Sito e racconto (struttura e testi, non grafica)

| # | Cosa | Gravità |
|---|---|---|
| 6.1 | **Gerarchia:** i 3 risultati «Per decidere» sono in testa e sono i più stimati. Dopo L15 (via etichette e riga «Limite») un lettore non vede quanto sono incerti: lo trova solo aprendo la parte chiusa. Proposta leggera: per i risultati da modello il numero grande con una forchetta («135-212») o la parola «circa», senza tornare alle etichette. | media |
| 6.2 | **Anteprime per LinkedIn** (`assets/anteprime/r1-6.jpg`): fatte in automatico da titolo e numero. Per i costi mostrano «269 euro» senza dire «con sosta pagata»: chi vede il post legge «l'auto costa 269 euro in più», e i commenti lo attaccheranno lì. | media (prima dei post) |
| 6.3 | Home: 6 riquadri in due gruppi, link al progetto; `risultati.html` più tecnica; `progetto.html` racconto. Struttura chiara. | ok |
| 6.4 | Il racconto «i dati vanno controllati» (punto forte del portfolio) è meno visibile di prima: il confronto feed GTT / GPS è uscito dalla scheda 5. | media |
| 6.5 | Inglese: completo per le schede (prova a ogni giro); la mappa resta in italiano (scelta). | ok |

---

## 7. Punti in sospeso (raccolti da piani, esiti, memoria)

| Cosa | Da quando | Chi |
|---|---|---|
| Controllo di GitHub rosso | 23/10 sera | agente |
| Media del carburante su 4 settimane (sito del Ministero irraggiungibile) | L20 | agente, a novembre |
| Tariffe agevolate GTT: data di validità non pubblicata | L22 | Leo (riconferma) |
| L13 scelta del mezzo: non valutabile; variante a giornata intera vista ma non usabile senza una regola nuova | L20 | Leo (lasciare com'è, consigliato) |
| P8: ritardi e attese con un mese di dati, Release di novembre | metà novembre | PC |
| Crescita dello storico sul Pi (storico per mese) | novembre-dicembre | Leo |
| GTFS nuovo (scade 31/01/2027): rilancio di accessibilità, 93, 94, 99, 100 | dicembre-gennaio | PC |
| Accessibilità 24 ore (~19 ore di calcolo) | P7 | PC, di notte |
| Gerarchia dei riquadri | rimandata da Leo | Leo |
| Tenere o no `risultati.html` / `progetto.html` | deciso: separate (L22) | chiuso |
| Rami `claude/*` da cancellare | ora | Leo |
| Post LinkedIn e Post Inspector | dopo il sito | Leo |
| Tema «Velocità e traffico» della mappa: medie del Pi senza scartare le letture inaffidabili (analisi del 23/10) | 23/10 | da ricontrollare |

---

## 8. Cosa aggiungere, togliere, cambiare

**Togliere / ridurre**
- Nella scheda 2, la riga «Prova sulla scelta del mezzo senza esito» (va nel documento R8).
- La seconda coppia di soglie della scheda 4 dal testo visibile (o spiegarla in una frase).
- Il numero troppo preciso «10.677 veicoli» e «79.598» (meglio «~80 mila»).

**Cambiare**
- Scheda dei costi: numero grande e titolo sul risultato vero: «Il parcheggio decide: senza sosta da pagare l'auto costa meno dell'abbonamento fino a ~6 km; con la sosta in strada ~270 euro in più al mese». Destinazione fuori dalla ZTL o detta chiaramente.
- Scheda 2: tempi dei mezzi corretti coi ritardi e le attese misurati (anche solo «+X minuti» medi per fascia): il rapporto diventa «misurato, non da orario».
- Scheda 3: titolo con la forchetta («da 1 su 2 a 3 su 4») e la regola «un parcheggio serve se il bus dopo è veloce» come punto chiave.
- Scheda 5: una riga che spiega l'anticipo (dopo averlo verificato) e il confronto con GTT di nuovo visibile, in una frase.
- Scheda 6: domanda solo sui servizi; numero grande a 5 o 10 minuti, o «chi resta senza».

**Aggiungere (risultati nuovi, già possibili coi dati)**
- **«Chi va dove»** (primo obiettivo, oggi solo nella mappa): i flussi principali del mattino dall'indagine 2022.
- **Uno scenario «cosa succede se»** (secondo obiettivo): per esempio un parcheggio di scambio a Santa Rita, quanti tempi cambiano; oppure un servizio aggiunto nei punti nuovi della scheda 6.
- **«Quanto ci si può fidare dei dati aperti»** (feed GTT contro GPS, orologi sbagliati, sensori esclusi): il punto più forte per un selezionatore, oggi disperso.
- **«Dove si fermano i bus»** (minuti persi fra due fermate, dal GPS): dato unico del progetto, utile per decidere (corsie, semafori).

---

## 9. Priorità dei prossimi passi (mio consiglio)

| # | Cosa | Perché ora | Lavoro | Dove |
|---|---|---|---|---|
| 1 | **Controllo di GitHub verde** (3 correzioni del § 2.1) e i passi del controllo dentro le prove di ogni giro | badge rosso visibile; prima dei post | piccolo | cloud |
| 2 | **Scheda dei costi onesta** (numero e titolo sul «parcheggio decide», destinazione fuori ZTL o detta, agevolate coerenti) e **anteprima r1** coerente | è il primo risultato in home e il più facile da attaccare nei commenti | piccolo-medio | PC (rilancio 103) |
| 3 | **Anticipo dei bus**: verificare arrivo/partenza alla fermata e spiegare (o correggere) | numero in vista nel grafico principale | piccolo-medio | PC (storico) |
| 4 | **Tempi dei mezzi coi ritardi misurati** nelle schede 2 e 3 | obiettivo dichiarato del progetto; rende il 1,9 «misurato» | medio | PC |
| 5 | Forchette nei numeri da modello (scheda 3) e piccoli testi (§ 8 «Togliere/ridurre») | onestà visibile, poco lavoro | piccolo | cloud |
| 6 | **LinkedIn**: anteprime riviste, Post Inspector, post (home, poi un risultato alla volta, partendo dai più solidi: ritardi e velocità dei bus, fragilità) | il sito è pronto dopo 1-3 | piccolo | Leo + Claude |
| 7 | Risultato nuovo «Quanto ci si può fidare dei dati aperti» | punto forte del portfolio | piccolo | PC |
| 8 | P8 a metà novembre; crescita dello storico; GTFS nuovo | date fisse | — | PC |
| 9 | «Chi va dove» e uno scenario «cosa succede se» | completano gli obiettivi scritti | medio | PC |
