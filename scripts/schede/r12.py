"""Risultato 12 (pubblico 6): quanto costa muoversi, in auto e coi mezzi pubblici."""
from schede.comune import circa, forma_base, leggi, num, ora, virgola


# ---------------------------------------------------------------- Risultato 12 (pubblico: 6) «Quanto costa muoversi»
# Tutti i numeri vengono da data/processed/costo_del_viaggio.json (script 103) e dai prezzi di data/ref/costi.json; qui niente e' scritto a mano.

def euro(x):
    """Importo con due decimali e la virgola: 13.6 -> «13,60»."""
    return f"{x:.2f}".replace(".", ",")


def dec(x, n):
    """Numero con n decimali e la virgola: dec(2.004, 3) -> «2,004»."""
    return f"{x:.{n}f}".replace(".", ",")


def euro_intero(x):
    return str(round(x))


def circa_dieci(x):
    """Arrotonda alla decina per i titoli: 269 -> «270»."""
    return str(int(round(x, -1)))


def nome_punto(n):
    """«PONTE CAVALIERI TEMPLARI» -> «Ponte Cavalieri Templari»."""
    return n.title().replace(" Di ", " di ").replace(" Fs", " FS")


def scheda_r12():
    j = leggi("costo_del_viaggio.json")
    r = j["riepilogo"]
    return {
        "risultato": "12",
        "titolo": "Quanto costa muoversi",
        "tag": "STIMATO / PREZZI",
        "stato": "Fatto",
        "in_breve": "Quanto costa andare in centro in auto e quanto coi mezzi pubblici, coi prezzi di oggi?",
        "domanda": "Quanto costa andare in centro in auto e quanto coi mezzi pubblici, oggi?",
        "numero_chiave": {"valore": round(r["differenza_mese_sente_mediana"]), "unita": "euro",
                          "testo": "in più al mese per andare al lavoro in centro in auto invece che coi mezzi"},
        "racconto": "", "risposta": [], "grafici": [], "metodo": [], "limiti": [], "parametri": [],
        "mappa": None,
        "fonti": ["docs/rapporti/RAPPORTO_COSTO_DEL_VIAGGIO.txt", "data/processed/costo_del_viaggio.json", "data/ref/costi.json"],
        "generato": ora(),
        "avviso": ["Dati [STIMATO]: prezzi di ottobre 2026 e chilometri della rete stradale. Costo medio di una Golf, non della propria auto."],
        "in_english": [],
        "scenari": [{
            "nome": "Oggi",
            "numeri": [
                num("Auto, lavoro in centro (costo che si sente, al mese)", round(r["auto_mese_sente_mediana"], 1), "euro"),
                num("Auto, costo pieno (al mese)", round(r["auto_mese_pieno_mediana"], 1), "euro"),
                num("Mezzi pubblici, abbonamento (al mese)", r["mezzi_mese"], "euro"),
                num("Minuti in più coi mezzi (mediana)", r["minuti_in_piu_mediana"], "min"),
            ],
            "nota": "Mediana dei 12 punti prioritari del risultato 3, verso Piazza Castello.",
        }],
    }


def forma_r12(s):
    j = leggi("costo_del_viaggio.json")
    r, pr, reg = j["riepilogo"], j["prezzi"], j["regole"]
    gm, ore_l, ore_c = reg["giorni_mese"], reg["ore_sosta_lavoro"], reg["ore_sosta_commissione"]
    sente, mezzi = r["auto_mese_sente_mediana"], r["mezzi_mese"]
    diff = r["differenza_mese_sente_mediana"]
    diff_pieno = r["differenza_mese_pieno_mediana"]
    # un mese di lavoro in centro, due casi per l'auto (sosta pagata in strada, parcheggio gratis al lavoro) e i tipi di abbonamento dei mezzi
    m = r["mese"]
    sp, pg, mz = m["sosta_pagata"], m["parcheggio_gratis"], m["mezzi"]
    ag = {a["id"]: a for a in mz["agevolati"]}

    def voce_auto(label, sente, pieno):
        return {"label": label, "valore": round(sente), "prima": round(pieno), "tono": "rosso", "testo": f"{round(sente)} ({round(pieno)} col costo pieno)"}

    def voce_mezzi(label, euro_mese):
        return {"label": label, "valore": round(euro_mese), "tono": "verde", "testo": str(round(euro_mese))}
    graf_mese = {"tipo": "barre_gruppi", "titolo": "Un mese di lavoro in centro: auto e mezzi pubblici", "unita": "euro",
                 "nota": "La barra chiara è il costo pieno dell'auto. Le tariffe agevolate sono quelle GTT per giovani e anziani, con certificato ISEE.",
                 "gruppi": [{"label": "Auto, sosta pagata in strada", "voci": [voce_auto("Carburante e sosta", sp["sente"], sp["pieno"])]},
                            {"label": "Auto, parcheggio gratis al lavoro", "voci": [voce_auto("Solo carburante", pg["sente"], pg["pieno"])]},
                            {"label": "Mezzi pubblici", "voci": [voce_mezzi(f"Biglietti ({reg['viaggi_abbonamento']} viaggi)", mz["biglietti"]),
                                                              voce_mezzi("Abbonamento mensile", mz["mensile"]),
                                                              voce_mezzi("Abbonamento annuale, al mese", mz["annuale_su_12"])]},
                            {"label": "Mezzi pubblici, tariffe agevolate",
                             "voci": [voce_mezzi(ag[i]["nome"], ag[i]["eur_mese"]) for i in ("under26_mensile", "under26_annuale_a", "over65_mensile", "over65_annuale_d")]}]}
    fasce = j["fasce_distanza"]

    def etichetta_fascia(f):
        if f["a_km"] is None:
            return f"Oltre {round(f['da_km'])} km ({f['coppie']} coppie)"
        if f["da_km"] == 0:
            return f"Sotto {round(f['a_km'])} km ({f['coppie']} coppie)"
        return f"Da {round(f['da_km'])} a {round(f['a_km'])} km ({f['coppie']} coppie)"
    graf_fasce = {"tipo": "barre_gruppi", "titolo": "Un mese di lavoro tra due zone di Torino, per distanza: auto e mezzi pubblici", "unita": "euro",
                  "nota": "Solo il carburante e il costo pieno, senza parcheggio: la barra chiara è il costo pieno dell'auto.",
                  "gruppi": [{"label": etichetta_fascia(f), "voci": [
                      {"label": "Auto", "valore": round(f["auto_sente_mese"]), "prima": round(f["auto_piena_mese"]), "tono": "rosso",
                       "testo": f"{round(f['auto_sente_mese'])} ({round(f['auto_piena_mese'])} col costo pieno)"},
                      {"label": "Mezzi pubblici", "valore": round(f["mezzi_mese"]), "tono": "verde", "testo": str(round(f["mezzi_mese"]))}]} for f in fasce]}
    graf_commissione = {"tipo": "barre", "titolo": f"Una commissione in centro ({ore_c} ore di sosta): costo di andata e ritorno", "unita": "euro",
                        "nota": "Mediana dei viaggi dai punti d'ingresso in città a Piazza Castello. Il costo pieno comprende anche assicurazione, usura e perdita di valore.",
                        "voci": [{"label": "Auto, costo che si sente", "valore": round(r["commissione_auto_sente_mediana"], 1), "tono": "rosso",
                                  "testo": euro(r["commissione_auto_sente_mediana"])},
                                 {"label": "Auto, costo pieno", "valore": round(r["commissione_auto_piena_mediana"], 1), "tono": "arancio",
                                  "testo": euro(r["commissione_auto_piena_mediana"])},
                                 {"label": "Mezzi pubblici, 2 biglietti", "valore": round(r["commissione_mezzi"], 1), "tono": "verde",
                                  "testo": euro(r["commissione_mezzi"])}]}
    anno_auto, anno_mezzi = sente * 12, mezzi * 12
    return forma_base(
        s,
        f"Con la sosta pagata, andare al lavoro in centro in auto costa circa {circa_dieci(diff)} euro al mese più dei mezzi",
        "Quanto costa andare in centro in auto e quanto coi mezzi pubblici, oggi?",
        {"valore": round(diff), "unita": "euro",
         "testo": f"in più al mese dei mezzi pubblici, in auto con la sosta pagata in strada. Col costo pieno dell'auto sono {circa(diff_pieno, ' euro')}.",
         "breve": "in più al mese, in auto"},
        graf_commissione,
        [f"Il parcheggio pesa più di tutto: {ore_l} ore in centro costano {euro(r['parcheggio_lavoro_giorno'])} euro al giorno, il carburante {euro(r['carburante_giorno_mediana'])} euro.",
         f"Con il parcheggio gratis al lavoro l'auto costa {circa(pg['sente'], ' euro')} al mese di carburante, l'abbonamento tra {euro_intero(mz['annuale_su_12'])} e {euro_intero(mz['mensile'])} euro.",
         f"Coi mezzi pubblici si impiegano {circa(r['minuti_in_piu_mediana'], ' minuti')} in più a ogni viaggio."],
        [graf_mese, graf_fasce],
        [f"Prezzi del {j['consultato'][8:10]}/{j['consultato'][5:7]}/{j['consultato'][:4]}. Carburante: media self degli impianti entro 5 km da Piazza Castello (Osservatorio prezzi). Tariffe GTT e sosta dalle pagine ufficiali, costo ACI 2026 della Gazzetta Ufficiale.",
         "Auto che si sente: chilometri × consumo urbano × prezzo del carburante, andata e ritorno, più il parcheggio. Auto piena: chilometri × costo ACI per chilometro, più il parcheggio.",
         f"Auto di riferimento: la stessa Golf da 115 CV, a benzina e a gasolio. Consumo in città: {virgola(pr['consumo_urbano_benzina'])} e {virgola(pr['consumo_urbano_gasolio'])} litri ogni 100 km. Il costo è la media delle due.",
         f"Lavoro: {gm} giorni al mese, {ore_l} ore di sosta a tariffa ordinaria ({euro(pr['sosta_ordinaria_ora'])} euro l'ora). Se il parcheggio è gratis, solo carburante.",
         f"Mezzi pubblici: abbonamento mensile urbano ({euro_intero(pr['abbonamento_mensile'])} euro), {reg['viaggi_abbonamento']} biglietti da {euro(pr['biglietto_urbano'])} euro o abbonamento annuale diviso 12.",
         f"Tariffe agevolate GTT: pagine ufficiali del {j['consultato'][8:10]}/{j['consultato'][5:7]}/{j['consultato'][:4]}, senza data di validità. "
         f"Under 26: mensile {euro_intero(ag['under26_mensile']['eur_mese'])} euro, annuale {euro_intero(ag['under26_annuale_ordinario']['eur_anno'])} euro, da {euro_intero(ag['under26_annuale_a']['eur_anno'])} a {euro_intero(ag['under26_annuale_c']['eur_anno'])} con ISEE. "
         f"Over 65: mensile {euro_intero(ag['over65_mensile']['eur_mese'])} euro, annuale da {euro_intero(ag['over65_annuale_a']['eur_anno'])} a {euro_intero(ag['over65_annuale_d']['eur_anno'])} euro con ISEE.",
         f"Commissione: {ore_c} ore di sosta contro 2 biglietti urbani ({euro(pr['biglietto_urbano'])} euro l'uno).",
         f"Punti: i {r['punti']} punti d'ingresso in città dei parcheggi verso Piazza Castello. Coppie: {r['coppie_torino']} coppie di zone di Torino, senza parcheggio. "
         f"Chilometri: percorso più veloce sulla rete stradale, controllato con un servizio di navigazione su {r['tomtom_percorsi']} percorsi. Minuti in più: dal confronto di tempi tra mezzi pubblici e auto, alle 8."],
        [["Carburante, self, prezzo del giorno", f"benzina {dec(pr['benzina_self_eur_l'], 3)}, gasolio {dec(pr['gasolio_self_eur_l'], 3)} euro al litro"],
         ["Consumo in città", f"benzina {dec(pr['consumo_urbano_benzina'], 1)}, gasolio {dec(pr['consumo_urbano_gasolio'], 1)} litri ogni 100 km"],
         ["Costo pieno ACI", f"benzina {dec(pr['aci_benzina_eur_km'], 4)}, gasolio {dec(pr['aci_gasolio_eur_km'], 4)} euro al km"],
         ["Mezzi pubblici", f"biglietto {euro(pr['biglietto_urbano'])} euro, abbonamento mensile {euro_intero(pr['abbonamento_mensile'])} euro"],
         ["Sosta in centro", f"{euro(pr['sosta_ordinaria_ora'])} euro l'ora, tariffa ordinaria"]],
        ["Carburante: prezzi del giorno, non la media di 4 settimane. Una Golf di consumo medio, non la propria auto.",
         "La zona a traffico limitato e gli abbonamenti alla sosta non contano; vale la tariffa ordinaria. Solo Torino: le tariffe a zone della cintura non sono assegnate alle zone dell'indagine.",
         "Le tariffe agevolate valgono solo con i requisiti (età, ISEE, residenza a Torino); la data delle tariffe non è pubblicata.",
         f"Chilometri: su {r['tomtom_fuori']} dei {r['tomtom_percorsi']} percorsi il servizio di navigazione dà una lunghezza diversa di oltre il 10%. Pesa poco: il parcheggio vale la maggior parte del costo."],
        anima={"tipo": "contatori", "mesi": 12, "etichetta": "mesi di lavoro",
               "righe": [{"label": "Auto", "mese": round(sente, 1), "tono": "rosso"}, {"label": "Mezzi pubblici", "mese": round(mezzi, 1), "tono": "verde"}],
               "didascalia": f"In un anno di lavoro in centro: {circa(anno_auto, ' euro')} in auto, {euro_intero(anno_mezzi)} euro coi mezzi pubblici (costo che si sente)."},
        )
