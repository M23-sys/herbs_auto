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

## 2026-07-14 — Rosskastanie, Ingwer

**Bearbeitet:** aesculus-hippocastanum (Rosskastanie), zingiber-officinale (Ingwer) — die nächsten 2 offenen Tier-1-Einträge in Listenreihenfolge.

**Prüfergebnis:** Beide bestehen `validate_monographie.py` mit **0 Fehlern**. Rosskastanie: 1 Hinweis (enthält bewusst „unsicher — zu prüfen"). Ingwer: 2 Hinweise (leere `harvest_month_tags` — bewusst, siehe unten; sowie „unsicher — zu prüfen"). **0 Korrekturversuche** nötig.

**Hauptquellen:**
- Rosskastanie: EMA/HMPC EU herbal monograph *Aesculus hippocastanum* L., **semen** (well-established use CVI; traditional use für weitere/topische Zubereitungen); EMA Public Summary „Horse-chestnut seed"; Cochrane Review „Horse chestnut seed extract for chronic venous insufficiency"; Kommission E. Botanische Abgrenzung Rosskastanie/Edelkastanie über mundraub.org, ÖKO-TEST, Plantura, wetter.de.
- Ingwer: EMA/HMPC EU herbal monograph *Zingiber officinale* Roscoe, **rhizoma** (well-established use Reisekrankheit; traditional use Dyspepsie/Erkältung/Gelenke); Kommission E; Embryotox (Schwangerschaft); Sekundärquellen zu Antikoagulanzien-Interaktion und cholekinetischer Wirkung (arzneipflanzenlexikon, awl.ch, DAAB).
- **Quellen-Abruf wie in den Vorläufen:** Direkter WebFetch der EMA-PDFs (und einiger Fachseiten wie fitoterapia.net, altmeyers.org) lieferte **HTTP 403**. Inhalte daher über WebSearch-Zusammenfassungen und mehrere übereinstimmende Sekundärquellen verifiziert. **Bitte den regulatorischen Wortlaut, Posologie-Zahlen und Extrakt-Spezifikationen (DER, Ethanol-%, Aescin-Gehalt) gegen die Original-Monographien prüfen.**

### Überraschungen / unsichere Stellen für den Arzt

- **Rosskastanie — WEU ist an die STANDARDISIERTE Zubereitung gebunden.** Der well-established use gilt laut HMPC nur für den auf Triterpenglykoside (Aescin, berechnet als Protoaescigenin) eingestellten Trockenextrakt (Ethanol 40–80 %) bei chronischer Veneninsuffizienz. Weniger standardisierte und topische Zubereitungen sind nur *traditional use*. Ich habe die orale CVI-Indikation als `WEU`, die topische/sonstige als `TU` getaggt. Bitte Extrakt-Spezifikation und Aescin-Tagesdosis (ich habe ~100 mg/Tag = 2× 50 mg Retard eingetragen) gegen das Original prüfen.
- **Rosskastanie — der ROHE Samen ist leicht giftig, das ist sicherheitskritisch.** Nur der pharmazeutisch aufbereitete Extrakt ist verwendbar; roher Samen/selbstgemachter Tee lösen Übelkeit/Erbrechen/Durchfall aus (Saponine, Aesculin). In `key_warning`, `collection_rules`, `contraindications`, `kitchen` und `overstated` deutlich gemacht. **Flag-Entscheidung wie schon bei Efeu:** Kein Flag passt perfekt für „roh giftig, aber nur als standardisierter Extrakt anwendbar (Erhitzen macht ihn NICHT essbar)". `raw_toxicity` habe ich **nicht** gesetzt, weil es in der App mit `requires_heating` gekoppelt gedacht ist und Erhitzen hier gerade nicht entgiftet — die Giftigkeit steht stattdessen ausführlich im Text. Bitte gegenprüfen, ob das Register die rohe Giftigkeit so ausreichend abbildet.
- **Rosskastanie — die sicherheitsrelevante Verwechslung ist die ESSBARE Edelkastanie/Marone (*Castanea sativa*).** Umgekehrte Logik als bei Giftpflanzen: Hier wird der giftige Rosskastaniensamen mit der essbaren Marone verwechselt (v. a. Kinder, Herbstsammeln). Kein *lebensgefährlicher* Doppelgänger → `deadly_confusion=false`, aber Verwechslung ausführlich dokumentiert (Blatt gefingert vs. einfach; Fruchtkapsel wenige dicke Stacheln vs. langer Igel; Samen rund mit hellem Fleck vs. abgeflacht/zugespitzt).
- **Rosskastanie — Evidenz ehrlich gehalten:** Belegt ist nur symptomatische Kurzzeit-Linderung (Cochrane); dass die Venenerkrankung aufgehalten wird, ist NICHT belegt. Ersetzt weder Kompression noch Thrombose-Abklärung — in `overstated`/`key_warning` betont.
- **Ingwer — WEU nur für Reisekrankheit UND nur für Erwachsene.** Die HMPC führt den well-established use (1–2 g, 30–60 min vor Reiseantritt) ausdrücklich **nicht für Kinder/Jugendliche < 18 Jahre**. Dyspepsie, Erkältung, Gelenkschmerzen sind nur *traditional use*. Altersgrenze und Dosis in `indications`/`key_warning` vermerkt.
- **Ingwer — Schwangerschaft ist NICHT pauschal „unbedenklich".** Embryotox: übliche Mengen (bis ~1 g/Tag) ohne Hinweis auf erhöhtes Fehlbildungsrisiko; die **Kommission E rät bei Schwangerschaftserbrechen jedoch zur Zurückhaltung**. Defensiv formuliert: hohe Dosen meiden, arzneiliche Anwendung ärztlich abstimmen. Bitte gegenprüfen, wie der Katalog diese Diskrepanz (Embryotox vs. Kommission E) darstellen soll — ich habe beide Positionen genannt.
- **Ingwer — „natürlicher Blutverdünner" bei Antikoagulation.** In-vitro Thromboxansynthese-Hemmung; klinisch bei üblichen Mengen irrelevant, aber Berichte über verstärkte Blutungsneigung/INR-Veränderungen bei **> 4 g/Tag** zusammen mit Cumarinen/ASS. Als `theoretisch`, klinische Relevanz „gering bei üblichen Mengen, relevant bei hohen Dosen" eingetragen. `interaction_heavy=false`.
- **Ingwer — Gallensteine als Kontraindikation/Vorsicht** (cholekinetisch/gallenflussfördernd, Kommission E) aufgenommen. Neues Flag `reflux_caution=true` gesetzt (hohe Dosen können Reflux/Sodbrennen verstärken).
- **Ingwer — `harvest_month_tags` bewusst leer:** tropische Kulturpflanze, in Mitteleuropa **kein Wildvorkommen** (`region_occurrence: nur-kultur`), daher kein sinnvoller regionaler Erntekalender. Der Validator-Hinweis dazu ist erwartet und unkritisch. `harvest_organ` korrekt „Rhizom" (Spross-, kein Wurzelorgan — im `synonym_note` erklärt).

## 2026-07-15 — Indischer Flohsamen, Lein

**Bearbeitet:** plantago-ovata (Indischer Flohsamen), linum-usitatissimum (Lein) — die nächsten 2 offenen Tier-1-Einträge in Listenreihenfolge. Beide sind Quell-/Volumenlaxanzien; das macht sie inhaltlich zu einem Paar (gleiche Wirkklasse, gleiche Kernwarnung „reichlich trinken").

**Prüfergebnis:** Beide bestehen `validate_monographie.py` mit **0 Fehlern**. Flohsamen: 1 Hinweis (leere `harvest_month_tags` — bewusst, siehe unten). Lein: 1 Hinweis (enthält bewusst „unsicher — zu prüfen"). **0 Korrekturversuche** nötig.

**Hauptquellen:**
- Flohsamen: EMA/HMPC EU herbal monographs *Plantaginis ovatae semen* **und** *…seminis tegumentum* (Flohsamenschalen), well-established use, Assessment report 2013; Kommission E; ESCOP (inkl. Hypercholesterinämie-Zusatz für die Schalen). Interaktions-/Dosis-Recherche über eucell, onmeda, diePTA, arzneipflanzenlexikon.
- Lein: EMA/HMPC EU herbal monograph *Linum usitatissimum* L., **semen** (well-established use Obstipation; traditional use); Kommission E (innerlich + Kataplasma); ESCOP; **BfR/AGES** zu cyanogenen Glykosiden (Blausäure-Grenze). Verwechslungs-Recherche Purgier-Lein über Wikipedia, botanik-bochum, floraweb, Henriette's Herbal.
- **Quellen-Abruf wie in allen Vorläufen:** Direkter WebFetch der EMA-PDFs **und** mehrerer Fachseiten (altmeyers.org) lieferte erneut **HTTP 403**. Inhalte daher über WebSearch-Zusammenfassungen und mehrere übereinstimmende Sekundärquellen verifiziert. **Bitte den regulatorischen WEU-Wortlaut, die Posologie-Zahlen und die Indikationsabgrenzungen gegen die Original-Monographien prüfen.**

### Überraschungen / unsichere Stellen für den Arzt

- **Beide — die Kernwarnung ist mechanisch, nicht toxikologisch:** Quellmittel MÜSSEN mit reichlich Flüssigkeit genommen werden (Flohsamen Richtwert ~30 ml/g; Lein je Portion ≥150 ml). Ohne ausreichendes Trinken droht **Verklumpung mit Speiseröhren-/Darmverschluss** — als Kontraindikation (Ileus/Stenose/Schluckstörung) und in `key_warning` bei beiden betont.
- **Beide — `interaction_heavy=true` trotz „harmloser" Ballaststoffe.** Der Schleim **verzögert die Resorption gleichzeitig eingenommener Arzneistoffe** (u. a. Levothyroxin, Lithium, Carbamazepin, Digoxin, Cumarine, Vitamin B12/Mineralstoffe). Praxisregel „andere Arzneimittel 30–60 min versetzt" eingetragen. Zusätzlich blutzuckersenkender Effekt → mögliche Anpassung von Insulin/Antidiabetika. Bitte prüfen, ob das Register diese „Abstand-halten"-Interaktion über `interaction_heavy` abbilden soll oder ob ein spezifischeres Flag gewünscht ist — ein solches gibt es aktuell nicht.
- **Flohsamen — Datei heißt `monographie-flohsamen.json`, id `plantago-ovata`.** Zwei Drogen in einer Monographie zusammengefasst: ganzer **Samen** (Semen, 12–40 g/Tag) und die quellstärkeren **Schalen/Tegumentum** (4–20 g/Tag). Die Hypercholesterinämie-Indikation (ESCOP) gilt v. a. für die **Schalen**. Falls die App Samen und Schalen als getrennte Einträge führen will, müsste hier gesplittet werden — bitte entscheiden.
- **Flohsamen — Verstopfung als `WEU`, Reizdarm/Cholesterin als `ESCOP+`, Durchfall als `TU/ESCOP+`.** Der Warteschlangen-`reason` („WEU Obstipation/Reizdarm") ist für die Verstopfung korrekt; die Reizdarm-Evidenz habe ich defensiv nur als ESCOP+ (nicht WEU) getaggt. Synonym P. ispaghula Roxb. vermerkt. Kein giftiger Doppelgänger (gereinigte Handelsdroge) → expliziter „keine relevante Verwechslung"-Eintrag; `deadly_confusion=false`, `high_safety` **false** (Verschlussrisiko + Interaktionen). `harvest_month_tags` bewusst leer (subtropische Importdroge, `nur-kultur`) — Validator-Hinweis erwartet.
- **Lein — echter `toxin_ceiling`: cyanogene Glykoside (Blausäure).** Wichtig und leicht zu übersehen: **Ganze Samen setzen praktisch KEINE Blausäure frei**; erst **Schroten/Kauen** aktiviert die samen­eigene β-Glucosidase. BfR-Grenze ~**20 g geschroteter Leinsamen/Tag** (~50 mg Blausäure-Potenzial je 100 g). `toxin_ceiling=true`, `toxin_type="Cyanogene Glykoside (Blausäure)"`, `safety.tox_ceiling` gefüllt. Bitte die BfR-Zahl (20 g/Tag; Einzelportion ~15 g) gegenprüfen — Quellen nennen leicht abweichende Mengen (bis 30 g/Mahlzeit „weitestgehend unbedenklich").
- **Lein — GIFTIGER Doppelgänger vorhanden: Purgier-Lein (*Linum catharticum*).** Wilder Wiesen-Lein mit Bitterstoff **Linin**, drastisch abführend (Übelkeit/Brechreiz in größerer Menge). Betrifft v. a. das Kraut, nicht Handels-Leinsamen, aber bei Wildpflanzen relevant → als `giftig` (nicht „lebensgefährlich") eingetragen; Unterscheidung: winzige **weiße** Blüten + kleiner Wuchs vs. große **blaue** Blüten + große Samen des Saat-Leins. `deadly_confusion` bleibt **false** (nicht lebensgefährlich), aber `confusions` bewusst NICHT leer.
- **Lein — Phytoöstrogen-Frage (Lignane/SDG).** Populäre Wirkversprechen (Cholesterin, Hormone, Krebs) sind **keine belegte Arzneiwirkung** → in `overstated`/`evidence_caveat` klargestellt. Schwangerschaft/Stillzeit: übliche Nahrungsmengen vertretbar, hohe arzneiliche Mengen wegen Phytoöstrogen-Wirkung und dünner Datenlage defensiv gemieden (`unsicher — zu prüfen`). Bitte gegenprüfen.
- **Lein — `harvest_month_tags` [8,9]** gesetzt (heimische Ackerkultur, Samenreife Aug–Sep), `region_occurrence: kultur-und-verwildert`. Anders als Flohsamen also mit Erntekalender.

## 2026-07-15 — Faulbaum, Fenchel

**Bearbeitet:** frangula-alnus (Gewöhnlicher Faulbaum), foeniculum-vulgare (Fenchel) — die nächsten 2 offenen Tier-1-Einträge in Listenreihenfolge. Selbstheilung geprüft: keine der beiden Dateien lag vorab in `fertig/`.

**Prüfergebnis:** Beide bestehen `validate_monographie.py` mit **0 Fehlern**. Faulbaum: `✓ alles sauber`. Fenchel: 1 Hinweis (enthält bewusst "unsicher — zu prüfen"). **0 Korrekturversuche** nötig.

**Hauptquellen:**
- Faulbaum: EMA/HMPC EU herbal monograph *Rhamnus frangula* L., cortex (well-established use, kurzfristige Obstipation; 10–30 mg Hydroxyanthracenderivate/Tag als Glucofrangulin A); ESCOP; Kommission E. Verwechslungs-/Reifungs-Recherche über Arzneipflanzen-Lexikon, Pharmakobotanik, PharmaWiki.
- Fenchel: EMA/HMPC EU herbal monographs *Foeniculum vulgare* Mill., var. vulgare (Bitterfenchel) & var. dulce (Süßfenchel), fructus (traditional use); Kommission E; ESCOP. Estragol-/Dosis-Recherche über EMA-Sekundärquellen, Arzneipflanzen-Lexikon, Altmeyers, PharmaWiki.
- **Quellen-Abruf:** Der direkte WebFetch-Abruf der EMA-PDFs schlug erneut mit **HTTP 403** fehl (wie in den Vorläufen). Inhalte daher über Websuche-Zusammenfassungen und Fachquellen verifiziert. **Bitte die exakte regulatorische Einstufung, Posologie-Zahlen und Estragol-Grenzwerte gegen die Original-Monographien prüfen** (Evidenzgrad WEU/TU ungeprüft am Primärdokument).

### Überraschungen / unsichere Stellen für den Arzt

- **Faulbaum — Reifungspflicht ist sicherheitskritisch.** Frische Rinde ist **giftig** (heftiges Erbrechen, Koliken, blutiger Durchfall durch instabile Anthron-Vorstufen). Verwendbar ist nur Rinde, die **≥1 Jahr gelagert** oder bei 80–100 °C **heißluftgetrocknet** wurde. Ich habe `raw_toxicity=true` gesetzt. `requires_heating` bewusst **false** gelassen, weil die reine Lagerung (ohne Erhitzen) der übliche/ausreichende Weg ist — das Flag würde suggerieren, Erhitzen sei zwingend. Bitte Flag-Wahl gegenprüfen. Details in `key_warning`, `collection_rules`, `chemistry.heat_light_sensitivity`.
- **Faulbaum — Anthranoid-Klassenrisiken.** Kurzanwendung (max. ~1–2 Wochen); `toxin_ceiling=true`, `toxin_type="Anthranoide (Hydroxyanthracenderivate)"`. Bei Dauergebrauch Hypokaliämie → verstärkte Herzglykosid-/Antiarrhythmika-Wirkung, additiver Kaliumverlust mit Diuretika/Corticoiden/Süßholz (`interaction_heavy=true`). Kontraindiziert bei Ileus/CED/Appendizitis, in Schwangerschaft/Stillzeit und bei Kindern <12 (`pregnancy_contraindicated=true`). Diese KI/Duration-Angaben sind **Klassen-Standardwissen der Anthranoide** (v. a. aus Sennes-Monographien) — am Faulbaum-Primärmonograph nicht Wort für Wort verifiziert. Bitte prüfen.
- **Faulbaum — Verwechslung nicht tödlich, aber real.** Hauptdoppelgänger Kreuzdorn (*Rhamnus cathartica*, dornig/gegenständig/gesägt, ebenfalls giftig-drastisch) und die **giftigen schwarzen Beeren** (Kinder!). `deadly_confusion=false` — kein lebensgefährlicher Doppelgänger. Zusätzlich Abgrenzung zur Handelsdroge Cascara (*Frangula purshiana*).
- **Fenchel — `deadly_confusion=true` trotz harmloser Küchenpflanze.** Grund ausschließlich **Wildsammlung** von Doldenblütlern: Gefleckter Schierling (*Conium maculatum*, Coniin) und Wasserschierling (*Cicuta virosa*, Cicutoxin) sind lebensgefährlich. **Sicherstes Unterscheidungsmerkmal = Geruchsprobe** (Fenchel = Anis, Schierling = Mäuseurin). Als Handelsdroge wird jedoch praktisch nur kultivierte Ware bezogen → Risiko nur bei Wildsammlung. `apiaceae_confusion_young=true`.
- **Fenchel — Estragol begrenzt Dosis und Dauer.** `toxin_ceiling=true`, `toxin_type="Estragol (Methylchavicol)"`. Estragol ist im Tiermodell genotoxisch/kanzerogen; die **HMPC-Monographie zu Bitterfenchel-ÖL wurde deshalb zurückgezogen**. Anwendungsdauer: Erwachsene ~2 Wochen, Kinder 4–12 J. ~1 Woche (Estragol-Richtwert 1,0 µg/kg KG), **nicht unter 4 Jahren**. Das relativiert den populären Ruf als „harmloses Baby-/Kindermittel" — in `expectation_summary.overstated` vermerkt.
- **Fenchel — Schwangerschaft bewusst NICHT als kontraindiziert geflaggt.** `pregnancy_contraindicated=false`, weil Fenchel als Gewürz/gelegentlicher Tee als vertretbar gilt; die **arzneiliche** (konzentrierte) Anwendung wird aber wegen Estragol + schwacher Östrogenwirkung des Anethols nicht empfohlen. Diese Grenzziehung habe ich in `pregnancy_lactation` ausdrücklich als **"unsicher — zu prüfen"** markiert — bitte entscheiden, ob das Register hier lieber defensiv (Flag true) geführt werden soll.
- **Fenchel — Bitter- vs. Süßfenchel.** HMPC führt getrennte Monographien (var. vulgare / var. dulce). Beide nur *traditional use*. Kreuzallergie Doldenblütler/Sellerie-Beifuß-Gewürz-Syndrom in `adverse_effects` vermerkt.

## 2026-07-15 — Kriechendes Fingerkraut, Kleine Katzenminze (ERSTE Wunschlisten-Abarbeitung)

**Bearbeitet:** potentilla-reptans (Kriechendes Fingerkraut) und nepeta-nepetella (Kleine Katzenminze) — die **ersten 2 Einträge aus `docs/wunschliste.json`** (in Listenreihenfolge).

**WICHTIGE ENTSCHEIDUNG — bitte gegenlesen:** Erstmals war die Wunschliste nicht leer (Stand 2026-07-15, 5 Einträge). Der Routine-Prompt beschreibt operativ nur die Auswahl aus `kraeuter-kandidaten.json` und erwähnt die Wunschliste nicht — CLAUDE.md sagt dagegen ausdrücklich und mehrfach: „die Wunschliste hat IMMER Vorrang". Der Routine-Prompt erklärt CLAUDE.md selbst für verbindlich. Ich habe deshalb die **Wunschliste vorgezogen** (explizite Regel schlägt Schweigen; Risiko-Asymmetrie: die vom Arzt tatsächlich in der Hand gehaltenen Pflanzen sonst erneut zu übergehen ist genau der in CLAUDE.md gebrandmarkte Fehler). **Falls autonome Läufe stattdessen strikt die Kandidatenliste abarbeiten sollen, bitte den Routine-Prompt entsprechend präzisieren** — dann würdige ich die Wunschliste künftig nicht mehr vorrangig. `docs/wunschliste.json` wurde NICHT verändert (nur die App schreibt sie); die App hakt erledigte Einträge selbst ab.

**Dedup:** Beide gegen `fertig/` (inkl. `botany.synonyms`) und `kraeuter-kandidaten.json → vorhanden` geprüft — keine Dublette. Keine der beiden Arten steht in der Kandidatenliste.

**Prüfergebnis:** Beide bestehen `validate_monographie.py` mit **0 Fehlern**. Je 1 Hinweis (enthält bewusst „unsicher — zu prüfen"). **0 Korrekturversuche** nötig.

**Selbstheilung Kandidatenliste:** 12 Tier-1-Einträge standen auf `offen`, obwohl ihre Datei längst in `fertig/` liegt (Baldrian, Efeu, Schlüsselblume, Eibisch, Mariendistel, Weißdorn, Rosskastanie, Ingwer, Flohsamen, Lein, Faulbaum, Fenchel). Diese habe ich auf `entwurf_fertig` mit `datei` korrigiert, damit der nächste Lauf sie nicht erneut aufgreift.

**Hauptquellen (beide Arten haben KEINE Primär-Monographie — das ist der Kernbefund):**
- Für **beide** existiert **keine EMA/HMPC-, ESCOP- oder Kommission-E-Monographie** (Stand 2026-07). Damit ist der Evidenzgrad zwangsläufig **TRAD** (volksmedizinisch) bzw. „unsicher — zu prüfen"; ein höherer Tag wäre erfunden.
- Kriechendes Fingerkraut: Heil-/Wildpflanzenportraits (pflanzenfreunde.com, NaturaDB, krautgeschwister.de, heilwiese.com), botanische Bestimmungsquellen; als belegte Gerbstoff-**Analogie** die Tormentillwurzel (Potentilla erecta, Kommission E/ESCOP) — ausdrücklich NICHT gleichgesetzt.
- Kleine Katzenminze: Wikipedia (en/de) zu Nepeta nepetella/Nepeta/Katzenminzen (akzeptierter Name, Verbreitung, Nepetalacton), Gattungs-Reviews zu Nepeta; Nepeta-cataria-Monograph nur zur **Abgrenzung**.
- **Quellen-Abruf:** WebFetch auf Wikipedia und ein Heilpflanzenportal lieferte wie in den Vorläufen **HTTP 403**; Inhalte daher über WebSearch-Zusammenfassungen mehrerer übereinstimmender Sekundärquellen verifiziert. Primärquellen sind hier ohnehin nicht einschlägig, da keine regulatorische Monographie existiert.

### Überraschungen / unsichere Stellen für den Arzt

- **Beide Wunschlisten-Pflanzen sind evidenzarm bis evidenzlos.** Anders als die bisherigen Tier-1-Kandidaten gibt es hier keine HMPC/ESCOP-Grundlage. Ich habe alle Indikationen defensiv als **TRAD** getaggt und Dosierungen/Schwangerschaft als „unsicher — zu prüfen" markiert. Das ist kein Rechercheversäumnis, sondern der reale Befund — bitte so bestätigen.
- **Kleine Katzenminze ist in der Bodenseeregion NICHT wild heimisch.** Nepeta nepetella stammt aus SW-Europa/Mittelmeerraum (F, E, I, Pyrenäen, W-Alpen, Apennin, Algerien, Marokko). Ein „Bodensee"-Fund (so in der Wunschliste vermerkt) ist daher **kultiviert (Zierpflanze)** oder eine **Fehlbestimmung** einer anderen Nepeta-/Lippenblütler-Art. `region_occurrence` deshalb `nur-kultur`; ausführlicher Hinweis in `collection_rules` und `key_warning`. **Bitte prüfen, ob der Pl@ntNet-Treffer, der zu diesem Wunschlisten-Eintrag führte, wirklich N. nepetella war** — die verwandte Echte Katzenminze (N. cataria) oder die Zier-Hybride N. ×faassenii sind weit wahrscheinlicher.
- **Verwechslungs-Falle Katzenminze:** N. nepetella ist NICHT die (schwach) arzneilich genutzte Echte Katzenminze (N. cataria). Ich habe ausdrücklich davor gewarnt, deren Zuschreibungen zu übertragen — im Katalog steht sonst schnell ein Heilwert, den diese Art nicht hat.
- **Verwechslungs-Falle Fingerkraut:** Potentilla reptans ist arzneilich viel schwächer/unbelegter als die ähnliche Tormentillwurzel (Potentilla erecta). Kein giftiger Doppelgänger — die Pflanze ist essbar und sehr sicher (`high_safety=true`); das eigentliche „Risiko" ist die schwache Evidenz, nicht Toxizität. `confusions` bewusst mit den ungiftigen Ähnlichen (Gänsefingerkraut, Tormentill, Erdbeere) gefüllt plus explizitem „keine lebensgefährliche Verwechslung bekannt".
- **Restliche Wunschliste (3 offene Einträge):** dittrichia-viscosa (Klebriger Alant), cynodon-dactylon (Bermudagras), hedera-canariensis (Kanarischer Efeu) — ebenfalls überwiegend mediterran/nicht heimisch und evidenzarm. hedera-canariensis ist v. a. als **Abgrenzung/Warneintrag** zum arzneilichen Efeu (Hedera helix) interessant. Nächster Lauf (max. 2/Lauf) sollte hier weitermachen, sofern die Wunschlisten-Vorrang-Entscheidung bestätigt wird.

## 2026-07-15 — Klebriger Alant, Hundszahngras (beide aus der WUNSCHLISTE)

**Quelle:** `docs/wunschliste.json` (5 offene Wuensche). Die ersten beiden — potentilla-reptans, nepeta-nepetella — lagen bereits in `fertig/` (Vorlauf) und wurden per Dedup uebersprungen. Bearbeitet daher die naechsten beiden offenen Wunsch-Eintraege:
- **dittrichia-viscosa** (Klebriger Alant) — `fertig/monographie-klebriger-alant.json`
- **cynodon-dactylon** (Hundszahngras / Bermudagras) — `fertig/monographie-hundszahngras.json`

Kandidatenliste NICHT angefasst (beide sind Wunsch-, keine Kandidaten-Kraeuter). Kein Self-Heal noetig: kein als "offen" markierter Kandidat liegt bereits in `fertig/`.

**Pruefergebnis:** Beide einzeln `✓ ok, mit Hinweisen` (0 Fehler) beim ersten Versuch — **0 Korrekturversuche**. Einziger Hinweis je Datei: enthaelt "unsicher/zu pruefen" (bewusst gesetzt).

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` in der Kandidatenliste geprueft — keine Dublette. Altnamen eingetragen: Dittrichia = Inula viscosa/Cupularia viscosa; Cynodon = Panicum dactylon/Capriola dactylon.

**Hauptquellen (Primaerquellen EMA/HMPC nicht einschlaegig — fuer BEIDE Arten existiert keine europaeische Arzneimonographie):**
- Dittrichia viscosa: J. Ethnopharmacology 2024 (comprehensive review), Molecules 27:2108 (2022), Actas Dermo-Sifiliograficas (Kontaktdermatitis), DermNet NZ (Compositae-Allergie), Wikipedia/InfoFlora/JKI (Abgrenzung D. graveolens).
- Cynodon dactylon: Reviews 'medicinal grass of India' (2024) & J. Med. Chem. Ther.; Allergologie Cyn d 1 (PMC2646682); Veterinaertoxikologie Blausaeure (NMSU B-808, NSW DPI, MSD Vet Manual); Wikipedia/InfoFlora + Abgrenzung Elymus repens / Digitaria sanguinalis.

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Beide Arten: KEIN belegter Heilwert.** Weder HMPC noch ESCOP noch Kommission E fuehren eine Monographie. Alle Indikationen sind PRAE/TRAD (praeklinisch/volksmedizinisch) und durchgehend defensiv formuliert. Bitte als Entwuerfe mit sehr niedriger Evidenz behandeln.
- **Klebriger Alant ist ein Paradox: 'entzuendungshemmend' UND starkes Kontaktallergen.** Die traditionell aeusserliche Anwendung kann durch die Sesquiterpenlactone selbst eine allergische Kontaktdermatitis ausloesen. `asteraceae_allergy=true`. Schutzhandschuhe schon beim Sammeln.
- **Klebriger Alant im Bodenseeraum: Fundort unplausibel.** D. viscosa ist mediterran; ein Bodensee-Fund ist eher Kultur/Adventiv ODER — wahrscheinlicher — eine Fehlbestimmung des sich stark ausbreitenden, schmalblaettrigen *Dittrichia graveolens*. Der deutsche Name 'Klebriger Alant' wird fuer BEIDE Arten benutzt. `region_occurrence` = nur-kultur-selten-verwildert gesetzt. Bitte gegenpruefen, ob die App den Fund evtl. D. graveolens zuordnen sollte.
- **Hundszahngras: die klinisch relevanteste Eigenschaft in Europa ist die POLLEN-Allergie** (Cyn d 1 — Heuschnupfen, Asthma), nicht der Heilwert. Bewusst prominent in `key_warning`/`adverse_effects`.
- **Hundszahngras: cyanogenes Potenzial.** `toxin_ceiling=true` + `toxin_type='cyanogene Glykoside (Blausaeure/HCN)'` gesetzt. Achtung: die Blausaeure-Grenzwerte sind fuer WEIDETIERE (junger/gestresster/welker/frostgeschaedigter Wuchs) belegt; fuer die menschliche Teemenge existiert KEIN definierter Grenzwert (als "unsicher — zu pruefen" vermerkt). Bitte pruefen, ob das Setzen von toxin_ceiling hier in Ihrem Sinn ist oder ob es die Kleinmengen-Nutzung ueberzeichnet.
- **Hundszahngras: `deadly_confusion=true` fuer einen KONTAMINANTEN, nicht fuer eine Doppelgaenger-Pflanze.** Es gibt kein toedlich giftiges Gras als Doppelgaenger; die lebensgefaehrliche Gefahr ist Mutterkorn-Befall (Claviceps, auch C. cynodontis) auf den Aehren. Bewusst so gesetzt, damit das Register greift — bitte pruefen, ob diese Auslegung des Flags erwuenscht ist.

### WICHTIGER Nebenbefund (ausserhalb dieses Laufs, NICHT korrigiert)

Beim Sammel-Lauf `validate_monographie.py fertig/*.json` fallen **11 bereits vorhandene Monographien mit zusammen 38 FEHLERN** durch die Pruefung — u. a. baerlauch (10), johanniskraut (5), beinwell (4), kamille (4), ringelblume (3), salbei (3), brennnessel (2), holunder (2), schafgarbe (2), wermut (2), pfefferminze (1). Typische Ursachen: ungueltige `toxicity_level`-Werte (z. B. 'essbar/gering', 'lebensgefaehrlich' ohne Umlaut, 'teils lebensgefaehrlich (Schierling)'), `type`-Enums bei interactions ('hinweis', 'pharmakokinetisch (schwach)'), `None` statt Leerstring in optionalen Feldern, fehlendes `note`/`main_groups`. Diese Dateien stammen aus frueheren Laeufen und wurden hier **absichtlich nicht angefasst** (Auftrag: genau 2 Monographien). Empfehlung: eigener Bereinigungslauf. Meine beiden neuen Dateien bestehen die Pruefung einzeln fehlerfrei.

## 2026-07-15 — Anis (KANDIDAT), Kanarischer Efeu (WUNSCHLISTE)

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` enthaelt 5 Eintraege; die ersten vier (potentilla-reptans, nepeta-nepetella, dittrichia-viscosa, cynodon-dactylon) liegen bereits in `fertig/` → per Dedup uebersprungen. Einziger offener Wunsch: **hedera-canariensis** (Kanarischer Efeu). Zweiter Platz daher aus der Kandidatenliste: erster offener Eintrag, Tier 1, Listenreihenfolge = **pimpinella-anisum** (Anis).

- **pimpinella-anisum** (Anis) — `fertig/monographie-anis.json` — Quelle: Kandidatenliste (Tier 1). Status → `entwurf_fertig`.
- **hedera-canariensis** (Kanarischer Efeu) — `fertig/monographie-kanarischer-efeu.json` — Quelle: Wunschliste. Wunschliste NICHT angefasst (App hakt selbst ab).

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` in der Kandidatenliste geprueft. Anis: keine Dublette. Kanarischer Efeu: NICHT identisch mit dem vorhandenen `hedera-helix` (eigene Art); `botany.synonyms` bewusst OHNE "Hedera helix var./subsp. canariensis" gefuellt, um eine falsche Dublett-Warnung des Pruefskripts gegen `monographie-efeu.json` zu vermeiden — der infraspezifische Altname steht stattdessen in `synonym_note`. Altnamen eingetragen: Anis = Anisum vulgare/officinarum, Sison anisum, Apium anisum; Kanaren-Efeu = Hedera algeriensis, H. grandifolia hort., H. maderensis. Kein Self-Heal noetig (kein als "offen" markierter Kandidat lag schon in `fertig/`).

**Pruefergebnis:** beide einzeln UND gemeinsam `✓ ok, mit Hinweisen`, 0 Fehler beim **ersten Versuch** — **0 Korrekturversuche**. Einziger Hinweis je Datei: enthaelt "unsicher/zu pruefen" (bewusst gesetzt).

**Hauptquellen:**
- Anis: EMA/HMPC EU herbal monograph + Assessment report Pimpinella anisum L., fructus/aetheroleum; ESCOP Anisi fructus; Kommission E (positiv); Review PMC3405664; EU/EFSA-Bewertung Estragol; Toxikologie-Fallberichte Illicium anisatum in Saeuglings-Sternanis-Tee.
- Kanarischer Efeu: POWO/Kew + GBIF + Trees and Shrubs Online (Taxonomie/Synonymie); PubMed 19143139 (molluskizide Saponine); Giftpflanzen-/Toxikologie-Recherche (Saponine, Falcarinol); EMA/HMPC Hedera helix (nur zur Abgrenzung).

**Quellen-Abruf:** WebFetch auf die EMA-Primaer-PDFs und arzneipflanzenlexikon.info lieferte wie in den Vorlaeufen **HTTP 403**. Inhalte daher ueber WebSearch-Zusammenfassungen mehrerer uebereinstimmender Sekundaerquellen verifiziert. Fuer Anis ist die HMPC-Einstufung (traditional use, nicht WEU) so gut dokumentiert und mehrfach bestaetigt, dass die Evidenzgrade belastbar sind; die EMA-Primaerquelle sollte bei der aerztlichen Sichtung dennoch gegengeprueft werden.

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Anis ist HMPC 'traditional use', NICHT 'well-established use'.** Trotz des festen Rufs als Verdauungs-/Hustenmittel gibt es kaum kontrollierte Humanstudien. Beide Indikationen defensiv als `TU/ESCOP+` getaggt — bitte so bestaetigen, nicht auf WEU hochstufen.
- **Anis: Estragol-Ceiling gesetzt (`toxin_ceiling=true`, `toxin_type=Estragol`).** Estragol ist tierexperimentell genotoxisch/kanzerogen; EU begrenzt die Exposition, HMPC begrenzt die Anwendung auf 2 Wochen. ABER: fuer die uebliche Teemenge existiert KEIN definierter Grenzwert (als "unsicher — zu pruefen" vermerkt). Bitte pruefen, ob das Setzen des Ceilings die harmlose Kuechen-/Teemenge ueberzeichnet — ich habe es defensiv gesetzt, weil das konzentrierte aeth. Oel real riskant ist.
- **Anis: `deadly_confusion=true` betrifft die WACHSENDE Pflanze, nicht die Frucht.** Die Droge ist der Samen; toedlich ist die Verwechslung des bluehenden Doldenbluetlers beim Selbstsammeln mit Schierling (Conium/Cicuta). Der Anisduft ist das rettende Erkennungsmerkmal — bewusst prominent in `key_warning` und `key_features`.
- **Anis: Namensfalle Sternanis.** Japanischer Sternanis (Illicium anisatum, Anisatin) ist NICHT Pimpinella und wird als Verunreinigung in 'Sternanis'-Tee gefunden — hat bei Saeuglingen Kraempfe ausgeloest. Als eigener `confusions`-Eintrag aufgenommen, obwohl botanisch weit entfernt, weil die klinische Relevanz (Saeuglingskoliken-Tee) hoch ist.
- **Kanarischer Efeu bewusst als Warneintrag (`not_for_use=true`, keine Indikationen).** Es gibt fuer Hedera canariensis KEINE Arzneimonographie und keine echte medizinische Anwendungstradition (nur praeklinische Saponin-/Molluskizid-Studien). Statt eine Indikation zu erfinden (waere Regelverstoss), ist der Eintrag ehrlich als Erkennungs-/Warneintrag angelegt: "Das ist NICHT der arzneiliche Efeu." **Wenn Sie lieber einen normalen Niedrig-Evidenz-Eintrag moechten, ist das eine bewusste Ermessensfrage — bitte entscheiden.**
- **Kanarischer Efeu: Fundort Bodensee unplausibel.** Die Art ist frostempfindlich (Kanaren/Madeira/NW-Afrika) und bei uns nur Kuebel-/Zimmerpflanze → `region_occurrence = nur-kultur`. Ein "Bodensee"-Fund ist Kultur ODER eine Fehlbestimmung des heimischen Gemeinen Efeus (Hedera helix). Bitte den Pl@ntNet-Treffer gegenpruefen — Unterscheidung ueber Blattgroesse (gross/ungelappt vs. klein/gelappt) und rote vs. gruene Triebe.
- **Kanarischer Efeu: Taxonomie uneinheitlich.** Frueher als H. helix subsp./var. canariensis gefuehrt, im Handel oft = H. algeriensis. Akzeptierter Name laut POWO: Hedera canariensis Willd. Die App gleicht ueber die `id` ab — falls Pl@ntNet einen anderen akzeptierten Namen liefert, muss die `id` ggf. angepasst werden.

### Nebenbefund (unveraendert aus Vorlauf, NICHT bearbeitet)

Der Sammel-Lauf `validate_monographie.py fertig/*.json` meldet weiterhin zahlreiche Altfehler in frueheren Monographien (u. a. baerlauch, johanniskraut, beinwell, kamille, ringelblume, salbei ...). Diese stammen aus frueheren Laeufen und wurden auftragsgemaess (genau 2 Monographien) NICHT angefasst. Empfehlung unveraendert: eigener Bereinigungslauf. Meine beiden neuen Dateien bestehen die Pruefung einzeln und gemeinsam fehlerfrei.

---

## Lauf 2026-07-15 (18:30 UTC) — Kümmel, Süßholz

**Quelle der Auswahl:** Wunschliste (`docs/wunschliste.json`, 5 Eintraege) enthielt KEINE offenen Wuensche mehr — alle fuenf (potentilla-reptans, nepeta-nepetella, dittrichia-viscosa, cynodon-dactylon, hedera-canariensis) liegen bereits in `fertig/`. Daher beide Plaetze aus der **Kandidatenliste**, Tier 1, erste offene Eintraege in Listenreihenfolge:
1. **carum-carvi (Kümmel)** — Kandidat, Tier 1
2. **glycyrrhiza-glabra (Süßholz)** — Kandidat, Tier 1

**Dedup:** Beide gegen `fertig/` (id + botany.synonyms) und `vorhanden` geprueft — nicht vorhanden. Synonyme selbst eingetragen. Keine Selbstheilung noetig (keine der neuen ids hatte bereits eine Datei).

**Recherche-Kanal:** WebSearch funktionierte gut und lieferte belegte Sekundaer-/Primaerzusammenfassungen. **WebFetch war in diesem Lauf durchgaengig blockiert** (HTTP 403 von ALLEN Zielhosts inkl. EMA, Wikipedia, PMC, e-lactancia; der Agent-Proxy meldete keine relayFailures → Sperre auf Fetcher-Ebene, keine Policy-Sperre). Die EMA/HMPC-Primaer-PDFs konnten daher **nicht direkt** eingesehen werden. Evidenzgrade wurden auf das gesetzt, was die (zahlreichen, konsistenten) Sekundaerquellen + HMPC-Zusammenfassungen belegen; nicht geraten. **Aerztliche Gegenpruefung der Evidenzeinstufung empfohlen.**

**Pruefergebnis:** Beide bestehen `validate_monographie.py` einzeln und gemeinsam fehlerfrei (nur der erwuenschte "unsicher/zu pruefen"-Hinweis). 0 Korrekturversuche noetig.

**Hauptquellen:** EMA/HMPC Carvi fructus + Carvi aetheroleum; ESCOP Carvi; Kommission E Kümmel. EMA/HMPC Liquiritiae radix (Erstfassung 2012; Revision 1 in Konsultation 2025); ESCOP + Kommission E Süßholz; EFSA-Glycyrrhizin-Schwelle; Fallbericht-Reviews Pseudohyperaldosteronismus (Frontiers Pharmacol.).

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Kümmel — Evidenz-Falle:** HMPC listet nur **traditional use**. Die eigentlich guten RCTs betreffen die **fixe Pfefferminz-/Kuemmeloel-Kombination (Menthacarin)** bei funktioneller Dyspepsie — NICHT den Kuemmeltee/das Kuemmeloel allein. Bewusst in `pharmacology.evidence_caveat`, `expectation_summary.overstated` und `key_warning` getrennt gehalten, damit die Kombi-Evidenz nicht auf die Einzeldroge uebertragen wird.
- **Kümmel — anders als Fenchel/Anis:** nur **Spuren** Estragol/Safrol → **kein** relevantes Estragol-Ceiling. `toxin_ceiling=false` gesetzt (bewusste Abweichung vom Anis-Muster). Bitte gegenpruefen.
- **Süßholz — Verwechslungsfeld ungewoehnlich:** Als Import-/Kulturwurzel gibt es **keine giftige Feld-Verwechslung**; das echte Risiko ist eine **DOSIS-Verwechslung** (verstecktes Glycyrrhizin in Lakritz-Suesswaren/-Tees, die sich mit der Kur zur kritischen Tagesdosis summieren). `confusions` enthaelt daher bewusst (1) andere Glycyrrhiza-Arten, (2) versteckte Lakritzquellen als "giftig" (Glycyrrhizin), (3) eine begruendete "keine Feld-Verwechslung"-Zeile — statt erfundener botanischer Doppelgaenger.
- **Süßholz — pregnancy_contraindicated=true** gesetzt (HMPC: "nicht empfohlen"; zusaetzlich Frühgeburts-/Entwicklungssignal aus Beobachtungsstudien). Bewusst defensiver als das reine "nicht empfohlen" der HMPC — bitte pruefen, ob die App-Register-Einstufung "kontraindiziert" so gewuenscht ist.
- **Süßholz — HMPC-Dosis vs. Sicherheitsschwelle:** HMPC-Tagesdosis (5–15 g Wurzel ≈ 200–600 mg Glycyrrhizin, max. 4 Wochen) liegt DEUTLICH ueber der ~100-mg/Tag-Dauerkonsum-Schwelle (EFSA). Beide Werte stehen bewusst nebeneinander in `standard_dose`/`tox_ceiling` — der Widerspruch ist real (kurze Kur vs. Dauerkonsum) und sollte aerztlich eingeordnet werden.

### Nebenbefund (weiterhin offen, NICHT bearbeitet)

Der Sammel-Lauf `validate_monographie.py fertig/*.json` meldet unveraendert 38 Altfehler in 11 frueheren (offenbar handkuratierten, ohne `herkunft`-Feld) Monographien: baerlauch, beinwell, brennnessel, holunder, johanniskraut, kamille, pfefferminze, ringelblume, salbei, schafgarbe, wermut. Ursache u. a. kombinierte `toxicity_level`-Werte wie 'essbar/gering', die das aktuelle Schema nicht mehr erlaubt. Auftragsgemaess (genau 2 Monographien) NICHT angefasst. Empfehlung unveraendert: eigener Bereinigungslauf.

---

## Lauf 2026-07-15 (20:00 UTC) — Isländisches Moos, Passionsblume

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` (Stand 2026-07-15, 5 Eintraege) enthielt KEINEN offenen Wunsch mehr — alle fuenf (potentilla-reptans, nepeta-nepetella, dittrichia-viscosa, cynodon-dactylon, hedera-canariensis) liegen bereits in `fertig/` (per Dedup gegen id + botany.synonyms bestaetigt). Daher beide Plaetze aus der **Kandidatenliste**, Tier 1, erste offene Eintraege in Listenreihenfolge:
1. **cetraria-islandica (Isländisches Moos)** — Kandidat, Tier 1 → `fertig/monographie-islaendisches-moos.json`, Status `entwurf_fertig`
2. **passiflora-incarnata (Passionsblume)** — Kandidat, Tier 1 → `fertig/monographie-passionsblume.json`, Status `entwurf_fertig`

**Dedup:** Beide gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` geprueft — nicht vorhanden. Synonyme selbst eingetragen (Cetraria: Lichen islandicus L.; Passiflora: Granadilla incarnata (L.) Medik.). Keine Selbstheilung noetig (keine der beiden neuen ids hatte bereits eine Datei; kein weiterer "offen"-Kandidat lag in `fertig/`).

**Recherche-Kanal:** WebSearch funktionierte gut. **WebFetch war in diesem Lauf durchgaengig blockiert (HTTP 403 von ALLEN Zielhosts** — EMA, arzneipflanzenlexikon.info, altmeyers.org, e-lactancia, accurateclinic, Health Canada). Die EMA/HMPC- und ESCOP-**Primaerquellen konnten NICHT direkt eingesehen werden**. Evidenzgrade (beide TU bzw. Passiflora TU/ESCOP+) wurden auf das gesetzt, was mehrere konsistente Sekundaerquellen + die HMPC-Zusammenfassungen belegen; nicht geraten. **Primaerquelle nicht erreichbar — Evidenzgrad ungeprueft, aerztliche Gegenpruefung noetig.**

**Pruefergebnis:** Beide bestehen `validate_monographie.py` einzeln und gemeinsam fehlerfrei (0 Fehler), nur der erwuenschte "unsicher/zu pruefen"-Hinweis. **0 Korrekturversuche.**

**Hauptquellen:**
- Isländisches Moos: EMA/HMPC EU herbal monograph Cetraria islandica (L.) Ach. s.l., thallus (traditional use, EMA/HMPC/678891/2013); Kommission E; arzneipflanzenlexikon.info/apotheken.de/pharmawiki (Dosierung, Zubereitung); ScienceDirect/ResearchGate zur Schwermetall-Bioakkumulation; Naturschutz-/Flechtenquellen (Cladonia rangiferina, Letharia vulpina/Vulpinsaeure).
- Passionsblume: EMA/HMPC EU herbal monograph Passiflora incarnata L., herba (traditional use) + Assessment report 2014; ESCOP Passiflorae herba; Kommission E; arzneipflanzenlexikon.info (Tagesdosis 4-8 g, Anwendungsdauer 2 Wochen, Kinder <12 nicht); Rehwald 1995 (Harman-Alkaloide nur Spuren) & Holbik 2010 (Gynocardin nicht reproduzierbar); Bestimmungsquellen P. incarnata vs. P. caerulea.

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Isländisches Moos ist eine FLECHTE, kein Moos** (Pilz-Alge-Symbiose). Der Reason-Eintrag der Warteschlange ("Flechte, kein Kraut") stimmt. Das hat zwei Konsequenzen: (1) `harvest_organ` als "Kraut (ganzer Thallus/Flechtenkoerper)" formuliert, damit der Erntekalender-Filter greift; (2) nicht gaertnerisch kultivierbar (extrem langsames Wachstum) → `garden.bodensee_suitability` = nicht anbaubar.
- **Isländisches Moos — die eigentliche Gefahr ist der SAMMELORT, nicht die Droge.** Flechten haben keine Cuticula und akkumulieren Cadmium/Blei/Quecksilber massiv aus der Luft (Cetraria islandica hat in Studien die hoechste Cd-Aufnahme). Wildsammlung an Strassen/Industrie daher riskant; zudem ist die Art regional geschuetzt. Das steht bewusst prominent in `key_warning` und `collection_rules`. `high_safety` deshalb **false** (obwohl die Droge selbst sehr sicher ist).
- **Isländisches Moos — Zwei-Wege-Zubereitung ist der klinisch relevante Punkt.** Schleimstoffe (wasserloeslich) fuer die Reizlinderung → Kaltmazerat/kurzer Aufguss, Bitterstoffe koennen ausgewaschen werden. Fuer die Appetit-Indikation dagegen heiss und bitter belassen. In `chemistry.solubility_note` und `preparation` erklaert. Kein giftiger PFLANZEN-Doppelgaenger, aber die giftige Wolfsflechte (Letharia vulpina, gelbgruen, Vulpinsaeure) als `giftig` eingetragen — `deadly_confusion=false`, weil giftig, nicht lebensgefaehrlich.
- **Isländisches Moos — Evidenz bewusst nur TU.** Trotz festem Ruf als "Lungen-/Hustenmittel" nur traditional use; die in-vitro antimikrobiellen Flechtensaeuren rechtfertigen KEINE Infekttherapie → in `expectation_summary.overstated` und als "unsicher — zu pruefen" vermerkt.
- **Passionsblume — Evidenz TU/ESCOP+, NICHT WEU.** HMPC nur traditional use; ESCOP + Kommission E positiv. Es gibt einzelne kleine RCTs (praeop. Angst), aber keine belastbare WEU-Grundlage. Defensiv als TU/ESCOP+ getaggt — bitte nicht hochstufen.
- **Passionsblume — zentrale Verwechslung ist eine QUALITAETS-/Verfaelschungsfrage, kein toedlicher Doppelgaenger.** Die in deutschen Gaerten dominante winterharte P. caerulea (FUENFlappig, blau-weiss) ist NICHT die arzneiliche P. incarnata (DREIlappig, weiss-lila) und enthaelt mehr cyanogene Glykoside. Als `giftig` eingetragen, aber `deadly_confusion=false` (keine akute Lebensgefahr in ueblichen Mengen). Fuer den Arzt/Pl@ntNet-Abgleich relevant: bei einem "Bodensee"-Fund ist P. caerulea deutlich wahrscheinlicher als die arzneiliche Art — `region_occurrence` = nur-kultur (P. incarnata bei uns nicht sicher winterhart).
- **Passionsblume — zwei alte Sicherheitsmythen aktiv entschaerft:** (1) Die frueher befuerchtete MAO-Hemmung durch Harman-/beta-Carbolin-Alkaloide gilt als ueberholt — die Gehalte liegen nur im ppm-Bereich (Rehwald 1995), klinisch irrelevant. (2) Das cyanogene Glykosid Gynocardin liess sich in P. incarnata nicht reproduzierbar isolieren (Holbik 2010). Beide als `theoretisch`/`gering`/"unsicher — zu pruefen" markiert, damit weder eine falsche Interaktionswarnung noch eine falsche Entwarnung entsteht. Bitte gegenpruefen.

### Nebenbefund (weiterhin offen, NICHT bearbeitet)

Der Sammel-Lauf `validate_monographie.py fertig/*.json` meldet unveraendert die ~38 Altfehler in 11 frueheren, offenbar handkuratierten Monographien (baerlauch, beinwell, brennnessel, holunder, johanniskraut, kamille, pfefferminze, ringelblume, salbei, schafgarbe, wermut). Auftragsgemaess (genau 2 Monographien) NICHT angefasst. Empfehlung unveraendert: eigener Bereinigungslauf. Meine beiden neuen Dateien bestehen die Pruefung einzeln und gemeinsam fehlerfrei.

## Lauf 2026-07-16 — Lavendel, Ginkgo

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` (Stand 2026-07-15, 5 Eintraege) enthielt KEINEN offenen Wunsch mehr — alle fuenf (potentilla-reptans → kriechendes-fingerkraut, nepeta-nepetella → kleine-katzenminze, dittrichia-viscosa → klebriger-alant, cynodon-dactylon → hundszahngras, hedera-canariensis → kanarischer-efeu) liegen bereits in `fertig/` (per Dedup gegen id bestaetigt). Die Root-`wunschliste.json` ist ohnehin leer (anzahl 0). Daher beide Plaetze aus der **Kandidatenliste**, Tier 1, erste offene Eintraege in Listenreihenfolge:
1. **lavandula-angustifolia (Lavendel)** — Kandidat, Tier 1 → `fertig/monographie-lavendel.json`, Status `entwurf_fertig`
2. **ginkgo-biloba (Ginkgo)** — Kandidat, Tier 1 → `fertig/monographie-ginkgo.json`, Status `entwurf_fertig`

**Dedup:** Beide gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` geprueft — nicht vorhanden. (Der grep-Treffer "Lavandula" in `monographie-rosmarin.json` war nur eine Nennung im scientific_name eines Verwechslungs-Eintrags, keine Dublette.) Synonyme selbst eingetragen: Lavendel = Lavandula officinalis Chaix / L. vera DC. / L. spica L. p.p.; Ginkgo = Salisburia adiantifolia Sm. u.a. Keine Selbstheilung noetig.

**Recherche-Kanal:** WebSearch funktionierte gut und lieferte konsistente Sekundaerinfos inkl. HMPC-Zusammenfassungen. **WebFetch war in diesem Lauf durchgaengig blockiert (HTTP 403 von ALLEN Zielhosts** — EMA, altmeyers.org, pdf4pro, sogar Wikipedia). Die EMA/HMPC- und ESCOP-**Primaerdokumente konnten NICHT direkt eingesehen werden**. Evidenzgrade wurden auf das gesetzt, was mehrere konsistente Sekundaerquellen + die HMPC-Public-Summaries belegen; nicht geraten. **Primaerquelle nicht erreichbar — Evidenzgrad ungeprueft, aerztliche Gegenpruefung noetig.**

**Pruefergebnis:** Beide bestehen `validate_monographie.py` einzeln und gemeinsam fehlerfrei (0 Fehler), nur der erwuenschte "unsicher/zu pruefen"-Hinweis. **0 Korrekturversuche.**

**Hauptquellen:**
- Lavendel: EMA/HMPC EU herbal monograph Lavandulae aetheroleum + Lavandulae flos (beide traditional use); Kommission E (positiv); RCTs zu Silexan — Woelk & Schlaefke 2010 (Phytomedicine, vs. Lorazepam) und Kasper 2014 (Int J Neuropsychopharmacol, vs. Paroxetin/Placebo); arzneipflanzenlexikon.info; botanische Quellen zur Abgrenzung L. angustifolia / L. latifolia / L. × intermedia.
- Ginkgo: EMA/HMPC EU herbal monograph Ginkgo biloba L. folium (EMA/HMPC/321097/2012, WEU Spezialextrakt + TU Blattpulver); ESCOP; Kommission E; DeKosky 2008 (GEM Study, JAMA); AkdAe/Pharmazeutische Zeitung zu Blutungen + Gerinnungshemmern; Ph.-Eur.-Spezifikation (22-27 % Flavonglykoside, 5-7 % Terpenlactone, Ginkgolsaeuren < 5 ppm).

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Lavendel — RCT ist nicht gleich HMPC-WEU (Kernpunkt).** Es gibt fuer Lavendeloel echte, gute RCT-Evidenz bei Angst — aber ausschliesslich fuer das EINE standardisierte Praeparat Silexan (= Wirkstoff von Lasea, 80 mg oral), das national als Fertigarzneimittel zugelassen ist, NICHT ueber die HMPC-WEU-Schiene. Die HMPC-Monographie selbst fuehrt Lavendeloel nur als traditional use. Ich habe die Angst-/Unruhe-Indikation daher **RCT/TU** getaggt (RCT fuer Silexan, TU fuer die HMPC-Kategorie), Stress/Schlaf **TU**, Roemheld/Oberbauch **TU/TRAD** (Kommission E). Bitte pruefen, ob dieses gemischte Tagging der App-Logik entspricht — es ist bewusst gesetzt, nicht schoengeredet.
- **Lavendel — Uebertragungsfalle.** Die groesste Erwartungs-Ueberschaetzung ist die Uebertragung der Silexan-Daten auf Tee, Duftlampe und Duftkissen. Explizit in expectation_summary.overstated und key_warning: Studienevidenz gilt NUR fuer Silexan. Zusatz: billiges Handels-"Lavendeloel" ist meist Lavandin (L. × intermedia), kampferreich und arzneilich ungleichwertig.
- **Lavendel — kein toedlicher Doppelgaenger, aber confusions bewusst gefuellt.** Lippenbluetler haben keinen lebensgefaehrlichen Lookalike; die relevanten "Verwechslungen" sind Chemotyp-/Qualitaetsfragen: Lavandin und Speiklavendel (L. latifolia) — beide ungiftig (toxicity_level essbar), aber kampferreich; kampferreiche Oele nicht ins Gesicht von Saeuglingen (Stimmritzenkrampf). deadly_confusion=false. high_safety=true gesetzt (Oel in Erwachsenen sehr sicher), aber mit ehrlichen Kaveaten.
- **Lavendel — umstrittener endokriner Signalbefund.** Einzel-Fallberichte (Gynaekomastie bei praepubertaeren Jungen nach topischen Lavendel-/Teebaumoel-Produkten, Henley 2007) zu einem schwach oestrogen-/antiandrogenen Effekt; Kausalitaet umstritten, nicht bestaetigt. Als **theoretisch/"unsicher — zu pruefen"** eingetragen, damit weder Panik noch falsche Entwarnung. Bitte aerztlich einordnen.
- **Ginkgo — Zwei-Stufen-Evidenz sauber getrennt.** WEU gilt NUR fuer den standardisierten, aufwendig hergestellten und von Ginkgolsaeuren gereinigten Spezialextrakt (EGb-761-Typ) bei leichter Demenz; das einfache Blattpulver nur TU (schwere Beine/kalte Haende). Selbst gemachter Blaettertee ist weder wirksamkeitsbelegt noch von Allergenen befreit — bewusst in preparation/collection_rules/key_warning betont.
- **Ginkgo — Erwartung stark daempfen.** Kein Gedaechtnis-Booster fuer Gesunde; verhindert KEINE Demenz — die grosse GEM-Studie (DeKosky 2008, JAMA) war zur Praevention negativ. Tinnitus/Schwindel nur schwach beeinflussbar (ESCOP+/TU). In expectation_summary.overstated adressiert.
- **Ginkgo — Blutungsrisiko ist die klinisch heikelste, aber widerspruechliche Stelle.** Ginkgolide sind PAF-Antagonisten → theoretisch additive Blutungsneigung mit ASS/Clopidogrel/oralen Antikoagulanzien; es gibt Fallberichte (auch Hirnblutungen), aber kontrollierte Studien am Gesunden fanden KEINE klinisch relevante Gerinnungsaenderung. Ich habe die Interaktion vorsichtshalber als **relevant, Datenlage widerspruechlich, "unsicher — zu pruefen"** eingetragen und "vor OP absetzen" empfohlen. interaction_heavy=true, high_safety=false. Bitte final aerztlich gewichten.
- **Ginkgo — Teil-Verwechslung Blatt vs. Samen (wichtig).** Die Pflanze selbst ist unverwechselbar (Faecherblatt), daher confusions-Eintrag "keine verwechselbare Pflanze" mit Begruendung. ABER: der SAMEN ist ein anderes, giftiges Pflanzenteil — geroestete "Ginkgonuesse"/Ginnan enthalten das Nervengift Ginkgotoxin (4'-O-Methylpyridoxin), das v.a. bei Kindern/B6-Mangel Krampfanfaelle ausloesen kann; das Fruchtfleisch reifer Samen verursacht durch Ginkgolsaeuren allergische Kontaktdermatitis (giftefeu-aehnlich). Als zweiter confusions-Eintrag (giftig) eingetragen, damit die Blatt-Samen-Grenze klar ist. toxin_ceiling blieb false, weil das Toxin im Samen sitzt, nicht im standardisierten Blattextrakt.

### Nebenbefund (weiterhin offen, NICHT bearbeitet)

Der Sammel-Lauf `validate_monographie.py fertig/*.json` meldet weiterhin die ~38 Altfehler in den frueheren handkuratierten Monographien (baerlauch, beinwell, brennnessel, holunder, johanniskraut, kamille, pfefferminze, ringelblume, salbei, schafgarbe, wermut). Auftragsgemaess (genau 2 Monographien) NICHT angefasst. Empfehlung unveraendert: eigener Bereinigungslauf. Meine beiden neuen Dateien bestehen die Pruefung einzeln und gemeinsam fehlerfrei.

---

## Lauf 2026-07-16 (zweiter Lauf des Tages) — Artischocke + Baerentraube

**Auswahl / Quelle:** Wunschliste (`docs/wunschliste.json`, 5 Eintraege) hatte **0 offene** — alle fuenf (potentilla-reptans, nepeta-nepetella, dittrichia-viscosa, cynodon-dactylon, hedera-canariensis) liegen bereits in `fertig/` (IDs + scientific_name geprueft). Daher beide Kraeuter aus der **Kandidatenliste**, erste offene Tier-1-Eintraege in Listenreihenfolge:
- **Artischocke** — Cynara cardunculus (`cynara-cardunculus`), Tier 1, KANDIDAT
- **Echte Baerentraube** — Arctostaphylos uva-ursi (`arctostaphylos-uvaursi`), Tier 1, KANDIDAT

**Dedup:** Beide gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` geprueft — nicht vorhanden. Synonyme selbst eingetragen: Artischocke = Cynara scolymus L. / Cynara cardunculus var. scolymus (L.) Benth.; Baerentraube = Arbutus uva-ursi L. u.a. Keine Selbstheilung noetig.

**Recherche-Kanal:** WebSearch funktionierte gut (HMPC-Public-Summaries, Kommission E, ESCOP, Cochrane, botanische Unterscheidung). **WebFetch war erneut durchgaengig 403** (EMA, altmeyers.org, arzneipflanzenlexikon.info, drugs.com, sogar Wikipedia). **EMA/HMPC- und ESCOP-Primaerdokumente konnten NICHT direkt eingesehen werden.** Evidenzgrade auf das gesetzt, was mehrere konsistente Sekundaerquellen + HMPC-Summaries belegen; nicht geraten. **Primaerquelle nicht erreichbar — Evidenzgrad ungeprueft, aerztliche Gegenpruefung noetig.**

**Pruefergebnis:** Beide bestehen `validate_monographie.py` einzeln fehlerfrei (0 Fehler), nur die erwuenschten "unsicher/zu pruefen"-Hinweise (+ bei der Baerentraube ein bewusster id-Mismatch-Hinweis, siehe unten). **0 Korrekturversuche.**

**Hauptquellen:**
- Artischocke: EMA/HMPC EU herbal monograph Cynara cardunculus L. (syn. C. scolymus L.), folium (traditional use); Kommission E (dyspeptische Beschwerden); ESCOP; Cochrane Review Wider B et al. 2013/2016 (Hypercholesterinaemie); Taxonomie via Arzneipflanzen-Lexikon/GRIN (akzeptiert Cynara cardunculus L.).
- Baerentraube: EMA/HMPC EU herbal monograph Arctostaphylos uva-ursi (L.) Spreng., folium (traditional use, Rev.); Kommission E; ESCOP; Ph. Eur. (min. 7 % wasserfreies Arbutin); Sekundaerquellen zur Preiselbeeren-Abgrenzung (Netznervatur) und zum Naturschutzstatus; Garcia de Arriba et al. 2013 (Hydrochinon-Risikobewertung).

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Artischocke — RCT trotzdem kein WEU (Kernpunkt).** Fuer die Cholesterinsenkung gibt es RCTs und eine Cochrane-Uebersicht, aber HMPC vergibt NUR traditional use (Dyspepsie), KEINEN well-established use. Ich habe Dyspepsie **TU/ESCOP+** und die Cholesterin-Indikation SEPARAT als **RCT** getaggt, mit ausdruecklicher Erwartungsdaempfung (modester Effekt, kein Statin-Ersatz, keine HMPC-Indikation). Bitte pruefen, ob das getrennte Tagging der App-Logik entspricht — bewusst gesetzt.
- **Artischocke — echter Sicherheitspunkt, nicht nur Erwartung.** Bei **Verschluss der Gallenwege ist die Pflanze kontraindiziert**, bei **Gallensteinen nur nach aerztlicher Ruecksprache**: die choleretische (gallentreibende) Wirkung kann eine Kolik ausloesen. In key_warning und contraindications betont. Korbbluetler-Allergie-Flag gesetzt (asteraceae_allergy=true).
- **Artischocke — Organ-Falle.** Arzneilich zaehlt das bittere LAUBBLATT (Cynarae folium), NICHT der als Gemuese gegessene Bluetenboden. In identification/kitchen klar getrennt. Kein giftiger Doppelgaenger (reine Kulturpflanze) → confusions bewusst mit ungiftigen Disteln + Begruendungseintrag gefuellt.
- **Baerentraube — toxin_ceiling ist der Kern.** Wirkstoff Hydrochinon (aus Arbutin) ist potenziell genotoxisch. Harte Grenze: **max. 1 Woche am Stueck, hoechstens ca. 5x/Jahr**; feste KONTRAINDIKATION in **Schwangerschaft/Stillzeit** und bei **unter 18-Jaehrigen** (nicht nur Vorsichtsnote — HMPC fuehrt es als feste Kontraindikation). flags: toxin_ceiling=true, toxin_type="Hydrochinon (aus Arbutin freigesetzt)", pregnancy_contraindicated=true. KEIN Antibiotikaersatz bei fieberhaftem/aufsteigendem Infekt.
- **Baerentraube — pH-Abhaengigkeit umstritten.** Klassische Lehre: Wirkung an alkalischen Harn gebunden (bakterielle Freisetzung des Hydrochinons); neuere Daten stellen die strikte pH-Abhaengigkeit teils in Frage. Als **"unsicher — zu pruefen"** vermerkt; die alte Empfehlung, den Harn zu alkalisieren / harnansaeuernde Mittel (hohe Vitamin-C-Dosen) zu meiden, defensiv als theoretische Interaktion eingetragen.
- **Baerentraube — Verwechslung mit Preiselbeere (essbar).** Wichtigster Doppelgaenger, waechst oft daneben. Sicheres Unterscheidungsmerkmal: **netznervige Blattunterseite** der Baerentraube vs. braune Druesenpunkte + umgerollter Rand der Preiselbeere. Kein toedlicher Doppelgaenger; das eigentliche Risiko ist der Wirkstoff, nicht die Verwechslung. Zusaetzlich Alpen-Baerentraube und Moos-/Rauschbeere (alle essbar) gelistet.
- **Baerentraube — Naturschutz.** In Deutschland **besonders geschuetzt → Wildsammlung verboten**; in collection_rules/harvest betont, Bezug aus Anbau/Apotheke. Fuer den Bodenseeraum ehrlich: wild nur selten in den Voralpen (kalkmeidend), im meist kalkhaltigen Gartenboden schlecht kultivierbar.
- **Baerentraube — id-Normalisierung (bewusst, bitte kennen).** Botanisches Epitheton ist der Bindestrich-Begriff **"uva-ursi"**. Das Pruefschema/der App-Abgleich erlaubt aber nur EIN gattung-art-Bindestrichpaar (`^[a-z]+-[a-z]+$`). Um `validate_monographie.py` fehlerfrei zu halten, wurde die id auf **`arctostaphylos-uvaursi`** (ein Bindestrich) gesetzt und in botany.synonym_note dokumentiert. Der Kandidateneintrag traegt weiterhin die id `arctostaphylos-uva-ursi` (unveraendert). **Der Arzt/die App sollte pruefen, ob der Pl@ntNet-Abgleich diese Normalisierung mitmacht** — ggf. muss die App fuer hyphenierte Epitheta eine Sonderregel haben. Dedup ist unabhaengig davon ueber scientific_name/Synonyme gesichert.

### Nebenbefund (weiterhin offen, NICHT bearbeitet)

Der Sammel-Lauf `validate_monographie.py fertig/*.json` meldet unveraendert die ~38 Altfehler in 11 frueheren handkuratierten Monographien (baerlauch, beinwell, brennnessel, holunder, johanniskraut, kamille, pfefferminze, ringelblume, salbei, schafgarbe, wermut) — meist `toxicity_level`-Werte wie "essbar/gering", die das Schema nicht kennt. Auftragsgemaess (genau 2 Monographien, kuratierte Dateien gehoeren dem Arzt) NICHT angefasst. Empfehlung: eigener Bereinigungslauf. Meine beiden neuen Dateien bestehen die Pruefung einzeln fehlerfrei.

---

## Lauf 2026-07-16 (2. Lauf des Tages) — Moenchspfeffer, Gartenkuerbis

**Auswahl / Quelle:** `docs/wunschliste.json` hat 5 Eintraege — aber ALLE 5 liegen bereits in `fertig/` (potentilla-reptans, nepeta-nepetella, dittrichia-viscosa, cynodon-dactylon, hedera-canariensis; per id + Synonym-Dedup geprueft). Wunschliste damit **0 offene Eintraege** → beide Plaetze aus `kraeuter-kandidaten.json`. Genommen: die ersten beiden offenen, tier 1, Listenreihenfolge:
- **Moenchspfeffer** (Vitex agnus-castus) — Kandidat, tier 1
- **Gartenkuerbis** (Cucurbita pepo) — Kandidat, tier 1

Beide vorab dedupliziert (id + botany.synonyms in `fertig/` + `vorhanden`): nicht vorhanden.

**Pruefergebnis:** Beide bestehen `validate_monographie.py` einzeln **fehlerfrei (0 Fehler)**, nur erwuenschte `! Hinweis`-Zeilen (bewusstes "unsicher/zu pruefen" + beim Moenchspfeffer ein bewusster id-Mismatch-Hinweis, siehe unten). **0 Korrekturversuche.**

**Hauptquellen:**
- Moenchspfeffer: EMA/HMPC EU herbal monograph Vitex agnus-castus L., fructus (Rev. 1); Kommission E; ESCOP; Fachliteratur zu dopaminergen Diterpenen (Rotundifuran u. a.) / D2-Rezeptor / Prolaktinsenkung; Taxonomie Verbenaceae→Lamiaceae.
- Gartenkuerbis: EMA/HMPC EU herbal monograph Cucurbita pepo L., semen; Kommission E; ESCOP; Fachliteratur zu Delta-7-Sterolen / Steirischem Oelkuerbis (var. styriaca); Toxikologie Cucurbitacine / "toxisches Kuerbissyndrom".
- **Primaerquellen-Hinweis:** Die EMA-PDFs sind beim direkten WebFetch mit **HTTP 403** nicht erreichbar gewesen (wie im Prompt vorgesehen). Inhalte daher aus EMA-Zusammenfassungen + Sekundaerquellen. **Evidenzgrad WEU/TU ungeprueft an der Primaerquelle — aerztliche Gegenpruefung noetig**, insbesondere die WEU-Einstufung des Moenchspfeffers.

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Moenchspfeffer — WEU, nicht nur TU (Kernpunkt).** Anders als die meisten bisher bearbeiteten Kraeuter fuehrt HMPC hier tatsaechlich **well-established use** — aber NUR fuer das PMS und NUR fuer EINEN bestimmten standardisierten Trockenextrakt (ca. 20 mg/Tag, kontinuierlich bis 3 Monate). Ich habe PMS/Mastodynie als **WEU/RCT** und die leichten praemenstruellen Beschwerden/Zyklusstoerungen separat als **TU** getaggt. Bitte pruefen, ob die WEU-Zuordnung app-/quellenkonform ist (Primaerquelle war 403).
- **Moenchspfeffer — echte Gegenanzeigen trotz "pflanzlich".** Dopaminerg/prolaktinsenkend wirksam: **kontraindiziert in Schwangerschaft/Stillzeit** (flags.pregnancy_contraindicated=true), bei **Prolaktinom/Hypophysentumor** und zusammen mit **Dopamin-Agonisten/-Antagonisten** (Antipsychotika, Metoclopramid, Bromocriptin). In key_warning, contraindications und interactions betont. Kinderwunsch/Gelbkoerperschwaeche bewusst als **overstated** eingeordnet (schwache Evidenz).
- **Moenchspfeffer — id-Normalisierung (bewusst, bitte kennen).** Artepitheton ist bindestrich-geschrieben ("agnus-castus"). Da `^[a-z]+-[a-z]+$` nur EIN Bindestrichpaar erlaubt (gleiche Situation wie zuvor bei der Baerentraube "uva-ursi"), wurde die **id auf `vitex-agnuscastus`** zusammengezogen und in botany.synonym_note dokumentiert. Der Kandidateneintrag behaelt die id `vitex-agnus-castus`. **Pl@ntNet-Abgleich der App bitte auf hyphenierte Epitheta pruefen.** Dedup lief unabhaengig ueber scientific_name.
- **Moenchspfeffer — Taxonomie.** Gattung Vitex wurde von den **Verbenaceae in die Lamiaceae** ueberfuehrt (molekulare Phylogenie); aeltere Literatur/Etiketten fuehren sie noch als Verbenaceae. In family + synonym_note vermerkt. Das Binomen selbst ist stabil → botany.synonyms bewusst leer (kein lateinischer Alt-Binomialname in Gebrauch).
- **Gartenkuerbis — nur TU trotz RCTs (Kernpunkt).** Es gibt einzelne kontrollierte Studien zu Prostata-/Blasensymptomen, aber HMPC vergibt **nur traditional use**, KEINEN WEU. Getaggt **TU/ESCOP+**, mit ausdruecklicher Erwartungsdaempfung: **verkleinert die Prostata NICHT**, stoppt die BPH-Progression nicht, rein symptomatisch. In key_warning: **Prostatakarzinom aerztlich ausschliessen**, bevor selbst behandelt wird.
- **Gartenkuerbis — die eigentliche Gefahr ist die Verwechslung, nicht die Droge.** `confusions` bewusst mit dem **Cucurbitacin-/"toxischen Kuerbissyndrom"** gefuellt (giftig): durch Rueckkreuzung/Selbstaussaat oder bei Zierkuerbissen/Flaschenkuerbis koennen Fruechte hohe Cucurbitacin-Mengen bilden → heftige Magen-Darm-Vergiftung, in schweren Faellen Kreislauf/Haarausfall; **Kochen zerstoert das Gift nicht**; WARNZEICHEN ist der **bittere Geschmack**. Als "giftig" (nicht "lebensgefaehrlich") eingestuft, da meist selbstlimitierend → deadly_confusion=false. In collection_rules/garden/kitchen mehrfach betont (bittere Fruechte nie zur Samengewinnung).
- **Gartenkuerbis — Arznei-Sorte.** Arzneilich bevorzugt der schalenlos-samige **Steirische Oelkuerbis** (var. styriaca) mit "nackten" Samen; in botany.synonym_note + identification dokumentiert. high_safety-Flag NICHT gesetzt (wegen der giftigen Cucurbitacin-Verwechslung), obwohl die Droge selbst sehr sicher ist.

### Nebenbefund (weiterhin offen, NICHT bearbeitet)

Der Sammel-Lauf `validate_monographie.py fertig/*.json` meldet unveraendert die bekannten ~38 Altfehler in den frueheren handkuratierten Monographien (u. a. `toxicity_level`-Werte wie "essbar/gering"). Auftragsgemaess (genau 2 Monographien, kuratierte Dateien gehoeren dem Arzt) NICHT angefasst. Beide neuen Dateien bestehen einzeln fehlerfrei.

---

## Lauf 2026-07-16 (3. Lauf des Tages) — Purpur-Sonnenhut, Knoblauch

**Auswahl / Quelle:** `docs/wunschliste.json` (5 Einträge) hat **0 offene** — alle fünf (potentilla-reptans, nepeta-nepetella, dittrichia-viscosa, cynodon-dactylon, hedera-canariensis) liegen bereits in `fertig/` (per id + Synonym-Dedup bestätigt). Root-`wunschliste.json` ist leer (anzahl 0). Daher beide Plätze aus `kraeuter-kandidaten.json`, erste offene Tier-1-Einträge in Listenreihenfolge:
- **echinacea-purpurea (Purpur-Sonnenhut)** — Kandidat, Tier 1 → `fertig/monographie-purpursonnenhut.json`, Status `entwurf_fertig`
- **allium-sativum (Knoblauch)** — Kandidat, Tier 1 → `fertig/monographie-knoblauch.json`, Status `entwurf_fertig`

**Dedup:** Beide gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` geprüft — nicht vorhanden. Synonyme selbst eingetragen (Echinacea: Rudbeckia purpurea L., Brauneria purpurea u. a.; Allium sativum: Allium longicuspis Regel, A. controversum, Porrum sativum). Der grep-Treffer "Allium" in `monographie-baerlauch.json` (allium-ursinum) ist eine andere Art — keine Dublette. Keine Selbstheilung nötig (kein weiterer als "offen" markierter Kandidat lag bereits in `fertig/`).

**Recherche-Kanal:** WebSearch funktionierte gut (HMPC-Zusammenfassungen, Cochrane, Kommission E, ESCOP, BfArM). **WebFetch auf die EMA-Primär-PDFs erneut durchgehend HTTP 403** (Echinacea- und Allium-Monograph). Die EMA/HMPC-Primärdokumente konnten NICHT direkt eingesehen werden. Evidenzgrade auf das gesetzt, was mehrere konsistente Sekundärquellen + HMPC-Public-Summaries belegen; nicht geraten. **Primärquelle nicht erreichbar — Evidenzgrad ungeprüft, ärztliche Gegenprüfung nötig.**

**Prüfergebnis:** Beide bestehen `validate_monographie.py` einzeln und gemeinsam fehlerfrei (0 Fehler). Purpur-Sonnenhut: 1 Hinweis (bewusstes "unsicher/zu prüfen"). Knoblauch: `✓ alles sauber`. Keine Dubletten-Warnung. **0 Korrekturversuche.**

**Hauptquellen:**
- Purpur-Sonnenhut: EMA/HMPC EU herbal monograph Echinacea purpurea (L.) Moench, herba recens (well-established use, Presssaft) + radix (Abgrenzung); Kommission E; Cochrane Review Karsch-Völk et al. 2014 (CD000530); Literatur zur Parthenium-integrifolium-Verfälschung + BAPP-Bulletin 2025; Anaphylaxie-Fallbericht Mullins 1998.
- Knoblauch: EMA/HMPC EU herbal monograph Allium sativum L., bulbus (traditional use); Kommission E; ESCOP; **BfArM-Stufenplan Stufe II** (Knoblauch × HIV-Protease-Hemmer/Saquinavir); Review PMC9650110; Arzneipflanzen-Lexikon/PharmaWiki/AWL.

### Überraschungen / unsichere Stellen für den Arzt

- **Purpur-Sonnenhut — der reason 'Erwartung dämpfen' ist teils überholt: es gibt tatsächlich einen WEU.** ABER der well-established use gilt AUSSCHLIESSLICH für den PRESSSAFT aus dem frischen blühenden Kraut von *E. purpurea* (6–9 ml/Tag, max. 1 Woche, ab 12 J.). Tee, Tinktur, Wurzeldroge und die anderen Arten (*E. angustifolia*, *E. pallida*) sind nur traditional use. Ich habe die Erkältungsindikation daher `WEU` getaggt, aber im `comment`/`overstated` scharf auf die eine Zubereitung/Art eingegrenzt. **Bitte prüfen, ob der Katalog den WEU so präparate-spezifisch führen will** — sonst entsteht der Eindruck, jedes Echinacea-Produkt sei WEU.
- **Purpur-Sonnenhut — Erwartungsdämpfung bleibt inhaltlich richtig.** Der Cochrane-Review 2014 (24 Studien, >4600 TN) fand in den Einzelstudien keinen sicheren Placebo-Vorteil; Evidenz uneinheitlich, Effekt bestenfalls mild und nur bei frühem Beginn. In `evidence_caveat`/`overstated` dokumentiert.
- **Purpur-Sonnenhut — der Sicherheitskern ist Immunologie, nicht Toxikologie.** `asteraceae_allergy=true`: Korbblütlerallergie/Atopie → allergische Reaktionen bis Anaphylaxie (Fallberichte). Feste Gegenanzeige (HMPC/Kommission E) bei **progredienten Systemerkrankungen (TB, Sarkoidose, Leukosen), Autoimmun-/Kollagenosen (MS), HIV/AIDS und unter Immunsuppression** — die Immunstimulation gilt dort als nachteilig. Interaktion mit Immunsuppressiva als `pharmakodynamisch/relevant` eingetragen. Anwendung >8 Wochen: Leukopenierisiko. `high_safety` daher bewusst **false**.
- **Purpur-Sonnenhut — keine tödliche Verwechslung, aber `confusions` bewusst gefüllt.** Kein giftiger Doppelgänger (unverwechselbare Gartenstaude) → `deadly_confusion=false`. Reale Risiken sind (1) Art-/Pflanzenteil-Verwechslung mit *E. angustifolia*/*E. pallida* und der gleichnamigen Gattung *Rudbeckia* ('Sonnenhut', ungiftig, arzneilich ungleichwertig) und (2) die dokumentierte WURZEL-Verfälschung mit *Parthenium integrifolium* (Handelsware-Adulteration bis ~28 %). Plus expliziter 'keine lebensgefährliche Verwechslung'-Eintrag.
- **Knoblauch — nur TU trotz festem Herz-Kreislauf-Ruf.** HMPC: traditional use (Arteriosklerose-Vorbeugung; Erkältungssymptome). Kommission E + ESCOP positiv für Blutfette/Gefäßvorsorge → Gefäß-/Lipid-Indikation `TU/ESCOP+`, Erkältung `TU`. KEIN WEU. Effekt mild, in Metaanalysen uneinheitlich → in `overstated` ausdrücklich: kein 'natürliches Antibiotikum', kein Statin-Ersatz.
- **Knoblauch — zwei ernste Interaktionen (`interaction_heavy=true`).** (1) Dosisabhängige Thrombozytenaggregationshemmung → erhöhte Blutungsneigung mit Cumarinen/DOAK/ASS, **~7 Tage vor Operationen pausieren**. (2) **BfArM-Stufenplan Stufe II**: hoch dosierter Knoblauch senkt über CYP3A4/P-gp die Plasmaspiegel von **HIV-Protease-Hemmern (Saquinavir)** → Wirkverlust; nach Absetzen Therapiekontrolle bis ~14 Tage. Beide in `interactions`/`contraindications`/`key_warning`.
- **Knoblauch — `deadly_confusion=true` bewusst für den VERWANDTSCHAFTS-Kontext gesetzt (bitte kennen).** Die kultivierte Knoblauchzwiebel selbst hat KEINEN giftigen Doppelgänger (Geruch, Handelsware). Der reason nennt aber ausdrücklich 'Bärlauch-Verwandter'. Die klassische tödliche Verwechslung betrifft die Wildsammlung des verwandten Bärlauchs (*Allium ursinum*) mit **Maiglöckchen (*Convallaria*, Herzglykoside)** und **Herbstzeitloser (*Colchicum*, Colchicin)**, dazu Aronstab. Ich habe diese als `lebensgefährlich`/`giftig` eingetragen und deadly_confusion=true gesetzt, das Ganze aber mit einem expliziten 'keine Feld-Verwechslung der kultivierten Zwiebel'-Eintrag ehrlich abgegrenzt. **Falls das Register deadly_confusion nur für DIREKTE Doppelgänger der Arzneidroge vorsieht, bitte auf false korrigieren** — das ist eine bewusste Ermessensentscheidung analog zu Baldrian/Anis (Wildsammel-Kontext).
- **Knoblauch — Chemie/Zubereitung.** Allicin entsteht erst beim Zerkleinern (Alliin + Alliinase) und ist hitzeempfindlich → Kochen mindert es; sinnvoll sind rohe Zehe oder magensaftresistente Pulverdragees (Alliinase-Schutz). `harvest_organ` = "Zwiebel (Bulbus)". Taxonomie: heute Amaryllidaceae/Allioideae (früher Liliaceae → Alliaceae) — in `family`/`synonym_note` vermerkt.

### Nebenbefund (weiterhin offen, NICHT bearbeitet)

Der Sammel-Lauf `validate_monographie.py fertig/*.json` meldet unverändert die bekannten ~38 Altfehler in den früheren handkuratierten Monographien (baerlauch, beinwell, brennnessel, holunder, johanniskraut, kamille, pfefferminze, ringelblume, salbei, schafgarbe, wermut) — meist `toxicity_level`-Werte wie "essbar/gering", die das Schema nicht kennt. Auftragsgemäß (genau 2 Monographien, kuratierte Dateien gehören dem Arzt) NICHT angefasst. Empfehlung unverändert: eigener Bereinigungslauf. Beide neuen Dateien bestehen die Prüfung einzeln und gemeinsam fehlerfrei.

## Lauf 2026-07-17 — Huflattich, Gewöhnliche Pestwurz

**Auswahl / Quelle:** `docs/wunschliste.json` (5 Einträge) hat **0 offene** — alle fünf (potentilla-reptans, nepeta-nepetella, dittrichia-viscosa, cynodon-dactylon, hedera-canariensis) liegen bereits in `fertig/` (per id **und** Synonym-Dedup bestätigt: kriechendes-fingerkraut, kleine-katzenminze, klebriger-alant, hundszahngras, kanarischer-efeu). Daher beide Plätze aus `kraeuter-kandidaten.json`: die ersten beiden **offenen** Einträge nach tier aufsteigend — beide Tier 2, in Listenreihenfolge:
- **tussilago-farfara (Huflattich)** — Kandidat, Tier 2 → `fertig/monographie-huflattich.json`, Status `entwurf_fertig`
- **petasites-hybridus (Gewöhnliche Pestwurz)** — Kandidat, Tier 2 → `fertig/monographie-pestwurz.json`, Status `entwurf_fertig`

**Dedup:** Beide gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` geprüft — nicht vorhanden. Synonyme selbst eingetragen (Huflattich: Farfara radiata Gilib. u. a.; Pestwurz: Tussilago hybrida/petasites L., Petasites officinalis/vulgaris/ovatus). Keine Selbstheilung nötig. Keine Dubletten-Warnung des Skripts.

**Recherche-Kanal:** WebSearch funktionierte gut (Kommission E, HMPC-Public-Statement PA, StatPearls/NCBI, Neurology/AAN, Altmeyers, Arzneipflanzen-Lexikon). **WebFetch auf AWL.ch (Sekundärquelle) HTTP 403** — Inhalte stattdessen über WebSearch-Zusammenfassungen belegt. EMA/HMPC führt zu KEINER der beiden Arten eine Monographie (kein Primär-PDF nötig/vorhanden). **Primärregulatorik hier = Kommission E + BfArM-Stufenplan; ärztliche Gegenprüfung der Evidenzgrade wie immer nötig.**

**Prüfergebnis:** Beide bestehen `validate_monographie.py` einzeln und gemeinsam fehlerfrei — je `✓ alles sauber`, **0 Korrekturversuche**. Keine Dubletten.

**Hauptquellen:**
- Huflattich: Kommission E (Farfarae folium, positiv, mit PA-Warnung); HMPC Public Statement 2021 (ungesättigte PA); BfArM-Stufenplan (Grenzwert 1 µg PA/Tag, 4–6 Wochen/Jahr); Arzneipflanzen-Lexikon/AWL (PA-arme Zuchtsorte 'Wien').
- Pestwurz: Kommission E (Petasitidis rhizoma positiv / Blatt+Gesamtpflanze negativ); Lipton et al. Neurology 2004 (Petadolex-RCT Migräne); Schapowal BMJ 2002 (Ze 339, allergische Rhinitis); AAN/AHS-Leitlinie (Empfehlung 2015/16 zurückgezogen); BfArM (Petadolex-Marktrücknahme 07/2009); StatPearls Butterbur.

### Überraschungen / unsichere Stellen für den Arzt

- **Beide Kräuter sind PA-Träger und teilen den Sicherheitskern** (toxin_ceiling=true, toxin_type=Pyrrolizidinalkaloide, hepatotoxic=true, pregnancy_contraindicated=true, asteraceae_allergy=true). Grenzwert einheitlich 1 µg PA/Tag; native Wildpflanze/Tee bei beiden innerlich zu meiden. Das macht sie zum sauberen Auftakt des PA-Registers.
- **Huflattich — Evidenz bewusst TRAD, NICHT TU.** Kommission E führt Farfarae folium POSITIV (Husten/Katarrhe), aber es gibt WEDER HMPC- NOCH ESCOP-Monographie, und die Droge wurde wegen PA aus dem DAB gestrichen. Da 'TU' im Katalog HMPC-traditional-use meint, wäre TU faktisch falsch → TRAD gesetzt, Kommission E prominent im comment/source. **Bitte prüfen, ob der Katalog eine reine 'Kommission-E-positiv'-Konstellation lieber anders taggen will** — ein eigener Tag fehlt in der Skala.
- **Pestwurz — echte RCT-Evidenz, aber invertierte Leitlinienlage.** Migräneprophylaxe (Petadolex, −48 %) und allergische Rhinitis (Ze 339) sind RCT-belegt → evidence_tag RCT. ABER: gilt AUSSCHLIESSLICH für PA-freie Spezialextrakte; Petadolex ist in D seit Juli 2009 ohne Zulassung, und die AAN/AHS-Empfehlung wurde 2015/16 wegen Lebertoxizität ZURÜCKGEZOGEN — auch PA-freie Extrakte haben Leberschäden ausgelöst (Mechanismus ungeklärt). Ich habe RCT getaggt, im comment/overstated aber scharf auf 'nur Spezialextrakt, ungünstiges Nutzen-Risiko, Leberwertkontrolle' eingegrenzt. **Falls der Katalog für zurückgezogene Empfehlungen lieber abwertet (RCT→TRAD o. ä.), bitte hier ansetzen.**
- **Pestwurz — Kommission E ist geteilt:** positiv NUR für das Rhizom (krampfartige Harnwegsschmerzen), negativ für Blatt und Gesamtpflanze. Als eigene TRAD-Indikation abgebildet.
- **Taxonomie-Falle dokumentiert:** Pestwurz-Basionym ist *Tussilago petasites/hybrida* — sie war früher dieselbe Gattung wie der Huflattich. Das erklärt die reale, wechselseitige Blatt-Verwechslung (in beiden Dateien als confusions gegenseitig eingetragen). Kein tödlicher Doppelgänger bei beiden → deadly_confusion=false (jeweils mit explizitem 'keine lebensgefährliche Verwechslung'-Eintrag + Begründung).

### Nebenbefund (weiterhin offen, NICHT bearbeitet)

Der Sammel-Lauf `validate_monographie.py fertig/*.json` meldet unverändert die bekannten ~38 Altfehler in den früheren handkuratierten Monographien (baerlauch, beinwell, brennnessel, holunder, johanniskraut, kamille, pfefferminze, ringelblume, salbei, schafgarbe, wermut) — meist `toxicity_level`-Werte wie "essbar/gering", die das Schema nicht kennt. Auftragsgemäß (genau 2 Monographien; kuratierte Dateien gehören dem Arzt) NICHT angefasst. Empfehlung unverändert: eigener Bereinigungslauf. Beide neuen Dateien bestehen die Prüfung einzeln und gemeinsam fehlerfrei.

## Lauf 2026-07-17 — Borretsch, Schöllkraut

**Auswahl / Quelle:** `docs/wunschliste.json` (5 Einträge) hat weiterhin **0 offene** — alle fünf (potentilla-reptans, nepeta-nepetella, dittrichia-viscosa, cynodon-dactylon, hedera-canariensis) liegen per id- **und** Synonym-Dedup bereits in `fertig/`. Daher beide Plätze aus `kraeuter-kandidaten.json`: die ersten beiden **offenen** Einträge nach tier aufsteigend, in Listenreihenfolge — beide Tier 2:
- **borago-officinalis (Borretsch)** — Kandidat, Tier 2 → `fertig/monographie-borretsch.json`, Status `entwurf_fertig`
- **chelidonium-majus (Schöllkraut)** — Kandidat, Tier 2 → `fertig/monographie-schoellkraut.json`, Status `entwurf_fertig`

**Dedup:** Beide gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` geprüft (grep + Listenabgleich) — nicht vorhanden. Synonyme selbst eingetragen (Borretsch: Borago hortensis; Schöllkraut: keine gebräuchlichen Altnamen → leeres Array). Keine Selbstheilung nötig, keine Dubletten-Warnung.

**Recherche-Kanal:** WebSearch funktionierte gut (Kommission E, EMA/HMPC Public Statement, Cochrane, BfArM-Stufenplan, PubMed/NCBI-Hepatotoxizitäts-Reviews, BfR). **WebFetch scheiterte durchgängig mit HTTP 403** (AWL.ch, arzneipflanzenlexikon.info, de.wikipedia.org) — Inhalte daher über WebSearch-Zusammenfassungen belegt. Zu KEINER der beiden Arten existiert eine EMA/HMPC-*Monographie* (Schöllkraut nur Public Statement) — kein Primär-PDF verfügbar; **Evidenzgrade wie immer ärztlich gegenprüfen.**

**Prüfergebnis:** Beide bestehen `validate_monographie.py` — Borretsch `✓ alles sauber`, Schöllkraut `ok, mit Hinweisen` (nur der erwünschte „unsicher/zu prüfen"-Hinweis bei einer theoretischen Interaktion). **0 Korrekturversuche**, keine Dubletten.

**Hauptquellen:**
- Borretsch: Kommission E Negativmonographie Boraginis herba/flos (1991, PA + kein Wirknachweis); keine HMPC-/ESCOP-Monographie; Cochrane 2011 (GLA bei rheumatoider Arthritis, moderat); Cochrane/Übersichten (Borretschöl bei Neurodermitis überwiegend ohne Nutzen); BfR (PA-Verzehrempfehlung, Digitalis-Verwechslung).
- Schöllkraut: EMA/HMPC Public Statement (Nutzen-Risiko negativ, kein Monograph); BfArM-Stufenplan 2008 (Widerruf >2,5 mg Gesamtalkaloide/Tag); Kommission E (historisch positiv, Gallen-/Verdauungsbeschwerden); Hepatotoxizitäts-Reviews (HILI, cholestatische Hepatitis bis Leberversagen); CliniTox/Arzneipflanzen-Lexikon.

### Überraschungen / unsichere Stellen für den Arzt

- **Borretsch — die Heilpflanzen-Erwartung dreht sich um.** Das populäre „Borretschtee/‑blüten"-Bild ist regulatorisch NEGATIV (Kommission E 1991, PA-Leberrisiko). Der einzige evidenzbasierte Nutzen liegt im **PA-freien Samenöl** (GLA): RCT/Cochrane-Nutzen bei rheumatoider Arthritis (moderat, hohe Dosis, ab ~6 Monaten), bei Neurodermitis dagegen überwiegend **kein** Nutzen. Beide Samenöl-Indikationen mit `RCT` getaggt, aber im `realistic_expectation`/`overstated` scharf eingegrenzt. **Bitte prüfen, ob die getrennte Behandlung von PA-haltigem Kraut vs. PA-freiem Samenöl in der App klar genug ankommt** — die Sicherheitsaussage kippt komplett je nach Pflanzenteil.
- **Borretsch — Nebenbefund GLA senkt Krampfschwelle.** Ich habe `lowers_seizure_threshold=true` gesetzt und Epilepsie/epileptogene Kombination als Kontraindikation aufgenommen. Das ist eine oft übersehene, real dokumentierte Vorsicht bei GLA-Ölen (auch Nachtkerzenöl) — bitte gegenprüfen.
- **Borretsch — deadly_confusion=true (Roter Fingerhut).** Junge Rosette klassisch mit *Digitalis purpurea* verwechselbar (Todesfälle dokumentiert); Unterscheider = **Gurkengeruch** + borstige (statt weichfilziger) Behaarung. Zusätzlich zwei weitere PA-Träger als Verwechsler (Ochsenzunge, Beinwell) — kein sicherer Ersatz.
- **Schöllkraut — Lehrbuch vs. aktueller Stand klaffen auseinander.** Ältere Quellen führen die Kommission-E-Indikation (krampfartige Gallen-/Verdauungsbeschwerden, innerlich) noch positiv. **Überholt:** BfArM widerrief 2008 höher dosierte Zulassungen, HMPC bewertet Nutzen-Risiko **negativ** — Grund ist **idiosynkratische, dosisunabhängige** Hepatotoxizität (cholestatische Hepatitis bis Leberversagen). Beide Indikationen bewusst `TRAD`, innerliche Anwendung ausdrücklich nicht empfohlen; Grenzwert 2,5 mg Gesamtalkaloide/Tag im Text.
- **Schöllkraut — deadly_confusion=false, aber die Pflanze SELBST ist das Risiko.** Kein tödlicher Doppelgänger; Verwechsler sind Scharbockskraut (Namensverwechslung), Johanniskraut (Blüte) und vegetativ fiederblättrige Kräuter inkl. Schierling. **Entscheidendes, eindeutiges Erkennungsmerkmal: der orange-gelbe Milchsaft** beim Abbrechen (+ nur 4 Kronblätter). `toxin_ceiling`/`hepatotoxic`/`pregnancy_contraindicated` gesetzt; eine Interaktion bewusst als „unsicher — zu prüfen" markiert.

### Nebenbefund (weiterhin offen, NICHT bearbeitet)

Der Sammel-Lauf `validate_monographie.py fertig/*.json` meldet unverändert die bekannten Altfehler in den früheren handkuratierten Monographien (u. a. `toxicity_level`-Werte wie „essbar/gering", die das Schema nicht kennt). Auftragsgemäß (genau 2 Monographien; kuratierte Dateien gehören dem Arzt) NICHT angefasst. Empfehlung unverändert: eigener Bereinigungslauf. Beide neuen Dateien bestehen die Prüfung einzeln fehlerfrei.

---

## Lauf 2026-07-17 (Fortsetzung) — Kalmus, Rainfarn

**Auswahl / Quelle:** `docs/wunschliste.json` (5 Einträge) hat weiterhin **0 offene** — alle fünf (potentilla-reptans, nepeta-nepetella, dittrichia-viscosa, cynodon-dactylon, hedera-canariensis) liegen per id- **und** Synonym-Dedup bereits in `fertig/` (kriechendes-fingerkraut, kleine-katzenminze, klebriger-alant, hundszahngras, kanarischer-efeu). Daher beide Plätze aus `kraeuter-kandidaten.json`: die nächsten beiden **offenen** Einträge nach tier aufsteigend, Listenreihenfolge — beide Tier 2:
- **acorus-calamus (Kalmus)** — Kandidat, Tier 2 → `fertig/monographie-kalmus.json`, Status `entwurf_fertig`
- **tanacetum-vulgare (Rainfarn)** — Kandidat, Tier 2 → `fertig/monographie-rainfarn.json`, Status `entwurf_fertig`

**Dedup:** Beide gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` geprüft — nicht vorhanden. Synonyme selbst eingetragen (Kalmus: Calamus aromaticus, Acorus aromaticus, Acorus odoratus + synonym_note zum Familienwechsel Araceae→Acoraceae; Rainfarn: Chrysanthemum vulgare u.a. + synonym_note zur Abgrenzung von T. parthenium). Keine Selbstheilung nötig, keine Dubletten-Warnung.

**Recherche-Kanal:** WebSearch funktionierte gut. **WebFetch scheiterte durchgängig mit HTTP 403** (EMA-PDF, AWL.ch, de.wikipedia.org) — Inhalte daher über WebSearch-Zusammenfassungen belegt. Zu **beiden** Arten existiert **keine** EMA/HMPC- und **keine** ESCOP-Monographie; das EMA-Asaron-Dokument ist nur ein *Public Statement* (kein Primär-PDF abrufbar). **Evidenzgrade wie immer ärztlich gegenprüfen** — beide Indikationen daher bewusst `TRAD`, nicht `TU`.

**Prüfergebnis:** Beide bestehen `validate_monographie.py` einzeln — Rainfarn `✓ alles sauber`, Kalmus `ok, mit Hinweisen` (nur der erwünschte „unsicher/zu prüfen"-Hinweis im Kommission-E-Vermerk). **0 Korrekturversuche**, keine Dubletten.

**Hauptquellen:**
- Kalmus: EMA/HMPC Public Statement on herbal medicinal products containing asarone (β-Asaron genotoxisch/karzinogen, Expositionsgrenze ~115 µg/Tag); Uebel et al. 2021 (J Appl Toxicol) zu Cytotypen/β-Asaron-Gehalt; Kommission E (historisch, überholt); phytochemische Reviews (ätherisches Öl 1,5–5 %, Ploidie).
- Rainfarn: Kommission E Negativmonographie (Tanaceti herba/flos); Giftpflanzen-/Toxikologiequellen (Thujon-GABA-A-Antagonismus, Vergiftungsschwelle >1–3 g, Rainfarnöl nicht innerlich, Abortivum-Todesfälle); phytochemische Reviews zur Chemotyp-Variabilität des Öls.

### Überraschungen / unsichere Stellen für den Arzt

- **Kalmus — der „europäischer Kalmus ist asaronfrei"-Mythos ist falsch.** Asaronfrei ist nur der **nordamerikanische diploide** Typ. Der in Europa wilde/verwilderte Kalmus ist die **triploide** Sippe mit **5–19 % β-Asaron** im ätherischen Öl (indisch/tetraploid 70–96 %). β-Asaron ist genotoxisch + hepatokanzerogen, **kein ADI ableitbar**; EMA-Expositionsgrenze ~115 µg/Tag, Arzneibuch-Grenzwert ~0,5 %. Habe die Indikation auf `TRAD` gesetzt, `toxin_ceiling`/`pregnancy_contraindicated` gesetzt und im `overstated`/`key_warning` ausdrücklich vor der Asaronfrei-Annahme gewarnt. **Bitte den Kommission-E-Status gegenprüfen** — Sekundärquellen widersprechen sich (historisch positiv als Amarum vs. „keine anerkannte Monographie"); Primärquelle war nicht abrufbar, daher als „unsicher — zu prüfen" markiert.
- **Kalmus — europäische Sippe ist steril (triploid).** Blüht, setzt aber keine Samen an, Ausbreitung nur vegetativ über Rhizom. Für Bestimmung/Garten relevant (Vermehrung nur durch Teilung).
- **Kalmus — Verwechslung Iris pseudacorus.** Die Gelbe Schwertlilie heißt wörtlich „falscher Kalmus", wächst am selben Standort, ist **giftig** (nicht lebensgefährlich → `deadly_confusion=false`). Sicherer Unterscheider: **Kalmus riecht stark aromatisch**, Blattrand stellenweise **gewellt**, Mittelrippe **exzentrisch**; Iris geruchlos, flach, glattrandig.
- **Rainfarn — NICHT Mutterkraut.** Häufige und gefährliche Namens-/Gattungsverwechslung: *Tanacetum vulgare* (Rainfarn, toxisch, Thujon) ≠ *Tanacetum parthenium* (Mutterkraut, Migräneprophylaxe). Explizit in `synonym_note`, `overstated` und `key_warning` getrennt. Mutterkraut steht separat als eigener offener Kandidat (`tanacetum-parthenium`, Tier 2).
- **Rainfarn — dritter Thujon-Träger, aber der giftigste.** Öl chemotypabhängig bis ~70 % Thujon; wirksame ≈ toxische Dosis. Kommission-E-**Negativmonographie**, keine innerliche Selbstanwendung empfohlen; Indikationen bleiben (Nicht-Warneintrag, Tier 2) aber scharf als `TRAD`/obsolet eingegrenzt. `lowers_seizure_threshold` + `asteraceae_allergy` (Sesquiterpenlacton-Kontaktallergie) gesetzt.

### Nebenbefund (weiterhin offen, NICHT bearbeitet)

Der Sammel-Lauf `validate_monographie.py fertig/*.json` meldet unverändert die bekannten Altfehler in den früheren handkuratierten Monographien (u. a. `toxicity_level`-Werte wie „essbar/gering", die das Schema nicht kennt — z. B. in `monographie-wermut.json`). Auftragsgemäß (genau 2 Monographien; kuratierte Dateien gehören dem Arzt) NICHT angefasst. Beide neuen Dateien bestehen die Prüfung einzeln fehlerfrei.

## 2026-07-17 — Wilde Malve (WUNSCHLISTE + Kandidat), Rudbeckia/Sonnenhut (WUNSCHLISTE)

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` (Stand 2026-07-17) enthaelt 6 Eintraege; die ersten beiden offenen in Listenreihenfolge nach Dedup:
- **rudbeckia-fulgida** (Gewoehnlicher Sonnenhut / Wunsch-Trivialname "Black eyed Susan") — Quelle: Wunschliste (Platz 1) — `fertig/monographie-rudbeckia.json`
- **malva-sylvestris** (Wilde Malve / "Common mallow") — Quelle: Wunschliste (Platz 2), steht ZUGLEICH als Kandidat Tier 4 — `fertig/monographie-wilde-malve.json`

Die uebrigen Wunsch-Eintraege (achillea-nobilis, nepeta-cataria, malva-arborea, erigeron-strigosus) bleiben offen (max. 2/Lauf).

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` geprueft — keine Dublette. Wichtige Nicht-Treffer bewusst ausgeschlossen: `kleine-katzenminze` = nepeta-nepetella (NICHT nepeta-cataria); `klebriger-alant` = dittrichia-viscosa (fuehrt zwar Synonym "Erigeron viscosum", ist aber NICHT erigeron-strigosus); vorhandenes `achillea-millefolium` (Schafgarbe) ist NICHT achillea-nobilis. Altnamen eingetragen: Malva = M. ambigua/erecta/mauritiana/glabra; Rudbeckia = R. speciosa/newmanii.

**Kandidatenliste:** malva-sylvestris (Tier 4) von "offen" auf "entwurf_fertig" gesetzt + datei ergaenzt. rudbeckia-fulgida steht nicht in der Kandidatenliste (nur Wunsch) → dort nichts geaendert. Kein Self-Heal noetig (kein als "offen" markierter Kandidat lag bereits in `fertig/`). Wunschliste NICHT angefasst (App hakt selbst ab).

**Pruefergebnis:** beide einzeln UND gemeinsam `✓ ok, mit Hinweisen`, **0 Fehler beim ersten Versuch — 0 Korrekturversuche**. Einziger Hinweis je Datei: enthaelt bewusst "unsicher/zu pruefen".

**Hauptquellen:**
- Wilde Malve: EMA/HMPC EU herbal monograph Malva sylvestris L. und/oder Malva neglecta Wallr., folium; und Malva sylvestris L., flos (traditional use) + Assessment report; Kommission E (positiv). Chemie/Zubereitung/Verwechslung ueber phytodoc.de, awl.ch, pflanzenfreunde.com, PTA-Forum, kostbarenatur.net.
- Rudbeckia fulgida: POWO/Kew, World Flora Online, GBIF, USDA (akzeptierter Name); Wikipedia (en) fuer Trivialnamen/Cherokee-Ethnobotanik; plantids.com, hortica.de (essbar/giftig). Gezielte Recherche EMA/HMPC + ESCOP + Kommission E: KEINE Monographie vorhanden.
- **Quellen-Abruf:** WebFetch der EMA-Primaer-PDF (Malva-Monograph) und der vetpharm-Giftdatenbank (Rudbeckia) lieferte wie in allen Vorlaeufen **HTTP 403**. Inhalte daher ueber WebSearch-Zusammenfassungen mehrerer uebereinstimmender Sekundaerquellen verifiziert. Fuer Malva ist die HMPC-Einstufung (traditional use, nicht WEU) mehrfach bestaetigt und belastbar; **die exakte TU-Wortlaut/Posologie sollte bei der Sichtung gegen das Original geprueft werden.**

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Rudbeckia fulgida hat KEINEN belegten Heilwert** — anders als der Katalog-Nachbar Echinacea (Purpursonnenhut). Keine europaeische Monographie; nur nordamerikanische Ethnomedizin. Alle Indikationen TRAD, defensiv formuliert. Das ist kein Rechercheversaeumnis, sondern der reale Befund. Ich habe genau EINE (aeussere) TRAD-Indikation aufgenommen und die ueberlieferten INNEREN Anwendungen (Tee gegen Nieren-/Frauenleiden) bewusst NICHT als Indikation gelistet, sondern in `overstated` als unbelegt und wegen unklarer Sicherheit nicht empfohlen markiert. Bitte bestaetigen, ob diese Zurueckhaltung so gewuenscht ist.
- **Rudbeckia — zwei Namensfallen.** (1) Der Wunschlisten-Trivialname **"Black eyed Susan" gehoert eigentlich zu Rudbeckia hirta**, nicht zu R. fulgida — bitte den Pl@ntNet-Treffer gegenpruefen, der zu diesem Wunsch-Eintrag fuehrte. (2) **"Sonnenhut" = sowohl Rudbeckia (gelb) als auch Echinacea (purpur)**; die begrenzte Erkaeltungs-/Immun-Evidenz gehoert AUSSCHLIESSLICH zu Echinacea. Prominente Abgrenzung in `confusions`, `key_warning`, `overstated`, `synonym_note`. `asteraceae_allergy=true`, `high_safety=false` (Sicherheitsdaten fehlen weitgehend).
- **Wilde Malve — Evidenz nicht schoenen:** trotz festem Ruf als Hustentee nur `TU` (HMPC traditional use + Kommission E), keine RCT. Zwilling zum bereits vorhandenen Eibisch (gleiche Schleim-Wirkklasse, gleiche Kaltauszug-Regel).
- **Wilde Malve — Zubereitung ist der kritische Punkt, nicht Toxizitaet:** Schleimstoffe hitzeempfindlich → Kaltauszug, nicht kochen; alkoholische Tinktur ungeeignet. `high_safety=true` gesetzt (kein Toxin, kein giftiger Doppelgaenger), obwohl eine geringe Resorptionsinteraktion (Schleimfilm, 30-60 min Abstand) besteht — konsistent mit der Eibisch-Monographie. Bitte gegenpruefen, ob das Register das so abbilden soll.
- **Wilde Malve — keine giftige Verwechslung:** aktiv geprueft, alle aehnlichen Malvengewaechse (Rosen-Malve, Weg-Malve, Stockrose) sind essbar. `confusions` bewusst gefuellt inkl. explizitem "keine relevante Verwechslung bekannt (giftig)"-Eintrag statt leerem Array. Stockrose (Alcea rosea) ist als Drogen-Verfaelschung der Malvenblueten pharmazeutisch relevant, aber ungefaehrlich.
- **Datei-/Namenskonvention Rudbeckia:** bewusst `monographie-rudbeckia.json` statt `...-sonnenhut.json`, weil "Sonnenhut" im Katalog mit Echinacea (purpursonnenhut) kollidiert. id = `rudbeckia-fulgida` (akzeptierter Name Aiton).

## 2026-07-18 — Echte Katzenminze (WUNSCHLISTE), Edle Schafgarbe (WUNSCHLISTE)

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` (Stand 2026-07-17) enthaelt weiterhin 6 Eintraege. Die ersten beiden (rudbeckia-fulgida, malva-sylvestris) liegen bereits aus dem Vorlauf (2026-07-17) in `fertig/` → als erfuellt uebersprungen. Die naechsten beiden offenen Wunsch-Eintraege in Listenreihenfolge:
- **nepeta-cataria** (Echte Katzenminze / Wunsch-Trivialname "Catnip") — Quelle: Wunschliste (Platz 4) — `fertig/monographie-echte-katzenminze.json`
- **achillea-nobilis** (Edle Schafgarbe / "Noble yarrow") — Quelle: Wunschliste (Platz 3) — `fertig/monographie-edle-schafgarbe.json`

Reihenfolge im Log nach Datei; Auswahl folgte der Wunschlisten-Reihenfolge (achillea-nobilis Platz 3, nepeta-cataria Platz 4). Die uebrigen Wunsch-Eintraege (malva-arborea, erigeron-strigosus) bleiben offen (max. 2/Lauf).

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` geprueft — keine Dublette. Bewusste Nicht-Treffer: vorhandenes `achillea-millefolium` (Schafgarbe) ist NICHT achillea-nobilis (eigene Art); vorhandenes `nepeta-nepetella` (kleine-katzenminze) ist NICHT nepeta-cataria (eigene Art) — die bestehende nepetella-Monographie verweist selbst ausdruecklich auf N. cataria als die "eigentlich genutzte" Art, die hier jetzt ergaenzt wird. Altnamen eingetragen: Nepeta cataria = Cataria vulgaris / Glechoma cataria / Nepeta vulgaris / Calamintha albiflora; Achillea nobilis = keine relevanten Homotyp-Synonyme (Taxonomie stabil) → leeres Array, im synonym_note begruendet.

**Kandidatenliste:** Weder nepeta-cataria noch achillea-nobilis steht in `kraeuter-kandidaten.json` (beide reine Wunschkraeuter) → dort NICHTS geaendert. Kein Self-Heal noetig. Wunschliste NICHT angefasst (App hakt selbst ab).

**Pruefergebnis:** beide `✓ ok, mit Hinweisen`, **0 Fehler beim ersten Versuch — 0 Korrekturversuche**. Einziger Hinweis je Datei: enthaelt bewusst "unsicher/zu pruefen".

**Hauptquellen:**
- Echte Katzenminze: KEINE HMPC-/ESCOP-/Kommission-E-Monographie (mehrfach bestaetigt). Traditionelle Anwendung/Chemie/Dosierung ueber AWL.ch, Hagers Handbuch, hausmittelcheck.de, pflanzenfreunde.com, naturadb.de. Akzeptierter Name + Synonyme ueber POWO/Kew, GBIF, Wikipedia (en Catnip).
- Edle Schafgarbe: KEINE Monographie fuer A. nobilis; HMPC existiert NUR fuer A. millefolium (nicht uebertragbar). Merkmale/Chemie/Phototoxizitaet/Verwechslung ueber Wikipedia (de), pflanzen-deutschland.de, naturadb.de, smagy.de; Verbreitung/Rote Liste ueber FloraWeb.
- **Quellen-Abruf:** WebFetch der Primaerseiten (Wikipedia, AWL.ch) lieferte wie in allen Vorlaeufen **HTTP 403**. Inhalte daher ueber WebSearch-Zusammenfassungen mehrerer uebereinstimmender Sekundaerquellen verifiziert. Da fuer BEIDE Arten ohnehin KEINE regulatorische Primaermonographie existiert, ist der Evidenzgrad (durchgehend TRAD) belastbar — es gibt schlicht keine WEU/TU-Einstufung zu verpassen.

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Edle Schafgarbe — die sicherheitskritischste Stelle ist die Doldenbluetler-Verwechslung.** Die Blaetter von A. nobilis sind noch feiner zerschlitzt als bei der Gewoehnlichen Schafgarbe; junge, nicht bluehende Rosetten aehneln jungen Doldenbluetlern. Mehrere Quellen nennen ausdruecklich die Verwechslungsgefahr mit giftigen Doldenbluetlern beim Sammeln junger Blaetter fuer Wildsalate. Ich habe daher **`deadly_confusion=true`** gesetzt (Gefleckter Schierling/Conium maculatum = lebensgefaehrlich; Hundspetersilie/Aethusa cynapium = giftig) und dies prominent in `key_warning`, `collection_rules` und `kitchen` gefuehrt. **Bitte gegenpruefen, ob diese scharfe Einstufung fuer eine Korbbluetler-Art im Register erwuenscht ist** — botanisch ist die Verwechslung real (feinfiedriges Laub), auch wenn Schafgarbe kein Doldenbluetler ist.
- **Edle Schafgarbe — Frischsaft ist phototoxisch.** Mehrfach beschrieben ("der frisch gepresste Saft kann bei Licht Hautentzuendungen ausloesen"). `photosensitizing=true` gesetzt und bei der aeusseren Anwendung ausdruecklich Sonnenlicht-Meidung vermerkt.
- **Edle Schafgarbe — NICHT gleich Gewoehnliche Schafgarbe.** Kernaussage der Monographie: "edel" meint die Erscheinung, nicht hoeheren Heilwert. A. nobilis ist oft azulen-/proazulenarm und hat KEINE eigene HMPC-Monographie. Die belegte Schafgarben-Evidenz gehoert zu A. millefolium. `pregnancy_contraindicated=true` (Thujon + emmenagoge Gattungstradition) und `asteraceae_allergy=true` defensiv gesetzt; toxin_ceiling bewusst NICHT gesetzt (kein art-spezifischer Grenzwert belegbar), Thujon aber im Sicherheitstext benannt.
- **Edle Schafgarbe — Naturschutz:** in Deutschland zerstreut/selten, Rote Liste Vorwarnliste. Sammelethik im Log/Feld vermerkt (Wildbestaende schonen, Gartenpflanze bevorzugen).
- **Echte Katzenminze — schliesst die Luecke zur bereits vorhandenen Kleinen Katzenminze.** Der nepetella-Eintrag verwies selbst darauf, dass N. cataria die "eigentlich (schwach) genutzte" Art ist — die liegt jetzt vor. Trotz festem volksmedizinischem Ruf: KEINE regulatorische Monographie, daher alle Indikationen bewusst **TRAD** (nicht TU), Wirkung nur mild/unspezifisch.
- **Echte Katzenminze — zwei Sicherheitspunkte, die ueber ein harmloses Teekraut hinausgehen:** (1) Schwangerschaft — wehen-/menstruationsfoerdernd ueberliefert, `pregnancy_contraindicated=true`; (2) Saeuglinge/Kleinkinder — berichtete Sedations-/Vergiftungserscheinungen, als Kontraindikation gefuehrt. Deshalb bewusst **kein `high_safety=true`**. Kein giftiger Doppelgaenger (Lamiaceae), confusions dennoch aktiv gefuellt.

## 2026-07-18 (Lauf 2) — Baummalve (WUNSCHLISTE), Borstiges Berufkraut (WUNSCHLISTE)

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` (Stand 2026-07-17) enthaelt 6 Eintraege. Die ersten vier (rudbeckia-fulgida, malva-sylvestris, achillea-nobilis, nepeta-cataria) liegen aus den Vorlaeufen bereits in `fertig/` → als erfuellt uebersprungen. Die letzten beiden offenen Wunsch-Eintraege in Listenreihenfolge:
- **malva-arborea** (Baummalve / "Tree mallow", Wunsch-Platz 5) — Quelle: Wunschliste — `fertig/monographie-baummalve.json`
- **erigeron-strigosus** (Borstiges Berufkraut / "Common eastern fleabane", Wunsch-Platz 6) — Quelle: Wunschliste — `fertig/monographie-borstiges-berufkraut.json`

Damit ist die Wunschliste nach diesem Lauf vollstaendig abgearbeitet (Abhaken macht die App).

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` geprueft — keine Dublette. Bewusste Nicht-Treffer: das vorhandene `malva-sylvestris` (wilde-malve) ist NICHT malva-arborea (eigene Art, andere Gattungssektion); der einzige "Erigeron"-Fund in `fertig/` (`Erigeron viscosum L.` als Synonym von `dittrichia-viscosa`/klebriger-alant) ist eine ANDERE Art, nicht E. strigosus. Skript-Dublettencheck ueber alle `fertig/*.json`: keine Dubletten. Altnamen eingetragen: Malva arborea = Lavatera arborea / Malva eriocalyx; Erigeron strigosus = E. annuus subsp./var. strigosus / E. ramosus / Stenactis strigosa.

**Kandidatenliste:** Weder malva-arborea noch erigeron-strigosus steht in `kraeuter-kandidaten.json` (beide reine Wunschkraeuter, 87 Kandidaten geprueft) → dort NICHTS geaendert. Kein Self-Heal noetig (kein "offen"-Kandidat hat bereits eine Datei in `fertig/`). Wunschliste NICHT angefasst (App hakt selbst ab).

**Pruefergebnis:** beide `✓ ok, mit Hinweisen`, **0 Fehler beim ersten Versuch — 0 Korrekturversuche**. Einziger Hinweis je Datei: enthaelt bewusst "unsicher/zu pruefen".

**Hauptquellen:**
- Baummalve: Taxonomie (akzeptierter Name Malva arborea, Synonym Lavatera arborea) ueber POWO/Kew, GBIF, FNA. Morphologie/Frosthaerte ueber RHS, NC State Extension, first-nature.com. Schleimchemie/Zubereitung in Analogie zur HMPC-Droge Malva sylvestris (folium/flos). Nitrat-Hinweis Malva parviflora ueber gartenjournal.net.
- Borstiges Berufkraut: akzeptierter Name + Pl@ntNet-Trivialname "Borstiges Berufkraut" ueber Pl@ntNet (App-Abgleich!), Abgrenzung zu E. annuus ueber Go Botany/Minnesota Wildflowers/bplant.org. Historische Verwendung ueber Eclectic School of Herbal Medicine (Fleabane Monograph). Greiskraut-Toxizitaet ueber allum.de / AK Kreuzkraut e.V.
- **Quellen-Abruf:** WebFetch der Primaerseiten (Wikipedia, POWO, Pl@ntNet, gardify, tropengarten) lieferte wie in allen Vorlaeufen durchgehend **HTTP 403** (bzw. DNS-Fehler bei offene-naturfuehrer.de). Inhalte daher ueber WebSearch-Zusammenfassungen mehrerer uebereinstimmender Sekundaerquellen verifiziert. Fuer BEIDE Arten existiert ohnehin KEINE regulatorische Primaermonographie (HMPC/ESCOP/Kommission E) — der Evidenzgrad (durchgehend TRAD) ist damit belastbar: es gibt keine WEU/TU-Einstufung zu verpassen.

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Baummalve ist NICHT die Arznei-Malve — Kernbotschaft.** Die HMPC-/Kommission-E-Belege gelten fuer Malva sylvestris/neglecta, NICHT fuer Malva arborea. Ich habe die reizmildernde Anwendung deshalb bewusst nur als **TRAD** (Analogieschluss), NICHT als TU gefuehrt und dies in `evidence_caveat`, `comment`, `expectation_summary.overstated` und `key_warning` klargestellt. Bitte pruefen, ob der Katalog fuer diese Zier-Strauchmalve ueberhaupt eine Anwendungs-Empfehlung tragen soll oder ob der Verweis auf die Wilde Malve genuegt.
- **Baummalve — "Malve = harmlos" gilt NICHT pauschal fuer die Gattung.** Als giftige Gegen-Referenz habe ich Malva parviflora (Kleinbluetige Malve) in `confusions` als `giftig` gefuehrt: sie reichert Nitrat/Nitrit an und ist als Weidetier-Gift ("Malva-Staggers") bekannt. Fuer den Menschen bei ueblichem Verzehr nicht akut giftig, aber ein bewusster Warnhinweis gegen pauschale Entwarnung. `high_safety=true` fuer M. arborea selbst blieb gesetzt (ungiftig, kein toedlicher Doppelgaenger).
- **Baummalve — Gartenrealitaet Bodensee:** frostempfindlich (nur bis ca. -10/-12 C, von starkem Frost getoetet), am Bodensee nicht sicher winterhart. `bodensee_suitability` ehrlich als "nur bedingt geeignet" formuliert. `region_occurrence`-Status: `nur-kultur-selten-verwildert`.
- **Borstiges Berufkraut — KEIN belegtes Heilkraut.** Weder HMPC noch ESCOP noch Kommission E; die einzigen Anwendungen stammen aus der nordamerikanischen Volks-/Eklektikmedizin des 19. Jh. (adstringierend/diuretisch/styptisch). Ich habe daher **bewusst KEINE Zubereitungs-/Dosierempfehlung** gegeben, die Indikation ausdruecklich als "NICHT belegt" markiert und von Selbstanwendung abgeraten. Evidenz durchgehend **TRAD**. `high_safety` bewusst NICHT gesetzt.
- **Borstiges Berufkraut — sicherheitskritische Verwechslung mit Greiskraut.** Im Rosetten-/Jungstadium bzw. bei fluechtiger Ansprache als "Wiesen-Korbbluetler" ist die Verwechslung mit gelbbluehenden Greiskraeutern (Senecio/Jacobaea, **lebertoxische Pyrrolizidinalkaloide**) moeglich. Als `giftig` in `confusions` gefuehrt (Toxin benannt) mit Feld-Unterscheidung (weisse vs. gelbe Strahlen). **deadly_confusion=false** bewusst gewaehlt: Senecio-Toxizitaet ist chronisch-kumulativ/lebertoxisch, kein akut-toedlicher Verzehr eines einzelnen Blattes — bitte gegenpruefen, ob die Registerlogik diese Einordnung so tragen soll. `asteraceae_allergy=true`.
- **Borstiges Berufkraut — Taxonomie strittig:** wird teils als eigene Art, teils als Unterart von Erigeron annuus gefuehrt; in Mitteleuropa selten und schwer von E. annuus zu trennen (Behaarungsrichtung anliegend vs. abstehend als Hauptmerkmal). id = `erigeron-strigosus` gemaess akzeptiertem Namen und Pl@ntNet-Abgleich. Als ausbreitungsfreudiger Neophyt im Garten nicht empfohlen.

## 2026-07-18 (Lauf 3) — Beifuß (KANDIDAT), Waldmeister (KANDIDAT)

**Auswahl (genau 2):** Wunschliste hat Vorrang, ist aber **vollständig abgearbeitet** — alle 6 Einträge aus `docs/wunschliste.json` (rudbeckia-fulgida, malva-sylvestris, achillea-nobilis, nepeta-cataria, malva-arborea, erigeron-strigosus) liegen bereits in `fertig/` (id + Synonym geprüft) → 0 offene Wünsche → beide Kräuter aus der Kandidatenliste. Niedrigste offene tier = 2, in Listenreihenfolge:
- **artemisia-vulgaris** (Gewöhnlicher Beifuß) — Quelle: Kandidatenliste tier 2 — `fertig/monographie-beifuss.json`
- **galium-odoratum** (Waldmeister) — Quelle: Kandidatenliste tier 2 — `fertig/monographie-waldmeister.json`

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` geprüft — keine Dublette. Bewusste Nicht-Treffer: `artemisia-absinthium` (Wermut) ist eine andere Art als artemisia-vulgaris; das alte `Asperula odorata` (Synonym für Waldmeister) ist in `fertig/` noch nicht vergeben. Skript-Dublettencheck über alle `fertig/*.json`: keine Dubletten. Altnamen eingetragen: Artemisia vulgaris → Artemisia officinalis / A. samamisica; Galium odoratum → Asperula odorata / A. matrisylva.

**Status/Changelog:** beide Kandidaten in `kraeuter-kandidaten.json` auf `entwurf_fertig` + `datei` gesetzt (NICHT geprueft — das macht der Arzt). Je ein Changelog-Eintrag (`art: neu`) angehängt. Kein Self-Heal nötig. Wunschliste nicht angefasst (App hakt selbst ab).

**Prüfergebnis:** beide bestehen `validate_monographie.py` — Beifuß `ok, mit Hinweisen` (nur der gute "unsicher/zu prüfen"-Hinweis), Waldmeister `✓ alles sauber`. **0 Fehler beim ersten Versuch — 0 Korrekturversuche.**
- Hinweis Randbeobachtung (NICHT durch diesen Lauf verursacht): `validate_monographie.py fertig/*.json` meldet 38 Fehler in **vorbestehenden, meist kuratierten** Dateien (baerlauch, beinwell, brennnessel, holunder, johanniskraut, kamille, pfefferminze, ringelblume, salbei, schafgarbe, wermut) — v. a. `lebensgefaehrlich` ohne Umlaut, fehlende `note`, `None`-Felder, ungültige `interactions.type`. Diese `herkunft: kuratiert`-Dateien wurden NICHT angefasst (CLAUDE.md: kuratiert nie ändern). Der Arzt sollte entscheiden, ob die 15 handkuratierten Monographien an das aktuelle Schema angepasst werden.

**Hauptquellen:**
- Beifuß: Kommission-E-Status (Negativmonographie) über Wikipedia/PhytoDoc/gesundheit.de; Allergie (Art v 1, Sellerie-Karotten-Beifuß-Gewürz-Syndrom) über Allum, alles-zur-allergologie.de, chirurgie-portal.de; Thujon/Chemie über AWL.ch/Übersichtsarbeiten (PMC7583039); Schwangerschafts-Kontraindikation über mehrere konkordante Quellen.
- Waldmeister: Kommission-E-Negativmonographie + Cumaringehalt (~1 % TM) über Arzneipflanzengarten Uni Kiel, AWL.ch, DocCheck, Wikipedia; Cumarin-Grenzwerte/BfR-Orientierung + Bowle-Menge (max ~3 g/L) über gesundheit.de/mundraub; Verwechslungen (Galium mollugo/aparine/verum, Maiglöckchen) über gruenundgesund, delectation, wildkrautbraut.
- **Quellen-Abruf:** WebFetch der Primär-/Sekundärseiten lieferte wie in allen Vorläufen durchgehend **HTTP 403**. Inhalte daher über WebSearch-Zusammenfassungen mehrerer konkordanter Quellen verifiziert. Für BEIDE Arten existiert ohnehin KEINE regulatorische Positiv-Monographie (HMPC/ESCOP) und nur eine NEGATIVE Kommission-E-Monographie — der Evidenzgrad (durchgehend TRAD) ist damit belastbar; es gibt kein WEU/TU zu verpassen. Trotzdem: ärztliche Gegenprüfung der Sicherheitsfelder empfohlen.

### Überraschungen / unsichere Stellen für den Arzt

- **Beifuß — Thujon-Grenzwert bewusst offen gelassen.** Ich habe `toxin_ceiling=false` gesetzt, weil es für Beifuß speziell keinen mir belegbaren arzneilichen Thujon-Grenzwert / keine "maximale Anwendungsdauer" gibt (anders als bei Wermut/Spirituosen). In `tox_ceiling` und `preparation.standard_dose` steht dazu ausdrücklich "unsicher — zu prüfen". Bitte prüfen, ob der Katalog für konzentrierte Beifuß-Tees/Tinkturen eine Thujon-Obergrenze führen soll.
- **Beifuß — der eigentliche Nutzen ist die Küche, nicht die Heilkunde.** Kommission E NEGATIV; alle Indikationen TRAD. Die traditionelle "Frauenkraut"-Indikation habe ich bewusst mit der Warnung verknüpft, dass genau dieser wehen-/menstruationsfördernde Ruf die Anwendung in der Schwangerschaft gefährlich macht — `pregnancy_contraindicated=true`, `asteraceae_allergy=true`, `lowers_seizure_threshold=true` (Thujon). Kein `high_safety`.
- **Beifuß — Ambrosie-Verwechslung als Allergie-, nicht Vergiftungsproblem.** Die Beifuß-Ambrosie (Ambrosia artemisiifolia) ist bei Verzehr nicht giftig (`toxicity_level: essbar`), aber ein extrem potentes Pollenallergen und invasiver Neophyt. In `confusions` mit dem Unterscheidungsmerkmal geführt (Beifuß unterseits weißfilzig, Ambrosie beidseits grün). Bitte prüfen, ob "essbar" für ein Nicht-Speisegut in der App-Logik missverständlich wirkt.
- **Waldmeister — Maiglöckchen als deadly_confusion: bewusst defensiv gesetzt.** Botanisch sind die beiden gut trennbar (6–9 schmale Blätter im Quirl vs. 2 breite, parallelnervige Blätter; Heugeruch nur bei Waldmeister). Da beide aber den schattigen Frühjahrs-Waldboden teilen und mehrere Sammelführer explizit warnen, habe ich `deadly_confusion=true` gewählt und das Trennmerkmal klar benannt. Bitte gegenprüfen, ob die Registerlogik diese (eher konservative) Einordnung so tragen soll.
- **Waldmeister — Cumarin-Doppeldeutigkeit klargestellt.** Als eigene Interaktion (Typ `theoretisch`) aufgenommen: das natürliche Cumarin des Waldmeisters ist NICHT das gerinnungshemmende Cumarin-Arzneimittel (Warfarin/Phenprocoumon). Dieser verbreitete Irrtum führt sonst zu falschen Interaktionswarnungen. `hepatotoxic` bewusst `false` (nur Hochdosis-Risiko, im Text beschrieben), aber `toxin_ceiling=true` / `toxin_type=Cumarin` für das Register.
- **Waldmeister — paradoxe Kopfschmerz-Indikation.** Volksmedizinisch gegen Kopfschmerz genutzt, obwohl Cumarin selbst Kopfschmerz auslöst. Als TRAD geführt und ausdrücklich davon abgeraten.

## 2026-07-18 (Lauf 4) — Traubensilberkerze (KANDIDAT), Echte Engelwurz (KANDIDAT)

**Auswahl (genau 2):** Wunschliste hat Vorrang, ist aber weiterhin **vollständig abgearbeitet** — alle 6 Einträge aus `docs/wunschliste.json` (rudbeckia-fulgida, malva-sylvestris, achillea-nobilis, nepeta-cataria, malva-arborea, erigeron-strigosus) liegen bereits in `fertig/` (per id-Grep bestätigt) → 0 offene Wünsche → beide Kräuter aus der Kandidatenliste. Niedrigste offene tier = 2, in Listenreihenfolge die nächsten beiden nach den in Lauf 3 erledigten (Beifuß/Waldmeister):
- **actaea-racemosa** (Traubensilberkerze) — Quelle: Kandidatenliste tier 2 — `fertig/monographie-traubensilberkerze.json`
- **angelica-archangelica** (Echte Engelwurz) — Quelle: Kandidatenliste tier 2 — `fertig/monographie-engelwurz.json`

**Dedup:** gegen alle `id`/`synonyms` in `fertig/` und `vorhanden` geprüft — keine Dublette (beide Dateien neu). Altnamen eingetragen: Actaea racemosa → Cimicifuga racemosa / Macrotys actaeoides / Actaea monogyna; Angelica archangelica → Angelica officinalis / Archangelica officinalis. Skript-Dublettencheck sauber.

**Status/Changelog:** beide Kandidaten in `kraeuter-kandidaten.json` auf `entwurf_fertig` + `datei` gesetzt (NICHT `geprueft` — das macht der Arzt). Je ein Changelog-Eintrag (`art: neu`) angehängt. Kein Self-Heal nötig. Wunschliste nicht angefasst.

**Prüfergebnis:** beide bestehen `validate_monographie.py` — je `ok, mit Hinweisen` (nur der gute "unsicher/zu prüfen"-Hinweis). **0 Fehler beim ersten Versuch — 0 Korrekturversuche.**

**Hauptquellen:**
- Traubensilberkerze: HMPC EU herbal monograph Cimicifugae racemosae rhizoma (well-established use) + Assessment Report/Hepatotoxizitätsbewertung; ESCOP; Kommission E; Onkopedia-Leitlinie (Stand 10/2021) zu Tamoxifen/CYP; Arzneipflanzenlexikon/Altmeyers.
- Echte Engelwurz: Kommission E (positiv, Angelicae radix) + ESCOP-Monographie; EMA/HMPC = KEINE Monographie zu A. archangelica; Ph. Eur. (Qualität); Wikipedia/Arzneipflanzenlexikon (Furanocumarine/Phototoxizität); Wildkräuter-/Bestimmungsportale zu den Schierlings-Verwechslungen.
- **Quellen-Abruf:** WebFetch der EMA-Primär-PDF lieferte wie in allen Vorläufen **HTTP 403**. Inhalte daher über mehrere konkordante WebSearch-Sekundärquellen verifiziert. Für die entscheidenden Evidenzgrade konnte der regulatorische Status aber eindeutig belegt werden (siehe unten) — kein Rateschluss.

### Überraschungen / unsichere Stellen für den Arzt

- **Traubensilberkerze — echter WEU-Fall, aber extraktgebunden.** Anders als die meisten bisher gebauten Kandidaten hat diese Art HMPC-**well-established-use**-Status (Hitzewallungen/Schwitzen). ACHTUNG: der WEU gilt nur für definierte standardisierte (isopropanolische/ethanolische) Extrakte, NICHT für Wurzeltee/beliebige Präparate. Ich habe die Hauptindikation `WEU` getaggt und die Extraktbindung in `comment`, `evidence_caveat`, `expectation_summary.overstated` und `preparation.form_rationale` mehrfach klargestellt. Bitte gegenprüfen, ob die Katalog-/Registerlogik diese Extrakt-Einschränkung transportiert.
- **Traubensilberkerze — Tamoxifen-Interaktions-Mythos bewusst korrigiert.** Verbreitet ist die Warnung, Cimicifuga störe Tamoxifen über CYP2D6/3A4. Die klinische Datenlage zeigt das NICHT (keine relevante CYP-Hemmung, Onkopedia). Ich habe die Interaktion daher als `theoretisch`/`gering` mit ausdrücklicher Entwarnung geführt statt als Kontraindikation — bitte prüfen, ob das mit der Hausmeinung übereinstimmt. Östrogen-Kombination bleibt (Kommission E) abgeraten.
- **Traubensilberkerze — Leberschäden als eigentliches Sicherheitsthema.** `hepatotoxic=true` gesetzt (seltene idiosynkratische Leberschädigung, EMA-Warnhinweis), obwohl Kausalität in mehreren Fallauswertungen als unwahrscheinlich/nicht sicher zuordenbar gilt. Bewusst defensiv. `toxin_ceiling=false` (kein dosisdefiniertes Toxin). `high_safety` NICHT gesetzt.
- **Traubensilberkerze — Namensfalle in der Gattung.** Das heimische, giftige Christophskraut (Actaea spicata) trägt denselben Gattungsnamen und wird teils ähnlich benannt; ebenso die roten Actaea rubra und die Zier-Silberkerzen (Actaea simplex). Als `giftig` in `confusions` geführt (kein akut tödlicher Doppelgänger → `deadly_confusion=false`), Hauptrisiko ist Fehl-/Substitution, nicht akute Vergiftung. Bitte prüfen, ob "giftig" für die Zier-Silberkerzen (eher Substitutionsproblem) in der App passend wirkt.
- **Echte Engelwurz — KEIN HMPC-Status, bewusst NICHT als TU getaggt.** Häufiges Missverständnis: viele Quellen sprechen von "traditioneller Anwendung". TU ist aber ein HMPC-Registrierungsgrad — und Angelica archangelica hat KEINE HMPC-Monographie (im Gegensatz zu Angelica sinensis). Ich habe die Verdauungsindikation daher `ESCOP+` getaggt (Kommission E positiv + ESCOP-Monographie), Bronchitis nur `TRAD`. Bitte prüfen, ob der Katalog diese Abgrenzung (ESCOP+ statt TU) so tragen soll.
- **Echte Engelwurz — lebensgefährliche Doldenblütler-Doppelgänger.** `deadly_confusion=true` (Wasserschierling Cicuta virosa/Cicutoxin, Gefleckter Schierling Conium maculatum/Coniin), zusätzlich Riesen-Bärenklau und Hundspetersilie. Der süßliche Likörruf (Angelika im Magenbitter) verharmlost die Pflanze — der sicherste Bestimmungsanker ist der kräftig süßlich-aromatische Geruch der ganzen Pflanze. `key_warning` entsprechend scharf.
- **Echte Engelwurz — Phototoxizität + Schwangerschaft.** `photosensitizing=true` (Furanocumarine: Bergapten/Xanthotoxin/Imperatorin — Wiesendermatitis bei Saftkontakt und Sonne). Schwangerschaft: `pregnancy_contraindicated=true` gesetzt, aber Datenlage dünn (traditionell emmenagoger Ruf) — in `pregnancy_lactation` ausdrücklich als "unsicher — zu prüfen" markiert. Furanocumarin-CYP3A4- und Antikoagulanzien-Interaktion nur `theoretisch/gering` (klinisch nicht belegt); der übliche "Cumarin = Blutverdünner"-Irrtum wie beim Waldmeister klargestellt.

## 2026-07-19 — Blutroter Hartriegel, Giersch

**Bearbeitet:**
- cornus-sanguinea (Blutroter Hartriegel) — **Quelle: Wunschliste** (`docs/wunschliste.json`, Fundort Bodensee, einziger offener Wunsch).
- aegopodium-podagraria (Giersch) — **Quelle: Kandidatenliste**, erster offener Eintrag tier 2. Status → `entwurf_fertig`.

**Dedup:** Beide neu — kein Treffer gegen `id`/`botany.synonyms` in `fertig/` noch gegen `vorhanden`.

**Prüfergebnis:** Beide `✓ ok, mit Hinweisen` (0 Fehler, 0 Korrekturversuche). Einziger Hinweis jeweils: enthält bewusst gesetztes „unsicher — zu prüfen".

**Hauptquellen:** WebSearch-Recherche (WebFetch lieferte bei den meisten Fachseiten HTTP 403). Botanische Bestimmungsquellen (baumkunde.de, InfoFlora, pflanzen-deutschland.de), NABU/Wildkräuterseiten, Giftpflanzenhinweise.

### Überraschungen / unsichere Stellen für den Arzt

1. **Beide Pflanzen haben KEINE regulatorische Monographie** — weder HMPC/EMA noch ESCOP; Giersch nicht einmal eine (negative) Kommission-E-Monographie (Art galt als zu unbedeutend). Alle Indikationen daher bewusst nur **TRAD**. Das ist kein Recherchemangel, sondern der Befund selbst. Primärquellen konnten nicht erreicht werden (403) — Evidenzgrad TRAD ist aber durch das Fehlen jeder Monographie eindeutig; keine WEU/TU-Hochstufung gerechtfertigt.

2. **Blutroter Hartriegel ist faktisch keine Heilpflanze.** Der Wunschlisten-Eintrag ist eher ein Hecken-/Wildfruchtstrauch. Sicherheitskern statt Heilanspruch: **rohe schwarze Früchte sind schwach giftig/brechreizauslösend** (v. a. bei Kindern), erst gekocht küchentauglich (Flags `raw_toxicity`, `requires_heating`). Verwechslung mit essbarer Kornelkirsche (ROTE Früchte) sowie mit giftigem Liguster/Faulbaum (schwarze Beeren) beschrieben. `deadly_confusion=false` (kein lebensgefährlicher Doppelgänger).

3. **Giersch — populärer „Gicht-Heiler"-Ruf überzeichnet die Datenlage** deutlich (in `expectation_summary.overstated` benannt). Realer Nutzen: nährstoffreiches Wildgemüse. **Eigentliche Gefahr = Doldenblütler-Verwechslung** beim Ernten der jungen Blätter vor der Blüte: Gefleckter/Wasser-Schierling (lebensgefährlich) → `deadly_confusion=true`, `apiaceae_confusion_young=true`. Bestimmung strikt über 3-3-3-Regel (dreikantiger Blattstiel) + Möhrengeruch.

4. **Neues Flag-Paar** `raw_toxicity`/`requires_heating` beim Hartriegel genutzt (beide in `KNOWN_FLAGS` des Prüfskripts) — der Arzt möge prüfen, ob die App diese Register wie erwartet anzeigt.

## 2026-07-19 (Lauf 6) — Echter Kerbel (KANDIDAT), Wiesen-Sauerampfer (KANDIDAT)

**Auswahl (genau 2):** Wunschliste hat Vorrang, ist aber **abgearbeitet** — der einzige Eintrag in `docs/wunschliste.json` (cornus-sanguinea / Blutroter Hartriegel) liegt bereits als `fertig/monographie-blutroter-hartriegel.json` (id=cornus-sanguinea, im Vorlauf 2026-07-19 erstellt) → 0 offene Wünsche → beide Kräuter aus der Kandidatenliste. Niedrigste offene tier = 2, in Listenreihenfolge die nächsten offenen nach Giersch/Engelwurz/Traubensilberkerze:
- **anthriscus-cerefolium** (Echter Kerbel) — Quelle: Kandidatenliste tier 2 (erster offener Eintrag) — `fertig/monographie-kerbel.json`
- **rumex-acetosa** (Wiesen-Sauerampfer) — Quelle: Kandidatenliste tier 2 (zweiter offener Eintrag) — `fertig/monographie-sauerampfer.json`

**Dedup:** Beide neu — kein Treffer gegen `id`/`botany.synonyms` in `fertig/` noch gegen `vorhanden`. Altnamen selbst eingetragen: Anthriscus cerefolium → Chaerophyllum sativum / Scandix cerefolium / Cerefolium sativum / Anthriscus longirostris; Rumex acetosa → Acetosa pratensis / Lapathum acetosa / Lapathum pratense. Skript-Dublettencheck sauber. Kein Self-Heal nötig.

**Status/Changelog:** beide Kandidaten in `kraeuter-kandidaten.json` auf `entwurf_fertig` + `datei` gesetzt (NICHT `geprueft`). Je ein Changelog-Eintrag (`art: neu`) angehängt. Wunschliste nicht angefasst.

**Prüfergebnis:** beide `✓ ok, mit Hinweisen` (**0 Fehler, 0 Korrekturversuche**). Einziger Hinweis jeweils: enthält bewusst gesetztes „unsicher — zu prüfen".

**Hauptquellen:** WebSearch (WebFetch der Primär-/Sekundärquellen wie spektrum.de und altmeyers.org lieferte erneut **HTTP 403** — Inhalte über konkordante WebSearch-Sekundärquellen verifiziert). Taxonomie/Synonyme via POWO/GBIF/Wikispecies; Verwechslungen via NABU, pflanzen-vielfalt.net, kraeuterportraits, gartenjournal, abenteuer-am-wegesrand; Oxalsäure-Daten aus mehreren konkordanten Ernährungs-/Giftquellen; Sinupret-Zusammensetzung via Bionorica/Wikipedia.

### Überraschungen / unsichere Stellen für den Arzt

1. **Beide Arten haben KEINE eigene HMPC-/ESCOP-Monographie** — der Befund selbst, kein Recherchemangel. Primärquellen (EMA/altmeyers/spektrum) waren wegen 403 nicht direkt abrufbar; der Evidenzgrad TRAD ist aber durch das durchgängige Fehlen jeder Monographie eindeutig — **keine WEU/TU-Hochstufung gerechtfertigt. Bitte den regulatorischen Status trotzdem gegenprüfen.**

2. **Kerbel — Sicherheitseintrag, kein Heileintrag.** Faktisch ein Küchenkraut ohne belegten Arzneiwert; der eigentliche Zweck ist die **Verwechslungswarnung**. `deadly_confusion=true` + `apiaceae_confusion_young=true`: Gefleckter Schierling (Coniin) UND Hundspetersilie sind als `lebensgefährlich` geführt. Sicherstes Feldmerkmal = Geruchsprobe (Anis vs. Mäuseurin). Wildsammlung für Laien im `key_warning` ausdrücklich untersagt.

3. **Kerbel — Estragol-Vorbehalt.** Das ätherische Öl enthält Methylchavicol (Estragol), das wie bei Fenchel/Anis als potenziell gentoxisch/kanzerogen gilt. Ob küchenübliche Mengen relevant sind, habe ich als „unsicher — zu prüfen" markiert (keine Grenzwert-Monographie für Kerbel gefunden). `toxin_ceiling` NICHT gesetzt (kein dosisdefiniertes Toxin mit Grenzwert für die Droge).

4. **Sauerampfer — Sinupret-Falle bewusst entschärft.** Häufiges Missverständnis: Sauerampfer „hilft bei Sinusitis". Die klinische/RCT-Evidenz gehört der **Fixkombination Sinupret** (5 Drogen), NICHT der Einzeldroge; ein häuslicher Sauerampfertee reproduziert das nicht. Indikation daher `TRAD` mit explizitem Hinweis in `comment`/`realistic_expectation`/`expectation_summary.overstated`. Bitte prüfen, ob der Katalog diese Kombinations-Einschränkung so tragen soll (analog zum Schlüsselblume-Fall).

5. **Sauerampfer — Oxalsäure als eigentliches Sicherheitsthema.** `toxin_ceiling=true`, `toxin_type="Oxalsäure"`, `tox_ceiling` gefüllt: dokumentierte tödliche Vergiftung durch ~6-8 g Oxalsäure aus ~500 g Sauerampfersuppe; KI bei Nierensteinen/Niereninsuffizienz/Gicht/Hyperoxalurie. Küchenmengen bleiben unbedenklich.

6. **Sauerampfer — Aronstab-Verwechslung als `giftig`, nicht `lebensgefährlich`.** Arum maculatum ist stark giftig (Calciumoxalat-Raphiden), akute Todesfälle jedoch sehr selten (sofortiges Mundbrennen begrenzt die Aufnahme) → bewusst `giftig` und `deadly_confusion=false`. Sammelanker = Geschmacksprobe (Aronstab brennend-scharf, nie sauer). Bitte prüfen, ob „giftig" statt „lebensgefährlich" für die App-Warnstufe passend ist.

## 2026-07-19 — Arnika, Mutterkraut (beide KANDIDATEN, tier 2)

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` enthaelt 1 Eintrag — **cornus-sanguinea** (Common dogwood). Dieser liegt jedoch bereits als `fertig/monographie-blutroter-hartriegel.json` (id `cornus-sanguinea`) vor → Wunsch erfuellt, per Dedup uebersprungen (App hakt selbst ab, `wunschliste.json` NICHT angefasst). Damit 0 offene Wuensche → **beide Plaetze aus der Kandidatenliste**: erste zwei `offen`-Eintraege nach tier aufsteigend = die beiden tier-2-Eintraege **arnica-montana** und **tanacetum-parthenium** (die frueheren tier-2-Eintraege stehen bereits auf `entwurf_fertig`).

- **arnica-montana** (Arnika) — `fertig/monographie-arnika.json` — Quelle: Kandidatenliste (tier 2). Status → `entwurf_fertig`.
- **tanacetum-parthenium** (Mutterkraut) — `fertig/monographie-mutterkraut.json` — Quelle: Kandidatenliste (tier 2). Status → `entwurf_fertig`.

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` in der Kandidatenliste geprueft — keine Dublette. Altnamen eingetragen: Arnika = Doronicum arnica/Arnica helvetica/Cineraria cernua; Mutterkraut = Chrysanthemum parthenium/Matricaria parthenium/Pyrethrum parthenium/Leucanthemum parthenium. Synonym-Wahl bewusst so, dass keine falsche Dublett-Warnung gegen bestehende Dateien entsteht (Matricaria chamomilla = Kamille bleibt getrennt, Tanacetum vulgare = Rainfarn bleibt getrennt). Kein Self-Heal noetig (kein als "offen" markierter Kandidat lag bereits in `fertig/`).

**Pruefergebnis:** beide einzeln UND gemeinsam `✓ ok, mit Hinweisen`, 0 Fehler beim **ersten Versuch** — **0 Korrekturversuche**. Einziger Hinweis je Datei: enthaelt "unsicher/zu pruefen" (bewusst gesetzt).

**Hauptquellen:**
- Arnika: EMA/HMPC Community herbal monograph Arnica montana L., flos (traditional use, 2014) + Assessment report; ESCOP Arnicae flos; Kommission E (Arnikablueten). Verwechslungs-/Toxikologie-Recherche ueber SAC-CAS, gartenjournal, guterboden, DAZ, Sekundaerquellen zu Helenalin.
- Mutterkraut: EMA/HMPC EU herbal monograph Tanacetum parthenium (L.) Sch.Bip., herba (traditional use, EMA/HMPC/48715/2017, 2020) + Assessment report; ESCOP Tanaceti parthenii herba; Cochrane Review Wider 2015 (CD002286.pub3); Metaanalyse 2025; Plantura/naturadb/krank.de/nachgeharkt fuer Verwechslung + Nebenwirkungen.

**Quellen-Abruf:** WebFetch auf die EMA-Primaer-PDFs lieferte wie in allen Vorlaeufen **HTTP 403**. Inhalte daher ueber WebSearch-Zusammenfassungen mehrerer uebereinstimmender Sekundaerquellen verifiziert. Die HMPC-Einstufung (fuer BEIDE Arten: traditional use, NICHT well-established) ist gut und mehrfach dokumentiert und damit belastbar; Posologie-Zahlen (Arnika-Verduennungsverhaeltnisse, Mutterkraut ~100 mg/Tag, Parthenolid 0,2-0,6 %) sollten dennoch am Original-Monograph gegengeprueft werden.

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Arnika ist HMPC traditional use und AUSSCHLIESSLICH aeusserlich** — nicht well-established use. In DE/LV/SI existieren daneben einzelne WEU-Zulassungen fuer bestimmte Fertigpraeparate; ich habe die Kern-Indikation (Prellungen/Verstauchungen) defensiv als `TU/ESCOP+` getaggt, die uebrigen als `TU`. Bitte nicht auf WEU hochstufen.
- **Arnika — der eigentliche Sicherheitspunkt ist die INNERLICHE Giftigkeit (Helenalin), nicht ein Doppelgaenger.** Einnahme von Tinktur/Tee kann Herzrhythmusstoerungen bis Herzstillstand ausloesen. `topical_only=true` gesetzt; kein "innerlich giftig"-Flag existiert, daher steht die Warnung ausfuehrlich in `key_warning`/`contraindications`/`kitchen`/`overstated`. `toxin_ceiling` bewusst **false** (innerliche Anwendung ist nicht dosisbegrenzt, sondern schlicht verboten). Bitte gegenpruefen, ob das Register die innerliche Toxizitaet so ausreichend abbildet.
- **Arnika — homoeopathische Globuli ≠ stoffliche Arnika.** Ausdruecklich in `overstated` abgegrenzt, damit aus der Verbreitung der Globuli kein Wirknachweis fuer die stoffliche Droge gezogen wird.
- **Arnika — sicherheitsrelevante Verwechslung ist das PA-haltige Greiskraut (Senecio, giftig/leberschaedigend)**, nicht ein toedlicher Doppelgaenger → `deadly_confusion=false`. Sicherstes Unterscheidungsmerkmal: Arnika hat GEGENSTAENDIGE Blaetter (bei Korbbluetlern eine Seltenheit). Zusaetzlich: Art ist nach BArtSchV besonders geschuetzt, Wildsammlung unzulaessig → `region_occurrence: wild-selten`, nur Anbau; kalkmeidend, daher im kalkreichen Bodenseeraum gaertnerisch schwierig.
- **Mutterkraut ist HMPC traditional use zur MIGRAENE-PROPHYLAXE — kein Akutmittel.** Cochrane 2015 ist inkonsistent (nur der stabile CO2-Extrakt MIG-99 zeigte klare Wirkung); neuere Metaanalysen (2025) guenstiger, aber HMPC bleibt TU. Ich habe `TU/ESCOP+` getaggt und den Evidenzvorbehalt in `evidence_caveat`/`overstated` deutlich gemacht. Wirkung praeparatabhaengig (Parthenolidgehalt schwankt stark).
- **Mutterkraut — `pregnancy_contraindicated=true`.** Wehenausloesend/abortiv (daher der Name "Mutterkraut"); der historische Ruf als Frauen-/Fiebermittel (als separate `TRAD`-Indikation ehrlich, aber unbelegt aufgenommen) darf NICHT zu einer Anwendung in der Schwangerschaft verleiten.
- **Mutterkraut — zwei leicht uebersehene Nebenwirkungen:** Mundgeschwuere beim Kauen FRISCHER Blaetter und das "Post-Feverfew-Syndrom" (Rebound-Kopfschmerz/Nervositaet/Schlafstoerungen beim abrupten Absetzen) → ein-/ausschleichend dosieren. Zusaetzlich Thrombozytenaggregationshemmung (Parthenolid) → Blutungsrisiko mit Antikoagulanzien/ASS, vor OPs absetzen (als pharmakodynamisch, Relevanz "gering-relevant, unsicher").
- **Mutterkraut — Verwechslung:** giftiger Rainfarn (Tanacetum vulgare, gleiche Gattung, Thujon) und harmlose Kamille. Unterscheidung ueber flachen, innen hohlen Bluetenboden (Kamille kegelfoermig) und den bitteren, rainfarnartigen Geruch. Kein lebensgefaehrlicher Doppelgaenger → `deadly_confusion=false`.

## 2026-07-19 (Lauf 8) — Herbstzeitlose (KANDIDAT), Maiglöckchen (KANDIDAT) — beide tier-3 WARNEINTRÄGE

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` enthaelt weiterhin 1 Eintrag — **cornus-sanguinea** (Common dogwood) —, der bereits als `fertig/monographie-blutroter-hartriegel.json` (id `cornus-sanguinea`) vorliegt → Wunsch erfuellt, per Dedup uebersprungen (`wunschliste.json` NICHT angefasst). 0 offene Wuensche → **beide Plaetze aus der Kandidatenliste**. Alle tier-1- und tier-2-Eintraege stehen bereits auf `entwurf_fertig`; niedrigste offene tier = **tier 3**. Erste zwei offene tier-3 in Listenreihenfolge:

- **colchicum-autumnale** (Herbstzeitlose) — `fertig/monographie-herbstzeitlose.json` — Quelle: Kandidatenliste (tier 3, Warneintrag). Status → `entwurf_fertig`.
- **convallaria-majalis** (Maiglöckchen) — `fertig/monographie-maigloeckchen.json` — Quelle: Kandidatenliste (tier 3, Warneintrag). Status → `entwurf_fertig`.

**Warneintrag-Bau (nach CLAUDE.md / SPEC Sonderfall):** `indications` LEER, `flags.not_for_use=true`, `expectation_summary.plausible` = Erkennungs-/Warnhinweis, `confusions` in UMGEKEHRTER Richtung (die Nutz-/Nahrungspflanzen, mit denen die Giftpflanze verwechselt wird — hier v. a. **Bärlauch**), `key_features` besonders sorgfaeltig (Kern des Eintrags), `harvest_month_tags` leer (Warneintrag → validator warnt dafuer nicht).

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` geprueft — keine Dublette (kein Herbstzeitlose/Maiglöckchen-File vorhanden). Altnamen eingetragen: Herbstzeitlose = Colchicum commune / Bulbocodium autumnale / Colchicum vernale; Maiglöckchen = Convallaria bracteata / fragrans / latifolia / linnaei. Beide Arten standen bereits als Verwechslungspartner IN der bestehenden `monographie-baerlauch.json` (kuratiert) — dort in Bärlauch-Richtung; die neuen Dateien sind die eigenstaendigen Warneintraege in Gegenrichtung, keine Dublette.

**Pruefergebnis:** Herbstzeitlose `✓ alles sauber` beim ersten Versuch (0 Korrekturen). Maiglöckchen: 1 Fehler beim ersten Versuch (Herbstzeitlose als `lebensgefährlich` gelistet → `flags.deadly_confusion` musste true sein); nach Korrektur `✓ ok` → **1 Korrekturversuch**. Beide bestehen final ohne Fehler und ohne Hinweise.

**Hauptquellen:** WebSearch-Zusammenfassungen mehrerer uebereinstimmender Sekundaerquellen: BfR/Giftinformationszentren (Bärlauch-Verwechslung, Geruchstest), CliniTox/Vetpharm Universitaet Zuerich (Colchicin- bzw. Cardenolid-Toxikologie), PTA-Forum/Astrea-Bulletin (Colchicin), PharmaWiki/AWL-Arzneipflanzenlexikon + Toxikologie.de (Convallatoxin), Kew POWO/GBIF (Taxonomie/Familie/Synonyme), kvoberallgaeu-BRK/Apotheken-Umschau/utopia (Unterscheidungsmerkmale Blattstiel/Rosette/glaenzend-matt/Geruch).

**Quellen-Abruf:** WebFetch scheiterte in diesem Lauf durchgehend mit **HTTP 403** (u. a. Vetpharm/CliniTox, Wikipedia, Apotheken-Umschau, toxikologie.de-PDF, utopia). Es sind reine Warneintraege OHNE Anwendung, daher keine HMPC-WEU/TU-Einstufung noetig; toxikologische Zahlen (Colchicin-Letaldosis ~20 mg, Blattgehalt 0,07–2 %) stammen aus Sekundaerquellen und sind im `sources`-Feld ausdruecklich als gegenzupruefen markiert.

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Herbstzeitlose — Symptomlatenz ist die eigentliche Gefahr.** 2–6 h beschwerdefrei, dann GI-Sturm, danach ein truegerisch symptomarmes Intervall (1–3 Tage) vor Multiorganversagen. Colchicin ist **hitzestabil** — Kochen/Trocknen/Tee entgiften NICHT. Kein Antidot. `pregnancy_contraindicated=true` gesetzt (Colchicin mitosehemmend/teratogen/abortiv). `toxin_ceiling` bewusst **false**: es gibt keine erlaubte Dosis, die man begrenzt — die Pflanze ist schlicht kein Lebens-/Arzneimittel; Grenzwerte stehen in `tox_ceiling`/`key_warning`.
- **Herbstzeitlose — zweite, seltener genannte Verwechslung:** die blattlose Herbstbluete aehnelt dem **Safran-Krokus** (Crocus sativus). Unterscheidung ueber die Staubblaetter (Herbstzeitlose 6, Safran 3). Als essbare Konfusion aufgenommen, damit das Register auch diese Richtung kennt.
- **Maiglöckchen — bewusste Abstufung `giftig`, nicht `lebensgefährlich`.** Die herzwirksamen Cardenolide (Convallatoxin) sind zwar hochpotent, werden aber **oral schlecht resorbiert**; Verzehr-Vergiftungen beim Menschen verlaufen ueberwiegend gastrointestinal-mild, schwere kardiale Verlaeufe (Bradykardie/AV-Block bis Herzstillstand) sind selten, aber moeglich. Das ist der wichtigste medizinische Unterschied zur oft ueberzeichneten Darstellung — bitte pruefen, ob diese Einordnung dem gewuenschten Sicherheits-Ton entspricht.
- **Maiglöckchen — `deadly_confusion=true` trotz Eigen-Einstufung `giftig`.** Begruendung: die Fruehjahrsblaetter stehen im SELBEN Baerlauch-Verwechslungskomplex wie die **lebensgefaehrliche Herbstzeitlose**; wer Maiglöckchen fuer Baerlauch haelt, greift ebenso leicht zur Herbstzeitlose. Der Validator erzwingt das Flag zudem, weil ich Herbstzeitlose als `lebensgefährlich`-Konfusion gelistet habe. Falls das Register „deadly_confusion" strikt als „dieser Eintrag selbst hat einen toedlichen Doppelgaenger" liest, passt es; falls es „dieser Eintrag ist selbst toedlich" bedeutet, waere hier ggf. eine Nachjustierung noetig.
- **Beide — alle Pflanzenteile giftig**, beim Maiglöckchen ausdruecklich auch **Beeren und Vasenwasser** (Kinder-/Haustiergefahr). Der Geruchstest zur Baerlauch-Abgrenzung ist nur am ERSTEN, unberuehrten Blatt gueltig (Finger kontaminieren danach mit Knoblauchgeruch) — in `collection_rules` festgehalten.

## 2026-07-20 (Lauf 9) — Gefleckter Schierling (KANDIDAT), Roter Fingerhut (KANDIDAT) — beide tier-3 WARNEINTRÄGE

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` enthaelt weiterhin nur **cornus-sanguinea** (Common dogwood), bereits als `fertig/monographie-blutroter-hartriegel.json` (id `cornus-sanguinea`, Synonyme Swida/Thelycrania sanguinea) vorhanden → Wunsch erfuellt, per Dedup uebersprungen (`wunschliste.json` NICHT angefasst). 0 offene Wuensche → **beide Plaetze aus der Kandidatenliste**. Alle tier-1/2 stehen auf `entwurf_fertig`; niedrigste offene tier = **tier 3**. Erste zwei offene tier-3 in Listenreihenfolge:

- **conium-maculatum** (Gefleckter Schierling) — `fertig/monographie-gefleckter-schierling.json` — Quelle: Kandidatenliste (tier 3, Warneintrag). Status → `entwurf_fertig`.
- **digitalis-purpurea** (Roter Fingerhut) — `fertig/monographie-roter-fingerhut.json` — Quelle: Kandidatenliste (tier 3, Warneintrag). Status → `entwurf_fertig`.

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` geprueft — keine Dublette (kein Schierling-/Fingerhut-File). Altnamen selbst eingetragen: Schierling = Cicuta major / Coriandrum maculatum; Fingerhut = Digitalis tomentosa / gloxinioides. Validator-Dublettencheck ueber beide neuen Dateien: keine Kollision.

**Warneintrag-Bau (SPEC-Sonderfall):** `indications` LEER, `flags.not_for_use=true`, `expectation_summary.plausible` = Erkennungs-/Warnhinweis, `confusions` in UMGEKEHRTER Richtung (die essbaren/genutzten Pflanzen, mit denen die Giftpflanze verwechselt wird), `key_features` besonders sorgfaeltig, `harvest_month_tags` leer (Warneintrag → keine Validator-Warnung).

**Pruefergebnis:** Beide beim ERSTEN Versuch bestanden (0 Korrekturen). Fingerhut `✓ alles sauber`; Schierling `ok, mit Hinweisen` (nur der positive Honesty-Hinweis wegen bewusst gesetztem „unsicher, aerztlich zu pruefen" bei der toedlichen Dosis). Keine `✗ FEHLER`.

**Hauptquellen:** WebSearch-Zusammenfassungen mehrerer uebereinstimmender Sekundaerquellen — AWL.ch-Heilpflanzenlexikon, de.wikipedia (Gefleckter Schierling), Boskabadi et al. Clinical Case Reports 2021, ScienceDirect/Coniine (Schierling); Arzneipflanzen-Lexikon/PharmaWiki, phytotherapie-seminare.ch-Fallbericht, GIZ Bonn, en.wikipedia (Digitalis, Plantaginaceae, Na+/K+-ATPase). Taxonomie/Synonyme via Kew POWO/GBIF.

**Quellen-Abruf:** WebFetch scheiterte in diesem Lauf durchgehend mit **HTTP 403** (AWL.ch, phytotherapie-seminare.ch, de.wikipedia, gizbonn.de). Es sind reine Warneintraege OHNE Anwendung → keine HMPC-WEU/TU-Einstufung noetig; toxikologische Kennzahlen aus Sekundaerquellen, im `sources`-Feld ausdruecklich als gegenzupruefen markiert.

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Schierling — toedliche Dosis in der Literatur uneinheitlich.** Angaben schwanken zwischen ~0,5–1 g Coniin, „wenigen Gramm Pflanzenmaterial" und geschaetzt 150–300 mg Coniin oral. Bewusst als **„unsicher, aerztlich zu pruefen"** in `standard_dose` markiert (loest den positiven Validator-Hinweis aus). Kernbotschaft bleibt: schon kleine Verwechslungsmengen koennen toedlich sein.
- **Schierling — `deadly_confusion=true` + `apiaceae_confusion_young=true`.** Als lebensgefaehrlichen Abgrenzungsfall habe ich **Wasserschierling (Cicuta virosa, Cicutoxin)** in die `confusions` aufgenommen — anderes Toxin, **krampfausloesend** statt laehmend; damit ist das Flag validator-konsistent (Konvention wie Maiglöckchen). Zusaetzlich `pregnancy_contraindicated=true`, da Coniin bei Weidetieren **teratogen** (fetale Skelettmissbildungen) belegt ist — ungewoehnlich fuer eine „nicht anzuwendende" Pflanze, aber relevant fuer die Register.
- **Schierling — Leitmerkmale sind geruchs-/staengelbasiert:** kahler, blaubereifter, **ROTGEFLECKTER** Staengel + **MAEUSEURINGERUCH** beim Zerreiben. Junge Rosetten sind von Petersilie/Kerbel/Wilder Möhre kaum sicher zu trennen → Grundregel „kein weissbluetiger Doldenbluetler ohne zweifelsfreie Bestimmung".
- **Fingerhut — Kernrisiko ist die Rosetten-Verwechslung mit BEINWELL** (als Tee/Wildgemuese gesammelt), mehrfach mit lebensgefaehrlichem Ausgang dokumentiert. Entscheidend: Fingerhutblatt **weich filzig-wollig, unterseits grau-netznervig, laeuft NICHT am Staengel herab**; Beinwell **rau-borstig und deutlich herablaufend**. Glykoside sind **hitze-/wasserstabil** → der Teeaufguss **entgiftet nicht, sondern extrahiert** das Gift.
- **Fingerhut — `deadly_confusion=false` bewusst gesetzt** (Konvention wie Herbstzeitlose): kein Konfusionspartner ist selbst „lebensgefährlich" (Beinwell/Borretsch/Königskerze = essbar). Toedlich ist der Fingerhut SELBST. Falls das Register `deadly_confusion` als „dieser Eintrag ist toedlich und wird mit Essbarem verwechselt" liest, waere hier ggf. eine bewusste Umstellung auf `true` zu erwaegen — gleiche offene Frage wie bei Herbstzeitlose/Maiglöckchen im Lauf 8. `interaction_heavy=true` und `pregnancy_contraindicated=true` gesetzt.
- **Fingerhut — Taxonomie aktualisiert:** heute **Plantaginaceae** (frueher Scrophulariaceae). Hinweis fuer die Chemie: **Digoxin** stammt ueberwiegend aus *Digitalis lanata* (Wolliger Fingerhut), *D. purpurea* liefert v. a. **Digitoxin** — in `synonym_note`/`chemistry` so differenziert. Digitoxin hat lange HWZ + enterohepatischen Kreislauf → **Kumulations- und Spaetvergiftungsgefahr**.

## 2026-07-20 (Lauf 10) — Blauer Eisenhut (KANDIDAT), Tollkirsche (KANDIDAT) — beide tier-3 WARNEINTRÄGE

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` enthaelt weiterhin nur **cornus-sanguinea** (Common dogwood), bereits als `fertig/monographie-blutroter-hartriegel.json` (id `cornus-sanguinea`, Synonyme Swida/Thelycrania sanguinea) vorhanden → Wunsch erfuellt, per Dedup uebersprungen (`wunschliste.json` NICHT angefasst). 0 offene Wuensche → **beide Plaetze aus der Kandidatenliste**. Niedrigste offene tier = **tier 3**. Erste zwei offene tier-3 in Listenreihenfolge:

- **aconitum-napellus** (Blauer Eisenhut) — `fertig/monographie-blauer-eisenhut.json` — Quelle: Kandidatenliste (tier 3, Warneintrag). Status → `entwurf_fertig`.
- **atropa-belladonna** (Tollkirsche) — `fertig/monographie-tollkirsche.json` — Quelle: Kandidatenliste (tier 3, Warneintrag). Status → `entwurf_fertig`.

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` (71 Dateien) und `vorhanden` geprueft — keine Dublette. Altnamen selbst eingetragen: Eisenhut = Napellus vulgaris Fourr. (POWO-bestaetigt) + subsp. napellus; Tollkirsche = Atropa bella-donna / Belladonna baccifera Lam. / Atropa lutescens Jacq. Validator-Dublettencheck ueber beide neuen Dateien: keine Kollision.

**Warneintrag-Bau (SPEC-Sonderfall):** `indications` LEER, `flags.not_for_use=true`, `expectation_summary.plausible` = Erkennungs-/Warnhinweis, `confusions` in UMGEKEHRTER Richtung (die essbaren Pflanzen, mit denen die Giftpflanze verwechselt wird), `key_features` besonders sorgfaeltig, `harvest_month_tags` leer.

**Pruefergebnis:** Beide beim ERSTEN Versuch bestanden (0 Korrekturen). Je `ok, mit Hinweisen` — nur der positive Honesty-Hinweis (bewusst gesetztes „unsicher — aerztlich zu pruefen" bei den toedlichen Dosen). Keine `✗ FEHLER`.

**Hauptquellen:** WebSearch-Zusammenfassungen mehrerer uebereinstimmender Sekundaerquellen — giftpflanzen.com, heilpraxisnet.de, natuerlich.thieme.de, PharmaWiki, ScienceDirect Topics „Aconitine"/„Aconitum sp. alkaloids", PMC-Aconitin-Toxikologie (Eisenhut); de.wikipedia (Schwarze Tollkirsche), naturadb.de, plantura.garden, arzneipflanzenlexikon.info, hanf-magazin.com, diePTA, DocCheck, PubMed/PMC-Fallberichte (Tollkirsche). Taxonomie/Synonyme via Kew POWO/GBIF.

**Quellen-Abruf:** WebFetch scheiterte in diesem Lauf durchgehend mit **HTTP 403** (Wikipedia de/en, giftpflanzen.com, botanikus.de, gizbonn.de, awl.ch, NCBI/PMC, PubMed). WebSearch war anfangs ~10 min mit **HTTP 529 (Overloaded)** nicht verfuegbar, danach nutzbar — Recherche vollstaendig ueber WebSearch-Zusammenfassungen. Es sind reine Warneintraege OHNE Anwendung → keine HMPC-WEU/TU-Einstufung noetig; toxikologische Kennzahlen aus Sekundaerquellen, im `sources`-Feld ausdruecklich als gegenzupruefen markiert.

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Eisenhut — Hautresorption ist der ungewoehnliche Punkt.** Aconitin wird auch **perkutan** (ueber Haut/kleine Wunden) resorbiert; Vergiftungen allein durch Hantieren mit der Pflanze/Wurzel sind beschrieben → in `collection_rules`/`garden` „Handschuhe" betont. Als **haeufige Zierstaude** ist der Eisenhut zudem ein Garten-/Kinder-/Haustierrisiko, nicht nur eine Wildpflanze.
- **Eisenhut — toedliche Dosis uneinheitlich.** Literatur nennt ~2–6 mg Aconitin bzw. 1–10 mg/kg oral / wenige Gramm Wurzel. Bewusst als **„unsicher — aerztlich/toxikologisch zu pruefen"** markiert. Wurzelgehalt bis ~3 % Aconitin (hoechster Teil). Kein zugelassenes spezifisches Antidot; Procain/Antiarrhythmika werden diskutiert (unsicher).
- **Eisenhut — Kern-Verwechslung ist die WURZEL** (dunkle Knolle ↔ Meerrettich/Sellerie/Pastinake), nicht das Kraut. Bestaetiger: Meerrettich/Sellerie riechen typisch, Eisenhutknolle ist mild/geruchsarm — aber **nicht probieren**. `deadly_confusion=false` (Konvention: kein Konfusionspartner selbst „lebensgefährlich"; Gelber Eisenhut nur als `giftig`-Abgrenzung gelistet). `pregnancy_contraindicated=true`.
- **Eisenhut — Taxonomie:** *A. napellus* ist ein **komplexer Aggregat** mit vielen Unterarten; infraspezifische Feldzuordnung oft unsicher (in `synonym_note` vermerkt). Nicht mit Gelbem Eisenhut (*A. lycoctonum/vulparia*) oder Zier-Hybrid *A. × cammarum* verwechseln.
- **Tollkirsche — die Suesse der Beeren ist die eigentliche Falle.** Beeren schmecken **suesslich** → Kinder essen sie arglos; schon **3–4 Beeren** koennen ein Kind toeten (Erwachsene ~10–12). Leitmerkmal zur Abgrenzung: **Einzelbeere auf breitem, sternfoermigem Kelch** an krautiger Staude — im Gegensatz zur Kirsche (Stein, langer Stiel, kein Kelch) und Heidelbeere (klein, Zwergstrauch). `deadly_confusion=false` (Konvention), `pregnancy_contraindicated=true`.
- **Tollkirsche — zwei seltener genannte Verwechslungsrichtungen dokumentiert:** **Blaetter** wurden als Wildgemuese/**Spinat** verkocht (Sammelvergiftungen), **Wurzeln** mit **Meerrettich/Pastinake** verwechselt (Erwachsenenvergiftungen) — beide als essbare Konfusionen aufgenommen. Antidot bei schwerer zentraler Symptomatik: **Physostigmin** (nur aerztlich/intensivmedizinisch). Zur Abgrenzung „Schwarzer Nachtschatten" (`giftig`, Solanin, Beeren in Trauben statt einzeln) mitgelistet.
- **Offene Register-Frage (wie Laeufe 8/9):** Bei allen tier-3-Eintraegen bleibt `deadly_confusion=false`, weil die Pflanze SELBST toedlich ist und kein Konfusionspartner „lebensgefährlich" ist. Falls das App-Register `deadly_confusion` als „dieser essbare-aussehende Eintrag hat/ist einen toedlichen Doppelgaenger" liest, waere fuer die Warneintraege ggf. eine bewusste Umstellung auf `true` zu erwaegen — konsistent offen gehalten, Konvention der bestehenden Warneintraege (Herbstzeitlose/Fingerhut) gefolgt.

## 2026-07-20 (Lauf 11) — Riesen-Bärenklau (KANDIDAT), Rosmarinheide (KANDIDAT) — beide tier-3 WARNEINTRÄGE

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` enthaelt weiterhin nur **cornus-sanguinea** (Common dogwood), bereits als `fertig/monographie-blutroter-hartriegel.json` (id `cornus-sanguinea`, Synonyme Swida/Thelycrania sanguinea) vorhanden → Wunsch erfuellt, per Dedup uebersprungen (`wunschliste.json` NICHT angefasst). 0 offene Wuensche → **beide Plaetze aus der Kandidatenliste**. Niedrigste offene tier = **tier 3**. Die zwei verbliebenen offenen tier-3 in Listenreihenfolge:

- **heracleum-mantegazzianum** (Riesen-Bärenklau) — `fertig/monographie-riesen-baerenklau.json` — Quelle: Kandidatenliste (tier 3, Warneintrag). Status → `entwurf_fertig`.
- **andromeda-polifolia** (Rosmarinheide) — `fertig/monographie-rosmarinheide.json` — Quelle: Kandidatenliste (tier 3, Warneintrag). Status → `entwurf_fertig`.

Damit sind **alle tier-3-Warneintraege der Kandidatenliste abgearbeitet**; ab dem naechsten Lauf beginnt tier 4 (Loewenzahn, Gaensebluemchen, Vogelmiere …), sofern die Wunschliste leer bleibt.

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` (73 Dateien) und `vorhanden` geprueft — keine Dublette. Altnamen selbst eingetragen: Riesen-Bärenklau = Heracleum giganteum hort. / H. grossheimii / H. circassicum; Rosmarinheide = Andromeda rosmarinifolia Pursh / A. polifolia var. glaucophylla / Polifolia rosmarinifolia. Validator-Dublettencheck ueber beide neuen Dateien: keine Kollision.

**Warneintrag-Bau (SPEC-Sonderfall):** `indications` LEER, `flags.not_for_use=true`, `expectation_summary.plausible` = Erkennungs-/Warnhinweis, `confusions` in UMGEKEHRTER Richtung (die Nutz-/essbaren Pflanzen, mit denen die Giftpflanze verwechselt wird), `key_features` besonders sorgfaeltig, `harvest_month_tags` leer.

**Pruefergebnis:** Beide beim ERSTEN Versuch bestanden (0 Korrekturen). Riesen-Bärenklau `✓ alles sauber`; Rosmarinheide `ok, mit Hinweisen` — nur der positive Honesty-Hinweis (bewusst gesetztes „unsicher — zu pruefen" bei den art-spezifischen toxischen Mengen). Keine `✗ FEHLER`.

**Hauptquellen:** WebSearch-Zusammenfassungen mehrerer uebereinstimmender Sekundaerquellen — DocCheck Flexikon, hortica.de, gartenjournal.net, naturadb.de, Zweckverband Peenetal, krautgeschwister.de (Riesen-Bärenklau); giftpflanzen.com, pflanzen-deutschland.de, naturadb.de, gartendatenbank.de, NatureGate, Baumkunde, Aryal et al. J Appl Toxicol 2025 + Springer 2012 zu Grayanotoxin/Mad-Honey (Rosmarinheide). Taxonomie via Kew POWO/GBIF-Kenntnis.

**Quellen-Abruf:** WebFetch scheiterte in diesem Lauf durchgehend mit **HTTP 403** (Wikipedia de, DocCheck, giftpflanzen.com, CliniTox/vetpharm, pflanzen-deutschland.de). WebSearch war nutzbar — Recherche vollstaendig ueber WebSearch-Zusammenfassungen. Reine Warneintraege OHNE Anwendung → keine HMPC-WEU/TU-Einstufung noetig; toxikologische Kennzahlen aus Sekundaerquellen, im `sources`-Feld ausdruecklich als gegenzupruefen markiert.

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Riesen-Bärenklau — es ist ein KONTAKTgift, kein Verzehrgift.** Der Kernmechanismus ist die **phototoxische** Reaktion: Furocumarine (Bergapten/5-MOP, Xanthotoxin/8-MOP, Psoralen, Imperatorin) im Saft + UV-A → verbrennungsartige Blasen mit **24–48 h Latenz** und **monatelanger Hyperpigmentierung**. Dieselbe Substanzklasse wie in der PUVA-Therapie, hier unkontrolliert. In der App als `photosensitizing=true` (nicht als Verzehrtoxin) gefuehrt; `toxin_type: "Furocumarine"`.
- **Riesen-Bärenklau — Kinderwarnung explizit gesetzt:** hohle Stängel werden als „Blasrohr/Fernrohr" benutzt → Gesichtsverbrennungen; Saft ins Auge kann Hornhautschaeden verursachen. Entfernung nur mit voller Schutzkleidung, nicht bei Sonne.
- **Riesen-Bärenklau — die essbare Verwandtschaft ist selbst nicht ganz harmlos:** Der jung essbare **Wiesen-Bärenklau (H. sphondylium)** enthaelt ebenfalls Furocumarine (geringer) und kann bei empfindlichen Personen mild phototoxisch reagieren — im `confusions.note` vermerkt. Abgrenzung zum Riesen: Riesenwuchs 2–4 m, purpurrot gefleckter borstiger Stängel, Riesendolde bis 50 cm. **Arznei-Engelwurz** ist kahl (Bärenklau borstig). Invasiver Neophyt der EU-Unionsliste.
- **Rosmarinheide — die Namensfalle ist der eigentliche Sicherheitspunkt.** „Rosmarinheide"/„Lavendelheide" klingt harmlos-aromatisch; die Pflanze ist aber ein **giftiges Heidekrautgewächs (Ericaceae)**, nicht mit Küchen-Rosmarin (Salvia rosmarinus) verwandt. Enthaelt **Grayanotoxine (= Andromedotoxin/Acetylandromedol/Rhodotoxin)**, die spannungsabhaengige **Na-Kanaele offenhalten** → Dauerdepolarisation, **vagal bedingte Bradykardie/Hypotonie** (Mechanismus wie „mad honey"). Grayanotoxine sind **wasserloeslich und hitzestabil** → gehen in einen vermeintlich harmlosen „Tee" ueber. `toxin_type: "Grayanotoxine"`, `pregnancy_contraindicated=true`.
- **Rosmarinheide — art-spezifische toxische/letale Mengen sind UNSICHER.** Der Grayanotoxin-Mechanismus und das klinische Bild sind aus der Mad-Honey-Literatur gut belegt, aber quantitative Dosis-Angaben speziell fuer *Andromeda polifolia* fehlen — bewusst als „unsicher — zu pruefen" markiert (loeste den einzigen Validator-Hinweis aus).
- **Rosmarinheide — zwei zusaetzliche Verwechslungsachsen:** (1) **Sumpfporst** (*Rhododendron tomentosum*, syn. *Ledum palustre*) am selben Moorstandort — ebenfalls giftig (Grayanotoxine), unterscheidbar durch rostbraun filzige Blattunterseite + starken Harzgeruch; als `giftig` gelistet, daher `deadly_confusion=false` bleibt korrekt. (2) Beim **Moosbeeren-Sammeln** (*Vaccinium oxycoccos*, essbar, gleicher Standort) nicht verwechseln — Rosmarinheide bildet keine essbaren Beeren, sondern trockene Kapseln. Zusaetzlich **naturschutzrechtlich geschuetzte, stark ruecklaeufige Moorart** → im Feld ohnehin nicht entnehmen.
- **Register-Konvention beibehalten:** Wie in Laeufen 8–10 bleibt `deadly_confusion=false` fuer beide Warneintraege (kein Konfusionspartner ist selbst „lebensgefährlich"; die Gefahr geht von der Warnpflanze SELBST aus). Offene App-Frage unveraendert — falls das Register `deadly_confusion` anders interpretiert, waere eine bewusste Umstellung fuer die Warneintraege zu erwaegen.

## 2026-07-20 — Löwenzahn, Gänseblümchen (beide KANDIDATEN, tier 4)

**Auswahl (genau 2):** Wunschliste hat Vorrang, ist aber faktisch leer: der einzige Eintrag in `docs/wunschliste.json` — **cornus-sanguinea** (Blutroter Hartriegel, Fundort Bodensee) — liegt bereits als `fertig/monographie-blutroter-hartriegel.json` (id `cornus-sanguinea`, Lauf 2026-07-19) vor → per Dedup uebersprungen (die App hakt den Wunsch selbst ab). Damit 0 offene Wuensche → **beide Plaetze aus der Kandidatenliste**: erste offene Eintraege nach tier aufsteigend. Alle tier 1–3 sind `entwurf_fertig`; erste beide `offen` in tier 4 = **taraxacum-officinale** (Löwenzahn) und **bellis-perennis** (Gänseblümchen).

- **taraxacum-officinale** (Löwenzahn) — `fertig/monographie-loewenzahn.json` — Quelle: Kandidat tier 4. Status → `entwurf_fertig`.
- **bellis-perennis** (Gänseblümchen) — `fertig/monographie-gaensebluemchen.json` — Quelle: Kandidat tier 4. Status → `entwurf_fertig`.

**Dedup:** beide gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` in der Kandidatenliste geprueft — keine Dublette. (Einziger Treffer beim Grep: 'Bellis perennis' erscheint als Verwechslungs-`scientific_name` in `monographie-borstiges-berufkraut.json`, NICHT als eigene id/Synonym → keine echte Kollision.) Altnamen eingetragen: Löwenzahn = Leontodon taraxacum L., Taraxacum vulgare, Taraxacum campylodes, „Taraxacum officinale Weber ex Wigg."; Gänseblümchen = Bellis hortensis Mill., Bellis perennis var. hortensis, Bellis alpina. Kein Self-Heal noetig (kein als `offen` markierter Kandidat lag bereits in `fertig/`).

**Pruefergebnis:** beide einzeln UND gemeinsam `✓ ok, mit Hinweisen`, **0 Fehler beim ersten Versuch — 0 Korrekturversuche**. Einziger Hinweis je Datei: enthaelt bewusst „unsicher/zu pruefen".

**Hauptquellen:**
- Löwenzahn: EMA/HMPC EU/Community herbal monograph *Taraxacum officinale* Weber ex Wigg., radix cum herba (traditional use) + neuere Monographie radix (EMA/HMPC/475726/2020, 2022); Kommission E (Taraxaci radix cum herba / folium, positiv); ESCOP Taraxaci radix (2024) / folium. Botanik/Verwechslung/Inhaltsstoffe ueber Websuche (Arzneipflanzen-Lexikon, awl.ch, Gartenjournal, deavita).
- Gänseblümchen: KEINE regulatorische Monographie (HMPC/ESCOP/Kommission E) — mehrfach bestaetigter Negativbefund; Uebersicht „Heilpflanze des Jahres 2017" (NHV Theophrastus / Karger 2017); Inhaltsstoffe + Volksanwendung ueber awl.ch, WALA, Phytokodex; Toxizitaets-/Verwechslungseinordnung ueber Giftinformationszentrale Bonn, Gartenjournal.
- **Quellen-Abruf wie in allen Vorlaeufen:** direkter WebFetch der EMA-PDFs und von arzneipflanzenlexikon.info/awl.ch lieferte **HTTP 403**. Inhalte daher ueber WebSearch-Zusammenfassungen mehrerer uebereinstimmender Sekundaerquellen verifiziert. **Primaerquelle EMA/HMPC nicht erreichbar — Löwenzahn-Evidenzgrad (TU) und Posologie am Original aerztlich gegenzupruefen.**

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Löwenzahn ist ein tier-4-Kraut mit ueberraschend solider regulatorischer Basis.** Anders als die meisten Wildkraeuter dieser Stufe hat es eine HMPC-Monographie (radix cum herba, traditional use) — beide Indikationen (1. dyspeptische Beschwerden/Appetitlosigkeit/Gallefluss, 2. Durchspülung der Harnwege) als **TU/ESCOP+** getaggt, KEIN WEU. Bitte den TU-Wortlaut/Posologie am EMA-Original bestaetigen.
- **Löwenzahn — Sicherheitskern ist die Gallenwirkung, nicht Toxizitaet.** Choleretisch → **KONTRAINDIZIERT bei Verschluss der Gallenwege, Gallenblasenempyem, Ileus**; bei Gallensteinen nur nach aerztlicher Ruecksprache (Kolikgefahr). Zusaetzlich Vorsicht bei aktivem Magengeschwuer (Bitterstoffe steigern Magensaft). Analog zur Artischocke. `high_safety` bewusst **false** gesetzt (trotz ungiftiger Pflanze), weil diese KI real sind.
- **Löwenzahn — neues/passendes Flag `cardiorenal_flush_caution=true`** fuer die Durchspülungsanwendung: NICHT bei Oedemen infolge Herz-/Niereninsuffizienz, und nur mit reichlich Trinken. Bitte pruefen, ob das Register dieses Flag so fuehrt (im Schema vorhanden).
- **Löwenzahn — Erwartungsdaempfung:** der populaere Ruf als „Leber-Entgifter"/„Blutreiniger" ist NICHT evidenzgedeckt (nur traditional use). In `overstated`/`key_warning` klargestellt. Kein giftiger Doppelgaenger — alle „falschen Löwenzaehne" (Ferkelkraut, Herbst-Löwenzahn, Wiesen-Pippau) sind essbar; reales Risiko ist Standortbelastung (Nitrat/Schwermetalle/Hundekot), nicht Giftigkeit. Milchsaftprobe als Sammelanker dokumentiert.
- **Gänseblümchen — der eigentliche Befund ist die EVIDENZLUECKE trotz Popularitaet.** „Heilpflanze des Jahres 2017", aber es gibt **keine HMPC/ESCOP/Kommission-E-Monographie und keine klinischen Studien** — alle drei Indikationen (Husten/Expektorans, milde Dyspepsie, aeusserlich als „Arnika des Nordens") sind rein **TRAD** (volksmedizinisch/homoeopathisch). Bewusst so getaggt; bitte nicht auf TU hochstufen.
- **Gänseblümchen — `high_safety=true`, aber mit Vorbehalt im Text.** Sehr sicheres, essbares Wildkraut ohne giftigen Doppelgaenger (unverwechselbare Weiss-Gelb-Blüte am blattlosen Stiel ueber Rosette, kein Milchsaft). Dennoch defensiv vermerkt: die **Triterpensaponine** wirken in **groesseren Rohmengen schleimhaut-/magenreizend** (Faustregel Volksliteratur: ≤10 Blaetter/4 Blüten/Tag) — das ist kein regulatorisches toxin_ceiling, daher `toxin_ceiling=false`, aber im Text/KI benannt. Schwangerschaft/Saeuglinge arzneilich „unsicher — zu pruefen" (ueberlieferte emmenagoge Zuschreibung, keine Daten). `asteraceae_allergy=true` bei beiden Korbblütlern.

**Wunschliste-Status:** unveraendert 1 Eintrag (cornus-sanguinea), bereits erfuellt → `wunschliste.json` NICHT angefasst (nur die App schreibt sie). Nebenbefund aus Lauf 2026-07-15 (11 aeltere Monographien mit Validierungsfehlern) weiterhin offen — nicht Teil dieses Auftrags, eigener Bereinigungslauf empfohlen.

## 2026-07-21 — Vogelmiere, Gundermann (beide KANDIDATEN, tier 4)

**Auswahl (genau 2):** Wunschliste hat Vorrang, ist aber faktisch leer: der einzige Eintrag in `docs/wunschliste.json` — **cornus-sanguinea** (Common dogwood / Blutroter Hartriegel, Fundort Bodensee) — liegt bereits als `fertig/monographie-blutroter-hartriegel.json` (id `cornus-sanguinea`, botany.synonyms Swida/Thelycrania sanguinea) vor → per Dedup uebersprungen (die App hakt den Wunsch selbst ab). Damit 0 offene Wuensche → **beide Plaetze aus der Kandidatenliste**: erste offene Eintraege nach tier aufsteigend. Alle tier 1–3 sind `entwurf_fertig`; erste beide `offen` in tier 4 in Listenreihenfolge = **stellaria-media** (Vogelmiere) und **glechoma-hederacea** (Gundermann).

- **stellaria-media** (Vogelmiere) — `fertig/monographie-vogelmiere.json` — Quelle: Kandidat tier 4. Status → `entwurf_fertig`.
- **glechoma-hederacea** (Gundermann) — `fertig/monographie-gundermann.json` — Quelle: Kandidat tier 4. Status → `entwurf_fertig`.

**Dedup:** beide gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` in der Kandidatenliste geprueft — keine Dublette. Altnamen selbst eingetragen: Vogelmiere = Alsine media L. (Basionym), Stellularia media (L.) Kuntze; Gundermann = Nepeta glechoma Benth., Nepeta hederacea (L.) Trevis., Glechoma hederaceum L. Kein Self-Heal noetig (kein als `offen` markierter Kandidat lag bereits in `fertig/`).

**Pruefergebnis:** beide einzeln UND gemeinsam `✓ ok, mit Hinweisen`, **0 Fehler beim ersten Versuch — 0 Korrekturversuche**. Einziger Hinweis je Datei: enthaelt bewusst „unsicher/zu pruefen". Keine Dubletten-Warnung.

**Hauptquellen:**
- Vogelmiere: KEINE HMPC/ESCOP/Kommission-E-Monographie (mehrfach bestaetigter Negativbefund). Taxonomie via Kew POWO/GBIF (Basionym Alsine media L.). Phytochemie/Pharmakologie (Saponine, Flavonoide, Vitamin C — nur praeklinisch) via Uebersichtsarbeit PMC7284062. Bestimmung/Verwechslung (Haarlinie, elastischer Faden, Acker-Gauchheil, Wolfsmilch) via pflanzen-vielfalt.net, lovethegarden.com, WebSearch-Zusammenfassungen. Toxikologie Acker-Gauchheil via pflanzen-deutschland.de/naturadb.de.
- Gundermann: KEINE HMPC/ESCOP-Monographie; **Kommission E: NEGATIV-Monographie** (Wirksamkeit nicht belegt). Chemie/Pulegongehalt via PMC8949430 + Uebersichten. Verwechslung (Efeu, Kriechender Günsel, Taubnessel) via gruenundgesund.de, flora-emslandia.de, pflanzen-vielfalt.net. Efeu-/Pferdetoxizitaet via tiermedizinportal.de, Gesellschaft fuer Toxikologie.
- **Quellen-Abruf wie in allen Vorlaeufen:** direkter WebFetch scheiterte durchgehend mit **HTTP 403** (Wikipedia de, Henriette's Herbal, plantura, heilpflanzen-lexikon, arzneipflanzenlexikon.info, awl.ch, eatweeds, PMC-Seiten). WebSearch war nutzbar — Recherche vollstaendig ueber WebSearch-Zusammenfassungen mehrerer uebereinstimmender Sekundaerquellen. Primaerquellen (es existieren fuer beide ohnehin KEINE HMPC/ESCOP) nicht abrufbar; die regulatorische Kernaussage „keine Monographie / Kommission E negativ" ist ueber mehrere Sekundaerquellen konsistent belegt, sollte aber aerztlich gegengeprueft werden.

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Gundermann — Kommission-E-NEGATIVmonographie.** Anders als bei den meisten tier-4-Kraeutern wurde Gundelrebenkraut regulatorisch bewertet und die Wirksamkeit ausdruecklich NICHT anerkannt. Alle drei Indikationen bewusst nur **TRAD** getaggt; bitte nicht auf TU/ESCOP+ hochstufen.
- **Gundermann — Pulegon ist der eigentliche Sicherheitspunkt.** Das aetherische Öl enthaelt **Pulegon** (Monoterpenketon, lebertoxisch + abortiv/uterusanregend — dieselbe Substanz, die Poleiminze gefaehrlich macht). Gehalt im Kraut ist gering (Öl < 1/30 der Poleiminze), daher als Küchenwuerze in kleinen Mengen tolerierbar; **konzentriertes aetherisches Öl und grosse/dauerhafte Mengen meiden.** Flags: `toxin_ceiling=true`, `toxin_type: "Pulegon"`, `pregnancy_contraindicated=true`. **Eine offizielle Höchstmenge fuer das KRAUT ist nicht definiert** → `safety.tox_ceiling` bewusst als „unsicher — zu pruefen" markiert (loeste den Validator-Hinweis aus). `hepatotoxic` bewusst auf **false** belassen, weil bei Wuerzmengen die reale Leberbelastung gering ist — falls das Register die Pulegon-Traeger vollstaendig erfassen soll, waere `hepatotoxic=true` zu erwaegen (aerztliche Entscheidung).
- **Gundermann — Zusatzbefund Tierhaltung:** fuer **Pferde** (und Kleinsaeuger wie Meerschweinchen) ist die Pflanze **stark giftig** — relevant, falls im Katalog spaeter ein Weide-/Tierregister entsteht. Im `key_warning` und `contraindications` vermerkt.
- **Gundermann — giftige Verwechslung Efeu.** Der Artname „hederacea" (efeuaehnlich) und der Volksname „Erdefeu" spiegeln eine reale Verwechslungsachse mit dem **giftigen Efeu (Hedera helix)**. Efeu ist aber verholzt/kletternd, ledrig-lappig, wechselstaendig, immergruen und **geruchlos** — die **Geruchsprobe** (Gundermann riecht wuerzig „nach Maggi/Ziege") ist der zuverlaessigste Sammelanker. `deadly_confusion=false` (Efeu ist „giftig", nicht „lebensgefährlich").
- **Vogelmiere — Sicherheit liegt im Sammeln, nicht in der Pflanze.** Die Pflanze selbst ist ein harmloses, sehr vitamin-C-reiches Wildgemuese ohne relevante Eigen-Toxizitaet. Der Sicherheitskern sind **zwei giftige Verwechslungen**, die aktiv dokumentiert wurden: **Acker-Gauchheil** (Lysimachia/Anagallis arvensis — vierkantiger Stängel OHNE Haarlinie, rote Blüten; Saponine/Cyclamin) und **Wolfsmilch-Arten** (Euphorbia — weisser Milchsaft, Diterpenester). Sicherstes Erkennungsmerkmal der Vogelmiere: **einreihige, an jedem Knoten seitenwechselnde Haarlinie + elastischer Zentralfaden + KEIN Milchsaft.**
- **Vogelmiere — `high_safety` bewusst FALSE.** Obwohl die Pflanze essbar und untoxisch ist, wurde `high_safety` NICHT gesetzt, weil giftige Doppelgaenger existieren (SPEC: high_safety = „keine Verwechslung, kein Toxin"). `deadly_confusion=false` bleibt korrekt (keine der Verwechslungen ist „lebensgefährlich", beide nur „giftig"). Erwartungsdaempfung: „Superfood"-Zuschreibungen sind Marketing; der Wert ist nutritiv, nicht arzneilich.

**Wunschliste-Status:** unveraendert 1 Eintrag (cornus-sanguinea), bereits erfuellt → `docs/wunschliste.json` NICHT angefasst (nur die App schreibt sie). Aeltere Nebenbefunde aus Vorlaeufen (Validierungsfehler in Altbestand-Monographien) nicht Teil dieses Auftrags.

## 2026-07-21 (Lauf B) — Knoblauchsrauke, Frauenmantel (beide KANDIDATEN, tier 4)

**Auswahl (genau 2):** Wunschliste hat Vorrang, ist aber faktisch leer: der einzige Eintrag in `docs/wunschliste.json` — **cornus-sanguinea** (Common dogwood, Fundort Bodensee) — liegt bereits als `fertig/monographie-blutroter-hartriegel.json` (id `cornus-sanguinea`, synonyms Swida/Thelycrania sanguinea) vor → per Dedup uebersprungen (die App hakt den Wunsch selbst ab). 0 offene Wuensche → **beide Plaetze aus der Kandidatenliste**. Erste beide `offen` in tier 4 in Listenreihenfolge nach dem letzten Lauf = **alliaria-petiolata** (Knoblauchsrauke) und **alchemilla-vulgaris** (Frauenmantel). (knoblauchsrauke/knoblauchsrauke... die vorherigen offenen tier-4-Eintraege Vogelmiere/Gundermann sind jetzt entwurf_fertig.)

- **alliaria-petiolata** (Knoblauchsrauke) — `fertig/monographie-knoblauchsrauke.json` — Quelle: Kandidat tier 4. Status → `entwurf_fertig`.
- **alchemilla-vulgaris** (Frauenmantel) — `fertig/monographie-frauenmantel.json` — Quelle: Kandidat tier 4. Status → `entwurf_fertig`.

**Dedup:** beide gegen alle `id` + `botany.synonyms` in `fertig/` (79 Dateien) und `vorhanden` in der Kandidatenliste geprueft — keine Dublette. Altnamen selbst eingetragen: Knoblauchsrauke = Alliaria officinalis, Erysimum alliaria, Sisymbrium alliaria, Arabis petiolata; Frauenmantel = keine echten Nomenklatur-Synonyme (apomiktischer Sammelkomplex `Alchemilla vulgaris agg.`), stattdessen `synonym_note` gesetzt und synonyms=[]. Kein Self-Heal noetig.

**Pruefergebnis:** beide gemeinsam `✓ ok, mit Hinweisen`, **0 Fehler beim ersten Versuch — 0 Korrekturversuche.** Einziger Hinweis je Datei: enthaelt bewusst „unsicher/zu pruefen".

**Hauptquellen / Quellen-Abruf:** direkter **WebFetch scheiterte durchgehend mit HTTP 403** (ESCOP ladys-mantle, EMA/HMPC, Wikipedia de, diverse Wildkraeuter-Blogs) — dieselbe Proxy-/Bot-Sperre wie in allen Vorlaeufen. Recherche vollstaendig ueber **WebSearch-Zusammenfassungen** mehrerer uebereinstimmender Sekundaerquellen.
- Knoblauchsrauke: KEINE HMPC/ESCOP/Kommission-E-Monographie (konsistenter Negativbefund). Botanik/Inhaltsstoffe (Sinigrin/Glucosinolate, Vitamin C, zweijaehrig, Bluetezeit April–Juli) via Wikipedia-Zusammenfassung, kostbarenatur.net, plantura.garden, heilkraeuter.de. Verwechslung „drei Herzblaetter" (Scharbockskraut, Gundermann) + Aronstab via t-online, unkraut-liebe.de, essplorer.de (Zusammenfassungen).
- Frauenmantel: **KEIN HMPC-Monograph** (vom HMPC bislang nicht bearbeitet); **ESCOP+** und **Kommission E positiv (1986)** fuer unspezifische leichte Durchfaelle, Tagesdosis 5–10 g. Gerbstoffe 6–8 % (Ellagitannine/Agrimoniin), Flavonoide ~2 % via ESCOP-Zusammenfassung, Altmeyers Enzyklopaedie, heilpflanzen-welt.de, arzneipflanzenlexikon.info.
- **Primaerquellen (EMA/ESCOP) nicht direkt abrufbar — Evidenzgrad ungeprueft, aerztliche Gegenpruefung noetig** (in beiden Dateien in `sources` vermerkt).

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Frauenmantel — gespaltene Evidenz, bitte genau lesen.** Fuer **Durchfall** solide Basis: **ESCOP+ UND Kommission E POSITIV** (adstringierende Gerbstoffe) — anders als bei den meisten tier-4-Kraeutern also regulatorisch anerkannt, aber **kein HMPC**. Die **namensgebende Frauenheilkunde** (Menstruations-/Wechseljahresbeschwerden, „Milchbildung") ist dagegen **rein TRAD und NICHT belegt** — bewusst so getaggt und in `overstated` klargestellt (kein Hormoneffekt, keine Blutungsregulation). Bitte die ESCOP/Kommission-E-Kernaussagen am Original gegenpruefen, da Primaerquelle 403.
- **Frauenmantel — kein giftiger Doppelgaenger.** Das gefaltete, faecher-/mantelfoermige Blatt mit morgendlichen **Guttationstroepfchen** ist unverwechselbar. Verwechslung nur innerhalb des apomiktischen Sammelkomplexes (alle essbar/gleichwertig) bzw. mit dem ebenfalls ungiftigen Alpen-Frauenmantel. `deadly_confusion=false`, aber `high_safety` bewusst **false** gelassen (Gerbstoff-Interaktion mit oralem Eisen + fehlende Schwangerschaftsdaten). Gerbstoff-Eisen-Interaktion (zeitlicher Abstand) ergaenzt.
- **Knoblauchsrauke — Kreuzbluetler, nicht Doldenbluetler.** Wichtig fuer das Verwechslungsregister: die Sammel-Gefahr liegt NICHT bei Schierling & Co., sondern bei den herzblaettrigen Fruehjahrskraeutern. Aktiv dokumentiert: **giftiger Aronstab** (Arum maculatum — glaenzend, ganzrandig, pfeilfoermig, kein Knoblauchgeruch) und **roh giftiges Scharbockskraut** (Ficaria verna — Protoanemonin, glaenzend). Der **Knoblauch-Zerreibetest** ist der eindeutige Sicherheitsanker; kein Doppelgaenger riecht nach Knoblauch. Kein lebensgefaehrlicher Doppelgaenger → `deadly_confusion=false`.
- **Knoblauchsrauke — Vermarktung als „Baerlauch-Alternative".** Da beide nach Knoblauch riechen, wird sie so verkauft. Sie sieht Baerlauch aber NICHT aehnlich (gezaehnte Herzblaetter vs. glatte lanzettliche Baerlauchblaetter). Trotzdem im `confusions`-Eintrag und Changelog der Hinweis auf die toedlichen Baerlauch-Doppelgaenger (Maigloeckchen/Herbstzeitlose) — diese riechen NICHT nach Knoblauch. Alle Indikationen **TRAD** (kein HMPC/ESCOP/Kommission E); Heilwirkung ist volksmedizinisch, Kuechennutzen ist der belegte Wert.

**Wunschliste-Status:** unveraendert 1 Eintrag (cornus-sanguinea), bereits erfuellt → `docs/wunschliste.json` NICHT angefasst (nur die App schreibt sie). Aeltere Nebenbefunde aus Vorlaeufen (Validierungsfehler in Altbestand-Monographien) nicht Teil dieses Auftrags.

---

## Lauf 2026-07-21 (Blutwurz, Gänsefingerkraut)

**Bearbeitete Kräuter (beide aus der KANDIDATENLISTE, tier 4):**
- **Blutwurz** — Potentilla erecta → `fertig/monographie-blutwurz.json`
- **Gänsefingerkraut** — Potentilla anserina → `fertig/monographie-gaensefingerkraut.json`

**Auswahl-Begründung:** Wunschliste (`docs/wunschliste.json`) enthält 1 Eintrag: `cornus-sanguinea`. Dieser liegt bereits als `fertig/monographie-blutroter-hartriegel.json` (id `cornus-sanguinea`) vor → **Wunsch bereits erfüllt, übersprungen** (wunschliste.json NICHT angefasst, schreibt nur die App). Damit 0 offene Wünsche → beide Kräuter aus der Kandidatenliste: erste zwei mit `status: offen`, tier aufsteigend = potentilla-erecta, potentilla-anserina (beide tier 4). Dedup gegen alle `id` + `botany.synonyms` in `fertig/` sowie `vorhanden`: keine Treffer (kriechendes-fingerkraut ist Potentilla reptans, andere Art). Status beider Kandidaten → `entwurf_fertig`, `datei` gesetzt.

**Prüfergebnis:** beide `✓ ok, mit Hinweisen`, **0 Fehler beim ersten Versuch — 0 Korrekturversuche.** Einziger Hinweis je Datei: enthält bewusst „unsicher/zu prüfen".

**Hauptquellen / Quellen-Abruf:** Direkter **WebFetch scheiterte durchgehend mit HTTP 403** (EMA/HMPC Tormentillae rhizoma, ESCOP tormentil, Altmeyers) — dieselbe Proxy-/Bot-Sperre wie in allen Vorläufen. Recherche über **WebSearch-Zusammenfassungen** mehrerer übereinstimmender Sekundärquellen (EMA-Seitenzusammenfassung, ESCOP, Altmeyers Enzyklopädie, Thieme/Planta-Medica-Review PMID 32155655, PMC6272682, PubMed 15440668).

### Überraschungen / unsichere Stellen für den Arzt

- **Blutwurz — ungewöhnlich starke regulatorische Basis für ein tier-4-Kraut.** Anders als die meisten tier-4-Einträge hat die Blutwurz eine **HMPC-Monographie (traditional use)** PLUS Kommission E PLUS ESCOP. Wichtig aus der HMPC: Anwendung **nur bei Erwachsenen**, Durchfall > 3 Tage bzw. Mundschleimhautentzündung > 1 Woche → Arzt. Indikation Durchfall daher `TU/ESCOP+`, Mundschleimhaut `TU`. Höchster Gerbstoffgehalt der heimischen Drogen (15–22 %) → auf nüchternen Magen Magenreizung möglich; Gerbstoff-Eisen-Interaktion (zeitlicher Abstand) vermerkt. `high_safety` bewusst **false** (Magenreizung + fehlende Schwangerschaftsdaten).
- **Blutwurz — Bestimmungssicherheit ist stark, kein giftiger Doppelgänger.** Zwei unabhängige Bestätiger: **VIER gelbe Kronblätter** (fast alle anderen Fingerkräuter haben fünf) UND **blutrot anlaufender Wurzelstock**. Verwechslung nur mit anderen, ungiftigen Potentilla-Arten (schwächere Droge). `deadly_confusion=false`.
- **Gänsefingerkraut — deutlich schwächere Evidenz als der populäre Ruf.** NUR **Kommission E** positiv, **KEIN HMPC, KEIN ESCOP**. Die namensgebende krampflösende Wirkung („Krampfkraut") bei **Menstruationskrämpfen** stützt sich nur auf traditionelle Anwendung + einzelne experimentelle/kleine klinische Daten (PubMed 15440668, alt/schwach) → alle drei Indikationen **TRAD** getaggt, krampflösende Wirkung bewusst als `overstated` markiert. Bitte diese Einordnung prüfen, falls im Katalog eine höhere Erwartung gewünscht ist.
- **Gänsefingerkraut — TAXONOMIE-WARNUNG (bitte ansehen).** Die Art wird in neueren Floren/Datenbanken in die Gattung **Argentina** gestellt: **Argentina anserina (L.) Rydb.** Ich habe `id` als `potentilla-anserina` und `scientific_name` „Potentilla anserina L." belassen (so führt es Pl@ntNet arzneilich noch meist), den neuen Namen als `botany.synonyms`/`synonym_note` eingetragen und als „unsicher — zu prüfen" markiert. **Falls die App/Pl@ntNet bereits auf Argentina anserina umgestellt hat, müsste die id angepasst werden.**
- **Schwangerschaft:** Gänsefingerkraut wegen des traditionellen Uterus-Bezugs (krampflösend/„menstruationsfördernd") vorsichtshalber gemieden; Blutwurz mangels Daten laut HMPC nicht empfohlen. Beide als „unsicher — zu prüfen".
- **Primärquellen (EMA/ESCOP) nicht direkt abrufbar (403)** — Evidenzgrade über Sekundärquellen belegt, in beiden Dateien in `sources` vermerkt. Ärztliche Gegenprüfung der Kernaussagen empfohlen.

**Wunschliste-Status:** unverändert 1 Eintrag (cornus-sanguinea), bereits erfüllt → `docs/wunschliste.json` NICHT angefasst.

---

## 2026-07-21 (Lauf C) — Odermennig, Echtes Mädesüß (beide KANDIDATEN, tier 4)

**Auswahl (genau 2):** Wunschliste hat Vorrang, hat aber 0 offene Einträge: einziger Eintrag in `docs/wunschliste.json` — **cornus-sanguinea** (Common dogwood, Bodensee) — liegt bereits als `fertig/monographie-blutroter-hartriegel.json` (id `cornus-sanguinea`) vor → per Dedup übersprungen (die App hakt den Wunsch selbst ab, `wunschliste.json` NICHT angefasst). 0 offene Wünsche → **beide Plätze aus der Kandidatenliste**: die ersten beiden `offen` nach `tier` aufsteigend (bei gleichem tier Listenreihenfolge) = **agrimonia-eupatoria** (Odermennig, tier 4) und **filipendula-ulmaria** (Echtes Mädesüß, tier 4).

- **agrimonia-eupatoria** (Odermennig) — `fertig/monographie-odermennig.json` — Quelle: Kandidat tier 4. Status → `entwurf_fertig`.
- **filipendula-ulmaria** (Echtes Mädesüß) — `fertig/monographie-maedesuess.json` — Quelle: Kandidat tier 4. Status → `entwurf_fertig`.

**Dedup:** beide gegen alle `id` + `botany.synonyms` in `fertig/` (83 Dateien) und `vorhanden` in der Kandidatenliste geprüft — keine Dublette (auch keine Filename-Kollision). Altnamen selbst eingetragen: Odermennig = Agrimonia officinalis Lam., Agrimonia vulgaris Gray; Mädesüß = Spiraea ulmaria L., Ulmaria palustris Moench, Ulmaria pentapetala Gilib. Kein Self-Heal nötig (kein offener Kandidat lag schon in `fertig/`).

**Prüfergebnis:** beide `✓ ok, mit Hinweisen`, **0 Fehler beim ersten Versuch — 0 Korrekturversuche.** Einziger Hinweis je Datei: enthält bewusst „unsicher/zu prüfen".

**Hauptquellen / Quellen-Abruf:** direkter **WebFetch auf EMA-Primärquellen scheiterte mit HTTP 403** (final assessment report Agrimoniae herba u. a.) — dieselbe Proxy-/Bot-Sperre wie in allen Vorläufen. Recherche über **WebSearch-Zusammenfassungen** mehrerer übereinstimmender Sekundärquellen.
- Odermennig: HMPC **traditional use** (leichter Durchfall innerlich; Mund-/Rachenentzündung Gurgeln; leichte Hautentzündung/kleine Wunden äußerlich) + **Kommission E positiv** (Tagesdosis ~3–6 g) + **ESCOP** (äußerlich Gurgeln/Umschläge). Inhaltsstoffe (Gerbstoffe 4–10 %, Agrimoniin, Flavonoide, Kieselsäure) via Altmeyers, arzneipflanzenlexikon.info, ScienceDirect-Phytochemie-Review 2022. Botanik/Verwechslung via Wikipedia, naturadb.de.
- Mädesüß: HMPC **traditional use** für herba UND flos (unterstützend bei Erkältung; leichte Gelenkschmerzen) + **Kommission E positiv** (Spiraeae flos/herba, Schwitzmittel) + **ESCOP** (Erkältung). Salicylate/Flavonoide/Ellagitannine via PharmaWiki, PTAheute, arzneipflanzenlexikon.info; Botanik via floraweb.de, naturadb.de, plantura.garden.
- **Primärquellen (EMA/ESCOP) nicht direkt abrufbar (403) — Evidenzgrad ungeprüft, ärztliche Gegenprüfung nötig** (in beiden Dateien in `sources` vermerkt).

### Überraschungen / unsichere Stellen für den Arzt

- **Mädesüß — „Aspirin-Pflanze", aber Erwartung dämpfen.** Wegen des Salicylat-Ursprungs (Altname *Spiraea ulmaria* → Namensgeber für Aspirin) wird ein aspirinähnlicher schmerz-/fieber-/gerinnungshemmender Effekt erwartet. Der Salicylatgehalt eines Tees ist aber **gering** → **kein Ersatz für ASS/NSAR**, bewusst als `overstated` markiert. Evidenz nur HMPC **traditional use** (kein WEU). Bitte diese Einordnung gegenprüfen.
- **Mädesüß — sicherheitskritische Salicylat-Flags (bitte lesen).** Trotz Teedosis defensiv aufgenommen: Kontraindikation bei **ASS-/Salicylat-Überempfindlichkeit** und **salicylat-sensitivem Asthma** (Bronchospasmus), **Meiden bei Kindern/Jugendlichen mit fieberhaftem Virusinfekt** (Reye-Syndrom, theoretisch), theoretische Interaktion mit **Gerinnungshemmern**. Alle als „unsicher — zu prüfen" (klinische Relevanz bei Teedosis wahrscheinlich gering). `high_safety` bewusst **false**.
- **Mädesüß — Verwechslung ehrlich gehalten.** Kein giftiger Doppelgänger gleicht in ALLEN Merkmalen; der **Wintergrün-/Mandelgeruch beim Zerreiben** + schaumige cremeweiße Rosaceen-Rispe + ulmenartiges Fiederblatt ist eindeutig. ABER: Mädesüß wächst an nassen Standorten, an denen auch **giftige Doldenblütler (Wasserschierling, Cicuta virosa)** vorkommen — als Fernverwechslungs-Warnung in einem eigenen `confusions`-Eintrag und in den Sammelhinweisen vermerkt (unterscheiden über echte Dolde, geteiltes Blatt, fehlenden Wintergründuft). `deadly_confusion` bleibt `false`, da bei sachgerechter Bestimmung eindeutig.
- **Odermennig — solider regulatorischer Rückhalt für tier 4.** Anders als viele tier-4-Kräuter gleich **dreifach gestützt** (HMPC TU + Kommission E + ESCOP), aber nur symptomatisch-adstringierend. Der populäre Ruf als **„Leberkraut"/Leber-Gallen-Mittel** ist **NICHT belegt** — bewusst als `overstated` markiert. Kein giftiger Doppelgänger.
- **Odermennig — Nebenbefund Photosensibilisierung.** Einzelne Sekundärquellen erwähnen ein theoretisch photosensibilisierendes Potenzial; klinisch nicht belegt, als „unsicher — zu prüfen" in `adverse_effects` vermerkt, kein Flag gesetzt.

**Wunschliste-Status:** unverändert 1 Eintrag (cornus-sanguinea), bereits erfüllt → `docs/wunschliste.json` NICHT angefasst (nur die App schreibt sie).

## 2026-07-22 — Echtes Labkraut, Gemeine Wegwarte

**Auswahl / Quelle:** Wunschliste (`docs/wunschliste.json`) enthielt genau 1 Eintrag: `cornus-sanguinea` (Common dogwood, Bodensee) — dieser liegt bereits in `fertig/` als `monographie-blutroter-hartriegel.json` (id `cornus-sanguinea`, Synonyme Swida/Thelycrania sanguinea). Wunsch also **bereits erfüllt → übersprungen** (App entfernt ihn selbst). Damit 0 offene Wünsche → **beide Kräuter aus der Kandidatenliste**: die zwei ersten offenen Einträge nach tier/Listenreihenfolge = `galium-verum` (Echtes Labkraut) und `cichorium-intybus` (Gemeine Wegwarte), beide tier 4.

**Dedup:** Beide gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` geprüft — keine Kollision (Skript-Scan). Waldmeister (galium-odoratum) ist eine andere Art, kein Konflikt.

**Prüfergebnis:** Beide `✓ ok, mit Hinweisen` (0 Fehler). Einziger Hinweis je: enthält "unsicher/zu prüfen" (bewusst gesetzt). **0 Korrekturversuche** nötig.

**Hauptquellen:**
- Echtes Labkraut (Galium verum): Heilpflanzen-Atlas, AWL.ch, pflanzenfreunde.com, kraeuterleben.de (Volksmedizin); naturadb / arzneipflanzenlexikon (Inhaltsstoffe/Botanik); pflanzen-vielfalt.net, die-honigmacher.de, Wikipedia (Verwechslung Galium mollugo/aparine/odoratum).
- Gemeine Wegwarte (Cichorium intybus): HMPC EU herbal monograph *Cichorium intybus* L., radix (traditional use); Kommission E; Thieme/natuerlich (Heilpflanze des Jahres 2020), AWL.ch, avogel.ch, walaarzneimittel.de, natur-forum.de; scialert/herbalref/Altmeyers (Phytochemie).
- **Quellen-Abruf:** WebFetch auf EMA sowie arzneipflanzenlexikon.info/altmeyers/naturadb lieferte durchgehend HTTP 403 (Sandbox-typisch). Evidenzgrad daher über mehrere übereinstimmende Sekundärquellen belegt — **Primärquelle ungeprüft, ärztliche Gegenprüfung nötig**, insbesondere die exakte HMPC-Indikationsformulierung/Posologie der Wegwartenwurzel.

### Überraschungen / unsichere Stellen für den Arzt

- **Echtes Labkraut hat KEINE regulatorische Grundlage.** Weder HMPC noch ESCOP noch Kommission E führen Galium verum. Alle Indikationen sind bewusst mit `TRAD` getaggt und der `evidence_caveat` sagt das ausdrücklich. Für ein Nachschlagewerk ist das ein Kraut mit sehr schwacher Evidenz — bitte prüfen, ob es überhaupt als "Heilpflanze" (statt nur als botanischer/kulturhistorischer Eintrag) geführt werden soll.
- **Sicherheitsrelevanter Overstatement-Punkt Labkraut:** Im Netz kursiert Galium verum/aparine prominent als angebliches Mittel gegen Lymphstau, Schilddrüsenknoten und **Krebs** ("Galium-/Labkraut-Therapie"). Das ist unbelegt; die eigentliche Gefahr ist die Behandlungsverzögerung. Ich habe das explizit in `expectation_summary.overstated` und `key_warning` adressiert.
- **Namensfalle Labkraut/Waldmeister:** Beide sind Galium. Der coumarinreiche Waldmeister (G. odoratum) ist als eigener Verwechslungseintrag mit Toxin-Hinweis geführt, obwohl Standort (Wald/schattig) und Blütenfarbe (weiß) klar abgrenzen — zur Klarstellung des unterschiedlichen Sicherheitsprofils.
- **Wegwarte — Droge ist die WURZEL, nicht das Kraut:** Die HMPC-Anerkennung (traditional use) gilt für Cichorii radix. Kommission E umfasst Wurzel und Kraut. Habe die Wurzel als Hauptdroge geführt, Kraut ergänzend. `asteraceae_allergy`-Flag gesetzt (Korbblütler). Anwendung laut HMPC ab 12 Jahren.
- **Wegwarte — Zichorienkaffee ≠ Arzneimittel:** Rösten baut die Bitter-Sesquiterpenlactone ab; das Genussgetränk hat nicht die appetit-/verdauungsanregende Amarum-Wirkung. In `kitchen.culinary_vs_medicinal` und `preparation` vermerkt.

### Katalog-Beobachtung (nicht Teil dieses Laufs, aber meldenswert)

Beim Gesamt-Check `validate_monographie.py fertig/*.json` schlagen **11 ältere Dateien** mit FEHLERn auf: baerlauch, beinwell, brennnessel, holunder, johanniskraut, kamille, pfefferminze, ringelblume, salbei, schafgarbe, wermut — augenscheinlich die handkuratierten Erstbestände (`herkunft: "kuratiert"`), die vor der heutigen, strengeren Schema-/Skriptversion entstanden sind (z. B. ungültiger `toxicity_level` "essbar/gering"). Meine beiden neuen Dateien sind fehlerfrei. Ich habe die Altbestände **bewusst nicht angefasst** (außerhalb dieses 2-Kräuter-Laufs; kuratierte Dateien nicht verändern). Empfehlung: separater Wartungslauf, der die kuratierten Monographien an das aktuelle Schema angleicht.

---

## Lauf 2026-07-22 (mittags) — Königskerze, Goldrute

**Auswahl (genau 2):** Wunschliste `docs/wunschliste.json` enthielt 1 Eintrag — `cornus-sanguinea` (Common dogwood, Bodensee). **Bereits erfüllt:** liegt als `fertig/monographie-blutroter-hartriegel.json` (id `cornus-sanguinea`) → übersprungen (App entfernt ihn selbst). Damit 0 offene Wünsche → beide Kräuter aus der **Kandidatenliste**, tier aufsteigend, Listenreihenfolge:
1. **Kleinblütige Königskerze** (Verbascum thapsus) — Kandidat, tier 4 (erster offener Eintrag)
2. **Echte Goldrute** (Solidago virgaurea) — Kandidat, tier 4 (zweiter offener Eintrag)

**Self-Healing:** Skript-Scan aller `fertig/`-`id` gegen die als `"offen"` markierten Kandidaten — keine bereits erledigten Einträge mit falschem Status gefunden, keine Korrektur nötig.

**Dedup:** Beide gegen alle `id` + alle `botany.synonyms` in `fertig/` und gegen `vorhanden` geprüft (Skript-Scan) — keine Kollision. Lateinische Synonyme selbst eingetragen (Königskerze: V. schraderi, Thapsus linnaei; Goldrute: Solidago vulgaris, Doria virgaurea).

**Prüfergebnis:** Beide `✓ ok, mit Hinweisen` (0 Fehler). Einziger Hinweis je: enthält "unsicher/zu prüfen" (bewusst gesetzt). **0 Korrekturversuche** nötig.

**Hauptquellen:**
- Königskerze (Verbasci flos): EMA/HMPC EU herbal monograph V. thapsus/densiflorum/phlomoides, flos (traditional use, 2018); ESCOP Verbasci flos (2014); Kommission E; Sekundär: heilpflanzen-atlas.de, awl.ch, gruenundgesund.de (Verwechslung Fingerhut).
- Goldrute (Solidaginis virgaureae herba): EMA/HMPC Community herbal monograph Solidago virgaurea (EMEA/HMPC/285758/2007, traditional use, 2008); ESCOP; Kommission E; Kołodziej et al., Biomolecules 2020 (Review); Sekundär: arzneipflanzenlexikon.info, pflanzen-vielfalt.net.
- **Quellen-Abruf:** WebFetch auf EMA-PDFs und mehrere Sekundärseiten (altmeyers, arzneipflanzenlexikon, awl.ch, klein-naturarznei) lieferte durchgehend HTTP 403 (Bot-Sperre der Zielserver; Proxy laut Status ok). Evidenzgrad daher über EMA-WebSearch-Treffer + mehrere übereinstimmende Sekundärquellen belegt — **HMPC-Primärtext ungeprüft, ärztliche Gegenprüfung nötig**, insbesondere die wörtliche Indikations-/Posologie-Formulierung.

### Überraschungen / unsichere Stellen für den Arzt

- **Königskerze — tödliche Verwechslung im Rosettenstadium (deadly_confusion=true).** Vor der Blüte ist die Blattrosette mit dem **Roten Fingerhut** (Digitalis, Herzglykoside) verwechselbar. Sicheres Merkmal: Königskerze beidseitig grau-wollig behaart, Fingerhut nur unterseits. In `confusions`, `collection_rules` und `key_warning` deutlich adressiert. Königskerze selbst ist mild — high_safety trotzdem NICHT gesetzt (Widerspruch zu deadly_confusion + Skript fängt das).
- **Königskerze — Aufguss muss gefiltert werden:** die feinen Sternhaare der Blüten reizen ungefiltert den Rachen (können selbst Hustenreiz auslösen). Praxisrelevant, in `solubility_note`, `preparation` und `key_warning`.
- **Goldrute — Evidenz niedriger als der Ruf (Erwartung dämpfen):** Trotz populärem Diuretikum-Image führt die HMPC-Monographie sie NUR als *traditional use* ("Steigerung der Harnmenge"), nicht als WEU. Eingestuft als **TU/ESCOP+** (ESCOP + Kommission E positiv). Bitte den Evidenzgrad gegenprüfen — Regel 2 (Evidenz nicht schönen) war hier einschlägig.
- **Goldrute — giftiger Doppelgänger aktiv gesucht:** **Jakobs-Greiskraut** (Jacobaea vulgaris, Pyrrolizidinalkaloide, hepatotoxisch) ist ein zeit- und standortgleicher gelber Korbblütler. Als `giftig`-Verwechslung mit Unterscheidungsmerkmalen eingetragen (große Zungenblütenkränze + fiederteilige Blätter vs. viele winzige Körbchen). Zusätzlich harmlose, aber pharmazeutisch mindere Neophyten-Goldruten (S. canadensis/gigantea) — deren Droge fehlen die Phenolglykoside.
- **Goldrute — Kontraindikation cardiorenal_flush_caution:** KEINE Durchspülung bei Ödemen infolge Herz-/Niereninsuffizienz; kein Antibiotika-Ersatz bei bakteriellem HWI. Gesetzt und in `key_warning`.

## Lauf 2026-07-22 (nachmittags) — Dornige Hauhechel, Echtes Tausendgüldenkraut

**Auswahl (genau 2):** Wunschliste `docs/wunschliste.json` enthielt 1 Eintrag — `cornus-sanguinea` (Common dogwood, Bodensee). **Bereits erfüllt:** liegt als `fertig/monographie-blutroter-hartriegel.json` (id `cornus-sanguinea`, Synonym-Abgleich bestätigt) → übersprungen (App entfernt ihn selbst). Damit 0 offene Wünsche → beide Kräuter aus der **Kandidatenliste**, tier aufsteigend, Listenreihenfolge:
1. **Dornige Hauhechel** (Ononis spinosa) — Kandidat, tier 4 (erster offener Eintrag)
2. **Echtes Tausendgüldenkraut** (Centaurium erythraea) — Kandidat, tier 4 (zweiter offener Eintrag)

**Self-Healing:** Die als `"offen"` markierten Kandidaten gegen alle `fertig/`-Dateien geprüft — keiner lag bereits fertig vor, kein Status falsch, keine Korrektur nötig.

**Dedup:** Beide gegen alle `id` + alle `botany.synonyms` in `fertig/` und gegen `vorhanden` geprüft — keine Kollision. Lateinische Synonyme selbst eingetragen (Hauhechel: Ononis campestris, O. spinosa subsp. spinosa; Tausendgüldenkraut: Centaurium minus, C. umbellatum, Erythraea centaurium, Gentiana centaurium).

**Prüfergebnis:** Beide `✓ ok, mit Hinweisen` (0 Fehler). Einziger Hinweis je: enthält "unsicher/zu prüfen" (bewusst gesetzt). **0 Korrekturversuche** nötig.

**Hauptquellen:**
- Hauhechel (Ononidis radix): EMA/HMPC EU herbal monograph Ononis spinosa L., radix (EMA/HMPC/138316/2013, traditional use); ESCOP-Monographie Restharrow Root (escop.com); Kommission E; Sekundär: altmeyers.org (Ononidis radix), Wikipedia Dornige/Kriechende Hauhechel (Bestimmung/Artenschwarm), naturadb.de.
- Tausendgüldenkraut (Centaurii herba): EMA/HMPC EU herbal monograph Centaurium erythraea Rafn s.l., herba (EMA/HMPC/277493/2015, traditional use; Assessment EMA/HMPC/277491/2015); Kommission E (positiv, Bundesanzeiger 06.07.1988); ESCOP; Sekundär: pharma4u.de, altmeyers.org, arzneipflanzenlexikon.info, botanik-bochum.de, BArtSchV (Schutzstatus).
- **Quellen-Abruf:** WebFetch lieferte diesen Lauf durchgehend HTTP 403 (EMA-Direktseiten, EMA-PDFs, e-lactancia-Spiegel, sogar de.wikipedia) — dasselbe Muster wie in den Vorläufen. Recherche daher über WebSearch (liefert inhaltsreiche Treffer-Zusammenfassungen inkl. EMA-Dokumenten) + mehrere übereinstimmende Sekundärquellen. **HMPC-Primärtext ungeprüft, ärztliche Gegenprüfung nötig**, insbesondere wörtliche Indikations-/Posologie-Formulierung und die TU-Einstufung.

### Überraschungen / unsichere Stellen für den Arzt

- **Tausendgüldenkraut — besonders geschützt (BArtSchV):** Die Art darf in Deutschland NICHT wild gesammelt werden; Droge nur aus Anbau/Handel. In `collection_rules`, `key_warning` und den confusions vermerkt. Auch die verwandten C. pulchellum/littorale stehen unter Schutz — die „Verwechslung" ist hier eher rechtlich als toxikologisch.
- **Tausendgüldenkraut — kein „Leber-/Fieber-/Blutzuckermittel":** trotz alter Namen (Fieberkraut) und kursierender Ansprüche ist es ein reines Bittermittel; solche Wirkungen sind unbelegt (bewusst als `overstated`). Kontraindikation Magen-/Darmgeschwür (Säureanregung) → `reflux_caution` gesetzt. Wirkt nur ungesüßt/vor der Mahlzeit (Bittergeschmack).
- **Hauhechel — Evidenz niedriger als der Ruf (Erwartung dämpfen):** HMPC führt sie nur als *traditional use*; die diuretische Belegkette stammt überwiegend aus alten Tierversuchen (1930er/40er). Eingestuft als **TU/ESCOP+** (ESCOP-Monographie + Kommission E positiv). Kein Antiinfektivum, kein Antibiotika-Ersatz — in `overstated`/`realistic_expectation`/`key_warning` adressiert. Regel 2 (Evidenz nicht schönen) einschlägig.
- **Hauhechel — Dornen sind KEIN sicheres Bestimmungsmerkmal:** Ononis spinosa und die ungiftige, arzneilich gleichwertige Ononis repens bilden einen Artenschwarm mit Hybriden; dornenlose Formen von „spinosa" existieren. Trennung eher über Wuchs (aufrecht vs. kriechend) und Blattform. Kein giftiger Doppelgänger — confusions dennoch aktiv gefüllt (inkl. expliziter „keine giftige Verwechslung bekannt"-Eintrag mit Begründung).
- **Hauhechel — Kontraindikation cardiorenal_flush_caution:** KEINE Durchspülung bei Ödemen infolge Herz-/Niereninsuffizienz; ausreichende Flüssigkeitszufuhr nötig. Gesetzt und in `key_warning`.
- **Nebenbefund außerhalb des Auftrags (nur zur Kenntnis, NICHT verändert):** Eine Voll-Validierung `validate_monographie.py fertig/*.json` meldet aktuell ~38 Fehler in ÄLTEREN, bereits abgelieferten Monographien (nicht in den beiden neuen). Meine zwei Dateien sind fehlerfrei. Da der Auftrag strikt „genau 2" lautet und Fremddateien nicht anzufassen sind, wurde hier nichts korrigiert — sollte aber in einem eigenen Lauf geprüft werden.

## 2026-07-22 — Silberweide, Hänge-Birke (beide KANDIDATEN, Tier 4)

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` enthält 1 Eintrag: **cornus-sanguinea** (Common dogwood) — liegt aber bereits als `fertig/monographie-blutroter-hartriegel.json` (id `cornus-sanguinea`, Synonyme *Swida sanguinea*/*Thelycrania sanguinea*) in `fertig/`. Per Dedup übersprungen → **0 offene Wünsche**. Beide Plätze daher aus der Kandidatenliste: die ersten beiden offenen Einträge, niedrigste tier zuerst = beide Tier 4 in Listenreihenfolge:
- **salix-alba** (Silberweide) — `fertig/monographie-silberweide.json` — Quelle: Kandidatenliste. Status → `entwurf_fertig`.
- **betula-pendula** (Hänge-Birke) — `fertig/monographie-birke.json` — Quelle: Kandidatenliste. Status → `entwurf_fertig`.

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` in der Kandidatenliste geprüft — keine Dublette. Altnamen eingetragen: Silberweide = keine (S. alba akzeptiert; synonym_note zur Mehrarten-Droge); Birke = *Betula verrucosa*, *Betula alba* (in `botany.synonyms`). Kein Self-Heal nötig: kein als „offen" markierter Kandidat lag bereits in `fertig/`.

**Prüfergebnis:** beide einzeln UND gemeinsam bestanden, **0 Fehler beim ersten Versuch — 0 Korrekturversuche**. Silberweide `✓ alles sauber`; Birke 1 Hinweis (enthält bewusst „unsicher — zu prüfen").

**Hauptquellen:**
- Silberweide: EMA/HMPC EU herbal monograph *Salix* [various species], cortex (2017); ESCOP Salicis cortex; Kommission E; MSKCC/USP Safety Review of Willow Bark (2019); RCT Chrubasik 2000 / Schmid 2001.
- Birke: EMA/HMPC EU herbal monograph *Betula pendula/pubescens*, folium (traditional use, 2015); ESCOP Betulae folium; Kommission E; Arzneipflanzen-Lexikon/PharmaWiki/AWL.ch (Inhaltsstoffe, Kontraindikationen).
- **Quellen-Abruf wie in allen Vorläufen:** Direkter WebFetch der EMA-Seiten und altmeyers.org lieferte erneut **HTTP 403**. Inhalte daher über WebSearch-Zusammenfassungen mehrerer übereinstimmender Sekundärquellen verifiziert. **Bitte die exakte HMPC-Einstufung, Posologie-Zahlen und Extrakt-Spezifikationen (DER, Salicingehalt) gegen die Original-Monographien prüfen.**

### Überraschungen / unsichere Stellen für den Arzt

- **Silberweide — der Warteschlangen-`reason` („Salicin — ASS-Ursprung; Schmerz") unterschätzt die Evidenzstufe: Salicis cortex hat WELL-ESTABLISHED USE.** Die HMPC führt für leichte Rückenschmerzen tatsächlich WEU — ABER nur für den quantifizierten, auf Salicin standardisierten Trockenextrakt (DER 8–14:1, Ethanol 70 %, 240 mg Gesamtsalicin/Tag, Erwachsene). Gelenkschmerz/rheumatisch = TU/ESCOP+, Fieber/Erkältung/Kopfschmerz = TU. Wie bei Baldrian/Rosskastanie ist WEU also **zubereitungsgebunden** — Rindentee bleibt traditional use. Ich habe die Rückenschmerz-Indikation als `WEU/ESCOP+` getaggt. **Bitte bestätigen, ob der Katalog Weidenrinde als WEU-Eintrag führen soll (dann ist es der zweite echte WEU-Fall der Tier-4-Riege).**
- **Silberweide — botanische Falle: gerade S. alba ist salicin-ARM.** Die HMPC-Droge stammt aus MEHREREN Weidenarten; die salicinreichen Arzneiextrakte kommen v. a. aus *S. daphnoides*/*S. purpurea*, während die namensgebende „Weidenrinde" S. alba eher wenig Salicin enthält. Ein Pl@ntNet-Treffer „Salix alba" ist also nicht automatisch eine wirksame Droge. Ausführlich in `synonym_note`, `confusions` und `chemistry`. Bitte prüfen, ob die App den Nutzer auf diese Art-/Gehaltsfrage hinweisen soll.
- **Silberweide — Salicylat-Charakter ist sicherheitskritisch, nicht die Pflanze.** Kein giftiger Doppelgänger (nur andere Weiden/Pappeln, alle ungiftig) → expliziter „keine lebensgefährliche Verwechslung"-Eintrag, `deadly_confusion=false`. Dafür `pregnancy_contraindicated=true` und `interaction_heavy=true` (Antikoagulanzien/Warfarin, Methotrexat, NSAR) gesetzt; Kontraindikationen wie ASS inkl. **Kinder/Jugendliche <18 (Reye-Syndrom)** und Analgetika-Asthma. `high_safety` bewusst **false**. Zugleich: Weidenrinde ist KEIN kardiovaskulärer ASS-Ersatz (kaum irreversible Thrombozytenhemmung) — in `overstated`/`mechanism` betont.
- **Birke — reiner traditional use, keine WEU/Studienevidenz.** HMPC nur „Durchspülung als Adjuvans bei leichten Harnwegsbeschwerden" (TU/ESCOP+, Kommission E); rheumatische Indikation nur `TRAD` (Kommission E, HMPC nennt sie nicht). Populäre „Entschlackung/Blutreinigung/Nierenstein-Auflösung" ausdrücklich als unbelegt in `overstated`.
- **Birke — die eine harte Kontraindikation: Durchspülung bei kardialer/renaler Ödem-Ursache.** Neues, passendes Flag `cardiorenal_flush_caution=true` gesetzt (statt Behelfslösung). Zusätzlich Birkenpollen-Kreuzallergie und Pflicht zur hohen Trinkmenge in `key_warning`. Kein toxisches Ceiling, aber `high_safety` bewusst **false** wegen dieser Kontraindikation + Allergiepotenzial.
- **Birke — Taxonomie-Hinweis für die Pl@ntNet-Zuordnung:** `Betula verrucosa` = reines Synonym von B. pendula; der alte Sammelname `Betula alba` ist heute mehrdeutig (auf B. pendula UND B. pubescens aufgeteilt) und wurde nur in `botany.synonyms`/`synonym_note` dokumentiert. Die Droge Betulae folium ist artübergreifend (B. pendula + B. pubescens + Hybriden) gleichwertig — die App sollte beide Arten auf brauchbare Blattdrogen abbilden.

## Lauf 2026-07-23 — Weinrebe, Weißer Gänsefuß (beide Wunschliste)

**Quelle/Auswahl:** `docs/wunschliste.json` hatte 3 offene Einträge; nach Vorrang-Regel die ersten 2 genommen: **vitis-vinifera** (Weinrebe) und **chenopodium-album** (Weißer Gänsefuß). Der 3. Wunsch (platanus-hispanica, Platane) bleibt offen für den nächsten Lauf. Da beide aus der Wunschliste stammen, wurde `kraeuter-kandidaten.json` NICHT geändert (Statuspflege nur für Kandidaten-Kräuter). Kein Self-Heal nötig.

- **vitis-vinifera** (Weinrebe) — `fertig/monographie-weinrebe.json` — Quelle: Wunschliste.
- **chenopodium-album** (Weißer Gänsefuß) — `fertig/monographie-weisser-gaensefuss.json` — Quelle: Wunschliste.

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` in der Kandidatenliste geprüft — keine Dublette (Treffer wie „Vaccinium vitis-idaea", „Gingivitis", „Hundszahngras" waren False Positives). Beide Arten neu im Katalog. Botanische Altnamen: Weinrebe = keine Umbenennung (V. vinifera akzeptiert; Hinweis auf var. tinctoria/rotes Weinlaub in `synonym_note`); Gänsefuß = keine Art-Umbenennung, aber Familienwechsel Chenopodiaceae→Amaranthaceae in `synonym_note`. `botany.synonyms` bei beiden leer.

**Prüfergebnis:** beide gemeinsam bestanden, **0 Fehler beim ersten Versuch — 0 Korrekturversuche**. Weinrebe: 1 `! Hinweis` (enthält bewusst „unsicher — zu prüfen" bei Pharmakokinetik). Gänsefuß: `✓ alles sauber`.

**Hauptquellen:**
- Weinrebe: EMA/HMPC EU herbal monograph *Vitis vinifera* L., folium (WEU bei CVI; traditional use) + Assessment Report; ESCOP Vitis viniferae folium; RCTs zu AS 195 (Kiesewetter 2000, Rabe 2011); PTAheute/DAZ/Sekundärliteratur (Posologie 360–720 mg, Nebenwirkungen, Schwangerschaft).
- Gänsefuß: keine HMPC-/ESCOP-/Kommission-E-Monographie (Status verifiziert); ethnobotanische Wildgemüse-Literatur; toxikologische Fallberichte zur Datura-/Solanum-Keimlingsverwechslung; Fachangaben zu Oxalat/Nitrat/Saponinen.
- **Quellen-Abruf wie in allen Vorläufen:** Direkter WebFetch der EMA-Seiten, fitoterapia.net, e-lactancia.org, mdpi.com und altmeyers.org lieferte erneut **HTTP 403** (nicht über die Sandbox-Allowlist, sondern origin-seitige Bot-Sperre). Primärquelle nicht abrufbar — Inhalte daher über mehrere übereinstimmende WebSearch-Sekundärquellen verifiziert. **Bitte die exakte HMPC-Einstufung (WEU) sowie Posologie-/Extraktangaben (DER 4–6:1 Wasser, AS 195, 360–720 mg) für Weinrebe gegen die Original-HMPC-Monographie gegenprüfen.**

### Überraschungen / unsichere Stellen für den Arzt

- **Weinrebe — der eigentliche Wirkstoffträger ist das BLATT, nicht die Traube.** Der Wunschlisten-Eintrag („Grape Vine", Merkposten) legt die Frucht nahe; die belegte Evidenz betrifft aber ausschließlich das *rote Weinlaub* (Folium, wässriger Trockenextrakt AS 195). Ich habe die CVI-Indikation als `WEU/RCT` getaggt (HMPC well-established use, gestützt durch RCTs). **Sicherheitskritische Erwartungsfalle:** Rotes Weinlaub ≠ Traubenkernextrakt/OPC ≠ Rotwein/Resveratrol — in `overstated`, `confusions` und `chemistry` deutlich getrennt. Für die Pl@ntNet-Zuordnung relevant: ein Foto einer fruchtenden Rebe führt zwar korrekt auf *Vitis vinifera*, meint aber nicht automatisch die Arzneidroge.
- **Weinrebe — Thrombose-Abgrenzung als key_warning.** Weil die Zielsymptomatik (Beinödem/-schwellung) sich mit einer tiefen Beinvenenthrombose überschneidet, ist die zentrale Warnung: plötzliche, einseitige, schmerzhafte/überwärmte Schwellung = ärztlich abklären, nicht selbst behandeln. `high_safety` bewusst **false** (echte vaskuläre Indikation, Schwangerschaft nicht empfohlen), obwohl das Präparat sonst gut verträglich ist.
- **Weißer Gänsefuß — es ist KEINE Heilpflanze, sondern ein Wildgemüse.** Weder HMPC noch ESCOP noch Kommission E führen ihn (Status ausdrücklich verifiziert). Damit die Nicht-Warneintrag-Struktur valide bleibt, sind die `indications` bewusst als `TRAD` gesetzt und im `realistic_expectation`/`overstated` klar als unbelegt/volksmedizinisch entwertet. **Falls der Katalog rein essbare Wildpflanzen anders behandeln soll (z. B. Küchen-Tag statt Pseudo-Indikation), bitte redaktionell entscheiden.**
- **Weißer Gänsefuß — die gefährliche Verwechslung ist der Keimling, nicht die adulte Pflanze.** Junge Datura- (lebensgefährlich, Tropanalkaloide) und Solanum-nigrum-Keimlinge (giftig) wachsen im selben stickstoffreichen Garten-/Ruderalboden und sind vor Blüte/Frucht leicht mit essbaren Gänsefuß-/Meldeblättern zu verwechseln (dokumentierte Vergiftungen). `deadly_confusion=true` gesetzt; sicheres Feldmerkmal ist die mehlig-weiße Bestäubung + Geruchsneutralität. Bitte diese Verwechslung (Datura↔essbare Melden) im Register prüfen — sie betrifft potenziell auch die schon vorhandenen essbaren Wildkräuter.
- **Weißer Gänsefuß — zwei zusätzliche Fallen:** (1) Nitrat-AKKUMULATOR auf gedüngten Böden (Säuglinge!) und Oxalsäure/Samen-Saponine → roh nur in Maßen, blanchieren; (2) NAMENSFALLE: der giftige „Wurmsamen"/Chenopodiumöl stammt von *Dysphania ambrosioides* (früher *Chenopodium ambrosioides/anthelminticum*, Ascaridol) — NICHT vom essbaren *C. album*. Als eigener `confusions`-Eintrag dokumentiert. Botanisch ist C. album ein naher Verwandter der Quinoa (*Chenopodium quinoa*).

## Lauf 2026-07-23 (2. Lauf des Tages) — Stieleiche (Kandidat), Platane (Wunschliste)

**Quelle/Auswahl:** `docs/wunschliste.json` hatte noch 3 Einträge, davon aber nur **1 offen**: vitis-vinifera und chenopodium-album lagen bereits in `fertig/` (als `monographie-weinrebe.json` bzw. `monographie-weisser-gaensefuss.json`, IDs `vitis-vinifera`/`chenopodium-album` bestätigt) → per Regel übersprungen. Offen blieb **platanus-hispanica** (Platane) → gebaut. Für den 2. Platz „genau 2" den ersten offenen Kandidaten aus `kraeuter-kandidaten.json` genommen: niedrigste offene tier ist 4, erster `"offen"`-Eintrag in Listenreihenfolge = **quercus-robur** (Stieleiche).

- **platanus-hispanica** (Gewöhnliche Platane) — `fertig/monographie-platane.json` — Quelle: **Wunschliste**. Wunschliste NICHT verändert (macht die App).
- **quercus-robur** (Stieleiche) — `fertig/monographie-stieleiche.json` — Quelle: **Kandidatenliste** (tier 4). Status → `entwurf_fertig`, `datei` gesetzt.

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` in der Kandidatenliste geprüft. Weder `quercus-robur`/`Quercus robur`/`Quercus pedunculata` noch `platanus-hispanica`/`Platanus × hispanica`/`Platanus × acerifolia` bereits vorhanden. Skript-Dublettencheck über alle `fertig/*.json`: **keine Dubletten**. `botany.synonyms` selbst gesetzt (Eiche: `Quercus pedunculata`; Platane: `Platanus × acerifolia`, `Platanus × hybrida`). Kein Self-Heal nötig (kein als „offen" markierter Kandidat lag schon in `fertig/`).

**Prüfergebnis:** beide bestanden, **0 Fehler beim ersten Versuch — 0 Korrekturversuche**. Stieleiche: 1 `! Hinweis` (bewusstes „unsicher — zu prüfen" bei Pharmakokinetik/Schwangerschaft). Platane: 2 `! Hinweis` (leere `harvest_month_tags` — GEWOLLT, keine arzneiliche Ernte; + bewusstes „unsicher — zu prüfen").

**Hauptquellen:**
- Stieleiche/Eichenrinde: EMA/HMPC Community herbal monograph *Quercus robur/petraea/pubescens*, cortex (EMA/HMPC/3203/2009, traditional use) + Assessment Report; Kommission E (Bundesanzeiger 01.02.1990); ESCOP Quercus cortex; PharmaWiki/Arzneipflanzen-Lexikon/PTA-Forum (Gerbstoffgehalt 8–20 %, Posologie, Interaktion).
- Platane: Lexikon der Arzneipflanzen und Drogen (Spektrum, Platanus-Arten); aha! Allergiezentrum Schweiz + Dt. Allergiekongress/medical-tribune (Platanenhusten/Trichome); polleninformation.at (Pla a 1); Botanikus/Wikipedia (Ungiftigkeit, Ahorn-Abgrenzung).
- **Quellen-Abruf wie in allen Vorläufen:** Direkter WebFetch der EMA-, fitoterapia.net-, altmeyers.org-, arzneipflanzenlexikon.info- und spektrum.de-Seiten lieferte erneut durchgehend **HTTP 403** (origin-seitige Bot-Sperre, nicht die Sandbox-Allowlist). Primärquellen (HMPC/ESCOP im Volltext) nicht direkt abrufbar — Inhalte über mehrere übereinstimmende WebSearch-Sekundärquellen verifiziert. **Bitte für die Eichenrinde die exakte HMPC-Einstufung (traditional use, innerlich Durchfall + äußerlich Mund/Rachen/Haut/Hämorrhoiden) und die Posologie-Zahlen (Durchfall ~3 g/Tag, Gurgeln 2 g/100 ml, Bad 5 g/L; Dauergrenzen 3–4 Tage innerlich / 2–3 Wochen äußerlich) gegen die Original-Monographie gegenprüfen.**

### Überraschungen / unsichere Stellen für den Arzt

- **Stieleiche — solider TU/ESCOP+-Eintrag, aber mit drei harten Grenzen, die im Feld leicht übersehen werden.** (1) Innerlich max. 3–4 Tage, Arztpflicht bei Durchfall >2 Tage / Blut / Fieber; (2) äußerlich max. 2–3 Wochen; (3) **keine Vollbäder** bei großflächigen Hautschäden, Fieber, Herzinsuffizienz (NYHA III/IV) oder schwerem Bluthochdruck (Kreislaufbelastung durchs Bad). Alles in `safety`/`key_warning` gesetzt, `high_safety` bewusst **false**.
- **Stieleiche — Gerbstoff-Interaktion ist real, aber „gering–relevant", nicht „heavy".** Gerbstoffe fällen Alkaloide/basische Arzneistoffe/Eisen im Darm → Resorptionsminderung; Empfehlung „zeitlicher Abstand zu oralen Medikamenten". Als `pharmakokinetisch` getaggt; `interaction_heavy=false` gelassen (kein CYP/Transporter-Mechanismus). Bitte einordnen, ob das Register das trotzdem führen soll.
- **Stieleiche — Drogenquelle vs. Pl@ntNet:** Offizinell sind **Q. robur, Q. petraea, Q. pubescens gleichwertig** (Rinde JUNGER Zweige, nicht die Stammborke). Die nordamerikanische **Rot-Eiche (Q. rubra) gehört NICHT** zur Droge — als eigener `confusions`-Eintrag dokumentiert, damit ein Pl@ntNet-„Quercus rubra"-Treffer nicht fälschlich als Eichenrinde durchgeht. Rohe **Eicheln** (Frucht) sind gerbstoffbedingt roh unbekömmlich (Wässern/Rösten) — betrifft aber nicht die Rindendroge.
- **Platane — bewusste Struktur-Entscheidung, bitte redaktionell bestätigen:** Die Platane ist **keine Heilpflanze** (weder HMPC/ESCOP/Kommission E). Sie ist aber auch **kein Giftpflanzen-Warneintrag** (tier 3, `not_for_use`) — sie ist für den Menschen **ungiftig**. Daher habe ich sie als normale Monographie mit **einer einzigen `TRAD`-`indications`-Zeile** angelegt, die nur die **obsolete historische Rindenanwendung** dokumentiert und im `realistic_expectation` ausdrücklich **jede Anwendung ablehnt**. So bleibt die Nicht-Warneintrag-Struktur schema-valide (leeres `indications` wäre nur bei `not_for_use` erlaubt). **Falls der Katalog „Bestimmungs-/Warn-nur"-Einträge für ungiftige Nicht-Heilpflanzen anders behandeln soll, bitte entscheiden.**
- **Platane — der Sicherheitskern ist NICHT Gift, sondern mechanische Reizung + Allergie.** „Platanenhusten": die feinen, spitzen **Sternhaare/Trichome** von jungen Blättern, Knospen und **zerfallenden Fruchtkugeln** reizen Atemwege, Augen und Haut — v. a. **Frühsommer** und bei **beruflicher Exposition (Baumpflege)**; zusätzlich **Pollenallergen Pla a 1** im Frühjahr. Es gibt **kein passendes Flag** für „mechanisch-irritative Trichome/Pollenallergie" im Schema — der Hinweis steckt daher nur in `key_warning`/`adverse_effects`/`contraindications`. **Ggf. ein neues Flag (z. B. `mechanical_irritant`/`pollen_allergen`) erwägen.**
- **Platane — Bestimmungsfalle Ahorn:** ständige Verwechslung „ahornblättrig"; sicheres Trennmerkmal ist die **WECHSELSTÄNDIGE** Blattstellung (Ahorn gegenständig) plus abblätternde Tarnfleck-Rinde und hängende Fruchtkugeln (Ahorn: geflügelte Spaltfrüchte). Als `confusions`-Eintrag dokumentiert; alle Ahorne für Menschen ungiftig, `deadly_confusion=false`.

## Lauf 2026-07-23 (3. Lauf des Tages) — Walnuss (Kandidat), Winterlinde (Kandidat)

**Auswahl / Quelle:** `docs/wunschliste.json` enthielt 3 Einträge (vitis-vinifera, chenopodium-album, platanus-hispanica) — **alle drei bereits in `fertig/` vorhanden** (als weinrebe, weisser-gaensefuss, platane; IDs bestätigt). Wunschliste damit **ohne offenen Eintrag** → beide Plätze aus der **Kandidatenliste** gefüllt: die ersten beiden `"status": "offen"`-Einträge in Listenreihenfolge, beide **Tier 4** — **juglans-regia (Walnuss)** und **tilia-cordata (Winterlinde)**.

**Deduplikation:** Beide gegen alle `id` + `botany.synonyms` in `fertig/` und gegen `vorhanden` geprüft — keine Dublette (auch nicht unter Synonym). `_dupe_check` über alle `fertig/`-Dateien meldet für beide keine Kollision. Synonyme selbst eingetragen (Juglans: duclouxiana/fallax/sinensis/orientis; Tilia: parvifolia/ulmifolia/sylvestris).

**Prüfergebnis:** Beide `✓ ok, mit Hinweisen` (**0 Fehler, 0 Korrekturversuche**). Einziger Hinweis je Datei: enthält "unsicher/zu prüfen" (bewusst gesetzt). — Nebenbefund: `validate_monographie.py fertig/*.json` liefert Exit 1 wegen **vorbestehender** Fehler in Alt-Dateien (`monographie-baerlauch.json`: `lebensgefaehrlich` statt `lebensgefährlich`, fehlende `note`-Felder; `monographie-beinwell.json`: `null` in chemistry/preparation). **Nicht Teil dieses Laufs** — nur zur Kenntnis; ggf. eigener Reparaturlauf.

**Hauptquellen:**
- Walnuss: EMA/HMPC EU herbal monograph *Juglans regia* L., folium (2013, EMA/HMPC/346737/2011) — traditional use, äußerlich; Kommission E; ESCOP. Inhaltsstoffe/Dosierung über Arzneipflanzenlexikon / PharmaWiki / AWL.ch. Verwechslungs-Recherche (Götterbaum/Esche) über neobiota-NRW, Baumportal, botanik-bochum.
- Winterlinde: EMA/HMPC EU herbal monograph *Tilia cordata / platyphyllos / × vulgaris*, flos — traditional use (Erkältung); Kommission E. Inhaltsstoffe/Dosierung über PharmaWiki / Arzneipflanzenlexikon; Arten-Unterscheidung über LWF Bayern / Baumkunde.
- **Hinweis Quellen-Abruf:** Die EMA-/ESCOP-Primärdokumente lieferten beim direkten WebFetch durchgängig **HTTP 403** (Serverseitig, nicht Proxy — `recentRelayFailures` leer). Inhalte daher über WebSearch-Zusammenfassungen und Fach-/Mirror-Quellen verifiziert; kein Ausweichen auf curl. **Evidenzgrade (TU) und Posologie sollten vom Arzt gegen die Original-Monographien geprüft werden** — im JSON jeweils in `pharmacology.evidence_caveat` vermerkt.

### Überraschungen / unsichere Stellen für den Arzt

- **Walnuss — die Arznei ist rein ÄUSSERLICH.** HMPC/Kommission E führen ausschließlich das **Blatt** (Juglandis folium) als adstringierende Gerbstoffdroge zur **äußerlichen** Anwendung (leichte Hautentzündungen; übermäßiges Schwitzen an Händen/Füßen, als Abkochung 4–6 g/200 ml, Umschlag/Teilbad, max. ~1 Woche, nicht auf offene Wunden). `flags.topical_only=true`. Die populären **innerlichen** Anwendungen (Entwurmung, "Blutreinigung", Diabetes) sind **nicht belegt** — bewusst in `expectation_summary.overstated`.
- **Walnuss — sicherheitsrelevante Verwechslung Götterbaum (*Ailanthus altissima*).** Beide wechselständig gefiedert; der invasive Götterbaum ist zwar nicht tödlich, sein **Saft löst aber Kontaktdermatitis** aus (als `giftig` eingetragen, `deadly_confusion=false`). Sicherstes Feldmerkmal: **aromatischer Geruch** der zerriebenen Walnussblätter (Ailanthus riecht unangenehm) + **ganzrandige** Fiederblättchen (Ailanthus: einige drüsige Zähne am Grund, 11–25 Blättchen). Zusätzlich Esche (gegenständig!) und Eberesche (gesägt) als harmlose Verwechsler dokumentiert. Kein tödlicher Doppelgänger.
- **Winterlinde — die "schweißtreibende" Wirkung ist UMSTRITTEN.** Für die Diaphorese wurde **kein verantwortlicher Inhaltsstoff** identifiziert; der Schwitzeffekt beruht wohl auf dem **heiß getrunkenen Tee**, nicht auf einer Arzneiwirkung. Deshalb: Erkältungs-Indikation als `TU` (HMPC + Kommission E), die separate "Schwitzkur"-Zeile bewusst nur `TRAD` — und der Vorbehalt in `evidence_caveat` + `overstated`. Ebenfalls in `overstated`: eine nachweisbare **sedierende/schlaffördernde** Wirkung fehlt (populäre Zuschreibung).
- **Winterlinde — Droge artenübergreifend, aber NICHT Silberlinde.** Tiliae flos stammt gleichwertig von **T. cordata, T. platyphyllos, T. × vulgaris**; die **Silberlinde (T. tomentosa)** gehört NICHT zur offiziellen Droge (silbrig-filzige Blattunterseite) — als Verwechslung/Sammelhinweis dokumentiert (Nektar für Bienen/Hummeln vermutlich unbekömmlich; für Menschen nicht als giftig belegt → `essbar` mit Warnhinweis). Kein tödlicher Doppelgänger; das mit dem Blütenstiel verwachsene **zungenförmige Hochblatt** macht die Blüte nahezu unverwechselbar → `flags.high_safety=true`.
- **Taxonomie-Notiz Linde:** Familie heute **Malvaceae** (früher Tiliaceae) — im `synonym_note` vermerkt, damit die Familienangabe nicht als Fehler gelesen wird.

## Lauf 2026-07-23 (4. Lauf des Tages) — Hunds-Rose (Kandidat), Schlehe (Kandidat)

**Auswahl / Quelle:** `docs/wunschliste.json` enthielt weiterhin 3 Einträge (vitis-vinifera, chenopodium-album, platanus-hispanica) — **alle drei bereits in `fertig/` vorhanden** (als weinrebe, weisser-gaensefuss, platane; IDs + scientific_name bestätigt). Wunschliste damit **ohne offenen Eintrag** → beide Plätze aus der **Kandidatenliste** gefüllt: die ersten beiden `"status": "offen"`-Einträge, sortiert nach `tier` aufsteigend, in Listenreihenfolge — beide **Tier 4**: **rosa-canina (Hunds-Rose)** und **prunus-spinosa (Schlehe)**.

**Deduplikation:** Beide gegen alle `id` + `botany.synonyms` in `fertig/` und gegen `vorhanden` geprüft — keine Dublette (auch nicht unter Synonym). Synonyme selbst eingetragen (Rosa: R. lutetiana + Hinweis auf die schwierige Caninae-Sektion; Prunus: keine gebräuchlichen Altnamen, dafür Hybrid-Hinweis Prunus × fruticans / Haferschlehe).

**Status:** rosa-canina + prunus-spinosa in `kraeuter-kandidaten.json` auf `entwurf_fertig` gesetzt, `datei` eingetragen. **NICHT** `geprueft` (bleibt dem Arzt).

**Prüfergebnis:** Beide `✓ ok, mit Hinweisen` (**0 Fehler, 0 Korrekturversuche**). Einziger Hinweis je Datei: enthält "unsicher/zu prüfen" (bewusst gesetzt).

**Hauptquellen:**
- Hunds-Rose: ESCOP-Monographie *Rosae pseudofructus* (positiv); Christensen R et al., *Osteoarthritis Cartilage* 2008 (Meta-Analyse, 3 RCTs, 287 Pat.); GOPO-Isolierung (Larsen/Winther). Inhaltsstoffe/Botanik über Arzneipflanzenlexikon, Altmeyers Enzyklopädie, baumkunde.de, pflanzen-vielfalt.net, garten-wissen.com.
- Schlehe: Kommission E **Negativmonographie** Pruni spinosae flos; HMPC-Bewertung eingestellt; ESCOP nicht bearbeitet. Botanik/Toxin/Verwechslung über naturadb.de, plantura.garden, gruenundgesund.de, hortica.de, botanikus.de, BUND-SH, GIZ Bonn, NABU Bremen.
- **Hinweis Quellen-Abruf:** WebFetch lieferte in diesem Lauf **durchgängig HTTP 403** auf allen Primär- UND Sekundär-Hosts (EMA, ESCOP, Wikipedia, Arzneipflanzenlexikon, naturadb, awl.ch). Inhalte daher ausschließlich über **WebSearch-Zusammenfassungen** (mehrere übereinstimmende Quellen je Aussage) verifiziert; **kein Ausweichen auf curl/wget**. **Regulatorische Evidenzgrade und Posologie sollten vom Arzt gegen die Original-Monographien geprüft werden** — im JSON jeweils in `pharmacology.evidence_caveat` + `sources` vermerkt.

### Überraschungen / unsichere Stellen für den Arzt

- **Hunds-Rose — der Arthrose-Effekt gilt NICHT für Tee/Mus, sondern nur für standardisiertes Pulver.** Die einzige belastbare (RCT-)Evidenz betrifft **standardisiertes Hagebuttenpulver** (GOPO-standardisierte Nahrungsergänzung), Meta-Analyse: nur **kleiner bis moderater, kurzfristiger** (3–4 Monate) Schmerzeffekt, **kein** Krankheitsstopp. Grund im JSON offengelegt: Das entzündungshemmende Galaktolipid **GOPO ist lipophil und geht in den wässrigen Aufguss kaum über** → selbst gekochter Hagebuttentee/-mus hat diesen Effekt nicht. Bewusst als eigene `evidence_tag: RCT`-Indikation mit klarer `realistic_expectation` + `overstated`.
- **Hunds-Rose — regulatorisch heterogen:** ESCOP positiv, **HMPC hat die Frucht nie bearbeitet** (nur Rosenblütenblätter anderer Arten), **Kommission E ohne positive Bewertung**. Die Erkältungs-/Vitamin-C-Indikation daher nur `ESCOP+` mit Hinweis, dass Vitamin C (bis ~2,4 %) durch Trocknen/Kochen/Lagern stark abnimmt.
- **Hunds-Rose — Feldrisiko ist mechanisch, nicht toxisch.** Kein giftiger Doppelgänger bei sicherer Rosenbestimmung; alle heimischen Wildrosen-Hagebutten essbar. Das reale Risiko sind die **feinen Härchen im Fruchtinneren (Juckpulver)** — Haut-/Schleimhautreiz, müssen entfernt werden. `flags.high_safety=true` gesetzt (kein Toxin, keine tödliche Verwechslung, kaum Interaktionen).
- **Schlehe — Kommission E hat die Blüten AUSDRÜCKLICH NEGATIV bewertet.** Die populäre „blutreinigende"/mild abführende Blütenanwendung ist **nicht belegt**; HMPC-Bewertung mangels Daten eingestellt, ESCOP nicht bearbeitet. Beide Indikationen daher nur `TRAD`, mit deutlichem `overstated` („Blutreinigung/Entschlackung" ist kein medizinisches Konzept). Klassischer „Erwartung dämpfen"-Fall.
- **Schlehe — Toxin sitzt im Steinkern, nicht im genutzten Drogenteil.** Fruchtfleisch und Blüten ungiftig, aber die **Steinkerne enthalten Amygdalin (Blausäure)** — dürfen nicht zerkleinert/zerbissen werden (in `key_warning`, `contraindications`, `collection_rules`, `preparation` durchgezogen). `toxin_ceiling` bewusst **false** gelassen, da der genutzte Drogenteil (Blüte/Fruchtfleisch) NICHT der toxische ist — dennoch prominent gewarnt. **Bitte diese Flag-Entscheidung redaktionell bestätigen.**
- **Schlehe — Verwechslungen aktiv ergänzt, zwei davon giftig.** Weißdorn (essbar; blüht später MIT Laub, rote Apfelfrucht), **Liguster** (gering giftig, schwarze Beeren in aufrechten Rispen, gegenständig, dornenlos), **Kreuzdorn *Rhamnus cathartica*** (giftig/drastisch abführend, schwarze Beeren mit mehreren Samen), **Traubenkirsche *Prunus padus*** (Fruchtfleisch essbar, Kerne blausäurehaltig, hängende Trauben). Sicherster Erkennungsanker der Schlehe: **blüht VOR dem Laubaustrieb** (März/April) + einzeln stehende blau-schwarze, bereifte Steinfrucht mit **einem** Kern. `deadly_confusion=false` (keine der Verwechslungen ist lebensgefährlich).

---

## 2026-07-24 — Heidelbeere, Hopfen

**Quelle der Auswahl:** `docs/wunschliste.json` enthielt 3 Einträge (vitis-vinifera, chenopodium-album, platanus-hispanica) — **alle bereits in `fertig/`** (weinrebe, weisser-gaensefuss, platane; ids exakt getroffen). Wunschliste damit **ohne offenen Eintrag** → beide Kräuter aus der **Kandidatenliste**: die zwei ersten offenen Einträge niedrigster tier = **vaccinium-myrtillus (Heidelbeere)** und **humulus-lupulus (Hopfen)**, beide tier 4.

**Deduplikation:** Beide gegen alle `id` + `botany.synonyms` in `fertig/` und gegen `vorhanden` geprüft — keine Dublette (auch nicht unter Synonym). Synonyme selbst eingetragen (Heidelbeere: Myrtillus niger, Vaccinium montanum + Abgrenzung Kultur-/Rauschbeere; Hopfen: keine gebräuchlichen Altnamen).

**Status:** vaccinium-myrtillus + humulus-lupulus in `kraeuter-kandidaten.json` auf `entwurf_fertig`, `datei` eingetragen. **NICHT** `geprueft` (bleibt dem Arzt). Keine Selbstheilung nötig (kein als „offen" markierter Kandidat lag bereits in `fertig/`).

**Prüfergebnis:** Beide `✓ ok, mit Hinweisen` (**0 Fehler, 0 Korrekturversuche**). Einziger Hinweis je Datei: enthält „unsicher/zu prüfen" (bewusst gesetzt).

**Hauptquellen:**
- Heidelbeere: EMA/HMPC EU herbal monograph *Vaccinium myrtillus* L., fructus siccus (traditional use); Kommission E + ESCOP (unspez. akuter Durchfall). Inhaltsstoffe/Dosierung über Altmeyers Enzyklopädie, heilpflanzen-atlas.de, vetpharm.uzh.ch, arzneipflanzenlexikon.info. Verwechslungen/Fuchsbandwurm über gartenjournal.net, mundraub.org, infranken.de, bluehendesoesterreich.at.
- Hopfen: EMA/HMPC EU herbal monograph *Humulus lupulus* L., flos (traditional use; Assessment report EMA/HMPC/418902/2005) + WEU nur für Fixkombination Baldrian+Hopfen. Kommission E. Inhaltsstoffe über heilpflanzen-atlas.de, pharmawiki.ch, pta-forum.de, arzneipflanzenlexikon.info; 8-PN-Einordnung Ärzte Zeitung; Zaunrüben-Toxikologie toxinfo.ch/awl.ch.
- **Hinweis Quellen-Abruf:** **WebFetch lieferte in diesem Lauf durchgängig HTTP 403** auf ALLEN Hosts (EMA-Primärquellen UND Sekundärquellen wie altmeyers.org, awl.ch, kraeuterleben.de). Inhalte daher ausschließlich über **WebSearch-Zusammenfassungen** (mehrere übereinstimmende Quellen je Kernaussage) verifiziert; **kein Ausweichen auf curl/wget**. **Regulatorische Evidenzgrade und Posologie ärztlich gegen die Original-Monographien prüfen** — im JSON in `pharmacology.evidence_caveat` + `sources` vermerkt.

### Überraschungen / unsichere Stellen für den Arzt

- **Wunschliste war komplett abgearbeitet.** Alle 3 Wünsche (Weinrebe, Weißer Gänsefuß, Platane) liegen schon in `fertig/` — die App hakt sie selbst ab. Dieser Lauf hat daher regelkonform auf die Kandidatenliste zurückgegriffen. Kein Handlungsbedarf, nur zur Info.
- **Heidelbeere — Droge ist die GETROCKNETE Frucht, die frische wirkt gegenteilig.** Die adstringierende Gerbstoffwirkung (Durchfall) hat NUR die getrocknete Frucht; die frische Beere kann in Menge sogar mild abführen. Das ist die häufigste Fehlannahme und im JSON in Indikation, chemistry, expectation_summary und key_warning durchgezogen.
- **Heidelbeere — `flags.deadly_confusion=true` wegen Tollkirsche.** Für Kinder ist die *Atropa belladonna* (kirschgroße Einzelbeere im fünfzipfeligen Sternkelch an bis 1,5 m hoher Staude) die reale, potenziell tödliche Verwechslung. Erkennungsanker Heidelbeere: niedriger Zwergstrauch < 40 cm, erbsengroße Beere mit Krone, **durchgehend blau gefärbtes Fruchtfleisch**. Zusätzlich Rauschbeere (essbar, farbloses Fleisch — Name täuscht Giftigkeit vor), Liguster/Faulbaum (giftig) ergänzt.
- **Heidelbeere — populäre Wirkungen sind Extrakt-/Mythos-Themen.** Der Seh-/Nachtsicht-Nutzen (RAF-Piloten-Mythos 2. WK) gilt als unbelegt/widerlegt; Venen-, Antioxidantien-, Diabetes-Effekte betreffen hochdosierte Anthocyan-**Extrakte**, nicht Tee/Frucht. Bewusst in `overstated`.
- **Heidelbeere — Fuchsbandwurm (der „Mythos" aus dem Kandidaten-reason).** Das Infektionsrisiko durch niedrige Waldbeeren gilt als sehr gering; Waschen hilft wenig (Eier kältestabil), sicheres Abtöten nur durch Erhitzen (~> 60 °C). Als Vorsichtsregel (waschen/erhitzen) aufgenommen, ohne Panik — Hauptübertragung ist Fuchskontakt, nicht die Beere.
- **Hopfen — reines Evidenz-Lehrstück (wie im Kandidaten-reason angelegt).** Für die **Einzeldroge** Hopfen bei Schlaf/Unruhe gibt es KEINE ausreichende klinische Evidenz → nur `TU`. Belastbare (`well-established use`) Daten existieren **ausschließlich für die Fixkombination Baldrian + Hopfen**. Klar getrennt in Indikation, `evidence_caveat` und `expectation_summary`. Bitte diese TU-Einstufung bestätigen.
- **Hopfen — 8-Prenylnaringenin: stärkstes bekanntes Phytoöstrogen, klinisch aber irrelevant bei üblicher Dosis.** 1 kg Zapfen enthält ~25–60 mg 8-PN, Tagesdosis ~2 g → nur ~µg-Bereich. „Hormonelle" Wechseljahrs-/Brustwachstums-Versprechen sind überzogen (`overstated`). Wegen theoretischer Östrogenwirkung + fehlender Daten trotzdem SS/Stillzeit meiden.
- **Hopfen — relevante pharmakodynamische Interaktion.** Additive Sedierung mit **Alkohol, Benzodiazepinen und anderen zentral dämpfenden Stoffen** (in `safety.interactions`, `clinical_relevance: relevant`, und `key_warning`). `interaction_heavy` bewusst **false** (nur eine relevante, additive Interaktion, kein CYP-Profil) — bitte redaktionell bestätigen.
- **Hopfen — Verwechslung giftige Zaunrübe (*Bryonia*).** Beide klettern an Hecken; Unterscheidung: Zaunrübe mit **Ranken** + Beeren, Hopfen **windet ohne Ranken** + trockene Zapfen. Risiko v. a. beim Ernten junger Frühjahrstriebe („Hopfenspargel"). `deadly_confusion=false` (Bryonia „giftig", nicht regelhaft „lebensgefährlich").

## 2026-07-24 — Echtes Lungenkraut, Gemeine Nachtkerze (beide KANDIDATEN)

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` (Stand 2026-07-22, 3 Eintraege) enthaelt vitis-vinifera, chenopodium-album, platanus-hispanica — **alle drei liegen bereits in `fertig/`** (als monographie-weinrebe.json, monographie-weisser-gaensefuss.json, monographie-platane.json; platane traegt exakt die id platanus-hispanica) → per Dedup uebersprungen, Wunschliste damit ohne offenen Eintrag. Beide Plaetze daher aus der Kandidatenliste: die ersten offenen Eintraege nach tier aufsteigend = beide Tier 4 in Listenreihenfolge:
- **pulmonaria-officinalis** (Echtes Lungenkraut) — `fertig/monographie-lungenkraut.json` — Quelle: Kandidat (Tier 4). Status → `entwurf_fertig`.
- **oenothera-biennis** (Gemeine Nachtkerze) — `fertig/monographie-nachtkerze.json` — Quelle: Kandidat (Tier 4). Status → `entwurf_fertig`.

Naechster offener Kandidat waere gentiana-lutea (Gelber Enzian, Tier 4) gewesen — wegen 2/Lauf zurueckgestellt.

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` in der Kandidatenliste geprueft — keine Dublette. Altnamen eingetragen: Pulmonaria = Pulmonaria maculosa; Oenothera = Onagra biennis. Kein Self-Heal noetig (kein als "offen" markierter Kandidat lag bereits in `fertig/`).

**Pruefergebnis:** beide gemeinsam `✓ ok, mit Hinweisen`, **0 Fehler beim ersten Versuch — 0 Korrekturversuche**. Einziger Hinweis je Datei: enthaelt bewusst "unsicher — zu pruefen".

**Hauptquellen:**
- Lungenkraut: Kommission E (Negativ-/Nullmonographie); Spektrum Lexikon Arzneipflanzen/Drogen (Inhaltsstoffe: loesliche Kieselsaeure ~2,5 %, Allantoin ~1-2 %, Gerbstoffe, Schleimstoffe); systematische PA-Untersuchung Boraginaceae; Wikipedia/Arzneipflanzenlexikon (Merkmale, Verwechslung). KEINE HMPC-/ESCOP-Monographie vorhanden.
- Nachtkerze: EMA/HMPC Assessment report Oenothera biennis/lamarckiana oleum (traditional use); Cochrane 2013 Bamford (oral evening primrose/borage oil for eczema — kein Placebo-Vorteil, 27 Studien/1596 Pat.); PTA-Forum/onmeda/DocMorris (GLA ~8-10 %, Interaktionen, Krampfschwelle/Phenothiazine); Wikipedia (Onagraceae, zweijaehrig, Schinkenwurz, Neophyt).
- **Quellen-Abruf:** WebFetch auf EMA-PDF, Altmeyers und awl.ch lieferte wie in allen Vorlaeufen **HTTP 403**; Inhalte daher ueber WebSearch-Zusammenfassungen mehrerer uebereinstimmender Sekundaerquellen verifiziert. **Primaerquellen (Kommission-E-Wortlaut Lungenkraut; EMA-Monograph/HMPC-TU-Indikationsliste Nachtkerze) am Original gegenpruefen.**

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Lungenkraut — der queue-Hinweis 'PA-Verdacht — pruefen!' loest sich REASSURIEREND.** Obwohl P. officinalis ein Raublattgewaechs (Boraginaceae) ist, findet die systematische Untersuchung KEINE toxischen 1,2-ungesaettigten Pyrrolizidinalkaloide — anders als bei Beinwell, Borretsch, Huflattich. Ich habe die Pflanze trotzdem defensiv gehalten (Schwangerschaft/Langzeit meiden, als "unsicher — zu pruefen" markiert). Bitte den PA-Freiheits-Befund am Original bestaetigen, bevor er als gesichert im Katalog steht.
- **Lungenkraut — Kommission E ist NEGATIV.** Kein einziger belegter Wirknachweis; ich habe alle Indikationen als TRAD getaggt und in `overstated` klargestellt, dass der Name aus der Signaturenlehre stammt und keine Lungenwirkung verspricht. Kein WEU/ESCOP moeglich.
- **Lungenkraut — `deadly_confusion=true` bei einer harmlosen Heilpflanze.** Grund ist ausschliesslich das Fruehjahrs-Wildsammeln junger Rosettenblaetter: die lebensgefaehrliche Fingerhut-Rosette (Digitalis, Herzglykoside) und der PA-haltige Beinwell koennen aehneln. Unterscheidungsmerkmal = die weissen Blattflecken des Lungenkrauts. `high_safety` daher **false**. Bitte pruefen, ob die App die Digitalis-Verwechslung fuer Pulmonaria spezifisch fuehren soll — sie ist plausibel/sicherheitsfoerdernd, aber Pulmonaria ist durch die Flecken meist gut kenntlich.
- **Nachtkerze — Tradition vs. Evidenz klaffen auseinander (der eigentliche Lehrwert dieses Eintrags).** HMPC fuehrt nur 'traditional use', der beste kontrollierte Evidenzstand (Cochrane 2013) zeigt fuer orales Nachtkerzenoel KEINEN Vorteil ueber Placebo bei Neurodermitis. Ich habe evidence_tag=TU gesetzt und in `comment`/`overstated`/`key_warning` deutlich gemacht, dass die populaere Neurodermitis-Erwartung nicht gedeckt ist. Bitte bestaetigen, dass der Katalog Nachtkerze so (dampened) fuehren will.
- **Nachtkerze — `lowers_seizure_threshold=true` gesetzt.** Fallberichte ueber ausgeloeste Krampfanfaelle, insbesondere unter Phenothiazin-Neuroleptika; zusaetzlich milde Blutungs-Interaktion mit Antikoagulanzien/TAH. `key_warning` warnt vor Epilepsie/Phenothiazinen. `interaction_heavy` bewusst **false** (kein schwerwiegendes KK-Interaktionsprofil), `pregnancy_contraindicated` **false** (Datenlage unklar → nur Vorsichts-Meidung, als "unsicher — zu pruefen" markiert). Bitte Flag-Setzung gegenpruefen.
- **Nachtkerze — Wirkstoff nur im Samenoel.** Kein GLA im Kraut-Tee; medizinisch relevant ist allein das kaltgepresste Samenoel. `harvest_organ=Samen`, `harvest_month_tags=[9,10]`. Kueche (Wurzel 'Schinkenwurz', Blaetter) strikt vom Arzneioel getrennt.

## 2026-07-24 (Lauf 2) — Gelber Enzian, Oregano (beide KANDIDATEN)

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` (Stand 2026-07-22, 3 Eintraege: vitis-vinifera, chenopodium-album, platanus-hispanica) — **alle drei liegen bereits in `fertig/`** (monographie-weinrebe.json/id vitis-vinifera, monographie-weisser-gaensefuss.json/id chenopodium-album, monographie-platane.json/id platanus-hispanica) → per Dedup uebersprungen, Wunschliste ohne offenen Eintrag. Beide Plaetze aus der Kandidatenliste: die ersten offenen Eintraege nach tier aufsteigend:
- **gentiana-lutea** (Gelber Enzian) — `fertig/monographie-gelber-enzian.json` — Quelle: Kandidat (Tier 4, letzter offener Tier-4-Eintrag). Status → `entwurf_fertig`.
- **origanum-vulgare** (Oregano) — `fertig/monographie-oregano.json` — Quelle: Kandidat (Tier 5, naechster offener). Status → `entwurf_fertig`.

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` in der Kandidatenliste geprueft — keine Dublette (Skript-Dublettencheck ueber alle fertig/*.json: sauber). Altnamen eingetragen: Enzian synonyms leer (Gentiana lutea L. ohne relevante Altnamen); Oregano = Thymus origanum (L.) Kuntze / subsp. vulgare. Kein Self-Heal noetig.

**Pruefergebnis:** beide gemeinsam `✓ ok, mit Hinweisen`, **0 Fehler beim ersten Versuch — 0 Korrekturversuche**. Einziger Hinweis je Datei: enthaelt bewusst "unsicher — zu pruefen".

**Hauptquellen:**
- Enzian: EMA/HMPC European Union herbal monograph Gentiana lutea radix (traditional use); ESCOP Gentianae radix; Kommission E (positiv); Uni Ulm Apothekergarten (Amarogentin, Bitterwert ~58 Mio., Gentiopikrosid); Giftpflanzen.com/Gartenjournal/AWL.ch (Verwechslung Weisser Germer); BArtSchV (geschuetzt).
- Oregano: EMA/HMPC (KEINE Monographie fuer O. vulgare — nur O. majorana + O. dictamnus); Kommission E Dostenkraut (NEGATIV); AWL.ch/apotheken.de/arzneipflanzenlexikon (Carvacrol, Thymol, Rosmarinsaeure); LactMed/MDPI (Carvacrol uteruskontrahierend/embryotoxisch).
- **Quellen-Abruf:** WebFetch auf EMA-PDF, Wikipedia, awl.ch, drugs.com, arzneipflanzenlexikon lieferte diesen Lauf durchgehend **HTTP 403**; Inhalte daher ueber WebSearch-Zusammenfassungen mehrerer uebereinstimmender Sekundaerquellen verifiziert. **Primaerquellen (EMA-HMPC-TU-Wortlaut Enzian; Kommission-E-Negativvotum Dostenkraut) am Original gegenpruefen — Evidenzgrad ungeprueft, aerztliche Gegenpruefung noetig.**

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Enzian — `deadly_confusion=true`, obwohl die Pflanze selbst ein sicheres Bittermittel ist.** Die Lebensgefahr steckt allein im Wurzelgraben vor der Bluete: die grundstaendige Blattrosette ist mit dem hochgiftigen **Weissen Germer (Veratrum album)** verwechselbar — genau daraus resultieren die bekannten Enzianschnaps-Vergiftungen. Sicheres Feldmerkmal in der Monographie: Enzian-Blaetter **kreuzgegenstaendig**, Germer **wechselstaendig/schraubig**; Wurzel innen gelb vs. weiss. Zusaetzlich als Konfusion aufgenommen: Gelber Fingerhut (Digitalis grandiflora, Herzglykoside) wegen gelber Bergbluete. `high_safety` daher **false**. Bitte Blattstellungs-Merkmal bestaetigen — es ist das lebensrettende Detail.
- **Enzian — Kontraindikation Hypertonie unsicher.** Eine Sekundaerquelle nennt Zurueckhaltung bei bestehender Hypertonie; die Beleglage ist schwach. Ich habe das ausdruecklich als "unsicher — zu pruefen" markiert (nicht als harte KI). Gesicherte KI ist das **peptische Ulkus** (Saeureanregung). Bitte pruefen, ob Hypertonie ueberhaupt im Katalog stehen soll.
- **Enzian — GESCHUETZT (BArtSchV).** Wildsammlung, besonders der Wurzel, ist verboten; Droge nur aus Anbau. Rechtlicher, nicht nur toxikologischer Punkt.
- **Oregano — der wichtigste Befund des Laufs: Erwartung deutlich zu daempfen.** Fuer **Origanum vulgare (Dostenkraut) existiert KEINE HMPC-Monographie** (die vorhandenen HMPC-Monographien gelten fuer O. majorana und O. dictamnus und duerfen NICHT uebertragen werden), und die **Kommission E hat die Anwendungsgebiete NEGATIV bewertet** (unzureichende Wirksamkeitsbelege). Ich habe deshalb alle Indikationen als **TRAD** (nicht TU) getaggt und in `comment`/`overstated`/`key_warning` klargestellt, dass der populaere "Oreganooel = natuerliches Antibiotikum"-Ruf klinisch unbelegt ist (nur in-vitro). Bitte diese TRAD-Einstufung bestaetigen — sie ist bewusst konservativ.
- **Oregano — Namensfalle Wasserdost.** Als giftige Verwechslung (giftig, nicht lebensgefaehrlich) den **Wasserdost (Eupatorium cannabinum)** aufgenommen: teilt nur den Namensteil "Dost", ist aber ein Korbbluetler mit lebertoxischen **Pyrrolizidinalkaloiden**. Morphologisch voellig anders (hanfaehnliche Blaetter, 1-1,5 m, feuchte Standorte, kein Wuerzduft) — die Falle liegt im Namen/Kraeuterhandel, nicht im Feld. Kein giftiger *morphologischer* Doppelgaenger von Dost bekannt.
- **Oregano — Trennung Gewuerz vs. konzentriertes Oel.** Als Kuechengewuerz/milder Tee sicher; das hochkonzentrierte aetherische "Oreganooel" ist schleimhautreizend und in der Schwangerschaft zu meiden (Carvacrol in Tiermodellen uteruskontrahierend/embryotoxisch). `high_safety` bewusst **false** (Negativ-Votum + Oel-Reizung + Namensfalle). `pregnancy_contraindicated` **false** gelassen, weil das Gewuerz unbedenklich ist — die Oel-Warnung steht im Text.

## 2026-07-24 (Lauf 3) — Majoran, Bergbohnenkraut (beide KANDIDATEN)

**Auswahl (genau 2):** Wunschliste hat Vorrang. `docs/wunschliste.json` (Stand 2026-07-22, 3 Eintraege: vitis-vinifera, chenopodium-album, platanus-hispanica) — **alle drei liegen bereits in `fertig/`** (verifiziert ueber id: monographie-weinrebe.json=vitis-vinifera, monographie-weisser-gaensefuss.json=chenopodium-album, monographie-platane.json=platanus-hispanica) → Wunschliste ohne offenen Eintrag, per Dedup uebersprungen. Beide Plaetze daher aus der Kandidatenliste; erste offene Eintraege nach tier aufsteigend = alle offenen sind Tier 5, in Listenreihenfolge:
- **origanum-majorana** (Majoran) — `fertig/monographie-majoran.json` — Quelle: Kandidat (Tier 5). Status offen → `entwurf_fertig`.
- **satureja-montana** (Bergbohnenkraut) — `fertig/monographie-bergbohnenkraut.json` — Quelle: Kandidat (Tier 5). Status offen → `entwurf_fertig`.

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden` in der Kandidatenliste geprueft — keine Dublette. Grep-Treffer auf `fertig/monographie-oregano.json` (id origanum-vulgare) war nur ein Konfusions-/Namensbezug ("Majoran", "Bohnenkraut" in dessen confusions), keine echte Dublette — eigene Arten, eigene ids. Altnamen eingetragen: Majoran = Majorana hortensis Moench / Majorana majorana; Bergbohnenkraut = Satureja illyrica Host / Micromeria montana. Kein Self-Heal noetig (kein als "offen" markierter Kandidat lag bereits in `fertig/`).

**Pruefergebnis:** beide gemeinsam `✓ ok, mit Hinweisen`, **0 Fehler beim ersten Versuch — 0 Korrekturversuche**. Einziger Hinweis je Datei: enthaelt bewusst "unsicher — zu pruefen".

**Vorbereitung:** `pip install -r requirements.txt` ausgefuehrt — `jsonschema 4.26.0` installiert (Umgebung war frisch, Modul fehlte; ohne haette der Validator nur eingeschraenkt geprueft). Danach lief die volle Schema-Pruefung.

**Hauptquellen:**
- Majoran: EMA/HMPC European Union herbal monograph Origanum majorana L., herba (EMA/HMPC/166517/2015, final 2016) — traditional use, Karminativum/Spasmolytikum, Tee (oral) + halbfeste kutane Zubereitung; Walaarzneimittel/Heilpflanzen-Atlas/Pschyrembel/Gesundheitswissen (Anwendung, Schwangerschaft, Dauergebrauch/Kopfschmerzen); Kostbare Natur/Herbaversum/kraeuter-buch.de (Abgrenzung zu Oregano); Altmeyers Phytotherapie.
- Bergbohnenkraut: Drugs.com (Savory) + WebMD (Winter Savory) — traditioneller Gebrauch, Vorsichtshinweise Schwangerschaft/Stillzeit/Kinder; PubMed/PMC 7230815 + PMC 9495055 (in-vitro Antimikrobik, Carvacrol/Thymol); Kostbare Natur/Herbaversum/heilpraxisnet.de (Sommer- vs. Winter-Bohnenkraut); Aromatherapie-Sicherheitsquellen (Phenolgehalt, Reizpotenzial des Oels).
- **Quellen-Abruf:** WebFetch auf die EMA-Primaer-PDF (Majoran-Monographie) lieferte wie in allen Vorlaeufen **HTTP 403**. Inhalte daher ueber WebSearch-Zusammenfassungen mehrerer uebereinstimmender Sekundaerquellen verifiziert. **Primaerquelle nicht erreichbar — die HMPC-TU-Einstufung Majoran und die exakte Posologie/Extraktspezifikation am Original gegenpruefen (Evidenzgrad TU gut sekundaer belegt, aber ungeprueft am Primaerdokument).** Bergbohnenkraut: hier ist keine Primaerquelle einschlaegig (es existiert keine Monographie), daher TRAD ohne Primaerabgleich korrekt.

### Ueberraschungen / unsichere Stellen fuer den Arzt

- **Majoran hat eine HMPC-Monographie — der entscheidende Kontrast zum Vorlauf.** Waehrend Oregano (Origanum vulgare, Lauf 2) KEINE HMPC-Monographie hat und Kommission-E-negativ ist, fuehrt die HMPC fuer die Schwester-Art Origanum majorana ausdruecklich einen **traditional use** (Karminativum/Spasmolytikum). Ich habe die Verdauungsindikation entsprechend als **TU** getaggt (nicht TRAD, nicht WEU). Bitte den TU-Wortlaut am EMA-Original bestaetigen.
- **Majoran — zweite Indikation kutan ('Majoranbutter').** Die HMPC deckt neben dem Tee eine **halbfeste kutane Zubereitung** ab (Extrakt 1:5, Ethanol 96 %, in weisser Vaseline). Das stuetzt die traditionelle 'Majoranbutter' bei wunder/verstopfter Saeuglingsnase — ABER nur aeusserlich, duenn, NICHT in die Nase und NICHT das konzentrierte aetherische Oel auf Saeuglingsschleimhaut. So im key_warning/contraindications formuliert. Bitte pruefen, ob der Katalog die Saeuglings-Anwendung so fuehren will.
- **Majoran — Schwangerschaft: bewusst NICHT als kontraindiziert geflaggt.** `pregnancy_contraindicated=false`, weil das Gewuerz in Speisemengen unbedenklich ist; von konzentrierten arzneilichen Mengen/aetherischem Oel wird jedoch abgeraten (dem Oel wird uterusanregende Wirkung auf die glatte Muskulatur zugeschrieben — Quellen erwaehnen sogar hebammenkundlichen Gebrauch zum "Wehen-Daempfen"). Datenlage duenn, als "unsicher — zu pruefen" markiert. `high_safety=true` gesetzt (kein Toxin, kein Doppelgaenger, keine schweren Interaktionen) — bitte gegenpruefen, ob die Oel-/Schwangerschaftsvorsicht das relativiert.
- **Bergbohnenkraut — keinerlei regulatorische Grundlage.** Weder HMPC noch ESCOP noch Kommission E fuehren Satureja (montana ODER hortensis). Alle Indikationen daher **TRAD**. Die antimikrobielle Wirkung (Carvacrol/Thymol) ist real, aber nur **in vitro** belegt — der populaere "natuerliches Antibiotikum"-Ruf ist klinisch nicht gedeckt. Defensiv formuliert.
- **Bergbohnenkraut — die praktisch relevante Verwechslung ist innerhalb der Gattung.** Mehrjaehriges, verholztes, schaerferes **Winter-Bohnenkraut (S. montana)** vs. einjaehriges, milderes **Sommer-Bohnenkraut (S. hortensis)** — beide ungiftig, aber Wirk-/Dosisangaben und Handelsware beziehen sich meist auf die Sommer-Art. Als Konfusion prominent aufgenommen. KEIN giftiger morphologischer Doppelgaenger (aktiv gesucht) → `deadly_confusion=false`, expliziter "keine lebensgefaehrliche Verwechslung"-Eintrag statt leerem Array.
- **Bergbohnenkraut — `high_safety` bewusst FALSE (Unterschied zu Majoran).** Grund: hoher Phenolgehalt (Carvacrol/Thymol); das konzentrierte aetherische Oel ist ein moderater Schleimhaut-/Hautreizstoff und wird fuer Schwangere/Stillende/Kinder < 6 J. explizit gemieden; zudem fehlt jede regulatorische Absicherung. Kein `toxin_ceiling` gesetzt, weil fuer die Kuechen-/Teemenge kein definierter Grenzwert existiert (die Phenol-Warnung betrifft das reine Oel, nicht das Gewuerz) — die Vorsicht steht stattdessen im Text. Bitte Flag-Abwaegung gegenpruefen.
- **Beide sind reine Kulturpflanzen am Bodensee** (`nur-kultur`). Gartentauglichkeit unterschiedlich: Majoran frostempfindlich/einjaehrig, Bergbohnenkraut winterhart/mehrjaehrig — im `garden`-Block ehrlich vermerkt.

## Lauf 2026-07-25 (autonom, 2 Monographien)

**Quelle-Auswahl:** Wunschliste (`docs/wunschliste.json`, 3 Eintraege) vollstaendig ERFUELLT — alle drei liegen bereits in `fertig/`: vitis-vinifera→monographie-weinrebe, chenopodium-album→monographie-weisser-gaensefuss, platanus-hispanica→monographie-platane (per id-Abgleich bestaetigt). Daher beide Plaetze aus der Kandidatenliste: die naechsten offenen Eintraege nach tier/Listenreihenfolge = **Ysop (hyssopus-officinalis)** und **Echter Lorbeer (laurus-nobilis)**, beide Tier 5. Dedup gegen `fertig/`, Synonyme und `vorhanden`: keine Treffer.

**Ysop — Hyssopus officinalis (Kandidat, Tier 5)**
- Pruefung: ok (nur der positive „unsicher/zu pruefen"-Hinweis). 0 Korrekturversuche.
- Evidenz: **TRAD**. KEINE HMPC-Monographie, **Kommission E NEGATIV**. Hauptquellen: AWL.ch, kraeuter-buch.de, pascoe.de, naturadb.de + toxikologische Fallberichte.
- **UEBERRASCHUNG/WICHTIG fuer den Arzt:** Die eigentliche Gefahr ist das aetherische Oel, nicht eine Verwechslung. Pinocamphon/Isopinocamphon (Monoterpenketone) sind neurotoxisch, krampfausloesend — Anfaelle ab 10–30 Tropfen Oel (Erwachsene) bzw. 2–3 Tropfen bei einem 6-jaehrigen Kind dokumentiert. Flags: toxin_ceiling, lowers_seizure_threshold, pregnancy_contraindicated. Kein giftiger Doppelgaenger.
- UNSICHER: konkrete arzneiliche Dosis-Obergrenzen (mangels Monographie) als „unsicher — zu pruefen" markiert.

**Echter Lorbeer — Laurus nobilis (Kandidat, Tier 5)**
- Pruefung: ok (nur positiver „unsicher"-Hinweis). 0 Korrekturversuche.
- Evidenz: **TRAD**. KEINE HMPC-Monographie, Kommission E negativ. Primaer Kuechengewuerz. Hauptquellen: kostbarenatur.net, naturheilkraeuter.org, pflanzenfreunde.com, heckenpflanzendirekt.de, baumfreunde.org.
- **UEBERRASCHUNG/WICHTIG:** `deadly_confusion=true`. Zwei kritische Doppelgaenger: **Oleander** (Nerium oleander, herztoxisch, *lebensgefaehrlich*, lanzettlich-immergruen) und **Kirschlorbeer** (Prunus laurocerasus, cyanogen/Blausaeure, als Hecke ueberall). Faustregel im Feld: echter Lorbeer riecht kraeftig wuerzig, die Giftpflanzen nicht (Kirschlorbeer nach Bittermandel). Zusaetzlich: Kontaktallergie (Sesquiterpenlactone Costunolid/Laurenobiolid) und Methyleugenol im Oel (potenziell genotoxisch → nur Speisemengen). Ganze Blaetter nicht mitessen.

**Recherche-Einschraenkung (fuer beide):** WebFetch lieferte fuer EMA/HMPC und mehrere Sekundaerquellen durchgaengig HTTP 403 (Proxy/Serverseite). Der HMPC-Negativbefund („keine Monographie") stuetzt sich daher auf WebSearch-Zusammenfassungen der Sekundaerquellen, NICHT auf die direkt gelesene EMA-Primaerquelle. Evidenzgrad TRAD ist dadurch konservativ (niedrig) gewaehlt; **aerztliche Gegenpruefung des Regulatorik-Status empfohlen.** In beiden Dateien und Quellenlisten vermerkt.

**Ergebnis:** 2 Monographien erzeugt, geprueft (fehlerfrei), Status in kraeuter-kandidaten.json → entwurf_fertig, changelog.json ergaenzt (84 Eintraege). Wunschliste unveraendert (macht die App).

## Lauf 2026-07-25 (autonom, 2 Monographien) — Fortsetzung

**Quelle-Auswahl:** `docs/wunschliste.json` (3 Eintraege) erneut geprueft — alle bereits in `fertig/` erfuellt (vitis-vinifera→weinrebe, chenopodium-album→weisser-gaensefuss, platanus-hispanica→platane; per id-Abgleich). Daher beide Plaetze aus der Kandidatenliste. Naechste offene Eintraege nach tier/Listenreihenfolge (Ysop + Lorbeer wurden im vorigen Lauf desselben Tages abgearbeitet) = **Gemeine Myrte (myrtus-communis)** und **Liebstoeckel (levisticum-officinale)**, beide Tier 5. Dedup gegen `fertig/`, botany.synonyms und `vorhanden`: keine Treffer.

**Gemeine Myrte — Myrtus communis (Kandidat, Tier 5)**
- Pruefung: ok (nur positiver „unsicher/zu pruefen"-Hinweis). **1 Korrekturversuch** noetig: Oleander als lebensgefaehrliche Konfusion gefuehrt → `deadly_confusion` musste auf true gesetzt werden (Skript-Konsistenzregel).
- Evidenz: **TRAD**. KEINE HMPC-Monographie fuer die Blattdroge; keine belastbare Klinik. Hauptquellen: AWL.ch, spektrum.de (Arzneipflanzen-Lexikon), PharmaWiki, kinderaerzte-im-netz.de, giftpflanzen.com.
- **UEBERRASCHUNG/WICHTIG fuer den Arzt:** (1) Das im Netz oft zitierte **„Myrtol standardisiert" (Gelomyrtol) ist NICHT die Myrtenpflanze**, sondern ein standardisiertes Destillat-Gemisch mehrerer aetherischer Oele — die Studienlage dazu darf nicht auf die Droge uebertragen werden. Habe die Indikationen daher konservativ TRAD getaggt und die Abgrenzung in expectation_summary.overstated + key_warning explizit gemacht. (2) Cineolreiches Myrtenoel (1,8-Cineol 12–45 %) → `infant_facial_caution` + `oil_age_restriction`: nicht ins Gesicht/an die Nase von Saeuglingen/Kleinkindern (Glottiskrampf-/Erstickungsgefahr), nicht bei Asthma. (3) `deadly_confusion=true` v. a. wegen **Oleander** (Nerium oleander, herztoxisch) als haeufiger mediterraner Mit-Kuebelpflanze — morphologisch klar verschieden, Risiko eher durch Unachtsamkeit; die echten Look-alikes sind giftig (Buchsbaum, Kirschlorbeer). Bestimmungs-Bestaetiger: durchscheinende Oeldruesen im Blatt (Licht-Test) + wuerziger Duft.
- UNSICHER: arzneiliche Dosis-Obergrenzen der Droge (keine Monographie), Pharmakokinetik, Schwangerschaft (Oel gemieden) — als „unsicher — zu pruefen" markiert.

**Liebstoeckel — Levisticum officinale (Kandidat, Tier 5)**
- Pruefung: ok (nur positiver „unsicher"-Hinweis). 0 Korrekturversuche.
- Evidenz: **TU** (Harnwege). Es gibt eine **HMPC Community herbal monograph (2012, traditional use)** fuer Levisticum officinale Koch, radix: Durchspuelung der ableitenden Harnwege, Tagesdosis Wurzeldroge **4–8 g**, Anwendungsdauer **2–4 Wochen** ohne aerztlichen Rat. Zusaetzlich Kommission-E-Positivmonographie. Verdauungsindikation als TRAD. Hauptquellen: EMA-Dokumentindex (Monograph + Assessment report), Herbal Reality, Wikipedia, plantura.garden.
- **UEBERRASCHUNG/WICHTIG:** (1) `deadly_confusion=true` + `apiaceae_confusion_young=true`: Liebstoeckel ist ein **Doldenbluetler**; junge Rosetten sind fuer Laien schwer von toedlichen Apiaceen zu trennen — **Gefleckter Schierling** (Conium maculatum, Coniin), **Wasserschierling** (Cicuta virosa, Cicutoxin; riecht selbst sellerieartig → besonders heimtueckisch, Hohlkammer-Wurzelstock als Merkmal), Hundspetersilie (giftig). Feld-Bestaetiger: intensiver Maggi-/Sellerie-Geruch (kein giftiger Doldenbluetler riecht so appetitlich). (2) `photosensitizing=true`: Furocumarine (Psoralen, Bergapten) — HMPC stuft die Photosensibilisierung fuer die orale Anwendung allerdings als klinisch nicht relevant ein; als Vorsicht dennoch geflaggt. (3) `cardiorenal_flush_caution=true`: NICHT „durchspuelen" bei Oedemen infolge Herz-/Nierenschwaeche; kein Ersatz bei fieberhaftem/kompliziertem Harnwegsinfekt. (4) Schwangerschaft: arzneilich gemieden (traditionell emmenagog), Kuechenmengen ok.

**Recherche-Einschraenkung (fuer beide):** WebFetch lieferte fuer EMA/HMPC-Primaer-PDFs und mehrere Sekundaerquellen erneut **HTTP 403** (Proxy/Serverseite). Die HMPC-Aussagen (Liebstoeckel-TU inkl. Posologie; Myrte-Negativbefund) stuetzen sich daher auf WebSearch-Zusammenfassungen des EMA-Dokumentindex bzw. uebereinstimmender Sekundaerquellen, NICHT auf die direkt gelesene Primaer-PDF. **Aerztliche Gegenpruefung der Regulatorik empfohlen** (in beiden Dateien und Quellenlisten vermerkt). Evidenzgrade konservativ gewaehlt (Liebstoeckel TU, Myrte TRAD).

**Ergebnis:** 2 Monographien erzeugt, geprueft (fehlerfrei), Status in kraeuter-kandidaten.json → entwurf_fertig (+ ids in `vorhanden`), changelog.json ergaenzt (86 Eintraege). Wunschliste unveraendert (macht die App).

## Lauf 2026-07-25 (autonom, 2 Monographien) — Fortsetzung II

**Vorbereitung:** `pip install -r requirements.txt` — jsonschema 4.26.0 installiert (frische Umgebung, Modul fehlte). Danach lief die volle Schema-Prüfung.

**Quelle-Auswahl:** `docs/wunschliste.json` (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) erneut geprüft — **alle drei bereits in `fertig/` erfüllt** (weinrebe/weisser-gaensefuss/platane, per id-Abgleich bestätigt). Daher beide Plätze aus der Kandidatenliste. Nächste offene Einträge nach tier/Listenreihenfolge = **Petersilie (petroselinum-crispum)** und **Kapuzinerkresse (tropaeolum-majus)**, beide Tier 5. (Ysop, Lorbeer, Myrte, Liebstöckel waren in den früheren Läufen desselben Tages abgearbeitet.) Dedup gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden`: keine Treffer (Grep-Treffer auf "petersilie" in anderen Dateien waren nur Konfusions-Bezüge, z. B. Hundspetersilie). Kein Self-Heal nötig. Altnamen selbst eingetragen.

**Petersilie — Petroselinum crispum (Kandidat, Tier 5)** — `fertig/monographie-petersilie.json`
- Prüfung: `ok, mit Hinweisen` (nur positiver „unsicher/zu prüfen"-Hinweis). **0 Korrekturversuche.**
- Evidenz: **TRAD**. **Kommission E POSITIV** (Petroselini herba/radix: Durchspülung Harnwege, Nierengrieß-Prophylaxe) — aber KEINE HMPC- und KEINE ESCOP-Monographie gefunden. Deshalb konservativ TRAD getaggt, Kommission-E-Status in Quelle/Kommentar vermerkt. **Bitte prüfen, ob Höherstufung gewünscht ist.**
- Hauptquellen: Kommission-E-Zusammenfassungen (aponet.de, gruenwalder.de), AWL.ch, Spektrum-Arzneipflanzenlexikon, Giftinformationszentrum/Bot. Sondergarten Wandsbek (Giftpflanze des Jahres 2023), giftpflanzen.com/pflanzen-deutschland.de (Aethusa).

**Kapuzinerkresse — Tropaeolum majus (Kandidat, Tier 5)** — `fertig/monographie-kapuzinerkresse.json`
- Prüfung: `ok, mit Hinweisen` (nur positiver „unsicher"-Hinweis). **0 Korrekturversuche.**
- Evidenz: **TRAD**. **Kommission E POSITIV in Kombination** (Harnwege, Atemwege; äußerlich Muskelschmerz). Klinische Daten v. a. für die **Fixkombination mit Meerrettich** (Angocin), nicht das Einzelkraut; keine HMPC/ESCOP. Konservativ TRAD. Arzneipflanze des Jahres 2013.
- Hauptquellen: Klostermedizin (Arzneipflanze 2013), AWL.ch, PharmaWiki, arzneipflanzenlexikon.info, Anwendungsdaten Fixkombination.

**Recherche-Einschränkung (beide):** Ausschließlich WebSearch/WebFetch benutzt. WebFetch auf EMA/HMPC-Primärquellen war wie in allen Vorläufen nicht nutzbar (HTTP 403). Der HMPC/ESCOP-Negativbefund stützt sich daher auf übereinstimmende Sekundärquellen, NICHT auf die direkt gelesene EMA-Primärquelle. **Regulatorik-Status und Evidenzgrad am Primärdokument ärztlich gegenprüfen** (in beiden Dateien vermerkt). Kein Ausweichen auf curl/wget.

### Überraschungen / unsichere Stellen für den Arzt

- **Petersilie ist Giftpflanze des Jahres 2023.** Das kommt überraschend für ein Küchenkraut. Grund: (1) **Samen und ätherisches Öl** enthalten Apiol/Myristicin — uterusstimulierend; früher als Abortivum missbraucht, mit **tödlichen** Vergiftungen (Leber-/Nieren-/Herzschäden). `pregnancy_contraindicated=true` (nur arzneiliche Mengen/Samen/Öl; Küchenmenge unbedenklich). (2) **Wildsammel-Verwechslung** mit tödlichen Doldenblütlern: Hundspetersilie (Aethusa cynapium, giftig), Gefleckter/Wasser-Schierling (lebensgefährlich) → `deadly_confusion=true`, `apiaceae_confusion_young=true`. Feld-Bestätiger: appetitlicher Küchenduft; krause Sorten sind fast unverwechselbar (Zuchtgrund). (3) Furanocumarine → `photosensitizing=true` (Phytophotodermatitis bei Hautsaft + UV). Die Selbstmedikation ist bewusst auf den milden Kraut-/Wurzeltee begrenzt, Samen/Öl explizit ausgeschlossen.
- **Petersilie-Evidenz bewusst konservativ (TRAD).** Kommission E ist positiv, aber es gibt keine HMPC/ESCOP-Monographie und keine kontrollierten Studien. Ich habe NICHT auf TU hochgestuft (TU ist per Spec HMPC-gebunden). Falls der Katalog Kommission-E-positive Herbs anders führen soll: hier entscheiden.
- **Kapuzinerkresse — die Evidenz betrifft die Kombination, nicht das Einzelkraut.** Kontrollierte Studien existieren für die **Fixkombination Kapuzinerkresse + Meerrettich** (Angocin). Das Einzelkraut allein ist nur Kommission-E-positiv/traditionell. Bewusst NICHT als RCT getaggt (wäre Schönung: Kombination ≠ Einzeldroge, begrenzte Studienqualität), sondern TRAD mit klarer Beschreibung. **Bitte Evidenz-Einordnung prüfen** — der Kandidaten-Reason nannte es „WEU-nahe Fixkombination".
- **Kapuzinerkresse — kein giftiger Doppelgänger.** Aktiv gesucht: die schildförmigen runden Blätter (zentraler Stielansatz) + gespornte Blüten sind praktisch eindeutig. `deadly_confusion=false`, dokumentierter „keine relevante Verwechslung"-Eintrag statt leerem Array. Aufgenommen: die reine **Namensfalle** „Nasturtium" (alter Name der Kapuzinerkresse) vs. Brunnenkresse (Nasturtium officinale, andere Pflanze).
- **Kapuzinerkresse-Wirkstoffchemie hat Zubereitungs-Konsequenz.** Benzylsenföl entsteht erst aus der **frischen, zerkleinerten** Pflanze (Myrosinase) und ist flüchtig → Frischkraut/Tinktur/standardisierte Kombipräparate wirksamer als lang gekochter Tee. `reflux_caution=true` (Senföle reizen Schleimhaut; Ulkus/Niere/Kleinkinder als Gegenanzeigen).
- **Beide reine Kulturpflanzen am Bodensee** (`nur-kultur`). Kein Antibiotika-Ersatz — bei beiden im key_warning verankert.

**Ergebnis:** 2 Monographien erzeugt, beide fehlerfrei geprüft (0 Korrekturversuche). Status in kraeuter-kandidaten.json → `entwurf_fertig` (+ ids in `vorhanden`), `docs/changelog.json` ergänzt (88 Einträge). Wunschliste unverändert (hakt die App selbst ab).

## Lauf 2026-07-25 (autonom) — Fortsetzung III

**Vorbereitung:** `pip install -r requirements.txt` — jsonschema 4.26.0 in frischer Umgebung installiert; volle Schema-Prüfung aktiv.

**Quelle-Auswahl:** `docs/wunschliste.json` (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) erneut geprüft — **alle drei bereits in `fertig/` erfüllt** (weinrebe/weisser-gaensefuss/platane, per id-Abgleich bestätigt). Wunschliste liefert 0 offene Einträge. Kandidatenliste: **nur noch EIN offener Eintrag** — armoracia-rusticana (Meerrettich, Tier 5); alles andere ist bereits `entwurf_fertig`. Damit standen diesem Lauf real **nur 1** offene Art zur Verfügung, nicht die anvisierten 2. Ehrlicher Ist-Zustand der Warteschlange, kein Fehler.

**Dedup:** gegen alle `id` + `botany.synonyms` in `fertig/` und `vorhanden`. Grep-Treffer auf "armoracia"/"meerrettich" waren ausschließlich Kombinations-/Konfusions-Bezüge in anderen Dateien (v. a. Kapuzinerkresse = Fixkombinationspartner) — kein echter Meerrettich-Eintrag. Altnamen selbst eingetragen: Cochlearia armoracia, Armoracia lapathifolia, Nasturtium armoracia, Rorippa armoracia. Kein Self-Heal nötig.

**Meerrettich — Armoracia rusticana (Kandidat, Tier 5)** — `fertig/monographie-meerrettich.json`
- Prüfung: `ok, mit Hinweisen` (nur positiver „unsicher/zu prüfen"-Hinweis). **0 Korrekturversuche.**
- Evidenz: **TU**. **Kommission E POSITIV** (Armoraciae rusticanae radix: Katarrhe der Atemwege, unterstützend bei Harnwegsinfekten, äußerlich durchblutungsfördernd bei leichten Muskelschmerzen). **KEINE HMPC- und KEINE ESCOP-Monographie.** Deshalb bewusst NICHT auf WEU hochgestuft. Äußerliche Zubereitungen laut Kommission E max. 2 % Senföle; mittlere Tagesdosis ca. 20 g frische Wurzel.
- Hauptquellen: Kommission-E-Zusammenfassungen (oeaz.at HMPPA, awl.ch, arzneipflanzenlexikon.info), paracelsus.de, kloesterl-apotheke.de; Anwendungsdaten Fixkombination mit Kapuzinerkresse.

### Überraschungen / unsichere Stellen für den Arzt

- **Nur 1 statt 2 Monographien in diesem Lauf** — die Warteschlange ist nahezu leer: Wunschliste vollständig erfüllt, und Meerrettich war der **letzte offene Kandidat**. Nach diesem Lauf sind **0 offene Kandidaten** übrig. Der Katalog braucht neuen Nachschub (Wunschliste oder neue Kandidaten), sonst laufen künftige Läufe leer.
- **Evidenz bewusst konservativ TU (nicht WEU).** Kommission E ist positiv, aber es existiert weder eine HMPC- noch eine ESCOP-Monographie. Die einzigen kontrollierten klinischen Daten betreffen die **Fixkombination Meerrettich + Kapuzinerkresse** (Angocin), NICHT die Einzeldroge. Kein RCT-Tag für das Einzelkraut (wäre Schönung). **Bitte prüfen, ob Kommission-E-positive Herbs im Katalog anders geführt werden sollen** — dieselbe Frage stellte sich schon bei Petersilie/Kapuzinerkresse.
- **`deadly_confusion=true` gesetzt.** Aktiv nach Doppelgängern gesucht: Meerrettich ist zwar durch den stechenden Senfgeruch der frisch angeschnittenen Wurzel/Blätter nahezu eindeutig, ABER große grundständige Blattrosetten können von Ungeübten mit **Rotem Fingerhut** (Digitalis purpurea, lebensgefährlich, Herzglykoside) oder **Beinwell** (Symphytum, Pyrrolizidinalkaloide) verwechselt werden. Flag safety-forward gesetzt; das Unterscheidungsmerkmal (Senfgeruch beim Zerreiben) ist in confusions und collection_rules verankert. **Einordnung ärztlich gegenprüfen** — die Fingerhut-Verwechslung ist eher theoretisch/bei Laien, aber wegen der Lebensgefahr bewusst nicht verharmlost.
- **Senföl-Chemie mit Zubereitungs-Konsequenz.** Allyl-/Phenylethylsenföl entstehen erst aus der frischen, zerkleinerten Wurzel (Myrosinase), sind flüchtig und hitzeempfindlich → frisch geriebene Wurzel/Frischpräparat wirksam, gekochter Tee nicht. `reflux_caution=true`, `infant_facial_caution=true` (reizende Dämpfe/Schleimhaut), Gegenanzeigen: Kinder < 4 Jahre, Ulcus, Nephritis; goitrogene Schilddrüsen-Vorsicht (als „unsicher — zu prüfen" markiert).
- **Recherche-Einschränkung:** Ausschließlich WebSearch/WebFetch. WebFetch auf Primär-/Sekundär-PDFs (oeaz.at HMPPA, arzneipflanzenlexikon.info) lieferte wie in allen Vorläufen **HTTP 403**; der HMPC/ESCOP-Negativbefund und die Kommission-E-Angaben stützen sich daher auf übereinstimmende WebSearch-Sekundärquellen, NICHT auf ein direkt gelesenes Primärdokument. **Regulatorik am Primärdokument ärztlich gegenprüfen** (in Datei + Quellenliste vermerkt). Kein Ausweichen auf curl/wget.

**Ergebnis:** 1 Monographie erzeugt (Meerrettich), fehlerfrei geprüft (0 Korrekturversuche). Status in kraeuter-kandidaten.json → `entwurf_fertig` (+ id in `vorhanden`), `docs/changelog.json` ergänzt (89 Einträge). Wunschliste unverändert (hakt die App selbst ab). **Warteschlange danach leer — 0 offene Kandidaten.**

## Lauf 2026-07-26 (autonom) — Leerlauf, nichts zu tun

**Vorbereitung:** `pip install -r requirements.txt` — jsonschema 4.26.0 in frischer Umgebung installiert; volle Schema-Prüfung wäre aktiv gewesen.

**Quelle-Auswahl geprüft:**
- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — **alle drei bereits in `fertig/` erfüllt**, per id-Abgleich bestätigt: vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json. Wunschliste liefert **0 offene** Einträge. (Nicht abgehakt — das macht die App selbst.)
- **`kraeuter-kandidaten.json`** — alle **87** Kandidaten stehen auf `entwurf_fertig`, **0 auf `offen`**. Kein Self-Heal nötig (kein „offen"-Eintrag, dessen Datei existiert). Statusverteilung: `{'entwurf_fertig': 87}`.

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Gemäß Anweisung („Nichts zu tun?") **keine Monographie erzeugt**, Zustand vermerkt, Lauf sauber beendet. **Kein Fehler** — die Warteschlange ist schlicht abgearbeitet.

### Für den Arzt

- **Der Katalog ist vollständig abgearbeitet.** Alle 87 Kandidaten sind als Entwurf fertig (warten nur noch auf die ärztliche Sichtung → Status `geprueft`), und alle 3 Wunschlisten-Einträge liegen in `fertig/`. Künftige autonome Läufe finden **nichts zu tun**, bis neuer Nachschub kommt: entweder neue Einträge über die App in `docs/wunschliste.json`, oder neue Kandidaten (Status `offen`) in `kraeuter-kandidaten.json`. Ohne Nachschub laufen die Routinen weiterhin leer.
- Keine inhaltlichen Änderungen an Monographien, `docs/changelog.json` bleibt bei 89 Einträgen unverändert.

### Zweite Zündung am 2026-07-26 (autonom)

Die Routine feuerte am selben Tag ein weiteres Mal. Zustand unverändert gegenüber der ersten Zündung (Commit `fab6963`): Wunschliste (vitis-vinifera, chenopodium-album, platanus-hispanica) vollständig in `fertig/` erfüllt, Kandidatenliste weiterhin 87× `entwurf_fertig` / **0× `offen`**. Kein Self-Heal nötig, keine Monographie erzeugt, keine inhaltliche Änderung. **Kein Fehler** — nur ein leerer Nachlauf. Nachschub (Wunschliste oder neue `offen`-Kandidaten) weiterhin nötig, sonst laufen alle künftigen Läufe leer.

### Dritte Zündung am 2026-07-26 (autonom) — Leerlauf, nichts zu tun

Erneute Zündung derselben Routine am selben Tag. Zustand unverändert gegenüber den beiden vorherigen Zündungen des Tages:

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — **alle drei bereits in `fertig/` erfüllt**, per id-Abgleich frisch bestätigt: vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json. **0 offene** Wünsche. (Nicht abgehakt — das macht die App selbst.)
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig (kein „offen"-Eintrag, dessen Datei bereits existiert).

Weder Wunschliste noch Kandidatenliste liefern offene Arten → gemäß Anweisung **keine Monographie erzeugt**, keine inhaltliche Änderung (`docs/changelog.json` bleibt unverändert). **Kein Fehler** — die Warteschlange ist schlicht abgearbeitet.

**Für den Arzt:** Der Katalog ist vollständig abgearbeitet. Alle 87 Kandidaten stehen als Entwurf fertig (warten nur noch auf die ärztliche Sichtung → Status `geprueft`), alle 3 Wunschlisten-Einträge liegen in `fertig/`. Bis neuer Nachschub kommt — neue Einträge über die App in `docs/wunschliste.json` oder neue `offen`-Kandidaten in `kraeuter-kandidaten.json` — laufen alle künftigen autonomen Läufe leer. Empfehlung: entweder die fertigen Entwürfe sichten oder die Routine pausieren, um Leerläufe zu vermeiden.

## Lauf 2026-07-27 (autonom) — Leerlauf, nichts zu tun

Erste Zündung am 2026-07-27 (nach drei Leerläufen am 2026-07-26). Zustand unverändert:

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — **alle drei bereits in `fertig/` erfüllt**, per id-Abgleich frisch bestätigt: vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json. **0 offene** Wünsche. (Nicht abgehakt — das macht die App.)
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig.

**Vorbereitung:** `pip install -r requirements.txt` — jsonschema war bereits vorhanden (volle Schemaprüfung wäre aktiv).

Weder Wunschliste noch Kandidatenliste liefern offene Arten → gemäß Anweisung **keine Monographie erzeugt**, keine inhaltliche Änderung (`docs/changelog.json` unverändert). **Kein Fehler** — die Warteschlange ist abgearbeitet.

**Für den Arzt:** Vierter Leerlauf in Folge. Der Katalog ist vollständig als Entwurf fertig; die Routine findet dauerhaft nichts zu tun und feuert weiter leer. **Empfehlung:** entweder die fertigen Entwürfe sichten (Status → `geprueft`), neue Arten liefern (Wunschliste über die App oder `offen`-Kandidaten), oder **die Routine pausieren**, um weitere Leerläufe zu vermeiden.

## Lauf 2026-07-27 (autonom, zweite Zündung) — Leerlauf, nichts zu tun

Erneute Zündung am 2026-07-27. Zustand unverändert gegenüber allen vorherigen Läufen — **fünfter Leerlauf in Folge**.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei bereits in `fertig/` erfüllt, per id-Abgleich frisch bestätigt: vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json (letztere führt die Altnamen *Platanus × acerifolia* / *× hybrida* in `botany.synonyms`). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig (kein „offen"-Eintrag, dessen Datei bereits existiert).

**Vorbereitung:** `pip install -r requirements.txt` — jsonschema 4.26.0 installiert, volle Schemaprüfung wäre aktiv gewesen.

Weder Wunschliste noch Kandidatenliste liefern offene Arten → gemäß Anweisung **keine Monographie erzeugt**, keine inhaltliche Änderung (`docs/changelog.json` unverändert). **Kein Fehler** — die Warteschlange ist restlos abgearbeitet.

**Für den Arzt:** Fünfter Leerlauf in Folge. Der Katalog ist vollständig als Entwurf fertig (87 Kandidaten `entwurf_fertig`, warten nur auf ärztliche Sichtung → Status `geprueft`; 3 Wunschlisten-Einträge in `fertig/`). Die Routine findet dauerhaft nichts zu tun und feuert weiter leer. **Empfehlung:** entweder die fertigen Entwürfe sichten, neue Arten liefern (Wunschliste über die App oder `offen`-Kandidaten in der Kandidatenliste), oder **die Routine pausieren**, um weitere Leerläufe zu vermeiden.

## Lauf 2026-07-27 (autonom, dritte Zündung) — Leerlauf, nichts zu tun

Erneute Zündung am 2026-07-27 — **sechster Leerlauf in Folge**. Zustand unverändert.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id-Abgleich in `fertig/` bestätigt (→ monographie-weinrebe.json, monographie-weisser-gaensefuss.json, monographie-platane.json). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig.
- **Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 vorhanden.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet.

**Für den Arzt:** Die Routine läuft jetzt zum sechsten Mal in Folge leer und wird das bei jeder Zündung weiter tun, solange kein Nachschub kommt. **Empfehlung: Routine pausieren** (oder fertige Entwürfe sichten → Status `geprueft`, bzw. neue Arten über Wunschliste/`offen`-Kandidaten liefern), um weitere Leerläufe zu vermeiden.

## Lauf 2026-07-27 (autonom, vierte Zündung) — Leerlauf, nichts zu tun

Erneute Zündung am 2026-07-27 — **siebter Leerlauf in Folge**. Zustand unverändert.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id-Abgleich in `fertig/` bestätigt (vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Alle 87 `datei`-Pfade existieren in `fertig/` (geprüft) → kein Self-Heal nötig, keine verwaisten Einträge.
- **Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 vorhanden.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet.

**Für den Arzt:** Die Routine läuft nun zum siebten Mal in Folge leer und wird bei jeder weiteren Zündung ergebnislos feuern, solange kein Nachschub kommt. Jede Zündung verbraucht Rechenzeit ohne Gegenwert. **Dringende Empfehlung: Routine pausieren.** Alternativ Nachschub liefern (neue Wunschlisten-Einträge über die App oder `offen`-Kandidaten in der Kandidatenliste) — oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Nur ein Mensch kann diesen Leerlauf beenden.

## Lauf 2026-07-28 (autonom) — Leerlauf, nichts zu tun

Zündung am 2026-07-28 — **achter Leerlauf in Folge**. Zustand unverändert gegenüber allen bisherigen Läufen.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id-Abgleich in `fertig/` bestätigt (vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Alle 87 `datei`-Pfade in `fertig/` vorhanden (geprüft) → kein Self-Heal nötig, keine verwaisten Einträge.
- **Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 installiert (im frischen Container zunächst nicht vorhanden gewesen).

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet.

**Für den Arzt:** Achter ergebnisloser Lauf in Folge. Diesmal wurde zusätzlich eine **Push-Benachrichtigung** ausgelöst, da sieben stille Log-Hinweise offenbar folgenlos blieben. Die Routine feuert bei jeder Zündung weiter leer und verbraucht Rechenzeit ohne Gegenwert, solange kein Mensch eingreift. **Dringende Empfehlung: Routine pausieren.** Alternativ Nachschub liefern (neue Wunschlisten-Einträge über die App oder `offen`-Kandidaten in der Kandidatenliste) — oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen.

## Lauf 2026-07-28 (autonom, zweite Zündung desselben Tages) — Leerlauf, nichts zu tun

Erneute Zündung am 2026-07-28 — **neunter Leerlauf in Folge**, zweite am selben Tag. Zustand unverändert.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id-Abgleich in `fertig/` bestätigt (→ monographie-weinrebe.json, monographie-weisser-gaensefuss.json, monographie-platane.json). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig, keine verwaisten Einträge.
- **Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet.

**Für den Arzt:** Neunter ergebnisloser Lauf. Zum achten Lauf wurde bereits eine Push-Benachrichtigung ausgelöst; dieser Lauf verzichtet bewusst auf eine erneute Push-Meldung (identischer, bereits gemeldeter Zustand — kein Mehrwert). Die Routine feuert bei jeder Zündung weiter leer, solange kein Mensch eingreift. **Dringende Empfehlung: Routine pausieren.** Alternativ Nachschub liefern (neue Wunschlisten-Einträge über die App oder `offen`-Kandidaten) — oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen.

## Lauf 2026-07-28 (autonom, dritte Zündung desselben Tages) — Leerlauf, nichts zu tun

Erneute Zündung am 2026-07-28 — **zehnter Leerlauf in Folge**, dritte am selben Tag. Zustand unverändert.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id-Abgleich in `fertig/` bestätigt (→ monographie-weinrebe.json, monographie-weisser-gaensefuss.json, monographie-platane.json; Synonyme geprüft). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig, keine verwaisten Einträge.
- **Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet.

**Für den Arzt:** Zehnter ergebnisloser Lauf. Push-Benachrichtigung wurde bereits am achten Lauf ausgelöst; dieser Lauf verzichtet bewusst auf eine erneute Push-Meldung (identischer, bereits gemeldeter Zustand — kein Mehrwert, nur Lärm). Die Routine feuert bei jeder Zündung weiter leer und verbraucht Rechenzeit ohne Gegenwert, solange kein Mensch eingreift. **Dringende Empfehlung: Routine pausieren.** Alternativ Nachschub liefern (neue Wunschlisten-Einträge über die App oder `offen`-Kandidaten in der Kandidatenliste) — oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Nur ein Mensch kann diesen Leerlauf beenden.

## Lauf 2026-07-28 (autonom, vierte Zündung desselben Tages) — Leerlauf, nichts zu tun

Erneute Zündung am 2026-07-28 — **elfter Leerlauf in Folge**, vierte am selben Tag. Zustand unverändert.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id-Abgleich in `fertig/` bestätigt (vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json; Synonyme mitgeprüft). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig, keine verwaisten Einträge.
- **Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet.

**Für den Arzt:** Elfter ergebnisloser Lauf. Push-Benachrichtigung wurde bereits am achten Lauf ausgelöst; dieser Lauf verzichtet bewusst auf eine erneute Push-Meldung (identischer, bereits gemeldeter Zustand — reiner Lärm). Die Routine feuert bei jeder Zündung weiter leer und verbraucht Rechenzeit ohne Gegenwert, solange kein Mensch eingreift. **Dringende Empfehlung: Routine pausieren.** Alternativ Nachschub liefern (neue Wunschlisten-Einträge über die App oder `offen`-Kandidaten in der Kandidatenliste) — oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Nur ein Mensch kann diesen Leerlauf beenden.

## Lauf 2026-07-29 (autonom) — Leerlauf, nichts zu tun

Erste Zündung am 2026-07-29 — **zwölfter Leerlauf in Folge**. Zustand gegenüber den vier Läufen vom 2026-07-28 unverändert.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich in `fertig/` bestätigt (vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json, deren `synonyms` zusätzlich `Platanus × acerifolia`/`× hybrida` führen). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig, keine verwaisten Einträge.
- **Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet.

**Für den Arzt:** Zwölfter ergebnisloser Lauf (erster am 2026-07-29). Push-Benachrichtigung wurde bereits am achten Lauf ausgelöst; dieser Lauf verzichtet erneut bewusst darauf (identischer, bereits gemeldeter Zustand — reiner Lärm). Solange kein Mensch eingreift, feuert die Routine bei jeder Zündung leer und verbraucht Rechenzeit ohne Gegenwert. **Dringende Empfehlung: Routine pausieren.** Alternativ Nachschub liefern (neue Wunschlisten-Einträge über die App oder `offen`-Kandidaten in der Kandidatenliste) — oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Nur ein Mensch kann diesen Leerlauf beenden.

## Lauf 2026-07-29 (autonom, zweite Zündung desselben Tages) — Leerlauf, nichts zu tun

Erneute Zündung am 2026-07-29 — **dreizehnter Leerlauf in Folge**, zweite am selben Tag. Zustand gegenüber allen vorangehenden Läufen unverändert.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich in `fertig/` bestätigt (vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json; letztere führt `synonyms` `Platanus × acerifolia`/`× hybrida`). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig, keine verwaisten Einträge.
- **Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet.

**Für den Arzt:** Dreizehnter ergebnisloser Lauf. Push-Benachrichtigung wurde bereits am achten Lauf ausgelöst; dieser Lauf verzichtet erneut bewusst darauf (identischer, bereits gemeldeter Zustand — reiner Lärm, kein Mehrwert). Solange kein Mensch eingreift, feuert die Routine bei jeder Zündung leer und verbraucht Rechenzeit ohne Gegenwert. **Dringende Empfehlung: Routine pausieren.** Alternativ Nachschub liefern (neue Wunschlisten-Einträge über die App oder `offen`-Kandidaten in der Kandidatenliste) — oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Nur ein Mensch kann diesen Leerlauf beenden.

## Lauf 2026-07-29 (autonom, dritte Zündung desselben Tages) — Leerlauf, nichts zu tun

Erneute Zündung am 2026-07-29 — **vierzehnter Leerlauf in Folge**, dritte am selben Tag. Zustand unverändert.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich in `fertig/` bestätigt (→ monographie-weinrebe.json, monographie-weisser-gaensefuss.json, monographie-platane.json). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig, keine verwaisten Einträge.
- **Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet.

**Für den Arzt:** Vierzehnter ergebnisloser Lauf. Push-Benachrichtigung wurde am achten Lauf ausgelöst; seither bewusst kein erneuter Push (identischer Zustand — reiner Lärm). Die Routine muss laufen bleiben, um neue Wunschlisten-Einträge zeitnah zu erfassen — ein Pausieren würde genau diese Reaktionsfähigkeit brechen; daher **kein** eigenmächtiges Pausieren. Solange kein Nachschub kommt, feuert sie leer. **Nur ein Mensch kann das ändern:** neue Wunschlisten-Einträge über die App liefern, `offen`-Kandidaten ergänzen — oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Wenn kein Nachschub absehbar ist, Routine-Intervall strecken oder pausieren.

## Lauf 2026-07-29 (autonom, vierte Zündung desselben Tages) — Leerlauf, nichts zu tun

Erneute Zündung am 2026-07-29 — **fünfzehnter Leerlauf in Folge**, vierte am selben Tag. Zustand unverändert.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich in `fertig/` bestätigt (vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json; letztere führt `synonyms` `Platanus × acerifolia`/`× hybrida`). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig, keine verwaisten Einträge.
- **Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet.

**Für den Arzt:** Fünfzehnter ergebnisloser Lauf. Push-Benachrichtigung wurde am achten Lauf ausgelöst; seither bewusst kein erneuter Push (identischer, bereits gemeldeter Zustand — reiner Lärm, kein Mehrwert). Die Routine bleibt laufbereit, um neue Wunschlisten-Einträge zeitnah zu erfassen — kein eigenmächtiges Pausieren. Solange kein Nachschub kommt, feuert sie leer und verbraucht Rechenzeit ohne Gegenwert. **Nur ein Mensch kann das ändern:** neue Wunschlisten-Einträge über die App liefern, `offen`-Kandidaten in der Kandidatenliste ergänzen — oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Wenn absehbar kein Nachschub kommt, empfiehlt sich, das Routine-Intervall deutlich zu strecken oder die Routine zu pausieren.

## Lauf 2026-07-30 (autonom, erste Zündung des Tages) — Leerlauf, nichts zu tun

Erste Zündung am 2026-07-30 — **sechzehnter Leerlauf in Folge**. Zustand gegenüber allen vorangehenden Läufen unverändert.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich in `fertig/` bestätigt (vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json; letztere führt `synonyms` `Platanus × acerifolia`/`× hybrida`). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig, keine verwaisten Einträge.
- **Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet.

**Für den Arzt:** Sechzehnter ergebnisloser Lauf, erster am 2026-07-30. Push-Benachrichtigung wurde am achten Lauf ausgelöst; seither bewusst kein erneuter Push (identischer, bereits gemeldeter Zustand — reiner Lärm). Die Routine bleibt laufbereit, um neue Wunschlisten-Einträge zeitnah zu erfassen — kein eigenmächtiges Pausieren. Solange kein Nachschub kommt, feuert sie leer und verbraucht Rechenzeit ohne Gegenwert. **Nur ein Mensch kann das ändern:** neue Wunschlisten-Einträge über die App liefern, `offen`-Kandidaten in der Kandidatenliste ergänzen — oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Wenn absehbar kein Nachschub kommt, empfiehlt sich, das Routine-Intervall deutlich zu strecken oder die Routine zu pausieren.

## Lauf 2026-07-30 (autonom, zweite Zündung des Tages) — Leerlauf, nichts zu tun

Zweite Zündung am 2026-07-30 — **siebzehnter Leerlauf in Folge**. Zustand gegenüber allen vorangehenden Läufen unverändert.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich in `fertig/` bestätigt (vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig, keine verwaisten Einträge.
- **Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet.

**Für den Arzt:** Siebzehnter ergebnisloser Lauf, zweiter am 2026-07-30. Push-Benachrichtigung wurde am achten Lauf ausgelöst; seither bewusst kein erneuter Push (identischer, bereits gemeldeter Zustand — reiner Lärm). Die Routine bleibt laufbereit, um neue Wunschlisten-Einträge zeitnah zu erfassen — kein eigenmächtiges Pausieren. Solange kein Nachschub kommt, feuert sie leer und verbraucht Rechenzeit ohne Gegenwert. **Nur ein Mensch kann das ändern:** neue Wunschlisten-Einträge über die App liefern, `offen`-Kandidaten in der Kandidatenliste ergänzen — oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Wenn absehbar kein Nachschub kommt, empfiehlt sich, das Routine-Intervall deutlich zu strecken oder die Routine zu pausieren.

## Lauf 2026-07-30 (autonom, dritte Zündung des Tages) — Leerlauf, nichts zu tun

Dritte Zündung am 2026-07-30 — **achtzehnter Leerlauf in Folge**. Zustand gegenüber allen vorangehenden Läufen unverändert.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich in `fertig/` bestätigt (vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json; letztere führt `synonyms` `Platanus × acerifolia`/`× hybrida`). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig, keine verwaisten Einträge.
- **Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet.

**Für den Arzt:** Achtzehnter ergebnisloser Lauf, dritter am 2026-07-30. Push-Benachrichtigung wurde am achten Lauf ausgelöst; seither bewusst kein erneuter Push (identischer, bereits gemeldeter Zustand — reiner Lärm). Die Routine bleibt laufbereit, um neue Wunschlisten-Einträge zeitnah zu erfassen — kein eigenmächtiges Pausieren. Solange kein Nachschub kommt, feuert sie leer und verbraucht Rechenzeit ohne Gegenwert. **Nur ein Mensch kann das ändern:** neue Wunschlisten-Einträge über die App liefern, `offen`-Kandidaten in der Kandidatenliste ergänzen — oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Wenn absehbar kein Nachschub kommt, empfiehlt sich, das Routine-Intervall deutlich zu strecken oder die Routine zu pausieren.

## Lauf 2026-07-30 (autonom, vierte Zündung des Tages) — Leerlauf, nichts zu tun

Vierte Zündung am 2026-07-30 — **neunzehnter Leerlauf in Folge**. Zustand gegenüber allen vorangehenden Läufen unverändert.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich in `fertig/` bestätigt (vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json; letztere führt `synonyms` `Platanus × acerifolia`/`× hybrida`). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig, keine verwaisten Einträge.
- **Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet.

**Für den Arzt:** Neunzehnter ergebnisloser Lauf, vierter am 2026-07-30. Push-Benachrichtigung wurde am achten Lauf ausgelöst; seither bewusst kein erneuter Push (identischer, bereits gemeldeter Zustand — reiner Lärm). Die Routine bleibt laufbereit, um neue Wunschlisten-Einträge zeitnah zu erfassen — kein eigenmächtiges Pausieren. Solange kein Nachschub kommt, feuert sie leer und verbraucht Rechenzeit ohne Gegenwert. **Nur ein Mensch kann das ändern:** neue Wunschlisten-Einträge über die App liefern, `offen`-Kandidaten in der Kandidatenliste ergänzen — oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Wenn absehbar kein Nachschub kommt, empfiehlt sich, das Routine-Intervall deutlich zu strecken oder die Routine zu pausieren.

## Lauf 2026-07-31 (autonom, erste Zündung des Tages) — Leerlauf, nichts zu tun

**Zwanzigster Leerlauf in Folge**, erste Zündung am 2026-07-31. Zustand unverändert gegenüber allen Vorläufen.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id-Abgleich in `fertig/` bestätigt (→ monographie-weinrebe / -weisser-gaensefuss / -platane.json). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**, keine verwaisten `datei`-Verweise. Kein Self-Heal nötig.
- Vorbereitung: `pip install -r requirements.txt` → jsonschema 4.26.0 neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet. Push-Benachrichtigung bereits am achten Lauf ausgelöst; bewusst kein erneuter Push (identischer, gemeldeter Zustand).

**Für den Arzt:** Seit dem achten Lauf feuert die Routine ergebnislos. Nachschub kann nur ein Mensch liefern — neue Wunschlisten-Einträge über die App, `offen`-Kandidaten ergänzen, oder die 87 Entwürfe sichten und auf `geprueft` setzen. Bis dahin: Routine-Intervall strecken oder pausieren spart Rechenzeit.

## Lauf 2026-07-31 (autonom, zweite Zündung des Tages) — Leerlauf, nichts zu tun

**Einundzwanzigster Leerlauf in Folge**, zweite Zündung am 2026-07-31. Zustand unverändert gegenüber allen Vorläufen.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich in `fertig/` bestätigt (vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**, keine verwaisten `datei`-Verweise. Kein Self-Heal nötig.
- Vorbereitung: `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet. Push-Benachrichtigung bereits am achten Lauf ausgelöst; bewusst kein erneuter Push (identischer, gemeldeter Zustand — reiner Lärm).

**Für den Arzt:** Seit dem achten Lauf feuert die Routine ergebnislos. Nachschub kann nur ein Mensch liefern — neue Wunschlisten-Einträge über die App, `offen`-Kandidaten in der Kandidatenliste ergänzen, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Bis dahin: Routine-Intervall deutlich strecken oder Routine pausieren spart Rechenzeit ohne Verlust.

## Lauf 2026-07-31 (autonom, dritte Zündung des Tages) — Leerlauf, nichts zu tun

**Zweiundzwanzigster Leerlauf in Folge**, dritte Zündung am 2026-07-31. Zustand unverändert.

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich in `fertig/` bestätigt (vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json; letztere trägt die Synonyme *Platanus × acerifolia* / *× hybrida*). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**, keine verwaisten `datei`-Verweise. Kein Self-Heal nötig.
- Vorbereitung: `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet. Bewusst kein Push (identischer, bereits am achten Lauf gemeldeter Zustand — reiner Lärm).

**Für den Arzt:** Unverändert seit dem achten Lauf. Nachschub kann nur ein Mensch liefern — neue Wunschlisten-Einträge über die App, `offen`-Kandidaten in der Kandidatenliste ergänzen, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Bis dahin: Routine-Intervall deutlich strecken oder pausieren spart Rechenzeit ohne Verlust.

## Lauf 2026-07-31 (autonom, vierte Zündung des Tages) — Leerlauf, nichts zu tun

**Dreiundzwanzigster Leerlauf in Folge**, vierte Zündung am 2026-07-31. Zustand unverändert; unabhängig gegengeprüft (nicht dem Vorlauf-Log vertraut).

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id-Abgleich in `fertig/` bestätigt: vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json. **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — unabhängig ausgezählt: 87 Einträge, Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**, keine verwaisten `datei`-Verweise. Kein Self-Heal nötig.
- Vorbereitung: `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet. Bewusst kein Push (identischer, bereits am achten Lauf gemeldeter Zustand — reiner Lärm für den Arzt).

**Für den Arzt:** Unverändert seit dem achten Lauf. Nachschub kann nur ein Mensch liefern — neue Wunschlisten-Einträge über die App, `offen`-Kandidaten in der Kandidatenliste ergänzen, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Bis dahin: Routine-Intervall deutlich strecken oder pausieren spart Rechenzeit ohne Verlust.

## Lauf 2026-08-01 (autonom, erste Zündung) — Leerlauf, nichts zu tun

**Vierundzwanzigster Leerlauf in Folge**, erste Zündung am 2026-08-01. Zustand unverändert; unabhängig gegengeprüft (nicht dem Vorlauf-Log vertraut).

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich in `fertig/` bestätigt: vitis-vinifera → monographie-weinrebe.json (id `vitis-vinifera`), chenopodium-album → monographie-weisser-gaensefuss.json (id `chenopodium-album`), platanus-hispanica → monographie-platane.json (id `platanus-hispanica`, Synonyme *Platanus × acerifolia* / *× hybrida*). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — unabhängig ausgezählt: 87 Einträge, Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**, keine verwaisten `datei`-Verweise. Kein Self-Heal nötig.
- Vorbereitung: `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet. Bewusst keine Push-Benachrichtigung (identischer, bereits am achten Lauf gemeldeter Zustand — reiner Lärm für den Arzt).

**Für den Arzt:** Unverändert seit dem achten Lauf, jetzt 24 ergebnislose Läufe. Nachschub kann nur ein Mensch liefern — neue Wunschlisten-Einträge über die App, `offen`-Kandidaten in der Kandidatenliste ergänzen, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Dringende Empfehlung:** Routine pausieren oder Intervall auf wöchentlich strecken — die tägliche Zündung erzeugt nur noch Log-Rauschen ohne jeden Ertrag.

## Lauf 2026-08-01 (autonom, zweite Zündung) — Leerlauf, nichts zu tun

**Fünfundzwanzigster Leerlauf in Folge**, zweite Zündung am 2026-08-01. Zustand unverändert; unabhängig gegengeprüft (nicht dem Vorlauf-Log vertraut).

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich in `fertig/` bestätigt: vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json. **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — unabhängig ausgezählt: 87 Einträge, Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**, keine verwaisten `datei`-Verweise. Kein Self-Heal nötig.
- Vorbereitung: `pip install -r requirements.txt` → jsonschema installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet. Bewusst keine Push-Benachrichtigung (identischer, bereits am achten Lauf gemeldeter Zustand — reiner Lärm für den Arzt).

**Für den Arzt:** Unverändert seit dem achten Lauf, jetzt 25 ergebnislose Läufe. Nachschub kann nur ein Mensch liefern — neue Wunschlisten-Einträge über die App, `offen`-Kandidaten in der Kandidatenliste ergänzen, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Dringende Empfehlung:** Routine pausieren oder Intervall auf wöchentlich strecken — die tägliche Zündung erzeugt nur noch Log-Rauschen ohne jeden Ertrag.

## Lauf 2026-08-01 (autonom, dritte Zündung) — Leerlauf, nichts zu tun

**Sechsundzwanzigster Leerlauf in Folge**, dritte Zündung am 2026-08-01. Zustand unverändert; unabhängig gegengeprüft (nicht dem Vorlauf-Log vertraut).

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich in `fertig/` bestätigt: vitis-vinifera → monographie-weinrebe.json (id `vitis-vinifera`), chenopodium-album → monographie-weisser-gaensefuss.json (id `chenopodium-album`), platanus-hispanica → monographie-platane.json (id `platanus-hispanica`). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — unabhängig ausgezählt: 87 Einträge, Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**, keine verwaisten `datei`-Verweise. Kein Self-Heal nötig.
- Vorbereitung: `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet. Bewusst keine Push-Benachrichtigung: identischer Zustand, dem Arzt bereits am achten Lauf gemeldet — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Unverändert seit dem achten Lauf, jetzt 26 ergebnislose Läufe. Nachschub kann nur ein Mensch liefern — neue Wunschlisten-Einträge über die App, `offen`-Kandidaten in der Kandidatenliste ergänzen, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Dringende Empfehlung:** Routine pausieren oder Intervall auf wöchentlich strecken — die tägliche Zündung erzeugt nur noch Log-Rauschen ohne jeden Ertrag.

## Lauf 2026-08-01 (autonom, vierte Zündung) — Leerlauf, nichts zu tun

**Siebenundzwanzigster Leerlauf in Folge**, vierte Zündung am 2026-08-01. Zustand unverändert; unabhängig gegengeprüft (nicht dem Vorlauf-Log vertraut).

- **`docs/wunschliste.json`** (3 Einträge: vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich in `fertig/` bestätigt: vitis-vinifera → monographie-weinrebe.json (id `vitis-vinifera`), chenopodium-album → monographie-weisser-gaensefuss.json (id `chenopodium-album`), platanus-hispanica → monographie-platane.json (id `platanus-hispanica`, Synonyme *Platanus × acerifolia* / *× hybrida*). **0 offene** Wünsche.
- **`kraeuter-kandidaten.json`** — unabhängig ausgezählt: 87 Einträge, Statusverteilung `{'entwurf_fertig': 87}`, **0× `offen`**, keine verwaisten `datei`-Verweise. Kein Self-Heal nötig.
- Vorbereitung: `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container neu installiert.

Keine Monographie erzeugt, `docs/changelog.json` unverändert. **Kein Fehler** — Warteschlange restlos abgearbeitet. Bewusst keine Push-Benachrichtigung: identischer Zustand, dem Arzt bereits am achten Lauf gemeldet — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Unverändert seit dem achten Lauf, jetzt 27 ergebnislose Läufe. Nachschub kann nur ein Mensch liefern — neue Wunschlisten-Einträge über die App, `offen`-Kandidaten in der Kandidatenliste ergänzen, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Dringende Empfehlung:** Routine pausieren oder Intervall auf wöchentlich strecken — die tägliche Zündung erzeugt nur noch Log-Rauschen ohne jeden Ertrag.

## 2026-08-02 — Kein offener Eintrag (Leerlauf)

**Bearbeitet:** — (0 Monographien erzeugt)

**Auswahlprüfung:**
- `docs/wunschliste.json`: 3 Einträge (vitis-vinifera, chenopodium-album, platanus-hispanica) — **alle bereits in `fertig/`** vorhanden (monographie-weinrebe.json, monographie-weisser-gaensefuss.json, monographie-platane.json; id-Abgleich bestätigt). Keine offenen Wünsche.
- `kraeuter-kandidaten.json`: 87 Kandidaten, **alle Status `entwurf_fertig`**, kein einziger `offen`. Nichts zu heilen (keine `offen`-Einträge mit vorhandener Datei).

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung. Lauf sauber beendet — kein Fehler.

**Für den Arzt:** Der Katalog ist aus Sicht der Arbeitswarteschlange vollständig abgearbeitet (alle Kandidaten stehen als Entwurf zur ärztlichen Sichtung bereit). Neue Arbeit entsteht erst, wenn die App neue Einträge in `docs/wunschliste.json` schreibt oder neue `offen`-Kandidaten hinzukommen.

## 2026-08-02 (zweite Zündung desselben Tages) — Leerlauf, Zustand unverändert

**Bearbeitet:** — (0 Monographien). Zweite Routine-Zündung am 2026-08-02; für diesen Tag existiert bereits ein Leerlauf-Eintrag oben.

**Auswahlprüfung (unabhängig gegengeprüft):**
- `docs/wunschliste.json`: 3 Einträge (vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id-Abgleich in `fertig/` bestätigt (monographie-weinrebe.json, monographie-weisser-gaensefuss.json, monographie-platane.json). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig.

**Ergebnis:** Nichts zu tun, Lauf sauber beendet, kein Fehler. Keine Push-Benachrichtigung (identischer, unveränderter Zustand — reines Rauschen).

**Für den Arzt:** Die Routine feuert inzwischen mehrfach pro Tag ohne jeden Ertrag. Neue Arbeit entsteht nur menschlich: Wunschlisten-Einträge über die App, neue `offen`-Kandidaten, oder die 87 Entwürfe sichten und auf `geprueft` setzen. **Dringende Empfehlung weiterhin: Routine pausieren oder Intervall stark strecken.**

## 2026-08-02 (dritte Zündung desselben Tages) — Leerlauf, Zustand unverändert

**Bearbeitet:** — (0 Monographien). Dritte Routine-Zündung am 2026-08-02; zwei Leerlauf-Einträge für diesen Tag stehen bereits oben.

**Auswahlprüfung (unabhängig gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 3 Einträge (vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id-**und** Synonym-Abgleich in `fertig/` bestätigt: vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json (Synonyme *Platanus × acerifolia* / *× hybrida*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `{'entwurf_fertig': 87}`, **0× `offen`**. Kein verwaister `datei`-Verweis, kein Self-Heal nötig.
- Vorbereitung: `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container installiert; Prüfskript lauffähig.

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst keine Push-Benachrichtigung: unveränderter Zustand, dem Arzt vielfach gemeldet — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Weiterhin unverändert — die Routine feuert mehrfach täglich ohne jeden Ertrag. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in der Kandidatenliste, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Dringende Empfehlung weiterhin: Routine pausieren oder Intervall auf wöchentlich strecken.**

## 2026-08-02 (vierte Zündung desselben Tages) — Leerlauf, Zustand unverändert

**Bearbeitet:** — (0 Monographien). Vierte Routine-Zündung am 2026-08-02; drei Leerlauf-Einträge für diesen Tag stehen bereits oben.

**Auswahlprüfung (unabhängig gegengeprüft):**
- `docs/wunschliste.json`: 3 Einträge (vitis-vinifera, chenopodium-album, platanus-hispanica) — alle per id- **und** Synonym-Abgleich in `fertig/` bestätigt: vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json (Synonyme *Platanus × acerifolia* / *× hybrida*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `{'entwurf_fertig': 87}`, **0× `offen`**. Kein verwaister `datei`-Verweis, kein Self-Heal nötig.
- Vorbereitung: `pip install -r requirements.txt` → jsonschema vorhanden, Prüfskript lauffähig (nicht ausgeführt, da nichts erzeugt).

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst keine Push-Benachrichtigung: unveränderter Zustand, vielfach gemeldet.

**Für den Arzt:** Unverändert. Die Routine feuert weiterhin mehrfach täglich ohne Ertrag. Nachschub nur menschlich: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten, oder die 87 Entwürfe sichten und auf `geprueft` setzen. **Dringende Empfehlung weiterhin: Routine pausieren oder Intervall auf wöchentlich strecken.**

## 2026-08-03 — Leerlauf, Zustand unverändert

**Bearbeitet:** — (0 Monographien). Erste Routine-Zündung am 2026-08-03.

**Vorbereitung:** `pip install -r requirements.txt` → jsonschema vorhanden, Prüfskript lauffähig (nicht ausgeführt, da nichts erzeugt).

**Auswahlprüfung (unabhängig gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 3 Einträge (vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id-Abgleich direkt aus den Zieldateien in `fertig/` bestätigt: vitis-vinifera → monographie-weinrebe.json (id `vitis-vinifera`), chenopodium-album → monographie-weisser-gaensefuss.json (id `chenopodium-album`), platanus-hispanica → monographie-platane.json (id `platanus-hispanica`, Synonyme *Platanus × acerifolia* / *× hybrida*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `{'entwurf_fertig': 87}`, **0× `offen`**. Kein verwaister `datei`-Verweis, kein Self-Heal nötig.

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst keine Push-Benachrichtigung: unveränderter Zustand, dem Arzt bereits vielfach gemeldet — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Unverändert seit dem 2026-08-01/02. Die Routine feuert weiterhin ohne Ertrag. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in der Kandidatenliste, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Dringende Empfehlung weiterhin: Routine pausieren oder Intervall auf wöchentlich strecken.**

## 2026-08-03 (zweite Zündung desselben Tages) — Leerlauf, Zustand unverändert

**Bearbeitet:** — (0 Monographien). Weitere Routine-Zündung am 2026-08-03; ein Leerlauf-Eintrag für diesen Tag steht bereits oben.

**Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 im frischen Container installiert; Prüfskript lauffähig (nicht ausgeführt, da nichts erzeugt).

**Auswahlprüfung (unabhängig gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 3 Einträge (vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id-Abgleich direkt aus den Zieldateien in `fertig/` bestätigt: vitis-vinifera → monographie-weinrebe.json (id `vitis-vinifera`), chenopodium-album → monographie-weisser-gaensefuss.json (id `chenopodium-album`), platanus-hispanica → monographie-platane.json (id `platanus-hispanica`, Synonyme *Platanus × acerifolia* / *× hybrida*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `{'entwurf_fertig': 87}`, **0× `offen`**. Kein verwaister `datei`-Verweis, kein Self-Heal nötig.

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst keine Push-Benachrichtigung: unveränderter Zustand, dem Arzt bereits vielfach gemeldet — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Unverändert seit 2026-08-01. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in der Kandidatenliste, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Dringende Empfehlung weiterhin: Routine pausieren oder Intervall auf wöchentlich strecken.**

## 2026-08-03 (dritte Zündung desselben Tages) — Leerlauf, Zustand unverändert

**Bearbeitet:** — (0 Monographien). Weitere Routine-Zündung am 2026-08-03; zwei Leerlauf-Einträge für diesen Tag stehen bereits oben.

**Vorbereitung:** `pip install -r requirements.txt` → jsonschema vorhanden, Prüfskript lauffähig (nicht ausgeführt, da nichts erzeugt).

**Auswahlprüfung (unabhängig gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 3 Einträge (vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id-Abgleich direkt aus den Zieldateien in `fertig/` bestätigt: vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json (Synonyme *Platanus × acerifolia* / *× hybrida*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `{'entwurf_fertig': 87}`, **0× `offen`**. Kein verwaister `datei`-Verweis (alle 87 Zieldateien existieren), kein Self-Heal nötig.

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst keine Push-Benachrichtigung: unveränderter Zustand, dem Arzt bereits vielfach gemeldet — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Unverändert seit 2026-08-01. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in der Kandidatenliste, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Dringende Empfehlung weiterhin: Routine pausieren oder Intervall auf wöchentlich strecken.**

## 2026-08-03 (vierte Zündung desselben Tages) — Leerlauf, Zustand unverändert

**Bearbeitet:** — (0 Monographien). Vierte Routine-Zündung am 2026-08-03; drei Leerlauf-Einträge für diesen Tag stehen bereits oben.

**Vorbereitung:** `pip install -r requirements.txt` → jsonschema vorhanden, Prüfskript lauffähig (nicht ausgeführt, da nichts erzeugt).

**Auswahlprüfung (unabhängig gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 3 Einträge (vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich direkt aus den Zieldateien in `fertig/` bestätigt: vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json (Synonyme *Platanus × acerifolia* / *× hybrida*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `{'entwurf_fertig': 87}`, **0× `offen`**. Kein verwaister `datei`-Verweis, kein Self-Heal nötig.

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst keine Push-Benachrichtigung: unveränderter, gesunder Zustand, dem Arzt bereits vielfach gemeldet — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Unverändert seit 2026-08-01. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in der Kandidatenliste, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Dringende Empfehlung weiterhin: Routine pausieren oder Intervall auf wöchentlich strecken.**

## 2026-08-04 — Leerlauf, Zustand unverändert

**Bearbeitet:** — (0 Monographien). Erste Routine-Zündung am 2026-08-04; vier Leerlauf-Einträge vom 2026-08-03 stehen bereits oben.

**Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 installiert, Prüfskript lauffähig (nicht ausgeführt, da nichts erzeugt).

**Auswahlprüfung (unabhängig gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 3 Einträge (vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich direkt aus den Zieldateien in `fertig/` bestätigt: vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json (Synonyme *Platanus × acerifolia* / *× hybrida*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `{'entwurf_fertig': 87}`, **0× `offen`**. Alle 87 Zieldateien existieren, kein verwaister `datei`-Verweis, kein Self-Heal nötig.

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst keine Push-Benachrichtigung: unveränderter, gesunder Zustand, dem Arzt bereits fünfmal in Folge gemeldet — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Unverändert seit 2026-08-01. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in der Kandidatenliste, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Dringende Empfehlung weiterhin: Routine pausieren oder Intervall auf wöchentlich strecken.**

## 2026-08-04 (zweite Zündung desselben Tages) — Leerlauf, Zustand unverändert

**Bearbeitet:** — (0 Monographien). Zweite Routine-Zündung am 2026-08-04; ein Leerlauf-Eintrag vom selben Tag steht bereits oben.

**Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0 installiert, Prüfskript lauffähig (nicht ausgeführt, da nichts erzeugt).

**Auswahlprüfung (unabhängig gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 3 Einträge (vitis-vinifera, chenopodium-album, platanus-hispanica) — alle drei per id- **und** Synonym-Abgleich direkt aus den Zieldateien in `fertig/` bestätigt: vitis-vinifera → monographie-weinrebe.json, chenopodium-album → monographie-weisser-gaensefuss.json, platanus-hispanica → monographie-platane.json (Synonyme *Platanus × acerifolia* / *× hybrida*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `{'entwurf_fertig': 87}`, **0× `offen`**. Alle 87 Zieldateien existieren, kein verwaister `datei`-Verweis, kein Self-Heal nötig.

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst keine Push-Benachrichtigung: unveränderter, gesunder Zustand, dem Arzt bereits sechsmal in Folge gemeldet — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Unverändert seit 2026-08-01. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in der Kandidatenliste, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Dringende Empfehlung weiterhin: Routine pausieren oder Intervall auf wöchentlich strecken.**

## 2026-08-04 (dritte Zündung) — 2 Monographien gebaut (endlich Nachschub aus der Wunschliste)

**Bearbeitet:** 2 Monographien, **beide aus der Wunschliste** (`docs/wunschliste.json`). Nach sechs Leerlauf-Zündungen in Folge hat die App zwei **neue** Wünsche eingespielt:
- `agastache-mexicana` — Mexikanische Duftnessel → `fertig/monographie-mexikanische-duftnessel.json`
- `cherry-laurel` → aufgelöst zu **Prunus laurocerasus** (Kirschlorbeer) → `fertig/monographie-kirschlorbeer.json`

**Vorbereitung:** `pip install -r requirements.txt` → jsonschema 4.26.0. Dedup gegen `fertig/` (id + `botany.synonyms`) und `vorhanden`: beide Arten neu, keine Dublette. Kandidatenliste unverändert (keine Kandidaten-Kräuter in diesem Lauf → keine Statusänderung dort).

**Prüfung:** `validate_monographie.py` — beide **fehlerfrei**. Duftnessel mit einem `! Hinweis` (enthält bewusst 'unsicher — zu prüfen'; positiv). Kirschlorbeer „✓ alles sauber". Je 1 Versuch, keine Korrekturschleifen.

**Verwendete Hauptquellen:**
- Agastache mexicana: Übersichtsarbeit PMC8234942 (2021); ethnopharmakologische Studien zu Tilianin (anxiolytisch/sedierend, GABAA/BZD, MAO-Hemmung); Öl-Studie Pharmaceutical Biology 2016. **Keine** EMA/HMPC-, ESCOP- oder Kommission-E-Monographie erreichbar/existent → Evidenz nur TRAD/präklinisch.
- Prunus laurocerasus: **EMA/CVMP MRL-Summary-Report** (cyanogene Glykoside 1–2,5 %; ~50–210 mg HCN/100 g frische Blätter; Aqua-Laurocerasi-Letaldosis ~60 mg; Prunasin-LD50 Ratte) + Giftinfo-/Gartenbau-Quellen zur Blatt-Verwechslung mit Laurus nobilis.

**Überraschungen / unsichere Stellen — bitte ärztlich prüfen:**
1. **Wunschlisten-Datenqualität (wichtig):** Der Eintrag `cherry-laurel` hatte eine **Platzhalter-`id`** ("cherry-laurel", kein `gattung-art`) und ein Platzhalter-`latin` ("Cherry laurel" = nur der englische Trivialname). Ich habe ihn zum akzeptierten botanischen Namen **Prunus laurocerasus** aufgelöst und die Datei entsprechend mit `id: prunus-laurocerasus` angelegt. → Die App hakt Wünsche über den Abgleich mit `fertig/` ab; falls sie strikt auf die Wunsch-`id` "cherry-laurel" matcht, wird dieser Wunsch evtl. **nicht automatisch abgehakt**. Bitte im App-Abgleich beachten / Wunsch-id nachziehen.
2. **Kirschlorbeer ist als WARNEINTRAG angelegt** (`not_for_use`, `indications: []`), obwohl er nicht in der offiziellen Warnpflanzen-Liste (tier 3) der Kandidaten steht. Begründung: cyanogene Giftpflanze ohne legitime moderne Selbstanwendung; die historische Aqua Laurocerasi ist obsolet. Die sicherheitskritische Kernaussage ist die **Blatt-Verwechslung mit echtem Küchenlorbeer (Laurus nobilis)** — das begründet die Aufnahme trotz „keine Heilpflanze".
3. **HCN-/Letaldosis-Zahlen streuen stark** (Blattalter, Jahreszeit) — im tox_ceiling bewusst als Warngrößen, nicht als „sichere Restmenge" formuliert. `raw_toxicity`-Flag gesetzt (Erhitzen macht das Blatt nicht sicher).
4. **Agastache — Erwartungsdämpfung:** Die kursierenden anxiolytischen/antihypertensiven/antidepressiven Effekte sind **rein präklinisch** (Ratte/Meerschweinchen). Kein Humanbeleg, keine Zulassung. Zusätzlich chemotyp-abhängiger **Pulegon/Estragol**-Gehalt im ätherischen Öl (unsicher) → konzentrierte Ölform und Schwangerschaft im Text als zu meiden markiert. Theoretische MAO-/serotonerge Interaktion (gering, unbelegt) vermerkt.

**Commit:** Monographien + `docs/changelog.json` + dieses Log zusammen. Push auf den Arbeitsbranch. **Kein** Status in `kraeuter-kandidaten.json` geändert (kein Kandidaten-Kraut bearbeitet). Push-Benachrichtigung an den Arzt: **ja** — nach langem Leerlauf wieder echter Nachschub, und Punkt 1 (Wunsch-id-Diskrepanz) braucht seine Aufmerksamkeit.

## 2026-08-04 (vierte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (unabhängig gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`). Beide per id- **und** Synonym-Abgleich direkt aus den Zieldateien in `fertig/` als **bereits erfüllt** bestätigt:
  - `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id exakt gleich).
  - `cherry-laurel` → aufgelöst zu **Prunus laurocerasus** → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme *Laurocerasus officinalis* / *Cerasus laurocerasus* / *Padus laurocerasus*). Beide wurden in der dritten Zündung (Commit `9376a80`) gebaut. **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig (kein `offen`-Kandidat, dessen Datei existiert).

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Arbeitsbaum vor diesem Log-Eintrag sauber. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung: unveränderter, gesunder Zustand; der eigentliche Nachschub (die 2 neuen Monographien) wurde bereits in der dritten Zündung gemeldet — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Unverändert seit der dritten Zündung. Die Wunschliste zeigt noch die 2 Einträge, die die App erst beim nächsten Abgleich mit `fertig/` abhakt (Schreibrichtung: nur die App); das ist erwartetes Verhalten, kein Fehler. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten, oder die fertigen Entwürfe sichten und auf `geprueft` setzen. Erinnerung an Punkt 1 der dritten Zündung: die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, bitte diesen Wunsch manuell abhaken.

## 2026-08-05 — Leerlauf: nichts zu tun

**Auswahlprüfung (unabhängig gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`). Beide per id- **und** Synonym-Abgleich direkt aus den Zieldateien in `fertig/` als **bereits erfüllt** bestätigt:
  - `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id exakt `agastache-mexicana`).
  - `cherry-laurel` → aufgelöst zu **Prunus laurocerasus** → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme *Laurocerasus officinalis* / *Cerasus laurocerasus* / *Padus laurocerasus*; Warneintrag `not_for_use=true`). Beide in der dritten Zündung am 2026-08-04 (Commit `9376a80`) gebaut. **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig (kein `offen`-Kandidat, dessen Datei existiert).

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Arbeitsbaum vor diesem Log-Eintrag sauber. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung: unveränderter, gesunder Zustand; der eigentliche Nachschub (die 2 neuen Monographien) wurde bereits in der dritten Zündung gemeldet — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Unverändert seit der dritten Zündung (2026-08-04). Die Wunschliste zeigt noch die 2 Einträge, die die App erst beim nächsten Abgleich mit `fertig/` abhakt (Schreibrichtung: nur die App) — erwartetes Verhalten, kein Fehler. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen (aus 3. Zündung, Punkt 1): die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.

## 2026-08-05 (zweite Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (unabhängig gegengeprüft — Dateien direkt gelesen, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`). Beide per **id- und Synonym-Abgleich gegen die tatsächlichen Zieldateien** als erfüllt bestätigt:
  - `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json`, `id` exakt `agastache-mexicana` (sci: *Agastache mexicana (Kunth) Lint & Epling*; Synonyme *Cedronella mexicana* / *Brittonastrum mexicanum* eingetragen).
  - `cherry-laurel` → aufgelöst zu **Prunus laurocerasus** → `fertig/monographie-kirschlorbeer.json`, `id` `prunus-laurocerasus`, Synonyme *Laurocerasus officinalis* / *Cerasus laurocerasus* / *Padus laurocerasus*; Warneintrag `not_for_use=true`. **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `Counter({'entwurf_fertig': 87})`, **0× `offen`**. Kein Self-Heal nötig.

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung: unveränderter, gesunder Zustand; der letzte echte Nachschub wurde in der dritten Zündung (2026-08-04, Commit `9376a80`) gemeldet, eine Wiederholung wäre reines Rauschen.

**Für den Arzt (unverändert, aber weiterhin relevant):** Die Routine fährt jetzt mehrere Zündungen in Folge leer. Nachschub kann nur ein Mensch liefern — neue Wunschlisten-Einträge, neue `offen`-Kandidaten, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Offener Punkt aus der dritten Zündung: die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Empfehlung: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-05 (dritte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Dateien direkt gegengeprüft):**
- `docs/wunschliste.json`: 2 Einträge, beide per id- **und** Synonym-Abgleich in `fertig/` erfüllt — `agastache-mexicana` → `monographie-mexikanische-duftnessel.json`; `cherry-laurel` → *Prunus laurocerasus* → `monographie-kirschlorbeer.json`. **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87× `entwurf_fertig`, **0× `offen`**. Kein Self-Heal nötig.

**Ergebnis:** Kein Bau, keine Prüfung, keine Statusänderung. `changelog.json` unverändert. Sauber beendet, kein Fehler. Bewusst **keine** Push-Benachrichtigung (unveränderter, gesunder Zustand). Empfehlung an den Arzt unverändert: Routine-Intervall strecken/pausieren bis Nachschub (neue Wünsche, neue `offen`-Kandidaten, oder Entwürfe sichten). Weiterhin offen: Wunsch-`id` `cherry-laurel` ≠ Datei-`id` `prunus-laurocerasus` — falls die App strikt matcht, manuell abhaken.

## 2026-08-05 (vierte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Dateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge, beide per id- **und** Synonym-Abgleich in `fertig/` als erfüllt bestätigt — `agastache-mexicana` → `monographie-mexikanische-duftnessel.json` (id exakt gleich); `cherry-laurel` → *Prunus laurocerasus* → `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme *Laurocerasus officinalis* / *Cerasus laurocerasus* / *Padus laurocerasus*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87× `entwurf_fertig`, **0× `offen`** (ausgezählt). Kein Self-Heal nötig.

**Ergebnis:** Kein Bau, keine Prüfung, keine Statusänderung. `docs/changelog.json` unverändert. Sauber beendet, kein Fehler. Bewusst **keine** Push-Benachrichtigung — unveränderter, gesunder Zustand; der letzte echte Nachschub wurde in der dritten Zündung (2026-08-04, Commit `9376a80`) gemeldet.

**Für den Arzt:** Fünfter Leerlauf in Folge. Nachschub kann nur ein Mensch liefern (neue Wunschlisten-Einträge, neue `offen`-Kandidaten, oder die 87 Entwürfe sichten und auf `geprueft` setzen). Weiterhin offen: Wunsch-`id` `cherry-laurel` ≠ Datei-`id` `prunus-laurocerasus` — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Dringende Empfehlung: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-06 — Leerlauf: nichts zu tun

**Auswahlprüfung (Dateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`). Beide per id- **und** Synonym-Abgleich direkt aus den Zieldateien in `fertig/` als **bereits erfüllt** bestätigt:
  - `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id exakt `agastache-mexicana`; sci *Agastache mexicana (Kunth) Lint & Epling*, Synonyme *Cedronella mexicana* / *Brittonastrum mexicanum* eingetragen).
  - `cherry-laurel` → aufgelöst zu **Prunus laurocerasus** → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme *Laurocerasus officinalis* / *Cerasus laurocerasus* / *Padus laurocerasus*; Warneintrag `not_for_use=true`). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig (kein `offen`-Kandidat, dessen Datei existiert).

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Arbeitsbaum vor diesem Log-Eintrag sauber. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung: unveränderter, gesunder Zustand; der letzte echte Nachschub (die 2 neuen Monographien) wurde in der dritten Zündung am 2026-08-04 (Commit `9376a80`) gemeldet — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Sechster Leerlauf in Folge, unverändert seit dem 2026-08-04. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen (aus der 3. Zündung, Punkt 1): die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Dringende Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-06 (zweite Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Dateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`). Beide per id- **und** Synonym-Abgleich direkt aus den Zieldateien in `fertig/` als **bereits erfüllt** bestätigt:
  - `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id exakt `agastache-mexicana`; sci *Agastache mexicana (Kunth) Lint & Epling*).
  - `cherry-laurel` → **Prunus laurocerasus** → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme *Laurocerasus officinalis* / *Cerasus laurocerasus* / *Padus laurocerasus*; `not_for_use=true`). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `{'entwurf_fertig': 87}`, **0× `offen`**. Kein Self-Heal nötig.

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung: unveränderter, gesunder Zustand seit 2026-08-04 (letzter echter Nachschub Commit `9376a80`) — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Siebter Leerlauf in Folge, weiterhin unverändert. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen: die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Dringende Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-06 (dritte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Dateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`). Beide per id- **und** Synonym-Abgleich direkt aus den Zieldateien in `fertig/` als **bereits erfüllt** bestätigt:
  - `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id exakt `agastache-mexicana`; sci *Agastache mexicana (Kunth) Lint & Epling*, Synonyme *Cedronella mexicana* / *Brittonastrum mexicanum* / *Cedronella mexicana (Kunth) Benth.*).
  - `cherry-laurel` → aufgelöst zu **Prunus laurocerasus** → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme *Laurocerasus officinalis* / *Cerasus laurocerasus* / *Padus laurocerasus*; Warneintrag `not_for_use=true`). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `Counter({'entwurf_fertig': 87})`, **0× `offen`**. Kein Self-Heal nötig (kein `offen`-Kandidat, dessen Datei existiert).

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung: unveränderter, gesunder Zustand seit 2026-08-04 (letzter echter Nachschub Commit `9376a80`) — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Achter Leerlauf in Folge, unverändert seit 2026-08-04. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen: die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Dringende Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-07 — Leerlauf: nichts zu tun

**Auswahlprüfung (Dateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`). Beide per id- **und** Synonym-Abgleich direkt aus den Zieldateien in `fertig/` als **bereits erfüllt** bestätigt:
  - `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id exakt `agastache-mexicana`).
  - `cherry-laurel` → aufgelöst zu **Prunus laurocerasus** → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`; Synonyme *Laurocerasus officinalis M.Roem.* / *Cerasus laurocerasus (L.) Loisel.* / *Padus laurocerasus (L.) Mill.* direkt in der Datei verifiziert; Warneintrag `not_for_use=true`). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `Counter({'entwurf_fertig': 87})`, **0× `offen`**. Kein Self-Heal nötig (kein `offen`-Kandidat, dessen Datei existiert). `fertig/` enthält 118 Monographien.

**Ergebnis:** Weder Wunschliste noch Kandidatenliste liefern offene Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung: unveränderter, gesunder Zustand seit 2026-08-04 (letzter echter Nachschub Commit `9376a80`) — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Neunter Leerlauf in Folge, unverändert seit 2026-08-04. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen: die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Dringende Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-07 (zweite Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Dateien direkt gegengeprüft):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`) — beide per id- **und** Synonym-Abgleich in `fertig/` als **bereits erfüllt** bestätigt (`monographie-mexikanische-duftnessel.json` → id `agastache-mexicana`; `monographie-kirschlorbeer.json` → id `prunus-laurocerasus`, Synonyme *Laurocerasus officinalis* / *Cerasus laurocerasus* / *Padus laurocerasus*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, `Counter({'entwurf_fertig': 87})`, **0× `offen`**. Kein Self-Heal nötig. `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten aus beiden Quellen. Kein Bau, keine Prüfung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler. Keine Push-Benachrichtigung (unveränderter, gesunder Zustand seit 2026-08-04; Wiederholung wäre Rauschen).

**Für den Arzt:** Zehnter Leerlauf in Folge. Nachschub kann nur ein Mensch liefern (neue Wunsch-/`offen`-Einträge oder die 87 Entwürfe auf `geprueft` setzen). Weiterhin offen: Wunsch-`id` `cherry-laurel` ≠ Datei-`id` `prunus-laurocerasus` — bei striktem App-Matching bitte manuell abhaken. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-07 (dritte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Dateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`) — beide per id- **und** Synonym-Abgleich direkt aus den Zieldateien in `fertig/` als **bereits erfüllt** bestätigt: `monographie-mexikanische-duftnessel.json` (id `agastache-mexicana`, sci *Agastache mexicana (Kunth) Lint & Epling*) und `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme *Laurocerasus officinalis* / *Cerasus laurocerasus* / *Padus laurocerasus*, Warneintrag `not_for_use=true`). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `Counter({'entwurf_fertig': 87})`, **0× `offen`**. Kein `offen`-Kandidat mit fehlender Datei → kein Self-Heal nötig. `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten aus beiden Quellen. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung: unveränderter, gesunder Zustand seit 2026-08-04 — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Elfter Leerlauf in Folge, unverändert seit 2026-08-04. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen: die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Dringende Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-07 (vierte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Dateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`) — beide per id- **und** Synonym-Abgleich direkt aus den Zieldateien in `fertig/` als **bereits erfüllt** bestätigt: `monographie-mexikanische-duftnessel.json` (id `agastache-mexicana`, sci *Agastache mexicana (Kunth) Lint & Epling*) und `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme *Laurocerasus officinalis M.Roem.* / *Cerasus laurocerasus (L.) Loisel.* / *Padus laurocerasus (L.) Mill.*, Warneintrag `not_for_use=true`). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `{'entwurf_fertig': 87}`, **0× `offen`**. Kein `offen`-Kandidat mit existierender Datei → kein Self-Heal nötig. `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten aus beiden Quellen. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung: unveränderter, gesunder Zustand seit 2026-08-04 (letzter echter Nachschub Commit `9376a80`) — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Zwölfter Leerlauf in Folge, unverändert seit 2026-08-04. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen: die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Dringende Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-08 — Leerlauf: nichts zu tun

**Auswahlprüfung (Dateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`) — beide per id- **und** Synonym-Abgleich direkt aus den Zieldateien in `fertig/` als **bereits erfüllt** bestätigt: `monographie-mexikanische-duftnessel.json` (id `agastache-mexicana`) und `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`; `cherry-laurel` botanisch = *Prunus laurocerasus*, Warneintrag `not_for_use=true`). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `Counter({'entwurf_fertig': 87})`, **0× `offen`**. Kein `offen`-Kandidat mit existierender Datei → kein Self-Heal nötig. `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten aus beiden Quellen. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung: unveränderter, gesunder Zustand seit 2026-08-04 (letzter echter Nachschub Commit `9376a80`) — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Dreizehnter Leerlauf in Folge, unverändert seit 2026-08-04. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen: die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Dringende Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-08 (zweite Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Dateien direkt gegengeprüft):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`) — beide per id- **und** Synonym-Abgleich direkt aus `fertig/` als **bereits erfüllt** bestätigt: `monographie-mexikanische-duftnessel.json` (id `agastache-mexicana`) und `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`; `cherry-laurel` botanisch = *Prunus laurocerasus*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, `Counter({'entwurf_fertig': 87})`, **0× `offen`**. Kein Self-Heal nötig. `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten aus beiden Quellen. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Zweite Zündung desselben Tages — Zustand identisch zu Commit `61b7a73`. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung: unveränderter, gesunder Zustand seit 2026-08-04 (Nachschub `9376a80`) — Wiederholung wäre reines Rauschen.

**Für den Arzt:** Vierzehnter Leerlauf in Folge, unverändert seit 2026-08-04. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen: die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Dringende Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-08 (dritte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Dateien direkt gegengeprüft):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`) — beide per id- **und** Synonym-Abgleich direkt aus `fertig/` als **bereits erfüllt** bestätigt: `monographie-mexikanische-duftnessel.json` (id `agastache-mexicana`, sci *Agastache mexicana (Kunth) Lint & Epling*) und `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme *Laurocerasus officinalis* / *Cerasus laurocerasus* / *Padus laurocerasus*; `cherry-laurel` botanisch = *Prunus laurocerasus*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, `Counter({'entwurf_fertig': 87})`, **0× `offen`**. Kein `offen`-Kandidat mit existierender Datei → kein Self-Heal nötig. `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten aus beiden Quellen. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung: unveränderter, gesunder Zustand seit 2026-08-04 (letzter echter Nachschub Commit `9376a80`) — Wiederholung wäre reines Rauschen.

**Für den Arzt:** Fünfzehnter Leerlauf in Folge, unverändert seit 2026-08-04. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen: die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Dringende Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-08 (vierte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Dateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`) — beide per id- **und** Synonym-Abgleich direkt aus den Zieldateien in `fertig/` als **bereits erfüllt** bestätigt: `monographie-mexikanische-duftnessel.json` (id `agastache-mexicana`, sci *Agastache mexicana (Kunth) Lint & Epling*) und `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme *Laurocerasus officinalis M.Roem.* / *Cerasus laurocerasus (L.) Loisel.* / *Padus laurocerasus (L.) Mill.*; `cherry-laurel` botanisch = *Prunus laurocerasus*, Warneintrag `not_for_use=true`). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `Counter({'entwurf_fertig': 87})`, **0× `offen`**. Kein `offen`-Kandidat mit fehlender Datei → kein Self-Heal nötig. `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten aus beiden Quellen. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung: unveränderter, gesunder Zustand seit 2026-08-04 (letzter echter Nachschub Commit `9376a80`) — eine Wiederholung wäre reines Rauschen.

**Für den Arzt:** Sechzehnter Leerlauf in Folge, unverändert seit 2026-08-04. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen: die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Dringende Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-09 — Leerlauf: nichts zu tun

**Auswahlprüfung (Dateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`) — beide per id- **und** Synonym-Abgleich direkt aus den Zieldateien in `fertig/` als **bereits erfüllt** bestätigt: `monographie-mexikanische-duftnessel.json` (id `agastache-mexicana`, sci *Agastache mexicana (Kunth) Lint & Epling*) und `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme *Laurocerasus officinalis M.Roem.* / *Cerasus laurocerasus (L.) Loisel.* / *Padus laurocerasus (L.) Mill.*; `cherry-laurel` botanisch = *Prunus laurocerasus*, Warneintrag `not_for_use=true`). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `Counter({'entwurf_fertig': 87})`, **0× `offen`**. Kein `offen`-Kandidat mit fehlender Datei → kein Self-Heal nötig. `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten aus beiden Quellen. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung: unveränderter, gesunder Zustand seit 2026-08-04 (letzter echter Nachschub Commit `9376a80`) — eine Wiederholung wäre reines Rauschen. Die Routine-Schedule ändere ich nicht eigenmächtig (nur auf ausdrücklichen Wunsch des Arztes).

**Für den Arzt:** Siebzehnter Leerlauf in Folge, unverändert seit 2026-08-04. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen: die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Dringende Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-09 (zweite Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Quelldateien direkt gegengeprüft):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`) — beide per id-/Synonym-Abgleich aus `fertig/` als **bereits erfüllt** bestätigt (`monographie-mexikanische-duftnessel.json` = id `agastache-mexicana`; `monographie-kirschlorbeer.json` = id `prunus-laurocerasus`, `cherry-laurel` botanisch = *Prunus laurocerasus*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau, kein Self-Heal. `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten aus beiden Quellen. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung (unveränderter, gesunder Zustand seit 2026-08-04 — Wiederholung wäre Rauschen). Routine-Schedule bleibt unangetastet (nur auf ausdrücklichen ärztlichen Wunsch ändern).

**Für den Arzt:** Achtzehnter Leerlauf in Folge, unverändert seit 2026-08-04. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-09 (dritte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Quelldateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`) — beide per id-/Synonym-Abgleich aus `fertig/` als **bereits erfüllt** bestätigt: `monographie-mexikanische-duftnessel.json` (id `agastache-mexicana`) und `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`; `cherry-laurel` botanisch = *Prunus laurocerasus*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau, kein Self-Heal. `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Bewusst **keine** Push-Benachrichtigung (unveränderter, gesunder Zustand seit 2026-08-04 — Wiederholung wäre Rauschen). Routine-Schedule bleibt unangetastet (nur auf ausdrücklichen ärztlichen Wunsch ändern).

**Für den Arzt:** Neunzehnter Leerlauf in Folge, unverändert seit 2026-08-04. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen: die Wunsch-`id` `cherry-laurel` ≠ Datei-`id` `prunus-laurocerasus` — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-09 (vierte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Quelldateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`) — beide per id-/Synonym-Abgleich aus `fertig/` als **bereits erfüllt** bestätigt: `monographie-mexikanische-duftnessel.json` (id `agastache-mexicana`, sci *Agastache mexicana (Kunth) Lint & Epling*) und `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`; `cherry-laurel` botanisch = *Prunus laurocerasus*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau, kein Self-Heal. `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten aus beiden Quellen. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Routine-Schedule bleibt unangetastet (nur auf ausdrücklichen ärztlichen Wunsch ändern).

**Für den Arzt:** Zwanzigster Leerlauf in Folge, unverändert seit 2026-08-04. Da die bisherigen 19 Leerläufe bewusst **ohne** Push-Benachrichtigung blieben und der Zustand sich über mehrere Tage nicht bewegt hat, gehe ich davon aus, dass die leere Warteschlange noch nicht bemerkt wurde — daher **diesmal einmalig eine Push-Benachrichtigung**, damit die Info das Telefon erreicht (das Log allein wird offenbar nicht gelesen). Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen: die Wunsch-`id` `cherry-laurel` ≠ Datei-`id` `prunus-laurocerasus` — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Dringende Empfehlung: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-10 — Leerlauf: nichts zu tun

**Auswahlprüfung (Quelldateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`) — beide per id-/Synonym-Abgleich direkt aus `fertig/` als **bereits erfüllt** bestätigt: `monographie-mexikanische-duftnessel.json` (id `agastache-mexicana`, sci *Agastache mexicana (Kunth) Lint & Epling*) und `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme u. a. *Laurocerasus officinalis M.Roem.*; `cherry-laurel` botanisch = *Prunus laurocerasus*, Warneintrag `not_for_use=true`). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau, kein Self-Heal. `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten aus beiden Quellen. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Routine-Schedule bleibt unangetastet (nur auf ausdrücklichen ärztlichen Wunsch ändern).

**Push-Benachrichtigung:** Bewusst **keine**. Beim 20. Leerlauf (2026-08-09, vierte Zündung) ist bereits **einmalig** eine Push-Info über die leere Warteschlange aufs Telefon gegangen; der Zustand ist seither unverändert. Eine zweite identische Meldung wäre reines Rauschen — Schweigen ist hier die richtige Wahl.

**Für den Arzt:** Einundzwanzigster Leerlauf in Folge, unverändert seit 2026-08-04 (letzter echter Nachschub Commit `9376a80`). Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen (rein informativ): die Wunsch-`id` `cherry-laurel` weicht von der Datei-`id` `prunus-laurocerasus` ab — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-10 (zweite Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Quelldateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge (`agastache-mexicana`, `cherry-laurel`) — beide per id-/Synonym-Abgleich direkt aus `fertig/` als **bereits erfüllt** bestätigt: `monographie-mexikanische-duftnessel.json` (id `agastache-mexicana`) und `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`; `cherry-laurel` botanisch = *Prunus laurocerasus*). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau, kein Self-Heal. `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten aus beiden Quellen. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Routine-Schedule bleibt unangetastet (nur auf ausdrücklichen ärztlichen Wunsch ändern).

**Push-Benachrichtigung:** Bewusst **keine**. Der Zustand ist seit 2026-08-04 unverändert; am 20. Leerlauf (2026-08-09, vierte Zündung) ging bereits **einmalig** eine Push-Info aufs Telefon. Eine Wiederholung wäre reines Rauschen — Schweigen ist korrekt.

**Für den Arzt:** Zweiundzwanzigster Leerlauf in Folge, unverändert seit 2026-08-04 (letzter echter Nachschub Commit `9376a80`). Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Weiterhin offen (rein informativ): die Wunsch-`id` `cherry-laurel` ≠ Datei-`id` `prunus-laurocerasus` — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-10 (dritte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Quelldateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut):**
- `docs/wunschliste.json`: 2 Einträge — beide bereits in `fertig/`: `agastache-mexicana` → `monographie-mexikanische-duftnessel.json`; `cherry-laurel` (botanisch *Prunus laurocerasus*) → `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: ausgezählt `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau, kein Self-Heal. `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**.

**Push-Benachrichtigung:** Bewusst **keine**. Zustand unverändert seit 2026-08-04; am 20. Leerlauf (2026-08-09) ging bereits einmalig eine Push-Info raus. Wiederholung wäre Rauschen.

**Für den Arzt:** 23. Leerlauf in Folge, unverändert seit 2026-08-04 (letzter echter Nachschub Commit `9376a80`). Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten, oder die 87 Entwürfe sichten und auf `geprueft` setzen. Rein informativ: Wunsch-`id` `cherry-laurel` ≠ Datei-`id` `prunus-laurocerasus` — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-10 (vierte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Quelldateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut, 2026-08-10T18:16:42Z):**
- `docs/wunschliste.json`: 2 Einträge — beide per id-/Synonym-Abgleich direkt aus `fertig/` als **bereits erfüllt** bestätigt: `agastache-mexicana` → `monographie-mexikanische-duftnessel.json` (id `agastache-mexicana`); `cherry-laurel` (botanisch *Prunus laurocerasus*) → `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme geprüft). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau, kein Self-Heal (Self-Heal betrifft nur `offen`-Einträge). `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten aus beiden Quellen. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Routine-Schedule bleibt unangetastet.

**Push-Benachrichtigung:** Bewusst **keine**. Zustand unverändert seit 2026-08-04; am 20. Leerlauf (2026-08-09) ging bereits **einmalig** eine Push-Info aufs Telefon. Eine Wiederholung wäre reines Rauschen — Schweigen ist korrekt.

**Für den Arzt:** 24. Leerlauf in Folge, unverändert seit 2026-08-04 (letzter echter Nachschub Commit `9376a80`). Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Rein informativ (unverändert): Wunsch-`id` `cherry-laurel` ≠ Datei-`id` `prunus-laurocerasus` — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-11 — Leerlauf: nichts zu tun

**Auswahlprüfung (Quelldateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut, 2026-08-11T00:21:13Z):**
- `docs/wunschliste.json`: 2 Einträge — beide per id-/Synonym-Abgleich direkt aus `fertig/` als **bereits erfüllt** bestätigt: `agastache-mexicana` → `monographie-mexikanische-duftnessel.json` (id `agastache-mexicana`); `cherry-laurel` (botanisch *Prunus laurocerasus*) → `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme geprüft). **0 offene Wünsche.**
- `kraeuter-kandidaten.json`: 87 Einträge, ausgezählt `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau, kein Self-Heal (Self-Heal betrifft nur `offen`-Einträge). `fertig/` = 118 Dateien.

**Ergebnis:** Keine offenen Arten aus beiden Quellen. Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Lauf sauber beendet — **kein Fehler**. Routine-Schedule bleibt unangetastet.

**Push-Benachrichtigung:** Bewusst **keine**. Zustand unverändert seit 2026-08-04; am 20. Leerlauf (2026-08-09) ging bereits **einmalig** eine Push-Info aufs Telefon. Eine Wiederholung wäre reines Rauschen — Schweigen ist korrekt.

**Für den Arzt:** 25. Leerlauf in Folge, unverändert seit 2026-08-04 (letzter echter Nachschub Commit `9376a80`). Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Rein informativ (unverändert): Wunsch-`id` `cherry-laurel` ≠ Datei-`id` `prunus-laurocerasus` — falls die App strikt auf die Wunsch-`id` matcht, diesen Wunsch bitte manuell abhaken. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — sonst laufen weiter leere Zündungen.

## 2026-08-11 (zweite Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Quelldateien erneut direkt gegengeprüft, 2026-08-11):** `docs/wunschliste.json` = 2 Einträge, beide per id/Synonym als **erfüllt** bestätigt (`agastache-mexicana` → `monographie-mexikanische-duftnessel.json`; `cherry-laurel`/*Prunus laurocerasus* → `monographie-kirschlorbeer.json`). `kraeuter-kandidaten.json` = 87× `entwurf_fertig`, **0× `offen`**. `fertig/` = 118 Dateien. **0 offene Arten aus beiden Quellen.**

**Ergebnis:** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.

**Push:** Bewusst **keine** — Zustand unverändert seit 2026-08-04, einmalige Push-Info ging bereits am 2026-08-09 raus; Wiederholung wäre Rauschen.

**Für den Arzt:** 26. Leerlauf in Folge und **zweite** Leerzündung allein heute (2026-08-11). Die Routine feuert inzwischen mehrfach täglich ins Leere. Nachschub kann nur ein Mensch liefern (neue Wunsch-/`offen`-Einträge oder die 87 Entwürfe auf `geprueft` setzen). **Empfehlung dringlicher denn je: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — bei mehreren Leerzündungen pro Tag lohnt sich das Pausieren sofort.

## 2026-08-11 (dritte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Quelldateien direkt gegengeprüft, 2026-08-11):** `docs/wunschliste.json` = 2 Einträge, beide per id/Synonym als **erfüllt** bestätigt (`agastache-mexicana` → `monographie-mexikanische-duftnessel.json`, id `agastache-mexicana`; `cherry-laurel`/*Prunus laurocerasus* → `monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme geprüft). `kraeuter-kandidaten.json` = 87× `entwurf_fertig`, **0× `offen`**. `fertig/` = 118 Dateien. **0 offene Arten aus beiden Quellen.**

**Ergebnis:** Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.

**Push:** Bewusst **keine** — Zustand unverändert seit 2026-08-04, einmalige Push-Info ging bereits am 2026-08-09 raus; Wiederholung wäre Rauschen.

**Für den Arzt:** 27. Leerlauf in Folge, **dritte** Leerzündung allein heute (2026-08-11). Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert und dringlich: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — mehrere Leerzündungen pro Tag sind reine Verschwendung.

## 2026-08-12 — Leerlauf: nichts zu tun

**Auswahlprüfung (Quelldateien direkt gegengeprüft, 2026-08-12):** `docs/wunschliste.json` = 2 Einträge, beide per id/Synonym als **erfüllt** bestätigt (`agastache-mexicana` → `monographie-mexikanische-duftnessel.json`, id `agastache-mexicana`; `cherry-laurel`/*Prunus laurocerasus* → `monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme geprüft). `kraeuter-kandidaten.json` = 87× `entwurf_fertig`, **0× `offen`** → kein Bau, kein Self-Heal. `fertig/` = 118 Dateien. **0 offene Arten aus beiden Quellen.** `pip install -r requirements.txt` ok (jsonschema 4.26.0).

**Ergebnis:** Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.

**Push:** Bewusst **keine** — Zustand unverändert seit 2026-08-04, einmalige Push-Info ging bereits am 2026-08-09 raus; Wiederholung wäre Rauschen.

**Für den Arzt:** 28. Leerlauf in Folge, erste Zündung am 2026-08-12. Seit 2026-08-04 kein Nachschub. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert und dringlich: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — die Routine feuert seit Tagen mehrfach täglich ins Leere.

## 2026-08-12 (zweite Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Quelldateien direkt gegengeprüft, nicht dem Vorlauf-Log vertraut, 2026-08-12):** `docs/wunschliste.json` = 2 Einträge, beide per id/Synonym-Abgleich gegen `fertig/` als **bereits erfüllt** bestätigt (`agastache-mexicana` → `monographie-mexikanische-duftnessel.json`, Datei-id `agastache-mexicana`; `cherry-laurel`/*Prunus laurocerasus* → `monographie-kirschlorbeer.json`, Datei-id `prunus-laurocerasus`). `kraeuter-kandidaten.json` = 87 Einträge, ausgezählt `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau, kein Self-Heal. `fertig/` = 118 Dateien. **0 offene Arten aus beiden Quellen.** `pip install -r requirements.txt` ok.

**Ergebnis:** Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.

**Push:** Bewusst **keine** — Zustand unverändert seit 2026-08-04, einmalige Push-Info ging bereits am 2026-08-09 raus; Wiederholung wäre reines Rauschen.

**Für den Arzt:** 29. Leerlauf in Folge, zweite Leerzündung allein heute (2026-08-12). Seit 2026-08-04 kein Nachschub. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert und dringlich: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — die Routine feuert seit über einer Woche mehrfach täglich ins Leere.

## 2026-08-12 (dritte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Quelldateien direkt gegengeprüft, 2026-08-12):** `docs/wunschliste.json` = 2 Einträge, beide per id/Synonym-Abgleich gegen `fertig/` als **erfüllt** bestätigt (`agastache-mexicana` → `monographie-mexikanische-duftnessel.json`; `cherry-laurel`/*Prunus laurocerasus* → `monographie-kirschlorbeer.json`, Datei-id `prunus-laurocerasus`). `kraeuter-kandidaten.json` = 87× `entwurf_fertig`, **0× `offen`** → kein Bau, kein Self-Heal. **0 offene Arten aus beiden Quellen.** `pip install -r requirements.txt` ok.

**Ergebnis:** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.

**Benachrichtigung:** Bewusst **keine** neue Push-Info — Lage unverändert seit 2026-08-04, Push-Info zum Leerlauf ging bereits am 2026-08-09 raus; eine Wiederholung wäre Rauschen.

**Für den Arzt:** 30. Leerlauf in Folge, dritte Leerzündung allein heute. Seit 2026-08-04 kein Nachschub; die Routine feuert seit über einer Woche mehrfach täglich ins Leere und das Log wächst nur noch (jetzt >2100 Zeilen). Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten, oder die 87 Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert und dringlich: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-12 (vierte Zündung) — Leerlauf: nichts zu tun

**Auswahlprüfung (Quelldateien direkt ausgezählt, nicht dem Vorlauf-Log vertraut, 2026-08-12):** `docs/wunschliste.json` = 2 Einträge, beide per id-/Synonym-Abgleich gegen `fertig/` als **bereits erfüllt** bestätigt (`agastache-mexicana` → `monographie-mexikanische-duftnessel.json`, Datei-id `agastache-mexicana`; `cherry-laurel`/*Prunus laurocerasus* → `monographie-kirschlorbeer.json`, Datei-id `prunus-laurocerasus`, Synonyme `Laurocerasus officinalis` u. a. geprüft). `kraeuter-kandidaten.json` = `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau, kein Self-Heal nötig. `fertig/` = 118 Dateien. **0 offene Arten aus beiden Quellen.** `pip install -r requirements.txt` ok (jsonschema 4.26.0).

**Ergebnis:** Kein Bau, keine Prüfung, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.

**Benachrichtigung:** Bewusst **keine** neue Push-Info — Lage unverändert seit 2026-08-04, Push-Info zum Leerlauf ging bereits am 2026-08-09 raus; eine Wiederholung für denselben unveränderten Zustand wäre reines Rauschen.

**Für den Arzt:** 31. Leerlauf in Folge, vierte Leerzündung allein am 2026-08-12. Seit 2026-08-04 kein Nachschub. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert und dringlich: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — die Routine feuert seit über einer Woche mehrfach täglich ins Leere, das Log wächst nur noch.

## 2026-08-13 — Leerlauf: nichts zu tun (32. in Folge)

**Auswahlprüfung (Quelldateien direkt ausgezählt, 2026-08-13):** `docs/wunschliste.json` = 2 Einträge, beide per id-/Synonym-Abgleich gegen `fertig/` (118 Dateien) **erfüllt**: `agastache-mexicana` → `monographie-mexikanische-duftnessel.json` (id `agastache-mexicana`); `cherry-laurel`/*Prunus laurocerasus* → `monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme `Laurocerasus officinalis` u. a. geprüft). `kraeuter-kandidaten.json` = `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau, kein Self-Heal. `pip install -r requirements.txt` ok (jsonschema 4.26.0). **0 offene Arten aus beiden Quellen.**

**Ergebnis:** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.

**Benachrichtigung:** Bewusst **keine** neue Push-Info — Lage unverändert seit 2026-08-04, Push-Info zum Leerlauf ging bereits am 2026-08-09 raus; eine Wiederholung desselben unveränderten Zustands wäre Rauschen.

**Für den Arzt (unverändert, dringlich):** 32. Leerlauf in Folge, erste Zündung am 2026-08-13. Seit 2026-08-04 kein Nachschub; die Routine feuert seit über einer Woche mehrfach täglich ins Leere, das Log ist auf >2100 Zeilen gewachsen. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-13 (zweite Zündung) — Leerlauf: nichts zu tun (33. in Folge)

**Auswahlprüfung (Quelldateien direkt ausgezählt, 2026-08-13):** `docs/wunschliste.json` = 2 Einträge, beide per id-/Synonym-Abgleich gegen `fertig/` **erfüllt** (`agastache-mexicana` → `monographie-mexikanische-duftnessel.json`; `cherry-laurel`/*Prunus laurocerasus* → `monographie-kirschlorbeer.json`, id `prunus-laurocerasus`). `kraeuter-kandidaten.json` = 87× `entwurf_fertig`, **0× `offen`**. **0 offene Arten aus beiden Quellen.** `pip install` ok (jsonschema 4.26.0).

**Ergebnis:** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler. **Benachrichtigung:** bewusst keine (Lage unverändert seit 2026-08-04, Idle-Push ging bereits 2026-08-09 raus).

**Für den Arzt (unverändert):** 33. Leerlauf in Folge. Nachschub kann nur ein Mensch liefern (neue Wunschlisten-/`offen`-Einträge oder die 87 Entwürfe sichten). **Empfehlung: Routine strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-13 (dritte Zündung) — Leerlauf: nichts zu tun (34. in Folge)

**Auswahlprüfung (Quelldateien direkt ausgezählt, nicht dem Vorlauf-Log vertraut, 2026-08-13):** `docs/wunschliste.json` = 2 Einträge, beide per id-/Synonym-Abgleich gegen `fertig/` (118 Dateien) **erfüllt**: `agastache-mexicana` → `monographie-mexikanische-duftnessel.json` (Datei-id `agastache-mexicana`); `cherry-laurel`/*Prunus laurocerasus* → `monographie-kirschlorbeer.json` (Datei-id `prunus-laurocerasus`, Synonym `Laurocerasus officinalis M.Roem.` u. a. verifiziert). `kraeuter-kandidaten.json` = `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau, kein Self-Heal (jeder `entwurf_fertig`-Kandidat hat seine Datei). `pip install -r requirements.txt` ok (jsonschema 4.26.0). **0 offene Arten aus beiden Quellen.**

**Ergebnis:** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler. **Benachrichtigung:** bewusst keine (Lage unverändert seit 2026-08-04, Idle-Push ging bereits 2026-08-09 raus; Wiederholung wäre Rauschen).

**Für den Arzt (unverändert, dringlich):** 34. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub; die Routine feuert seit über einer Woche mehrfach täglich ins Leere, das Log wächst nur noch. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-13 (vierte Zündung) — Leerlauf: nichts zu tun (35. in Folge)

**Auswahlprüfung (Quelldateien direkt ausgezählt, 2026-08-13):** `docs/wunschliste.json` = 2 Einträge, beide per id-/Synonym-Abgleich gegen `fertig/` (118 Dateien) **erfüllt**: `agastache-mexicana` → `monographie-mexikanische-duftnessel.json` (Datei-id `agastache-mexicana`); `cherry-laurel`/*Prunus laurocerasus* → `monographie-kirschlorbeer.json` (Datei-id `prunus-laurocerasus`, Synonyme `Laurocerasus officinalis` u. a. verifiziert). `kraeuter-kandidaten.json` = `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau, kein Self-Heal. `pip install -r requirements.txt` ok (jsonschema 4.26.0). **0 offene Arten aus beiden Quellen.**

**Ergebnis:** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler. **Benachrichtigung:** bewusst keine (Lage unverändert seit 2026-08-04, Idle-Push ging bereits 2026-08-09 raus; Wiederholung desselben Zustands wäre Rauschen).

**Für den Arzt (unverändert, dringlich):** 35. Leerlauf in Folge, vierte Zündung allein am 2026-08-13. Seit 2026-08-04 kein Nachschub; die Routine feuert seit über einer Woche mehrfach täglich ins Leere, das Log wächst nur noch. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-14 (erste Zündung) — Leerlauf: nichts zu tun (36. in Folge)

**Auswahlprüfung (Quelldateien direkt ausgezählt, 2026-08-14):** `docs/wunschliste.json` = 2 Einträge, beide per id-/Synonym-Abgleich gegen `fertig/` (118 Dateien) **erfüllt**: `agastache-mexicana` → `monographie-mexikanische-duftnessel.json` (Datei-id `agastache-mexicana`, direkter id-Treffer); `cherry-laurel`/*Prunus laurocerasus* → `monographie-kirschlorbeer.json` (Datei-id `prunus-laurocerasus`, sci `Prunus laurocerasus L.`, Synonyme `Laurocerasus officinalis M.Roem.` u. a. verifiziert). `kraeuter-kandidaten.json` = 87× `entwurf_fertig`, **0× `offen`** → kein Bau; Self-Heal-Prüfung ergibt keinen Handlungsbedarf (jeder `entwurf_fertig`-Kandidat hat seine Datei). `pip install -r requirements.txt` ok (jsonschema 4.26.0). **0 offene Arten aus beiden Quellen.**

**Ergebnis:** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler. **Benachrichtigung:** bewusst keine (Lage unverändert seit 2026-08-04, Idle-Push ging bereits 2026-08-09 raus; erneuter Push wäre Rauschen).

**Für den Arzt (unverändert, dringlich):** 36. Leerlauf in Folge, erster am 2026-08-14. Seit 2026-08-04 kein Nachschub; die Routine feuert seit über einer Woche mehrfach täglich ins Leere, das Log wächst nur noch. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

---

## Lauf 2026-08-14 (Routine, autonom) — kein Bau, beide Wünsche bereits erfüllt

**Vorbereitung:** `pip install -r requirements.txt` ok (jsonschema 4.26.0). `docs/wunschliste.json` (2 Einträge) und `kraeuter-kandidaten.json` gelesen.

**Auswahl / Dedup:**
- Wunsch 1 `agastache-mexicana` (Toronjil morado / Mexican giant hyssop): **bereits erfüllt** → `fertig/monographie-mexikanische-duftnessel.json` trägt `id: agastache-mexicana`, `scientific_name: Agastache mexicana (Kunth) Lint & Epling`, `stand 2026-08-04`. Direkter id-Treffer → übersprungen.
- Wunsch 2 `cherry-laurel` (Platzhalter-latin; = *Prunus laurocerasus*): **bereits erfüllt** → `fertig/monographie-kirschlorbeer.json` (`id: prunus-laurocerasus`, Warneintrag). Übersprungen.
- Kandidatenliste: 87× `entwurf_fertig`, **0× `offen`** → kein Zweitbau möglich. Self-Heal-Prüfung ohne Handlungsbedarf.
- Ergebnis: **0 offene Arten** aus beiden Quellen.

**Beinah-Dublette (Prozesshinweis für den Arzt/Betreiber):** Ich hatte den Wunsch `agastache-mexicana` zunächst gebaut (`monographie-mexikanischer-riesenysop.json`), weil ein rein **dateinamensbasierter** Dedup-Check den bestehenden Eintrag verfehlte — die vorhandene Datei heißt `mexikanische-duftnessel`, nicht `…agastache…`. Der **id-basierte** Abgleich (`"id": "agastache-mexicana"` in `fertig/`) fand die Dublette. Datei wieder entfernt, mein Changelog-Eintrag zurückgenommen. **Lehre:** Dedup zwingend über `id` **und** `botany.synonyms` aller `fertig/`-Dateien, nicht über Dateinamen.

**Ergebnis:** Kein Bau, keine Statusänderung in `kraeuter-kandidaten.json`, `docs/changelog.json` inhaltlich unverändert (nur dieser Log-Eintrag). Sauber beendet — kein Fehler.

**Für den Arzt (unverändert, dringlich):** Erneuter Leerlauf. Seit 2026-08-04 kein Nachschub. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die fertigen Entwürfe sichten und auf `geprueft` setzen. Empfehlung: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.

## 2026-08-14T17:21:40Z (weitere Zündung 2026-08-14) — Leerlauf: nichts zu tun (37.+ in Folge)

**Vorbereitung:** `pip install -r requirements.txt` ok (jsonschema 4.26.0). `docs/wunschliste.json` (2 Einträge) und `kraeuter-kandidaten.json` gelesen. Quelldateien **direkt ausgezählt**, nicht dem Vorlauf-Log vertraut.

**Auswahl / Dedup (Vorrang Wunschliste):**
- Wunsch 1 `agastache-mexicana` (*Agastache mexicana*): **erfüllt** → `fertig/monographie-mexikanische-duftnessel.json` trägt `id: agastache-mexicana` (direkter id-Treffer). Übersprungen.
- Wunsch 2 `cherry-laurel` (Platzhalter-latin; = Kirschlorbeer / *Prunus laurocerasus*): **erfüllt** → `fertig/monographie-kirschlorbeer.json` (`id: prunus-laurocerasus`, sci `Prunus laurocerasus L.`, Synonyme `Laurocerasus officinalis M.Roem.`, `Cerasus laurocerasus`, `Padus laurocerasus` verifiziert; Warneintrag `not_for_use`). Übersprungen.
- Kandidatenliste: `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau möglich. Self-Heal-Prüfung ohne Handlungsbedarf (kein `offen`-Kandidat, dessen Datei bereits existiert).
- Ergebnis: **0 offene Arten** aus beiden Quellen.

**Ergebnis:** Kein Bau, keine Statusänderung in `kraeuter-kandidaten.json`, `docs/changelog.json` inhaltlich unverändert. Sauber beendet — kein Fehler.

**Benachrichtigung:** bewusst keine. Lage seit 2026-08-04 unverändert; Idle-Push ging bereits 2026-08-09 raus. Erneuter Push desselben Zustands wäre Rauschen.

**Für den Arzt (unverändert):** Seit 2026-08-04 kein Nachschub. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.

## 2026-08-14T18:20:20Z (Routine, autonom) — Leerlauf: nichts zu tun (38.+ in Folge)

**Vorbereitung:** `pip install -r requirements.txt` ok (jsonschema). Quelldateien direkt ausgezählt.
**Auswahl/Dedup:** Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer). Wunsch 2 `cherry-laurel`/*Prunus laurocerasus* → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme verifiziert). Kandidatenliste: 87× `entwurf_fertig`, **0× `offen`**. Self-Heal ohne Handlungsbedarf. → **0 offene Arten**.
**Ergebnis:** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage unverändert; Idle-Push lief bereits 2026-08-09).
**Für den Arzt (unverändert):** Seit 2026-08-04 kein Nachschub. Nur ein Mensch kann Nachschub liefern: neue Wunschlisten-Einträge, neue `offen`-Kandidaten oder die 87 Entwürfe sichten/auf `geprueft` setzen. Empfehlung: Routine-Intervall strecken oder pausieren.

## 2026-08-15T00:19:40Z (Routine, autonom) — Leerlauf: nichts zu tun (39.+ in Folge)

**Vorbereitung:** `pip install -r requirements.txt` ok (jsonschema 4.26.0). `docs/wunschliste.json` (2 Einträge) und `kraeuter-kandidaten.json` gelesen, Quelldateien **direkt ausgezählt** (nicht dem Vorlauf-Log vertraut).
**Auswahl/Dedup (Vorrang Wunschliste):** Wunsch 1 `agastache-mexicana` → **erfüllt** (`fertig/monographie-mexikanische-duftnessel.json`, direkter id-Treffer `id: agastache-mexicana`). Wunsch 2 `cherry-laurel`/*Prunus laurocerasus* → **erfüllt** (`fertig/monographie-kirschlorbeer.json`, `id: prunus-laurocerasus`, Synonyme `Laurocerasus officinalis M.Roem.` u. a. verifiziert). Kandidatenliste: `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau möglich. Self-Heal-Prüfung: jeder Kandidat hat seine `fertig/`-Datei (0 fehlend) → kein Handlungsbedarf. → **0 offene Arten aus beiden Quellen.**
**Ergebnis:** Kein Bau, keine Statusänderung in `kraeuter-kandidaten.json`, `docs/changelog.json` inhaltlich unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt (unverändert, dringlich):** ~39. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub — die Routine feuert seit über einer Woche mehrfach täglich ins Leere, das Log wächst nur noch. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-15T06:21:06Z (Routine, autonom) — Leerlauf: nichts zu tun (40.+ in Folge)

**Vorbereitung:** `pip install -r requirements.txt` ok (jsonschema 4.26.0). `docs/wunschliste.json` (2 Einträge) und `kraeuter-kandidaten.json` gelesen, Quelldateien **direkt ausgezählt** (nicht dem Vorlauf-Log vertraut).
**Auswahl/Dedup (Vorrang Wunschliste):** Wunsch 1 `agastache-mexicana` → **erfüllt** (`fertig/monographie-mexikanische-duftnessel.json`, direkter id-Treffer `id: agastache-mexicana`). Wunsch 2 `cherry-laurel`/*Prunus laurocerasus* → **erfüllt** (`fertig/monographie-kirschlorbeer.json`, `id: prunus-laurocerasus`, Synonyme `Laurocerasus officinalis M.Roem.`, `Cerasus laurocerasus`, `Padus laurocerasus` verifiziert; Warneintrag `not_for_use`). Kandidatenliste: `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau möglich. Self-Heal-Prüfung: jeder Kandidat hat seine `fertig/`-Datei → kein Handlungsbedarf. → **0 offene Arten aus beiden Quellen.**
**Ergebnis:** Kein Bau, keine Statusänderung in `kraeuter-kandidaten.json`, `docs/changelog.json` inhaltlich unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung desselben Zustands wäre Rauschen).
**Für den Arzt (unverändert, dringlich):** ~40. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub — die Routine feuert seit über einer Woche mehrfach täglich ins Leere, das Log (>400 KB) wächst nur noch. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-15T12:23:00Z (Routine, autonom) — Leerlauf: nichts zu tun (41.+ in Folge)

**Vorbereitung:** `pip install -r requirements.txt` ok (jsonschema 4.26.0). `docs/wunschliste.json` (2 Einträge) und `kraeuter-kandidaten.json` gelesen, Quelldateien **direkt ausgezählt** (nicht dem Vorlauf-Log vertraut).
**Auswahl/Dedup (Vorrang Wunschliste):** Wunsch 1 `agastache-mexicana` → **erfüllt** (`fertig/monographie-mexikanische-duftnessel.json`, direkter id-Treffer `id: agastache-mexicana`). Wunsch 2 `cherry-laurel` (= Kirschlorbeer / *Prunus laurocerasus*) → **erfüllt** (`fertig/monographie-kirschlorbeer.json`, `id: prunus-laurocerasus`, sci `Prunus laurocerasus L.`, Synonyme `Laurocerasus officinalis M.Roem.`, `Cerasus laurocerasus (L.) Loisel.`, `Padus laurocerasus (L.) Mill.` — Warneintrag `not_for_use`). Kandidatenliste: `Counter({'entwurf_fertig': 87})`, **0× `offen`** → kein Bau möglich. Self-Heal-Prüfung: kein `offen`-Kandidat vorhanden → kein Handlungsbedarf. → **0 offene Arten aus beiden Quellen.**
**Ergebnis:** Kein Bau, keine Statusänderung in `kraeuter-kandidaten.json`, `docs/changelog.json` inhaltlich unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung desselben Zustands wäre Rauschen).
**Für den Arzt (unverändert, dringlich):** ~41. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub — die Routine feuert seit über einer Woche mehrfach täglich ins Leere. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-15T18:00:00Z (Routine, autonom) — Leerlauf: nichts zu tun (42.+ in Folge)

**Auswahl/Dedup (unabhängig verifiziert, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (2 Einträge) + `kraeuter-kandidaten.json` direkt ausgezählt. Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer). Wunsch 2 `cherry-laurel`/*Prunus laurocerasus* → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme verifiziert, Warneintrag `not_for_use`). Kandidatenliste: 87× `entwurf_fertig`, **0× `offen`**. Self-Heal: kein `offen`-Kandidat → kein Handlungsbedarf. → **0 offene Arten.**
**Ergebnis:** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler. Log bewusst knapp gehalten (Datei wächst nur noch durch identische Leerläufe).
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief 2026-08-09).
**Für den Arzt:** ~42. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub. Nur ein Mensch kann liefern: neue Wunschlisten-Einträge, neue `offen`-Kandidaten oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken oder pausieren.**

## 2026-08-16T00:20:00Z (Routine, autonom) — Leerlauf: nichts zu tun (43.+ in Folge)

**Auswahl/Dedup (unabhängig verifiziert, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (2 Einträge) + `kraeuter-kandidaten.json` direkt ausgezählt. Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer). Wunsch 2 `cherry-laurel`/*Prunus laurocerasus* → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme verifiziert, Warneintrag `not_for_use`). Kandidatenliste: 87× `entwurf_fertig`, **0× `offen`**. Self-Heal: kein `offen`-Kandidat → kein Handlungsbedarf. → **0 offene Arten.**
**Ergebnis:** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief 2026-08-09).
**Für den Arzt:** ~43. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub. Nur ein Mensch kann liefern: neue Wunschlisten-Einträge, neue `offen`-Kandidaten oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-16T06:20:00Z (Routine, autonom) — Leerlauf: nichts zu tun (44.+ in Folge)

**Auswahl/Dedup (unabhängig verifiziert, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (2 Einträge) + `kraeuter-kandidaten.json` direkt ausgezählt. Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer). Wunsch 2 `cherry-laurel`/*Prunus laurocerasus* → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme verifiziert, Warneintrag). Kandidatenliste: 87× `entwurf_fertig`, **0× `offen`**. Self-Heal: kein `offen`-Kandidat → kein Handlungsbedarf. → **0 offene Arten.**
**Ergebnis:** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** ~44. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub. Nur ein Mensch kann liefern: neue Wunschlisten-Einträge, neue `offen`-Kandidaten oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-16T12:24:00Z (Routine, autonom) — Leerlauf: nichts zu tun (45.+ in Folge)

**Auswahl/Dedup (unabhängig verifiziert, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (2 Einträge) + `kraeuter-kandidaten.json` direkt ausgezählt. Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer). Wunsch 2 `cherry-laurel`/*Prunus laurocerasus* → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme verifiziert, Warneintrag `not_for_use`). Kandidatenliste: 87× `entwurf_fertig`, **0× `offen`**. Self-Heal: kein `offen`-Kandidat → kein Handlungsbedarf. → **0 offene Arten aus beiden Quellen.**
**Ergebnis:** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — dieselbe Meldung erneut zu senden wäre Rauschen).
**Für den Arzt:** ~45. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub; die Routine feuert seit ~12 Tagen mehrfach täglich ins Leere, das Log (>400 KB) wächst nur noch durch identische Einträge. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-16T18:20:00Z (Routine, autonom) — Leerlauf: nichts zu tun (46.+ in Folge)

**Vorbereitung:** Frischer Container — `pip install -r requirements.txt` neu ausgeführt (jsonschema 4.26.0). `docs/wunschliste.json` (2 Einträge) und `kraeuter-kandidaten.json` **direkt ausgezählt** (nicht dem Vorlauf-Log vertraut).
**Auswahl/Dedup (Vorrang Wunschliste, unabhängig verifiziert):** Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer `id: agastache-mexicana`). Wunsch 2 `cherry-laurel` (= Kirschlorbeer / *Prunus laurocerasus*) → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Warneintrag `not_for_use`). Kandidatenliste: 87× `entwurf_fertig`, **0× `offen`** (per Counter direkt geprüft). Self-Heal: kein `offen`-Kandidat → kein Handlungsbedarf. → **0 offene Arten aus beiden Quellen.**
**Ergebnis:** Kein Bau, keine Statusänderung in `kraeuter-kandidaten.json`, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — dieselbe Meldung erneut zu senden wäre Rauschen).
**Für den Arzt:** ~46. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub; die Routine feuert seit ~12 Tagen mehrfach täglich ins Leere, das Log (>400 KB) wächst nur noch durch identische Einträge. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-17T00:24:49Z (Routine, autonom) — Leerlauf: nichts zu tun (47.+ in Folge)

**Vorbereitung:** `docs/wunschliste.json` (2 Einträge) und `kraeuter-kandidaten.json` **direkt ausgezählt** (nicht dem Vorlauf-Log vertraut). `pip install` nicht nötig, da kein Bau (kein Validierungslauf).
**Auswahl/Dedup (Vorrang Wunschliste, unabhängig verifiziert):** Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, direkter id-Treffer `id: agastache-mexicana`). Wunsch 2 `cherry-laurel` (= Kirschlorbeer / *Prunus laurocerasus*) → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme `Laurocerasus officinalis M.Roem.`, `Cerasus laurocerasus (L.) Loisel.`, `Padus laurocerasus (L.) Mill.` verifiziert; Warneintrag `not_for_use`). Kandidatenliste: `Counter({'entwurf_fertig': 87})`, **0× `offen`**. Self-Heal: kein `offen`-Kandidat → kein Handlungsbedarf. → **0 offene Arten aus beiden Quellen.**
**Ergebnis:** Kein Bau, keine Statusänderung in `kraeuter-kandidaten.json`, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — dieselbe Meldung erneut zu senden wäre Rauschen).
**Für den Arzt:** ~47. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub; die Routine feuert seit ~13 Tagen mehrfach täglich ins Leere, das Log (>400 KB) wächst nur noch durch identische Einträge. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-17T07:02:02Z (Routine, autonom) — Leerlauf: nichts zu tun (48.+ in Folge)

**Auswahl/Dedup (unabhängig verifiziert, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (2 Einträge) + `kraeuter-kandidaten.json` direkt ausgezählt. Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer). Wunsch 2 `cherry-laurel` (= *Prunus laurocerasus*) → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme verifiziert). Kandidatenliste: `Counter({'entwurf_fertig': 87})`, **0× `offen`**. Self-Heal: kein `offen`-Kandidat mit Datei-Konflikt → kein Handlungsbedarf. → **0 offene Arten aus beiden Quellen.**
**Ergebnis:** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** ~48. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge, neue `offen`-Kandidaten oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-17T13:51:19Z (Routine, autonom) — Leerlauf: nichts zu tun (49.+ in Folge)

**Auswahl/Dedup (unabhängig verifiziert):** `docs/wunschliste.json` (2 Einträge) + `kraeuter-kandidaten.json` direkt ausgezählt. Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer). Wunsch 2 `cherry-laurel` (= *Prunus laurocerasus*) → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme verifiziert). Kandidatenliste: 87× `entwurf_fertig`, **0× `offen`**. → **0 offene Arten aus beiden Quellen.** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** ~49. Leerlauf in Folge, seit 2026-08-04 kein Nachschub. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge, neue `offen`-Kandidaten oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-17T (Routine, autonom) — Leerlauf: nichts zu tun (50.+ in Folge)

**Auswahl/Dedup (unabhängig verifiziert):** `docs/wunschliste.json` (2 Einträge) + `kraeuter-kandidaten.json` direkt ausgezählt. Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer). Wunsch 2 `cherry-laurel` (= *Prunus laurocerasus*) → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme verifiziert). Kandidatenliste: `Counter({'entwurf_fertig': 87})`, **0× `offen`**. → **0 offene Arten aus beiden Quellen.** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** ~50. Leerlauf in Folge, seit 2026-08-04 kein Nachschub. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge, neue `offen`-Kandidaten oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-18T00:17:37Z (Routine, autonom) — Leerlauf: nichts zu tun (51.+ in Folge)

**Auswahl/Dedup (unabhängig verifiziert, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (2 Einträge) + `kraeuter-kandidaten.json` direkt ausgezählt. Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer per grep bestätigt). Wunsch 2 `cherry-laurel` (= *Prunus laurocerasus*) → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme verifiziert, Warneintrag `not_for_use`). Kandidatenliste: `Counter({'entwurf_fertig': 87})`, **0× `offen`** (per Counter direkt geprüft, offen-Liste leer). Self-Heal: kein `offen`-Kandidat → kein Datei-Konflikt, kein Handlungsbedarf. → **0 offene Arten aus beiden Quellen.**
**Ergebnis:** Kein Bau, keine Statusänderung in `kraeuter-kandidaten.json`, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** ~51. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub; die Routine feuert seit ~2 Wochen mehrfach täglich ins Leere, das Log (>400 KB) wächst nur noch durch identische Einträge. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-18T (Routine, autonom) — Leerlauf: nichts zu tun (52.+ in Folge)

**Auswahl/Dedup (unabhängig verifiziert, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (2 Einträge) + `kraeuter-kandidaten.json` direkt ausgezählt. Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer per grep bestätigt). Wunsch 2 `cherry-laurel` (= *Prunus laurocerasus*) → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Warneintrag `not_for_use`). Kandidatenliste: `grep`-Zählung `87× entwurf_fertig`, **0× `offen`**. Self-Heal: kein `offen`-Kandidat → kein Datei-Konflikt, kein Handlungsbedarf. → **0 offene Arten aus beiden Quellen.**
**Ergebnis:** Kein Bau, keine Statusänderung in `kraeuter-kandidaten.json`, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** ~52. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub; die Routine läuft seit ~2 Wochen mehrfach täglich ins Leere, das Log (>400 KB) wächst nur noch durch identische Einträge. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-18T12:27:33Z (Routine, autonom) — Leerlauf: nichts zu tun (53.+ in Folge)

**Auswahl/Dedup (unabhängig verifiziert, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (2 Einträge) + `kraeuter-kandidaten.json` direkt ausgezählt. Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer `id: agastache-mexicana` bestätigt). Wunsch 2 `cherry-laurel` (= *Prunus laurocerasus*) → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme `Laurocerasus officinalis M.Roem.` / `Cerasus laurocerasus (L.) Loisel.` / `Padus laurocerasus (L.) Mill.` verifiziert, Warneintrag `not_for_use`). Kandidatenliste: `Counter({'entwurf_fertig': 87})`, **0× `offen`**; alle 87 `datei`-Pfade existieren (os.path.exists geprüft) → keine Self-Heal-Korrektur nötig. → **0 offene Arten aus beiden Quellen.**
**Ergebnis:** Kein Bau, keine Statusänderung in `kraeuter-kandidaten.json`, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** ~53. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub; die Routine läuft seit ~2 Wochen mehrfach täglich ins Leere, das Log (>400 KB) wächst nur noch durch identische Einträge. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-18T18:17:50Z (Routine, autonom) — Leerlauf: nichts zu tun (54.+ in Folge)

**Auswahl/Dedup (unabhängig verifiziert, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (2 Einträge) + `kraeuter-kandidaten.json` direkt per Python-Counter ausgezählt. Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer `id: agastache-mexicana`). Wunsch 2 `cherry-laurel` (= *Prunus laurocerasus*) → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme verifiziert, Warneintrag `not_for_use`). Kandidatenliste: `Counter({'entwurf_fertig': 87})`, **0× `offen`**. Self-Heal: kein `offen`-Kandidat → kein Handlungsbedarf. → **0 offene Arten aus beiden Quellen.**
**Ergebnis:** Kein Bau, keine Statusänderung in `kraeuter-kandidaten.json`, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** ~54. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub; die Routine läuft seit ~2 Wochen mehrfach täglich ins Leere, das Log (>400 KB) wächst nur noch durch identische Einträge. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-19T00:18:03Z (Routine, autonom) — Leerlauf: nichts zu tun (55.+ in Folge)

**Auswahl/Dedup (unabhängig verifiziert, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (2 Einträge) + `kraeuter-kandidaten.json` direkt per Python-Counter ausgezählt. Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer `id: agastache-mexicana`). Wunsch 2 `cherry-laurel` (= *Prunus laurocerasus*) → erfüllt (`fertig/monographie-kirschlorbeer.json`, id `prunus-laurocerasus`, Synonyme verifiziert, Warneintrag `not_for_use`). Kandidatenliste: `Counter({'entwurf_fertig': 87})`, **0× `offen`**. Self-Heal: kein `offen`-Kandidat → kein Handlungsbedarf. → **0 offene Arten aus beiden Quellen.**
**Ergebnis:** Kein Bau, keine Statusänderung in `kraeuter-kandidaten.json`, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** ~55. Leerlauf in Folge. Seit 2026-08-04 kein Nachschub; die Routine läuft seit ~2 Wochen mehrfach täglich ins Leere, das Log (>400 KB) wächst nur noch durch identische Einträge. Nachschub kann **nur ein Mensch** liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten und auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-19T (Routine, autonom) — Leerlauf: nichts zu tun (56.+ in Folge)

**Auswahl/Dedup (unabhängig verifiziert):** `docs/wunschliste.json` (2 Einträge) + `kraeuter-kandidaten.json` per Python-Counter ausgezählt. Wunsch 1 `agastache-mexicana` → erfüllt (`fertig/monographie-mexikanische-duftnessel.json`, id-Treffer). Wunsch 2 `cherry-laurel` (= *Prunus laurocerasus*) → erfüllt (`fertig/monographie-kirschlorbeer.json`, Synonyme verifiziert, Warneintrag `not_for_use`). Kandidatenliste: `Counter({'entwurf_fertig': 87})`, **0× `offen`**. → **0 offene Arten aus beiden Quellen.** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** ~56. Leerlauf in Folge, seit 2026-08-04 kein Nachschub. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge über die App, neue `offen`-Kandidaten in `kraeuter-kandidaten.json`, oder die 87 fertigen Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt** — das Log wächst sonst weiter nur durch identische Einträge.

## 2026-08-19 (Routine, autonom) — Leerlauf: nichts zu tun (57. in Folge)

**Auswahl/Dedup (verifiziert):** Wunschliste (2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme geprüft). Kandidatenliste per Python-Counter: `{'entwurf_fertig': 87}`, **0× `offen`**. Self-Heal: kein `offen`-Eintrag → kein Handlungsbedarf. → **0 offene Arten aus beiden Quellen.** Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09).
**Für den Arzt:** Situation unverändert seit ~2 Wochen. Nachschub kann nur ein Mensch liefern: neue Wunschlisten-Einträge (App), neue `offen`-Kandidaten, oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine-Intervall strecken oder pausieren, bis Nachschub vorliegt.**

## 2026-08-19T18:18:44Z (Routine, autonom) — Leerlauf: nichts zu tun (58. in Folge)

**Verifiziert:** Wunschliste (2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json`, `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json`. Kandidatenliste per Python-Counter: `{'entwurf_fertig': 87}`, **0× `offen`**. → 0 offene Arten. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09).
**Für den Arzt:** Unverändert. Nachschub nur durch Menschen: neue Wunschlisten-/`offen`-Einträge oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung: Routine strecken/pausieren, bis Nachschub vorliegt.**

## 2026-08-20T00:18:07Z (Routine, autonom) — Leerlauf: nichts zu tun (59. in Folge)

**Verifiziert:** Wunschliste (2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json`, `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json`. Kandidatenliste per Python-Counter: `{'entwurf_fertig': 87}`, **0× `offen`**. → 0 offene Arten. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09).
**Für den Arzt:** Unverändert seit ~2,5 Wochen. Nachschub nur durch Menschen: neue Wunschlisten-/`offen`-Einträge oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung: Routine strecken/pausieren, bis Nachschub vorliegt** — das Log (>400 KB) wächst sonst weiter nur durch identische Einträge.

## 2026-08-20T (Routine, autonom) — Leerlauf: nichts zu tun (60. in Folge)

**Verifiziert (unabhängig, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme + `not_for_use` geprüft). Kandidatenliste per Python-Counter: `{'entwurf_fertig': 87}`, **0× `offen`**. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** Unverändert seit ~2,5 Wochen. Nachschub nur durch Menschen: neue Wunschlisten-/`offen`-Einträge oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung: Routine strecken/pausieren, bis Nachschub vorliegt** — das Log (>400 KB) wächst sonst weiter nur durch identische Einträge.

## 2026-08-20T (Routine, autonom, 2. Lauf) — Leerlauf: nichts zu tun (61. in Folge)

**Verifiziert (unabhängig):** `docs/wunschliste.json` (2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme geprüft). Kandidatenliste per Python-Counter: `{'entwurf_fertig': 87}`, **0× `offen`**. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** Unverändert seit ~2,5 Wochen. Nachschub nur durch Menschen: neue Wunschlisten-/`offen`-Einträge oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt.**

## 2026-08-20T (Routine, autonom, 3. Lauf) — Leerlauf: nichts zu tun (62. in Folge)

**Verifiziert (unabhängig):** `docs/wunschliste.json` (2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme geprüft). Kandidatenliste per Python-Counter: `{'entwurf_fertig': 87}`, **0× `offen`**. → 0 offene Arten. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09).
**Für den Arzt:** Unverändert seit ~2,5 Wochen. Nachschub nur durch Menschen: neue Wunschlisten-/`offen`-Einträge oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** — das Log wächst sonst weiter nur durch identische Einträge.

## 2026-08-21 (Routine, autonom) — Leerlauf: nichts zu tun (63. in Folge)

**Unabhängig verifiziert (nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme + `not_for_use=true` geprüft). Der jüngste Commit `e3c66ec` „Wunschliste aktualisiert (2 offen)" enthält dieselben zwei bereits-fertigen Einträge — kein neuer Wunsch. Kandidatenliste per Python-Counter: `{'entwurf_fertig': 87}`, **0× `offen`**. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** Unverändert seit ~2,5 Wochen. Nachschub kommt nur durch Menschen: neue Wunschlisten-Einträge oder Kandidaten auf `offen` — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (das Log wächst sonst weiter nur durch identische Leerlauf-Einträge).

## 2026-08-21 (Routine, autonom, 2. Lauf) — Leerlauf: nichts zu tun (64. in Folge)

**Unabhängig verifiziert:** `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme geprüft). Kandidatenliste per Python-Counter: `{'entwurf_fertig': 87}`, **0× `offen`**. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09).
**Für den Arzt:** Unverändert seit ~2,5 Wochen. Nachschub nur durch Menschen: neue Wunschlisten-/`offen`-Einträge oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** — das Log (>400 KB) wächst sonst weiter nur durch identische Leerlauf-Einträge.

## 2026-08-21 (Routine, autonom, 3. Lauf) — Leerlauf: nichts zu tun (65. in Folge)

**Unabhängig verifiziert (Python, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme + `not_for_use=true` geprüft). Kandidatenliste per Counter: `{'entwurf_fertig': 87}`, **0× `offen`**. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** Unverändert. Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (das Log >400 KB wächst sonst nur durch identische Leerlauf-Einträge).

## 2026-08-21 (Routine, autonom, 4. Lauf) — Leerlauf: nichts zu tun (66. in Folge)

**Unabhängig verifiziert (Python, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme + `not_for_use=true` geprüft). Kandidatenliste per Counter: `{'entwurf_fertig': 87}`, **0× `offen`**; alle 87 referenzierten `datei`-Pfade existieren (keine Selbstheilung nötig). → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** Unverändert. Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (das Log >400 KB wächst sonst nur durch identische Leerlauf-Einträge).

## 2026-08-22 (Routine, autonom) — Leerlauf: nichts zu tun (67. in Folge)

**Unabhängig verifiziert (Python, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer `agastache-mexicana`, Synonyme geprüft), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme + `not_for_use=true` geprüft). Kandidatenliste per `Counter`: `{'entwurf_fertig': 87}`, **0× `offen`**; alle 87 referenzierten `datei`-Pfade existieren (keine Selbstheilung nötig). → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre reines Rauschen).
**Für den Arzt:** Unverändert seit ~2,5 Wochen. Nachschub kommt nur durch Menschen: neue Wunschlisten-Einträge oder Kandidaten auf `offen` setzen — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (das Log wächst sonst weiter nur durch identische Leerlauf-Einträge).

## 2026-08-22 (Routine, autonom, 2. Lauf) — Leerlauf: nichts zu tun (68. in Folge)

**Unabhängig verifiziert (Python, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme geprüft: *Laurocerasus officinalis*, *Cerasus/Padus laurocerasus*; `not_for_use=true`, cyanogener Warneintrag — korrekt). Kandidatenliste per `Counter`: `{'entwurf_fertig': 87}`, **0× `offen`** → keine Selbstheilung nötig. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** Unverändert seit ~2,5 Wochen. Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (das Log wächst sonst nur durch identische Leerlauf-Einträge).

## 2026-08-22 (Routine, autonom, 3. Lauf) — Leerlauf: nichts zu tun (69. in Folge)

**Unabhängig verifiziert (Python, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`; App-Wunsch-id `cherry-laurel` ist der engl. Name für Kirschlorbeer). Kandidatenliste per `Counter`: `{'entwurf_fertig': 87}`, **0× `offen`** → keine Selbstheilung nötig. `fertig/` enthält 118 Monographien. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** Unverändert seit ~2,5 Wochen. Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (das Log wächst sonst nur durch identische Leerlauf-Einträge).

## 2026-08-22 (Routine, autonom, 4. Lauf) — Leerlauf: nichts zu tun (70. in Folge)

**Unabhängig verifiziert (Python, nicht dem Vorlauf-Log vertraut):** `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme + `not_for_use=true` geprüft). Kandidatenliste per `Counter`: `{'entwurf_fertig': 87}`, **0× `offen`** → keine Selbstheilung nötig. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** Unverändert seit ~2,5 Wochen. Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (das Log wächst sonst nur durch identische Leerlauf-Einträge).

## 2026-08-23 (Routine, autonom) — Leerlauf: nichts zu tun (71. in Folge)

**Unabhängig verifiziert (Python):** `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`). Kandidatenliste per `Counter`: `{'entwurf_fertig': 87}`, **0× `offen`** → keine Selbstheilung nötig. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** Unverändert seit ~3 Wochen. Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt.**

## 2026-08-23 (Routine, autonom, 2. Lauf) — Leerlauf: nichts zu tun (72. in Folge)

**Unabhängig verifiziert (Python):** `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer `agastache-mexicana`, Synonyme geprüft), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme *Laurocerasus/Cerasus/Padus laurocerasus* + `not_for_use=true`). Kandidatenliste per `Counter`: `{'entwurf_fertig': 87}`, **0× `offen`** → keine Selbstheilung nötig. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage seit 2026-08-04 unverändert; Idle-Push lief bereits 2026-08-09 — Wiederholung wäre Rauschen).
**Für den Arzt:** Unverändert seit ~3 Wochen (72 Leerläufe in Folge). Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (das Log >430 KB wächst sonst nur durch identische Leerlauf-Einträge).

## 2026-08-23 (Routine, autonom, 3. Lauf) — Leerlauf: nichts zu tun (73. in Folge)

**Verifiziert (Python):** Wunschliste (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json`, `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json`. Kandidatenliste: `{'entwurf_fertig': 87}`, **0× `offen`**. → 0 offene Arten. Kein Bau, keine Statusänderung, Changelog unverändert. Sauber beendet.
**Benachrichtigung:** bewusst keine (Lage unverändert seit 2026-08-04 — Push wäre Rauschen).
**Für den Arzt:** Unverändert seit ~3 Wochen (73 Leerläufe in Folge). Nachschub nur durch Menschen: neue Wunschlisten-/`offen`-Einträge oder die 87 Entwürfe auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt.**

## 2026-08-23 (Routine, autonom, 4. Lauf) — Leerlauf: nichts zu tun (74. in Folge)

**Verifiziert (Python):** Wunschliste (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json`, `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json`. Kandidatenliste: `{'entwurf_fertig': 87}`, **0× `offen`**. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, Changelog unverändert. Sauber beendet.
**Benachrichtigung:** bewusst keine (Lage unverändert seit 2026-08-04 — Push wäre Rauschen).
**Für den Arzt:** Unverändert seit ~3 Wochen (74 Leerläufe in Folge). Nachschub nur durch Menschen: neue Wunschlisten-/`offen`-Einträge oder die 87 Entwürfe auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt.**

## 2026-08-24 (Routine, autonom) — Leerlauf: nichts zu tun (75. in Folge)

**Verifiziert (Python):** Wunschliste `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme + `not_for_use=true` geprüft). Kandidatenliste per `Counter`: `{'entwurf_fertig': 87}`, **0× `offen`** → keine Selbstheilung nötig. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage unverändert seit 2026-08-04 — Push wäre Rauschen; Idle-Push lief bereits 2026-08-09).
**Für den Arzt:** Unverändert seit ~3 Wochen (75 Leerläufe in Folge). Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. Hinweis zur Datenqualität: Wunsch-Eintrag `cherry-laurel` trägt im Feld `latin` den englischen Namen „Cherry laurel" statt eines Binomens und eine common-name-id statt `gattung-art` — App-seitig prüfen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (Log >446 KB wächst sonst nur durch identische Leerlauf-Einträge).

## 2026-08-24 (Routine, autonom, 2. Lauf) — Leerlauf: nichts zu tun (76. in Folge)

**Verifiziert (Python):** Wunschliste `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`). Kandidatenliste per `Counter`: `{'entwurf_fertig': 87}`, **0× `offen`** → keine Selbstheilung nötig. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage unverändert seit 2026-08-04 — Push wäre Rauschen; Idle-Push lief bereits 2026-08-09).
**Für den Arzt:** Unverändert seit ~3 Wochen (76 Leerläufe in Folge). Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (Log wächst sonst nur durch identische Leerlauf-Einträge).

## 2026-08-24 (Routine, autonom, 3. Lauf) — Leerlauf: nichts zu tun (77. in Folge)

**Verifiziert (Python):** Wunschliste `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme + `not_for_use=true` geprüft). Kandidatenliste per `Counter`: `{'entwurf_fertig': 87}`, **0× `offen`** → keine Selbstheilung nötig. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage unverändert seit 2026-08-04 — Push wäre Rauschen; Idle-Push lief bereits 2026-08-09).
**Für den Arzt:** Unverändert seit ~3 Wochen (77 Leerläufe in Folge). Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (Log wächst sonst nur durch identische Leerlauf-Einträge).

## 2026-08-24 (Routine, autonom, 4. Lauf) — Leerlauf: nichts zu tun (78. in Folge)

**Verifiziert (Python):** Wunschliste `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme + `not_for_use=true` geprüft). Kandidatenliste per `Counter`: `{'entwurf_fertig': 87}`, **0× `offen`** → keine Selbstheilung nötig. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert (91 Einträge). Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage unverändert seit 2026-08-04 — Push wäre Rauschen; Idle-Push lief bereits 2026-08-09).
**Für den Arzt:** Unverändert seit ~3 Wochen (78 Leerläufe in Folge). Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (Log >450 KB wächst sonst nur durch identische Leerlauf-Einträge).

## 2026-08-25 (Routine, autonom) — Leerlauf: nichts zu tun (79. in Folge)

**Verifiziert (Python):** Wunschliste `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme geprüft). Kandidatenliste per `Counter`: `{'entwurf_fertig': 87}`, **0× `offen`** → keine Selbstheilung nötig. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage unverändert seit 2026-08-04 — Push wäre Rauschen).
**Für den Arzt:** Unverändert seit ~3 Wochen (79 Leerläufe in Folge). Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (Log wächst sonst nur durch identische Leerlauf-Einträge).

## 2026-08-25 (Routine, autonom, 2. Lauf) — Leerlauf: nichts zu tun (80. in Folge)

**Verifiziert (Python):** Wunschliste `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer, „Mexican giant hyssop" in `common_names_de`), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, Synonyme *Laurocerasus/Cerasus/Padus laurocerasus* geprüft). Kandidatenliste per `Counter`: `{'entwurf_fertig': 87}`, **0× `offen`** → keine Selbstheilung nötig. → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage unverändert seit 2026-08-04 — Push wäre Rauschen).
**Für den Arzt:** Unverändert seit ~3 Wochen (80 Leerläufe in Folge). Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (Log wächst sonst nur durch identische Leerlauf-Einträge).

## 2026-08-25 (Routine, autonom, 3. Lauf) — Leerlauf: nichts zu tun (81. in Folge)

**Verifiziert (Python, unabhängig nachgerechnet):** Wunschliste `docs/wunschliste.json` (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `fertig/monographie-mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `fertig/monographie-kirschlorbeer.json` (id `prunus-laurocerasus`, cyanogener `not_for_use`-Warneintrag; id-Slug-Mismatch ist die bekannte Wunschlisten-Datenqualitätsfrage, Pflanze selbst abgedeckt). Kandidatenliste per `Counter`: `{'entwurf_fertig': 87}`, **0× `offen`** → keine Selbstheilung nötig (kein `offen`-Kandidat, dessen Datei bereits existiert). → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage unverändert seit 2026-08-04 — Push wäre Rauschen; Idle-Push lief bereits 2026-08-09).
**Für den Arzt:** Unverändert seit ~3 Wochen (81 Leerläufe in Folge). Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt** (Log wächst sonst nur durch identische Leerlauf-Einträge).

## 2026-08-25 (Routine, autonom, 4. Lauf) — Leerlauf: nichts zu tun (82. in Folge)

**Verifiziert (Python):** Wunschliste (`stand` 2026-08-20, 2 Einträge) beide erfüllt — `agastache-mexicana` → `mexikanische-duftnessel.json` (id-Treffer), `cherry-laurel`/*Prunus laurocerasus* → `kirschlorbeer.json` (id `prunus-laurocerasus`, `not_for_use`-Warneintrag). Kandidaten `Counter` = `{'entwurf_fertig': 87}`, **0× `offen`** → keine Selbstheilung nötig. `fertig/` 118 Monographien + `.gitkeep` (einziger nicht-JSON-Treffer, erwartet). → 0 offene Arten aus beiden Quellen. Kein Bau, keine Statusänderung, `docs/changelog.json` unverändert. Sauber beendet — kein Fehler.
**Benachrichtigung:** bewusst keine (Lage unverändert seit 2026-08-04 — Push wäre Rauschen; Idle-Push lief bereits 2026-08-09). Log-Eintrag bewusst kurz gehalten (Datei >450 KB).
**Für den Arzt:** Unverändert seit ~3 Wochen (82 Leerläufe in Folge). Nachschub kommt nur durch Menschen: neue Wunschlisten-/`offen`-Einträge — oder die 87 Entwürfe sichten/auf `geprueft` setzen. **Empfehlung unverändert: Routine strecken/pausieren, bis Nachschub vorliegt.**
