#!/usr/bin/env python3
# fix_last2.py
import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

file_path = r"C:\Users\mjsis\OneDrive\Desktop\web de 2do soft\2do\clase-php-mysql-I26.html"
with open(file_path, "rb") as f:
    raw = f.read()
text = raw.decode("utf-8")

pairs = [
    ("r??pidas.",                    "rápidas."),
    ("Clave For??nea",               "Clave Foránea"),
    ("un v??nculo",                  "un vínculo"),
    ("Declaraci??n de la FOREIGN",  "Declaración de la FOREIGN"),
    ("la garant??a",                 "la garantía"),
    ("datos hu??rfanos.",            "datos huérfanos."),
    ("'Mar??a'",                     "'María'"),
    ("'P??rez'",                     "'Pérez'"),
    ("'L??pez'",                     "'López'"),
    ("alg??n alumno",                "algún alumno"),
    ("DOCUMENTACI??N",               "DOCUMENTACIÓN"),
    ("C??MO PROBARLO",               "CÓMO PROBARLO"),
    ("Segu?? este checklist",        "Seguí este checklist"),
    ("Descarg?? XAMPP",              "Descargá XAMPP"),
    ("terminar, abr??",              "terminar, abrí"),
]

fixed = text
count = 0
for broken, correct in pairs:
    n = fixed.count(broken)
    if n:
        fixed = fixed.replace(broken, correct)
        count += n

remaining = len(re.findall(r'\?\?', fixed))
print(f"Fixed: {count}, Remaining: {remaining}")

if remaining > 0:
    for m in re.finditer(r'\?\?', fixed):
        print(repr(fixed[max(0,m.start()-30):m.start()+35]))

encoded = fixed.encode("utf-8")
with open(file_path, "wb") as f:
    f.write(encoded)
print(f"Saved ({len(encoded)} bytes)")
