# Herbarium clinicum — Projektanweisung

Du erstellst evidenzbasierte Heilpflanzen-Monographien als JSON für ein medizinisches Nachschlagewerk. Der Nutzer ist **Arzt** und prüft jede Monographie nach. Schreibe entsprechend: fachlich präzise, aber defensiv.

## Dateien in diesem Projekt

| Datei | Zweck |
|---|---|
| `kraeuter-kandidaten.json` | Arbeitswarteschlange — hier steht, was zu tun ist |
| `monographie-schema.json` | Struktureller Vertrag (JSON Schema) |
| `monographie-template.json` | Leeres Gerüst zum Ausfüllen |
| `validate_monographie.py` | Prüfskript — **muss** fehlerfrei laufen |
| `fertig/` | Hier landen abgeschlossene Monographien |

Einmalig: `pip install jsonschema` (sonst prüft das Skript nur eingeschränkt).

## Reihenfolge — die Wunschliste hat IMMER Vorrang

**1. Zuerst `docs/wunschliste.json` lesen.** Sie wird von der Herbarium-App geschrieben und enthält Kräuter, die der Arzt **tatsächlich in der Hand hatte**. Das schlägt jede theoretische Prioritätsstufe.

**2. Erst wenn die Wunschliste leer ist**, den nächsten offenen Kandidaten aus `kraeuter-kandidaten.json` nehmen — niedrigste `tier` zuerst.

**3. Ist auch die Kandidatenliste leer**, weiter mit der Wunschliste, sobald dort etwas Neues auftaucht.

Die Wunschliste hakst du **nicht** ab — das macht die App selbst, sobald die Monographie in `fertig/` liegt. Du **überspringst** einfach, was schon da ist. Eine Schreibrichtung pro Datei, keine Konflikte:

| Datei | Wer schreibt |
|---|---|
| `docs/wunschliste.json` | **nur die App** |
| `fertig/*.json` | **nur du** |
| `docs/changelog.json` | **nur du** |
| `kraeuter-kandidaten.json` | **nur du** |

## Deduplikation — vor jedem Stapel

Bevor du etwas baust, prüfe gegen **drei** Quellen, ob die Pflanze schon existiert:

1. alle `id` in `fertig/`
2. alle `botany.synonyms` in `fertig/` — **wichtig!**
3. `kraeuter-kandidaten.json` → `vorhanden`

**Warum die Synonyme entscheidend sind:** Botanische Namen ändern sich. Rosmarin heißt heute *Salvia rosmarinus*, früher *Rosmarinus officinalis*. Ohne Synonym-Abgleich baust du eine zweite Monographie unter dem alten Namen — und niemand merkt es. Trage bei jeder Art die lateinischen Altnamen in `botany.synonyms` ein.

## Ablauf pro Stapel

**Stapelgröße: 3–5 Kräuter. Nicht mehr.** Der Engpass ist die ärztliche Sichtung, nicht die Erzeugung.

1. `docs/wunschliste.json` lesen → sonst `kraeuter-kandidaten.json`
2. Deduplikation gegen `fertig/` **inkl. Synonyme**
3. **Recherchieren** (siehe unten) — nicht aus dem Gedächtnis schreiben
4. JSON nach `monographie-template.json` ausfüllen — mit `stand` (heutiges Datum) und `herkunft: "ki-recherchiert"`
5. `python3 validate_monographie.py fertig/monographie-xyz.json` — muss fehlerfrei sein
6. Datei nach `fertig/` legen
7. **`docs/changelog.json` ergänzen** (siehe unten)
8. Kurz zusammenfassen, was du gefunden hast — **besonders Überraschungen**

## Changelog — ein Satz pro Änderung

Nach jedem Stapel `docs/changelog.json` ergänzen (anhängen, nicht überschreiben):

```json
{"eintraege": [
  {"ts": "2026-07-14T09:00:00Z",
   "id": "valeriana-officinalis",
   "common": "Baldrian",
   "art": "neu",
   "sha": "",
   "text": "Erstfassung. HMPC führt WEU für Einschlafstörungen; ESCOP zusätzlich Unruhe."}
]}
```

Bei **Aktualisierungen** ist der `text` das Wichtigste. Schreib ihn **bewusst** — nicht aus der Commit-Nachricht:

> *„Interaktion mit Benzodiazepinen ergänzt; Evidenz von TU auf ESCOP+ korrigiert."*

Die App zeigt diesen Satz oben in der Monographie und setzt sie automatisch auf **„ungesichtet"** zurück. Der Arzt wird also genau dorthin geführt, wo sich etwas geändert hat. Ein nichtssagender Text („Datei aktualisiert") macht diesen Mechanismus wertlos.

Das Feld `sha` darfst du leer lassen — die App füllt es beim Abgleich selbst.

## Neue Pflichtfelder

- **`stand`**: `"2026-07-14"` — Datum der Recherche. Nach zwei Jahren erkennt der Arzt damit, was veraltet ist (HMPC-Monographien werden überarbeitet).
- **`herkunft`**: `"ki-recherchiert"` — deine Monographien. Die 15 handkuratierten tragen `"kuratiert"`. Die App zeigt den Unterschied dauerhaft an. **Ändere `"kuratiert"` niemals in `"ki-recherchiert"`.**
- **`botany.synonyms`**: lateinische Altnamen, z. B. `["Rosmarinus officinalis"]`. Leeres Array, wenn keine.

## Recherche — nicht verhandelbar

Vor jeder Monographie **im Netz nachschlagen**:

- **EMA/HMPC-Monographie** der Art (entscheidet über `WEU` vs. `TU`)
- **ESCOP** und **Kommission E**
- Bei Sicherheitsfragen: Toxin, Grenzwerte, Fallberichte

**Wenn du etwas nicht belegen kannst, schreibe `"unsicher — zu prüfen"`.** Ein ehrliches Fragezeichen ist wertvoll; eine erfundene Gewissheit ist gefährlich.

## Die drei Regeln, an denen alles hängt

**1. Verwechslungen niemals stillschweigend leer lassen.**
Ein leeres `confusions`-Array sieht in der App aus wie „ungefährlich". Das ist die gefährlichste Lüge, die diese Datei erzählen kann. Suche **aktiv** nach giftigen Doppelgängern — besonders bei Doldenblütlern (Schierling!), Zwiebelpflanzen (Herbstzeitlose, Maiglöckchen) und Raublattgewächsen. Gibt es wirklich keine, trage einen Eintrag `"keine relevante Verwechslung bekannt"` mit Begründung ein.

**2. Evidenz nicht schönen.**
`WEU` nur, wenn die HMPC-Monographie das ausdrücklich so führt. Populärer Ruf ist kein Evidenzgrad. Der Nutzer will ausdrücklich wissen, wo die Erwartungen zu hoch sind — dafür ist `expectation_summary.overstated` da. Nutze es.

**3. Flags müssen zur Substanz passen.**
Wenn ein Doppelgänger `lebensgefährlich` ist, muss `flags.deadly_confusion` true sein. Wenn `toxin_ceiling` true ist, brauchst du `toxin_type` und `safety.tox_ceiling`. Das Prüfskript fängt Widersprüche — verlass dich nicht darauf, sondern denk mit.

## Evidenz-Skala

| Tag | Bedeutung |
|---|---|
| `WEU` | HMPC well-established use — wissenschaftlich hinreichend belegt |
| `RCT` | Eigene randomisiert-kontrollierte Studienevidenz |
| `ESCOP+` | Positive ESCOP-Monographie |
| `TU` | HMPC traditional use — langjährig angewendet, nicht belegt |
| `PRÄ` | Nur präklinisch (in vitro / Tier) |
| `TRAD` | Rein volksmedizinisch |

Kombination erlaubt: `TU/ESCOP+`, `WEU/RCT`.

## Warneinträge (tier 3)

Herbstzeitlose, Schierling, Fingerhut, Eisenhut, Maiglöckchen, Tollkirsche, Riesen-Bärenklau, Rosmarinheide.

Das sind **keine Heilpflanzen**, sondern Erkennungs- und Warneinträge:

- `indications`: **leeres Array**
- `flags.not_for_use`: `true`
- `confusions`: die **Nutzpflanzen**, mit denen sie verwechselt werden (umgekehrte Richtung!)
- `key_warning`: unmissverständlich, was bei Verzehr passiert
- `key_features`: besonders sorgfältig — das ist der ganze Zweck des Eintrags
- `expectation_summary.plausible`: `"Keine Anwendung. Dieser Eintrag dient der Erkennung und Warnung."`

## Konventionen

- **Dateiname:** `monographie-<deutscher-name>.json` — klein, ohne Umlaute (`monographie-baerlauch.json`)
- **`id`:** `gattung-art`, klein (`allium-ursinum`). Muss dem **aktuell akzeptierten** botanischen Namen entsprechen — die App gleicht Pl@ntNet-Treffer darüber ab. Achtung: Rosmarin ist heute *Salvia rosmarinus*.
- **Sprache:** durchgehend Deutsch
- **`synonyms` pro Indikation:** Laienbegriffe! Davon lebt die Symptomsuche („Halsschmerzen" muss „Rachenentzündung" finden)
- **`realistic_expectation`:** Was darf man erwarten — und was **nicht**

## Zum Schluss

Das Prüfskript kontrolliert Struktur und Konsistenz. Es kann **nicht** prüfen, ob deine Inhalte stimmen. Diese Verantwortung liegt bei dir und danach beim Arzt.

Wenn dir bei der Recherche etwas auffällt, das über die Monographie hinausgeht — ein Widerspruch, eine überraschende Interaktion, eine Verwechslung, die im Katalog noch nirgends steht — **sag es dazu.** Genau solche Funde machen das Herbarium besser.
