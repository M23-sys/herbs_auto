# Lauf-Protokoll

## 2026-07-14 — Baldrian, Efeu

**Bearbeitet:** valeriana-officinalis (Baldrian), hedera-helix (Efeu) — die 2 ersten offenen Tier-1-Einträge.

**Prüfergebnis:** Beide `✓ ok` (0 Fehler). Einziger Hinweis: enthält "unsicher/zu prüfen" (bewusst gesetzt, siehe unten). **0 Korrekturversuche** nötig.

**Hauptquellen:**
- Baldrian: EMA/HMPC EU herbal monograph *Valeriana officinalis* L., radix (EMA/HMPC/150846/2015, final 2016); ESCOP; Kommission E. Verwechslungs-Recherche über Gartenjournal / Arzneipflanzenlexikon / giftpflanzen.com.
- Efeu: EMA/HMPC EU herbal monograph *Hedera helix* L., folium (Revision 2); ESCOP; Kommission E. Giftigkeits-Recherche über Gesellschaft für Toxikologie u. a.
- **Hinweis Quellen-Abruf:** Die EMA-PDFs selbst lieferten beim direkten Abruf HTTP 403; Inhalte daher über Websuche-Zusammenfassungen und Mirror-/Fachquellen verifiziert. Die exakten Extrakt-Spezifikationen (DER, Ethanol-%) und Posologie-Zahlen sollten vom Arzt gegen das Original-Monograph geprüft werden.

### Überraschungen / unsichere Stellen für den Arzt

- **Baldrian — WEU vs. TU ist zubereitungsabhängig.** Der well-established-use-Status gilt laut EMA-Monograph **nur** für den ethanolischen Trockenextrakt (DER 3–7,4:1, Ethanol 40–70 % V/V). Tee, Tinktur und Presssaft sind lediglich *traditional use*. Ich habe die Indikationen entsprechend als `WEU/ESCOP+` bzw. `WEU/TU` getaggt und den Vorbehalt in `comment`/`realistic_expectation` vermerkt. Bitte prüfen, ob diese differenzierte Darstellung so gewünscht ist.
- **Baldrian — `deadly_confusion=true` trotz sehr sicherer Pflanze.** Die Pflanze selbst ist harmlos; die tödliche Gefahr entsteht ausschließlich beim **Wildsammeln**: junge gefiederte Baldrianblätter ähneln tödlich giftigen Doldenblütlern (Wasserschierling *Cicuta virosa*, Gefleckter Schierling *Conium maculatum*). Das Flag speist das Register — ist hier m. E. korrekt, aber ungewöhnlich für ein Tier-1-Sedativum. `high_safety` daher bewusst **false**.
- **Efeu ist eine Giftpflanze** (Beeren + frisches Laub: Saponine, Falcarinol; 2–3 Beeren → Vergiftungssymptome bei Kindern; Falcarinol-Kontaktdermatitis). Die Arznei ist **ausschließlich** der standardisierte Extrakt — kein selbst gekochter Tee. Ich habe `raw_toxicity=true` gesetzt; es gibt allerdings **kein** perfekt passendes Flag für "roh giftig, aber nur als standardisierter Extrakt anwendbar (Erhitzen macht sie NICHT essbar)". `requires_heating` wäre irreführend und wurde weggelassen. Bitte Flag-Wahl gegenprüfen.
- **Efeu — pharmakodynamische Interaktion mit Antitussiva** (Sekretstau bei gleichzeitiger Gabe von Hustenstillern) als `relevant` eingetragen; die CYP2C8/2C19-Hemmung ist nur in-vitro belegt → als `theoretisch`/`unsicher — zu prüfen` markiert.
- **Efeu — Altersgrenze:** Anwendung ab 2 Jahren, unter 2 Jahren kontraindiziert; Kinder 2–5 Jahre nur unter ärztlicher Begleitung (EMA).
- **Taxonomie:** Baldrian-Familie im Katalog als *Caprifoliaceae* geführt (früher Valerianaceae, heute Unterfamilie Valerianoideae) — im `synonym_note` vermerkt. Efeu = *Araliaceae*.

## 2026-07-14 — Echte Schlüsselblume, Eibisch

**Bearbeitet:** primula-veris (Echte Schlüsselblume), althaea-officinalis (Eibisch) — die nächsten 2 offenen Tier-1-Einträge in Listenreihenfolge.

**Prüfergebnis:** Beide bestehen `validate_monographie.py` mit **0 Fehlern**. Schlüsselblume: 1 Hinweis (enthält bewusst "unsicher — zu prüfen"). Eibisch: `✓ alles sauber`. **0 Korrekturversuche** nötig.

**Hauptquellen:**
- Schlüsselblume: EMA/HMPC EU herbal monographs *Primula veris/elatior*, radix **und** flos (traditional use); Kommission E (positiv); ESCOP. Verwechslungs-/Naturschutz-Recherche über Arzneipflanzen-Lexikon, giftpflanzen-DB (vetpharm.uzh.ch), BUND/NABU.
- Eibisch: EMA/HMPC EU herbal monograph *Althaea officinalis*, radix (traditional use); Kommission E; ESCOP; Phytotherapie-Fachquellen zu Kaltauszug und Resorptionsinteraktion.
- **Quellen-Abruf:** Der direkte Abruf der EMA-PDFs schlug erneut fehl (DNS/Proxy: `www.ema.europa.eu` nicht auflösbar; im Vorlauf zuvor HTTP 403). Inhalte daher über Websuche-Zusammenfassungen und Fachquellen verifiziert. **Bitte die exakte regulatorische Einstufung (TU-Wortlaut), Posologie-Zahlen und DER gegen die Original-Monographien prüfen.**

### Überraschungen / unsichere Stellen für den Arzt

- **Schlüsselblume — WEU vs. TU / das „Evidenz-Lehrstück".** Der reason-Eintrag der Warteschlange nennt „WEU nur in Fixkombination (mit Thymian)". Bestätigt: Die **Einzeldroge** (Primulae radix/flos) ist in den HMPC-Monographien nur **traditional use**; die belastbare RCT-Evidenz (akute Bronchitis) betrifft die **Fixkombination Schlüsselblumenwurzel + Thymian** (z. B. Bronchipret TP). Ich habe daher die Hustenindikation als `TU/ESCOP+` (nicht WEU) getaggt und den Vorbehalt ausdrücklich in `pharmacology.evidence_caveat` und `expectation_summary.overstated` vermerkt. Bitte prüfen, ob diese Trennung so gewünscht ist.
- **Schlüsselblume — `deadly_confusion=true` bei einer fast harmlosen Heilpflanze.** Grund: die **blütenlose Blattrosette** ist der erstjährigen Rosette des **tödlich giftigen Fingerhuts (*Digitalis purpurea*)** ähnlich (beide weichhaarig-runzelig). Das speist das Verwechslungs-Register korrekt; `high_safety` daher **false**. Zusätzlich: Art ist in DE **besonders geschützt** (BArtSchV), Wildsammlung unzulässig — in `collection_rules` und `key_warning` vermerkt. `region_occurrence` daher `wild-selten`.
- **Schlüsselblume — Primin/Primel-Allergie.** Das starke Kontaktallergen Primin steckt v. a. in der Zimmerpflanze *Primula obconica*; *P. veris* enthält nur sehr wenig. Als Verwechslungs-/Allergiehinweis aufgenommen, damit die Kreuzsensibilisierung nicht untergeht.
- **Eibisch — Zubereitung ist der kritische Punkt, nicht die Toxizität.** Die Pflanze ist sehr sicher (`high_safety=true`, kein Toxin, kein giftiger Doppelgänger), ABER die Schleimstoffe sind **hitzeempfindlich** → **Kaltauszug**, nicht kochen; Tinktur fällt den Schleim aus und ist ungeeignet. Das steht in `key_warning`, `chemistry.solubility_note` und `preparation`.
- **Eibisch — Resorptionsinteraktion.** Der Schleimfilm kann die Aufnahme **gleichzeitig eingenommener Arzneistoffe** verzögern/vermindern → als `pharmakokinetisch` mit Empfehlung „zeitlicher Abstand ~30–60 min" eingetragen. Trotzdem `high_safety=true` gesetzt (Interaktion nicht schwerwiegend, `interaction_heavy=false`) — bitte gegenprüfen, ob das Register das so abbilden soll.
- **Eibisch — Schleimgehalt-Angaben schwanken.** Quellen nennen für die Wurzel 10–20 % bis „~35 %". Ich habe die Spanne transparent angegeben statt eine Zahl zu behaupten.
- **Eibisch — keine lebensgefährliche Verwechslung.** Aktiv gesucht: nur ungiftige Malvaceen (Wilde Malve, Stockrose). Das ist als expliziter Eintrag „keine lebensgefährliche Verwechslung bekannt" mit Begründung dokumentiert (nicht stillschweigend leer).

## 2026-07-14 — Mariendistel, Weißdorn

**Bearbeitet:** silybum-marianum (Mariendistel), crataegus-monogyna (Weißdorn) — die nächsten 2 offenen Tier-1-Einträge in Listenreihenfolge.

**Prüfergebnis:** Beide bestehen `validate_monographie.py` mit **0 Fehlern**. Je 1 Hinweis (enthält bewusst „unsicher — zu prüfen"). **0 Korrekturversuche** nötig.

**Hauptquellen:**
- Mariendistel: EMA/HMPC EU herbal monograph *Silybum marianum* (L.) Gaertn., **fructus** (traditional use); Kommission E; ESCOP. Chemie/Löslichkeit/CYP über Fach-Sekundärquellen (vitalstoff-lexikon, MSD Manual, arzneipflanzenlexikon). Verwechslungs-Recherche über Wikipedia/Wildpflanzen-Portale.
- Weißdorn: EMA/HMPC EU herbal monograph *Crataegus* spp., **folium cum flore** (traditional use, 2016); Kommission E (historisch); ESCOP; Benefit-Risk-Review WS 1442 / SPICE-Studie; Botanik über baumkunde.de / heilpflanzen-atlas / openflora.
- **Quellen-Abruf wie in den Vorläufen:** Direkter Abruf der EMA-PDFs schlug fehl (`www.ema.europa.eu` DNS nicht auflösbar); zahlreiche Fachseiten (arzneipflanzenlexikon.info, awl.ch, Wikipedia) lieferten beim WebFetch **HTTP 403**. Inhalte daher über WebSearch-Zusammenfassungen und mehrere übereinstimmende Sekundärquellen verifiziert. **Bitte den regulatorischen TU-Wortlaut, Posologie-Zahlen und die Extrakt-Spezifikationen gegen die Original-Monographien prüfen.**

### Überraschungen / unsichere Stellen für den Arzt — WICHTIG, beide Warteschlangen-„reason" sind veraltet

- **Mariendistel — die Warteschlange sagt „WEU Lebererkrankungen", das ist FALSCH/überholt.** Die HMPC führt *Silybi mariani fructus* ausschließlich als **traditional use** (Verdauungsbeschwerden/Völlegefühl/Blähungen; „Unterstützung der Leberfunktion"), **NICHT** als well-established use — die klinische Wirksamkeit der oralen Zubereitung ist uneinheitlich. Ich habe die Leber-Indikation defensiv als `TU/ESCOP+` (nicht WEU) getaggt und den Vorbehalt in `evidence_caveat`, `overstated` und `key_warning` deutlich gemacht. **Bitte diese Herabstufung gegenüber der reason-Zeile bestätigen.**
- **Mariendistel — Tee praktisch unwirksam.** Silymarin ist lipophil/wasserunlöslich → nur standardisierte Trockenextrakte sinnvoll; das steht in `solubility_note`, `preparation` und `key_warning`. Häufiger Laien-Irrtum („Mariendisteltee zur Leberkur").
- **Mariendistel — i.v.-Silibinin ≠ Kapsel.** Die spektakuläre Wirkung bei Knollenblätterpilz-(Amanita-)Vergiftung betrifft die **intravenöse** Silibinin-Notfalltherapie (Legalon SIL), nicht die orale Selbstanwendung. Ausdrücklich in `mechanism`/`overstated` abgegrenzt, damit daraus kein falscher Wirknachweis für die Kapsel gezogen wird.
- **Mariendistel — Verwechslung/Flags.** Kein giftiger Doppelgänger (nur andere ungiftige Disteln ohne weiße Blattmarmorierung) → expliziter „keine giftige Verwechslung"-Eintrag. `asteraceae_allergy=true` (Korbblütler). `high_safety` bewusst **false** wegen Kreuzallergie-Risiko und unklarer Schwangerschaftsdaten. CYP-Interaktion nur `theoretisch`/in vitro.
- **Weißdorn — die Warteschlange sagt „WEU Herzinsuffizienz NYHA II", das ist der zentrale Streitpunkt.** Die **HMPC hat die NYHA-II-Indikation 2016 gestrichen** und vergibt nur **traditional use** für „vorübergehende nervöse Herzbeschwerden (Herzklopfen), nachdem ein Arzt ernste Ursachen ausgeschlossen hat" sowie leichte Stress-/Einschlafhilfe. Grund: Die SPICE-Studie (WS 1442) zeigte im Gesamtkollektiv keinen sicheren Mortalitäts-/Morbiditätsnutzen (nur ein Subgruppensignal bei milder Herzinsuffizienz). Ich habe beide Indikationen als `TU` getaggt und die Streichung in `evidence_caveat`, `overstated` und `key_warning` dokumentiert. **Bitte prüfen, ob der Katalog Weißdorn weiterhin unter „kardiale WEU-Indikation" führen will — nach aktueller HMPC ist das nicht mehr haltbar.**
- **Weißdorn — eigentliche Gefahr ist die Fehl-/Selbstdiagnose,** nicht die Pflanze (sehr sicher). Deshalb `high_safety` **false** gesetzt und in `contraindications`/`key_warning` betont, dass echte Herzsymptome zuerst ärztlich abzuklären sind.
- **Weißdorn — Art-Doppelnutzung:** *C. monogyna* (1 Griffel/Steinkern) und *C. laevigata* (2–3) sind arzneilich gleichwertig; HMPC fasst sie als „Crataegus spp.". In `synonym_note` und `confusions` vermerkt — die App sollte beide Arten auf diese id abbilden.
- **Weißdorn — Verwechslung Schlehe/Kirschpflaume:** Blatt/Blüte ungefährlich; nur die **Samenkerne** von Prunus-Arten enthalten Blausäureglykoside. Unterscheidung über Blütezeit (Schlehe blüht vor dem Laub) und tief gelappte Weißdornblätter dokumentiert. Kein lebensgefährlicher Doppelgänger → expliziter Eintrag statt leerem Array.
