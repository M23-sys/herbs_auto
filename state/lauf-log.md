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
