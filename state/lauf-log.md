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
