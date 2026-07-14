# Bau-Anleitung für Monographien

**Für Claude Code.** Diese Datei ist die verbindliche Spezifikation. Jede erzeugte Monographie muss ihr entsprechen und das Prüfskript `validate_monographie.py` fehlerfrei durchlaufen.

---

## Grundregeln — nicht verhandelbar

**1. Recherchiere, erfinde nicht.**
Vor jeder Monographie: EMA/HMPC-Monographie der Art suchen, ESCOP und Kommission E prüfen. Wenn du eine Angabe nicht belegen kannst, schreibe `"unsicher — zu prüfen"` statt einer Behauptung. Ein leeres, ehrliches Feld ist besser als ein gefülltes, falsches.

**2. Verwechslungen sind sicherheitskritisch.**
Das Feld `confusions` darf **niemals** stillschweigend leer bleiben. Recherchiere aktiv nach giftigen Doppelgängern. Gibt es wirklich keine, schreibe einen Eintrag mit `"name": "keine relevante Verwechslung bekannt"` und begründe kurz. Ein leeres Array sieht aus wie „ungefährlich" — das ist die gefährlichste Lüge, die diese Datei erzählen kann.

**3. Evidenz nicht schönen.**
`WEU` (well-established use) nur, wenn die HMPC-Monographie das ausdrücklich so führt. Im Zweifel `TU`. Populärer Ruf ist kein Evidenzgrad.

**4. Jede Indikation braucht eine Quelle.**
Feld `source` — konkret: „HMPC traditional use", „ESCOP", „Kommission E", „Cochrane Review 2016". Nicht „Studien zeigen".

**5. Alles auf Deutsch.** Fachbegriffe medizinisch korrekt.

---

## Evidenz-Skala (feste Werte für `evidence_tag`)

| Tag | Bedeutung |
|---|---|
| `WEU` | HMPC well-established use — wissenschaftlich hinreichend belegt |
| `RCT` | Eigene randomisiert-kontrollierte Studienevidenz |
| `ESCOP+` | Positive ESCOP-Monographie |
| `TU` | HMPC traditional use — langjährige Anwendung, keine belastbare Evidenz |
| `PRÄ` | Nur präklinisch (in vitro / Tiermodell) |
| `TRAD` | Rein volksmedizinisch |

Kombination mit Schrägstrich erlaubt: `TU/ESCOP+`, `WEU/RCT`.

---

## Sicherheits-Flags (Register-Steuerung)

Setze `true`, wenn zutreffend — diese Flags speisen die Querschnitts-Register der App:

| Flag | Wann |
|---|---|
| `deadly_confusion` | Tödlich giftiger Doppelgänger existiert |
| `toxin_ceiling` | Toxin mit Dosis-/Zeitgrenze (dann `toxin_type` setzen: „Thujon", „Pyrrolizidinalkaloide", „Cumarin", „β-Asaron" …) |
| `raw_toxicity` | Roh giftig, Erhitzen nötig |
| `requires_heating` | siehe oben |
| `hepatotoxic` | Lebertoxizität |
| `pregnancy_contraindicated` | In Schwangerschaft kontraindiziert |
| `interaction_heavy` | Klinisch relevante Arzneimittelinteraktionen |
| `cyp3a4_inducer` / `pgp_inducer` | Enzym-/Transporter-Induktion |
| `serotonergic` | Serotonerges Potenzial |
| `lowers_seizure_threshold` | Senkt Krampfschwelle |
| `photosensitizing` | Lichtsensibilisierung |
| `asteraceae_allergy` | Korbblütler — Kreuzallergie |
| `apiaceae_confusion_young` | Doldenblütler, jung schwer bestimmbar |
| `topical_only` | Nur äußerlich anwenden |
| `high_safety` | Sehr sicher: keine Verwechslung, kein Toxin, kaum Interaktionen |
| `infant_facial_caution` | Öl nicht ins Gesicht von Kleinkindern |
| `not_for_use` | **Giftpflanze — Warneintrag, keine Anwendung** (Stufe-3-Arten) |

---

## Dateikonvention

- **Dateiname:** `monographie-<deutscher-name>.json` — klein, ohne Umlaute (`monographie-baerlauch.json`)
- **`id`:** botanisch, `gattung-art`, klein, mit Bindestrich (`allium-ursinum`)
- Die `id` muss **exakt** Gattung + Art des akzeptierten Namens sein — die App gleicht Pl@ntNet-Treffer darüber ab.
- Achtung Taxonomie: Rosmarin ist heute *Salvia rosmarinus*, nicht *Rosmarinus officinalis*. Prüfe den **aktuell akzeptierten** Namen.

---

## Schema

```json
{
  "schema_version": "1.0",
  "id": "gattung-art",

  "botany": {
    "scientific_name": "Gattung art",
    "common_names_de": ["Hauptname", "Nebenname"],
    "family": "Familie (deutsch in Klammern)",
    "drug_part": ["Blatt (Folium)", "Wurzel (Radix)"],
    "drug_name_latin": "Drogenname",
    "synonym_note": "nur falls Taxonomie sich geändert hat"
  },

  "identification": {
    "key_features": ["4–6 Merkmale, das SICHERSTE zuerst"],
    "season": "Blütezeit",
    "habitat": "Standort",
    "region_occurrence": [
      {"region": "Bodensee/Voralpen", "status": "wild-haeufig | wild-selten | kultur-und-verwildert | nur-kultur"}
    ],
    "collection_rules": ["Bestätiger-Merkmale, Abgrenzung zu Doppelgängern"]
  },

  "confusions": [
    {
      "name": "Deutscher Name",
      "scientific_name": "Gattung art",
      "toxicity_level": "essbar | giftig | lebensgefährlich",
      "toxin": "Toxin, falls giftig",
      "note": "WIE unterscheiden — konkret und feldtauglich"
    }
  ],

  "chemistry": {
    "main_groups": ["Stoffgruppen mit Gehalt, wenn bekannt"],
    "lead_substance": "Leitsubstanz + Wirkbezug",
    "solubility_note": "Was heißt das für die Zubereitung? (Tee vs. Öl vs. Tinktur)",
    "heat_light_sensitivity": ""
  },

  "pharmacology": {
    "mechanism": "Wirkmechanismus, soweit belegt",
    "evidence_caveat": "Wo ist die Datenlage schwach? Ehrlich sein.",
    "pharmacokinetics": ""
  },

  "indications": [
    {
      "canonical": "Medizinischer Fachbegriff",
      "synonyms": ["umgangssprachlich", "Laienbegriffe", "Symptomnamen"],
      "evidence_tag": "TU",
      "comment": "Regulatorische Einordnung",
      "realistic_expectation": "Was darf man erwarten — und was NICHT",
      "source": "HMPC traditional use; ESCOP"
    }
  ],

  "expectation_summary": {
    "plausible": "Was diese Pflanze wirklich kann",
    "overstated": "Womit sie überschätzt wird",
    "effect_size": "mild | moderat | stark; symptomatisch?"
  },

  "preparation": {
    "recommended_forms": ["Tee", "Tinktur", "Salbe", "Öl-Kapsel"],
    "form_rationale": "Aus der Chemie abgeleitet: WARUM diese Form?",
    "standard_dose": "Konkret, mit Zeitgrenze falls nötig",
    "preservation": ""
  },

  "safety": {
    "tox_ceiling": "Toxin, Grenzwert, maximale Anwendungsdauer",
    "contraindications": ["konkret"],
    "pregnancy_lactation": "",
    "adverse_effects": "",
    "interactions": [
      {"type": "pharmakokinetisch | pharmakodynamisch | theoretisch",
       "mechanism": "", "affected": "betroffene Arzneistoffe", "clinical_relevance": "hoch | relevant | gering"}
    ],
    "flags": { "siehe Flag-Tabelle": false },
    "key_warning": "Der EINE Satz, der im Feld zählt"
  },

  "harvest_processing_storage": {
    "harvest_time": "",
    "harvest_month_tags": [5, 6, 7],
    "harvest_organ": "Blatt | Blüte | Wurzel | Kraut | Frucht | Rinde",
    "method": "",
    "processing": "",
    "storage": ""
  },

  "kitchen": {
    "uses": [],
    "culinary_vs_medicinal": "Wo verläuft die Grenze?"
  },

  "garden": {
    "site_soil": "",
    "hardiness": "",
    "propagation": "",
    "bodensee_suitability": "Ehrlich — auch wenn ungeeignet"
  },

  "images": [
    {"role": "habitus", "caption": "", "url": "", "source": "", "license": ""},
    {"role": "diagnostic", "caption": "", "url": "", "source": "", "license": ""}
  ],

  "user_layer": {"notes": "", "own_photos": [], "found_locations": [], "garden_status": ""},

  "sources": ["EMA/HMPC …", "ESCOP …", "Kommission E …"]
}
```

---

## Sonderfall: Warneinträge (Stufe 3, Giftpflanzen)

Für Herbstzeitlose, Maiglöckchen, Schierling, Fingerhut, Eisenhut, Tollkirsche, Riesen-Bärenklau, Rosmarinheide:

- `indications`: **leeres Array** — diese Pflanzen haben keine Selbstanwendung
- `flags.not_for_use`: `true`
- `key_warning`: unmissverständlich, was passiert
- `confusions`: die **Nutzpflanzen**, mit denen sie verwechselt werden (umgekehrte Richtung!)
- `expectation_summary.plausible`: `"Keine Anwendung. Dieser Eintrag dient der Erkennung und Warnung."`
- Merkmale besonders sorgfältig — das ist der Zweck des Eintrags

---

## Ablauf pro Kraut

1. Art aus `kraeuter-kandidaten.md` nehmen (Stufe 1 zuerst)
2. **Recherche:** HMPC-Monographie, ESCOP, Kommission E — belegen, nicht raten
3. **Verwechslungen aktiv suchen** — gerade bei Doldenblütlern und Zwiebelpflanzen
4. JSON schreiben
5. `python3 validate_monographie.py monographie-xyz.json` — muss fehlerfrei sein
6. In `fertig/` ablegen, Kraut in der Kandidatenliste abhaken

**Stapelgröße: 3–5 Kräuter.** Nicht mehr. Der Engpass ist die ärztliche Prüfung, nicht die Erzeugung.

---

## Was danach passiert

Jede Monographie ist ein **Entwurf**, bis der Nutzer (Arzt) sie geprüft hat. Er importiert sie in die App, wo sie als „importiert" markiert erscheint. Die sicherheitskritischen Felder — Verwechslungen, Toxin-Grenzen, Kontraindikationen — prüft er gegen HMPC/ESCOP nach.

**Schreibe entsprechend defensiv.** Lieber ein „unsicher — zu prüfen" zu viel als eine erfundene Gewissheit.
