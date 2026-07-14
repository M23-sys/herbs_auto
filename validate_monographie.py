#!/usr/bin/env python3
"""
Prüfskript für Kräuter-Monographien.

    python3 validate_monographie.py monographie-baldrian.json
    python3 validate_monographie.py *.json

Prüft Struktur, Pflichtfelder und — vor allem — die sicherheitskritischen
Regeln aus MONOGRAPHIE-SPEC.md. Beendet sich mit Code 1, wenn ein FEHLER
gefunden wurde. WARNUNGEN blockieren nicht, sollten aber gelesen werden.
"""

import json
import os
import sys
import re

# Strukturelle Prüfung gegen monographie-schema.json.
#
# WICHTIG: Fehlt die Bibliothek jsonschema, BRICHT das Skript ab (Exit-Code 3),
# statt stillschweigend ohne Schema-Prüfung durchzulaufen. Ein "ok" ohne
# Schema-Prüfung ist ein wertloses "ok" — genau so entstehen 87 Monographien,
# die nie validiert wurden.
#
# Nur zum lokalen Herumprobieren umgehbar mit:  HERB_ALLOW_NO_SCHEMA=1
SCHEMA = None
try:
    import jsonschema
    _SCHEMA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "monographie-schema.json")
    with open(_SCHEMA_PATH, encoding="utf-8") as _fh:
        SCHEMA = json.load(_fh)
except ImportError:
    if os.environ.get("HERB_ALLOW_NO_SCHEMA") != "1":
        sys.stderr.write(
            "ABBRUCH: Bibliothek 'jsonschema' fehlt — ohne sie findet KEINE\n"
            "Schema-Prüfung statt und ein 'ok' waere wertlos.\n"
            "  Abhilfe:  pip install -r requirements.txt\n"
        )
        sys.exit(3)
    sys.stderr.write("WARNUNG: ohne jsonschema — Schema-Pruefung uebersprungen.\n")
except Exception as _exc:
    sys.stderr.write(f"ABBRUCH: monographie-schema.json nicht lesbar: {_exc}\n")
    sys.exit(3)

EVIDENCE = {"WEU", "RCT", "ESCOP+", "TU", "PRÄ", "TRAD"}
TOXICITY = {"essbar", "giftig", "lebensgefährlich"}
ORGANS = {"Blatt", "Blüte", "Wurzel", "Kraut", "Frucht", "Rinde", "Samen", "Zwiebel", "Rhizom"}

TOP_LEVEL = [
    "schema_version", "id", "botany", "identification", "confusions", "chemistry",
    "pharmacology", "indications", "expectation_summary", "preparation", "safety",
    "harvest_processing_storage", "kitchen", "garden", "sources",
]

KNOWN_FLAGS = {
    "deadly_confusion", "toxin_ceiling", "toxin_type", "raw_toxicity", "requires_heating",
    "hepatotoxic", "pregnancy_contraindicated", "interaction_heavy", "cyp3a4_inducer",
    "pgp_inducer", "serotonergic", "lowers_seizure_threshold", "photosensitizing",
    "asteraceae_allergy", "apiaceae_confusion_young", "topical_only", "high_safety",
    "infant_facial_caution", "not_for_use", "reflux_caution", "cardiorenal_flush_caution",
    "oil_age_restriction",
}


def check(path):
    errors, warns = [], []

    try:
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
    except json.JSONDecodeError as exc:
        return [f"JSON unlesbar: {exc}"], []

    # --- Struktur ---
    for key in TOP_LEVEL:
        if key not in d:
            errors.append(f"Pflichtfeld fehlt: '{key}'")
    if errors:
        return errors, warns

    # --- Schema (falls jsonschema verfügbar) ---
    if SCHEMA is not None:
        for e in sorted(jsonschema.Draft7Validator(SCHEMA).iter_errors(d), key=lambda x: list(x.path)):
            loc = "/".join(str(x) for x in e.path) or "(root)"
            errors.append(f"Schema {loc}: {e.message}")

    # --- id ---
    hid = d.get("id", "")
    if not re.fullmatch(r"[a-z]+-[a-z]+", hid):
        errors.append(f"id '{hid}' muss 'gattung-art' sein (klein, ein Bindestrich)")

    sci = d["botany"].get("scientific_name", "")
    if sci:
        # Hybridzeichen und Autorenkürzel entfernen: "Mentha × piperita L." -> "mentha-piperita"
        parts = [w for w in sci.replace("×", " ").split() if w not in ("x", "X")]
        expect = "-".join(parts[:2]).lower()
        expect = re.sub(r"[^a-z-]", "", expect)
        if expect and expect != hid:
            warns.append(f"id '{hid}' passt nicht zu scientific_name '{sci}' (erwartet '{expect}')")

    # --- Botanik ---
    if not d["botany"].get("common_names_de"):
        errors.append("botany.common_names_de ist leer")
    if not d["botany"].get("family"):
        errors.append("botany.family fehlt")

    # --- Bestimmung ---
    feats = d["identification"].get("key_features", [])
    if len(feats) < 3:
        errors.append(f"identification.key_features: nur {len(feats)} — mindestens 3 nötig")

    flags = d["safety"].get("flags", {})
    warn_entry = flags.get("not_for_use", False)

    # --- VERWECHSLUNGEN (sicherheitskritisch) ---
    conf = d.get("confusions", [])
    if not conf:
        errors.append(
            "confusions ist LEER. Niemals stillschweigend leer lassen — "
            "entweder Doppelgänger eintragen oder explizit "
            "'keine relevante Verwechslung bekannt' mit Begründung."
        )
    for i, c in enumerate(conf):
        tox = c.get("toxicity_level", "")
        if tox not in TOXICITY:
            errors.append(f"confusions[{i}].toxicity_level '{tox}' ungültig — erlaubt: {sorted(TOXICITY)}")
        if not c.get("note"):
            errors.append(f"confusions[{i}]: 'note' fehlt — WIE unterscheiden?")
        if tox in ("giftig", "lebensgefährlich") and not c.get("toxin"):
            warns.append(f"confusions[{i}] ({c.get('name')}): giftig, aber kein 'toxin' benannt")

    deadly = any(c.get("toxicity_level") == "lebensgefährlich" for c in conf)
    if deadly and not flags.get("deadly_confusion"):
        errors.append("Lebensgefährlicher Doppelgänger vorhanden, aber flags.deadly_confusion ist nicht true")
    if flags.get("deadly_confusion") and not deadly:
        warns.append("flags.deadly_confusion=true, aber kein Doppelgänger ist 'lebensgefährlich'")

    # --- Indikationen ---
    inds = d.get("indications", [])
    if warn_entry:
        if inds:
            errors.append("Warneintrag (not_for_use): indications muss LEER sein")
    else:
        if not inds:
            errors.append("indications ist leer (bei einer Heilpflanze nicht zulässig)")
        for i, ind in enumerate(inds):
            for f in ("canonical", "synonyms", "evidence_tag", "realistic_expectation", "source"):
                if not ind.get(f):
                    errors.append(f"indications[{i}]: '{f}' fehlt")
            tag = ind.get("evidence_tag", "")
            for part in str(tag).split("/"):
                if part and part not in EVIDENCE:
                    errors.append(f"indications[{i}].evidence_tag '{part}' ungültig — erlaubt: {sorted(EVIDENCE)}")
            if not ind.get("synonyms"):
                warns.append(f"indications[{i}]: keine Synonyme — die Suche findet sie schlecht")

    # --- Sicherheit ---
    if not d["safety"].get("key_warning"):
        errors.append("safety.key_warning fehlt — der eine Satz, der im Feld zählt")
    if not d["safety"].get("pregnancy_lactation"):
        errors.append("safety.pregnancy_lactation fehlt")

    if flags.get("toxin_ceiling") and not flags.get("toxin_type"):
        errors.append("flags.toxin_ceiling=true, aber 'toxin_type' fehlt")
    if flags.get("toxin_ceiling") and not d["safety"].get("tox_ceiling"):
        errors.append("flags.toxin_ceiling=true, aber safety.tox_ceiling ist leer")

    for f in flags:
        if f not in KNOWN_FLAGS:
            warns.append(f"Unbekanntes Flag '{f}' — Tippfehler? (Register greift dann nicht)")

    if flags.get("high_safety"):
        risky = [k for k in ("deadly_confusion", "toxin_ceiling", "interaction_heavy",
                             "pregnancy_contraindicated", "hepatotoxic") if flags.get(k)]
        if risky:
            errors.append(f"flags.high_safety=true widerspricht: {risky}")

    # --- Ernte ---
    months = d["harvest_processing_storage"].get("harvest_month_tags", [])
    if not warn_entry and not months:
        warns.append("harvest_month_tags leer — Kraut erscheint nie im Erntekalender")
    for m in months:
        if not isinstance(m, int) or not 1 <= m <= 12:
            errors.append(f"harvest_month_tags: '{m}' ist kein Monat 1–12")

    organ = d["harvest_processing_storage"].get("harvest_organ", "")
    if organ and not any(o.lower() in organ.lower() for o in ORGANS):
        warns.append(f"harvest_organ '{organ}' — Filter erkennt nur: {sorted(ORGANS)}")

    # --- Quellen ---
    if not d.get("sources"):
        errors.append("sources ist leer — jede Monographie braucht Belege")

    # --- Ehrlichkeits-Check ---
    blob = json.dumps(d, ensure_ascii=False).lower()
    if "unsicher" in blob or "zu prüfen" in blob:
        warns.append("Enthält 'unsicher/zu prüfen' — gut! Der Arzt muss diese Stellen ansehen.")
    if not warn_entry and "hmpc" not in blob and "escop" not in blob and "kommission e" not in blob:
        warns.append("Keine regulatorische Quelle (HMPC/ESCOP/Kommission E) erwähnt — wirklich recherchiert?")

    return errors, warns


def main():
    paths = sys.argv[1:]
    if not paths:
        print(__doc__)
        sys.exit(2)

    total_err = 0
    for p in paths:
        errors, warns = check(p)
        status = "FEHLER" if errors else ("ok, mit Hinweisen" if warns else "ok")
        print(f"\n=== {p} — {status} ===")
        for e in errors:
            print(f"  ✗ FEHLER  {e}")
        for w in warns:
            print(f"  ! Hinweis {w}")
        if not errors and not warns:
            print("  ✓ alles sauber")
        total_err += len(errors)

    print(f"\n{'-' * 50}")
    if total_err:
        print(f"{total_err} Fehler — Monographie(n) NICHT abliefern, bis behoben.")
        sys.exit(1)
    print("Alle Monographien bestehen die Prüfung.")
    print("ACHTUNG: Das Skript prüft Struktur und Konsistenz — NICHT die inhaltliche")
    print("Richtigkeit. Die medizinische Prüfung bleibt beim Arzt.")


if __name__ == "__main__":
    main()
