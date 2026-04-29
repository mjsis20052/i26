#!/usr/bin/env python3
import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
file_path = r"C:\Users\mjsis\OneDrive\Desktop\web de 2do soft\2do\clase-php-mysql-I26.html"
with open(file_path, "rb") as f:
    raw = f.read()
text = raw.decode("utf-8")

pairs = [
    ("cambi?? el puerto",        "cambiá el puerto"),
    ("Cre?? una carpeta",         "Creá una carpeta"),
    ('"??Nueva??"',               '"Nueva"'),
    ("Copi?? ",                   "Copí "),
    ("deber??as ver",             "deberías ver"),
    ("Prob?? agregar",            "Probá agregar"),
    ("Soluci??n",                 "Solución"),
    ("la l??gica.",               "la lógica."),
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
if remaining:
    for m in re.finditer(r'\?\?', fixed):
        print(repr(fixed[max(0,m.start()-30):m.start()+35]))

encoded = fixed.encode("utf-8")
with open(file_path, "wb") as f:
    f.write(encoded)
print(f"Saved ({len(encoded)} bytes) - DONE!")
