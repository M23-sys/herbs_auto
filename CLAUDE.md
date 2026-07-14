# Herbarium clinicum — Projektanweisung

Du erstellst evidenzbasierte Heilpflanzen-Monographien als JSON für ein medizinisches
Nachschlagewerk. Der Nutzer ist **Arzt** und prüft jede Monographie nach. Schreibe
entsprechend: fachlich präzise, aber defensiv.

> **Betriebsart: autonome Cloud-Routine.** Dieses Repository wird alle 6 Stunden von
> einer Claude-Code-Routine bearbeitet. **Niemand bestätigt dabei etwas, niemand liest
> mit.** Jeder Lauf startet mit einem frischen Klon von `main` und ohne jede Erinnerung
> an den Lauf davor. Der gesamte Zustand steckt in den Dateien dieses Repos — was du
> nicht committest, ist verloren.

## Dateien in diesem Projekt

| Datei | Zweck |
|---|---|
| `kraeuter-kandidaten.json` | **Arbeitswarteschlange — die maßgebliche Quelle.** Hier steht, was zu tun ist und was erledigt ist. |
| `monographie-schema.json` | Struktureller Vertrag (JSON Schema, Draft-07) |
| `monographie-template.json` | Leeres Gerüst zum Ausfüllen |
| `validate_monographie.py` | Prüfskript — **muss** fehlerfrei laufen |
| `MONOGRAPHIE-SPEC.md` | Ausführliche Bau-Spezifikation — bei Zweifeln dort nachsehen |
| `requirements.txt` | `pip install -r requirements.txt` **vor** dem ersten Prüflauf |
| `fertig/` | Hier landen abgeschlossene Monographien |
| `state/lauf-log.md` | Protokoll jedes Laufs |
| `docs/kraeuter-kandidaten.md` | Nur Lesestoff. **Nicht maßgeblich, nicht bearbeiten.** |

## Ablauf pro Lauf

**Genau 2 Kräuter pro Lauf. Nicht mehr, auch wenn Zeit bleibt.** Der Engpass ist die
ärztliche Prüfung, nicht die Erzeugung. Ein Rückstau ungeprüfter Monographien ist
schlimmer als ein kleiner Katalog.

1. `pip install -r requirements.txt` — ohne `jsonschema` bricht das Prüfskript ab
2. `kraeuter-kandidaten.json` lesen; die nächsten 2 Einträge mit `"status": "offen"`
   nehmen — **niedrigste `tier` zuerst**, bei gleicher Stufe in Listenreihenfolge
3. **Selbstheilung:** Existiert `fertig/monographie-<name>.json` bereits, gilt der
   Eintrag als erledigt — Status korrigieren und den nächsten nehmen
4. **Recherchieren** (siehe unten) — nicht aus dem Gedächtnis schreiben
5. JSON nach `monographie-template.json` ausfüllen
6. `python3 validate_monographie.py fertig/monographie-xyz.json` — muss fehlerfrei sein
7. Status auf `"entwurf_fertig"` setzen, `"datei"` eintragen
8. `state/lauf-log.md` ergänzen, committen, auf `main` pushen

### Abbruchbedingung — wichtig

**Maximal 3 Korrekturversuche pro Kraut.** Danach: Datei nicht nach `fertig/` legen,
Status auf `"uebersprungen"`, Grund ins Log, mit dem nächsten Kraut weitermachen.
Der Lauf darf daran nicht scheitern — eine Endlosschleife verbrennt das Tageslimit.

Setze `status` **niemals** auf `"geprueft"`. Das macht nur der Arzt.

## Recherche — nicht verhandelbar

Vor jeder Monographie **im Netz nachschlagen**:

- **EMA/HMPC-Monographie** der Art (entscheidet über `WEU` vs. `TU`)
- **ESCOP** und **Kommission E**
- Bei Sicherheitsfragen: Toxin, Grenzwerte, Fallberichte
- **Aktuell akzeptierter botanischer Name** (Taxonomie ändert sich!)

**Wenn du etwas nicht belegen kannst, schreibe `"unsicher — zu prüfen"`.** Ein ehrliches
Fragezeichen ist wertvoll; eine erfundene Gewissheit ist gefährlich. Weil niemand
mitliest, gilt hier strenger als sonst: **im Zweifel defensiv.**

## Die drei Regeln, an denen alles hängt

**1. Verwechslungen niemals stillschweigend leer lassen.**
Ein leeres `confusions`-Array sieht in der App aus wie „ungefährlich". Das ist die
gefährlichste Lüge, die diese Datei erzählen kann. Suche **aktiv** nach giftigen
Doppelgängern — besonders bei Doldenblütlern (Schierling!), Zwiebelpflanzen
(Herbstzeitlose, Maiglöckchen) und Raublattgewächsen. Gibt es wirklich keine, trage
einen Eintrag `"keine relevante Verwechslung bekannt"` mit Begründung ein.

**2. Evidenz nicht schönen.**
`WEU` nur, wenn die HMPC-Monographie das ausdrücklich so führt. Populärer Ruf ist kein
Evidenzgrad. Der Nutzer will ausdrücklich wissen, wo die Erwartungen zu hoch sind —
dafür ist `expectation_summary.overstated` da. Nutze es.

**3. Flags müssen zur Substanz passen.**
Wenn ein Doppelgänger `lebensgefährlich` ist, muss `flags.deadly_confusion` true sein.
Wenn `toxin_ceiling` true ist, brauchst du `toxin_type` und `safety.tox_ceiling`. Das
Prüfskript fängt Widersprüche — verlass dich nicht darauf, sondern denk mit.

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

Herbstzeitlose, Schierling, Fingerhut, Eisenhut, Maiglöckchen, Tollkirsche,
Riesen-Bärenklau, Rosmarinheide.

Das sind **keine Heilpflanzen**, sondern Erkennungs- und Warneinträge:

- `indications`: **leeres Array**
- `flags.not_for_use`: `true`
- `confusions`: die **Nutzpflanzen**, mit denen sie verwechselt werden (umgekehrte Richtung!)
- `key_warning`: unmissverständlich, was bei Verzehr passiert
- `key_features`: besonders sorgfältig — das ist der ganze Zweck des Eintrags
- `expectation_summary.plausible`: `"Keine Anwendung. Dieser Eintrag dient der Erkennung und Warnung."`

## Konventionen

- **Dateiname:** `monographie-<deutscher-name>.json` — klein, ohne Umlaute
  (`monographie-baerlauch.json`)
- **`id`:** `gattung-art`, klein (`allium-ursinum`). Muss dem **aktuell akzeptierten**
  botanischen Namen entsprechen — die App gleicht Pl@ntNet-Treffer darüber ab.
  Achtung: Rosmarin ist heute *Salvia rosmarinus*.
- **Sprache:** durchgehend Deutsch
- **`synonyms` pro Indikation:** Laienbegriffe! Davon lebt die Symptomsuche
  („Halsschmerzen" muss „Rachenentzündung" finden)
- **`realistic_expectation`:** Was darf man erwarten — und was **nicht**

## Git

- Committe auf `main`. Commit-Message: `monographien: <Kraut1>, <Kraut2>`
- Scheitert der Push, weil `main` sich geändert hat: `git pull --rebase`, dann erneut pushen
- Committe **immer** alles zusammen: die Monographien, den Status in
  `kraeuter-kandidaten.json` und das Log. Ein Commit ohne Statusänderung führt dazu,
  dass der nächste Lauf dieselben Kräuter noch einmal bearbeitet.

## Zum Schluss

Das Prüfskript kontrolliert Struktur und Konsistenz. Es kann **nicht** prüfen, ob deine
Inhalte stimmen. Diese Verantwortung liegt bei dir und danach beim Arzt.

Wenn dir bei der Recherche etwas auffällt, das über die Monographie hinausgeht — ein
Widerspruch, eine überraschende Interaktion, eine Verwechslung, die im Katalog noch
nirgends steht — **schreib es ins Log.** Es liest niemand mit; das Log ist dein einziger
Kanal zum Arzt. Genau solche Funde machen das Herbarium besser.
