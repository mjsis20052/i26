#!/usr/bin/env python3
# fix_final.py - Fixes broken chars by writing correct bytes directly
import re

file_path = r"C:\Users\mjsis\OneDrive\Desktop\web de 2do soft\2do\clase-php-mysql-I26.html"

with open(file_path, "rb") as f:
    raw = f.read()

# The file has '??' where accented chars should be
# We work at the byte level
text = raw.decode("latin-1")

# Mapping of broken patterns (with ??) to correct UTF-8 character
# ? in the file = 0x3F byte = lost character
# We know the original words from the source code we wrote

pairs = [
    ("Conexi??n",       "Conexi\u00f3n"),
    ("CONEXI??N",       "CONEXI\u00d3N"),
    ("Documentaci??n",  "Documentaci\u00f3n"),
    ("documentaci??n",  "documentaci\u00f3n"),
    ("creaci??n",       "creaci\u00f3n"),
    ("conexi??n",       "conexi\u00f3n"),
    ("SECCI??N",        "SECCI\u00d3N"),
    ("Secci??n",        "Secci\u00f3n"),
    ("secci??n",        "secci\u00f3n"),
    ("informaci??n",    "informaci\u00f3n"),
    ("propagaci??n",    "propagaci\u00f3n"),
    ("verificaci??n",   "verificaci\u00f3n"),
    ("acci??n",         "acci\u00f3n"),
    ("Acci??n",         "Acci\u00f3n"),
    ("relaci??n",       "relaci\u00f3n"),
    ("Relaci??n",       "Relaci\u00f3n"),
    ("protecci??n",     "protecci\u00f3n"),
    ("inserci??n",      "inserci\u00f3n"),
    ("abstracci??n",    "abstracci\u00f3n"),
    ("abstracci??n",    "abstracci\u00f3n"),
    ("opci??n",         "opci\u00f3n"),
    ("operaci??n",      "operaci\u00f3n"),
    ("definici??n",     "definici\u00f3n"),
    ("configuraci??n",  "configuraci\u00f3n"),
    ("comunicaci??n",   "comunicaci\u00f3n"),
    ("aplicaci??n",     "aplicaci\u00f3n"),
    ("validaci??n",     "validaci\u00f3n"),
    ("denominaci??n",   "denominaci\u00f3n"),  
    ("implementaci??n", "implementaci\u00f3n"),
    ("producci??n",     "producci\u00f3n"),
    ("soluci??n",       "soluci\u00f3n"),
    ("elecci??n",       "elecci\u00f3n"),
    ("descripci??n",    "descripci\u00f3n"),
    ("gesti??n",        "gesti\u00f3n"),
    ("autentificaci??n","autentificaci\u00f3n"),
    # others with o
    ("c??mo",           "c\u00f3mo"),
    ("C??mo",           "C\u00f3mo"),
    ("n??mero",         "n\u00famero"),
    ("n??meros",        "n\u00fameros"),
    # a-accented
    ("m??s",            "m\u00e1s"),
    ("adem??s",         "adem\u00e1s"),
    ("est??ndar",       "est\u00e1ndar"),
    ("autom??tico",     "autom\u00e1tico"),
    ("autom??ticamente","autom\u00e1ticamente"),
    ("pr??ctica",       "pr\u00e1ctica"),
    ("pr??ctico",       "pr\u00e1ctico"),
    ("b??sica",         "b\u00e1sica"),
    ("b??sico",         "b\u00e1sico"),
    ("p??gina",         "p\u00e1gina"),
    ("m??xima",         "m\u00e1xima"),
    ("m??ximo",         "m\u00e1ximo"),
    ("car??cter",       "car\u00e1cter"),
    ("caract??r",       "car\u00e1cter"),
    ("ac??",            "ac\u00e1"),
    ("Ac??",            "Ac\u00e1"),
    # e-accented  
    ("tambi??n",        "tambi\u00e9n"),
    ("despu??s",        "despu\u00e9s"),
    ("Despu??s",        "Despu\u00e9s"),
    ("p??rdida",        "p\u00e9rdida"),
    ("v??lido",         "v\u00e1lido"),
    ("v??lida",         "v\u00e1lida"),
    # i-accented
    ("m??nimo",         "m\u00ednimo"),
    # u-accented
    ("??nico",          "\u00fanico"),
    ("??nica",          "\u00fanica"),
    ("??ltimo",         "\u00faltimo"),
    # inverted punctuation
    ("??Qu??",          "\u00bfQu\u00e9"),
    ("??Cu??ndo",       "\u00bfCu\u00e1ndo"),
    ("??Por",           "\u00bfPor"),
    ("??D??nde",        "\u00bfD\u00f3nde"),
    ("??C??mo",         "\u00bfC\u00f3mo"),
    ("??Qu??",          "\u00bfQu\u00e9"),
]

fixed = text
count = 0
for broken, correct in pairs:
    if broken in fixed:
        fixed = fixed.replace(broken, correct)
        count += 1

# Now find remaining ?? patterns
remaining = [(m.start(), fixed[max(0,m.start()-15):m.start()+20]) for m in re.finditer(r'\?\?', fixed)]
if remaining:
    print(f"Remaining {len(remaining)} '??' patterns (first 20):")
    for pos, ctx in remaining[:20]:
        print(f"  {repr(ctx)}")

print(f"Applied {count} targeted replacements")

# Write back as UTF-8 bytes directly
encoded = fixed.encode("utf-8")
with open(file_path, "wb") as f:
    f.write(encoded)

print("Saved as UTF-8")

# Verify
with open(file_path, "rb") as f:
    data2 = f.read()
idx = data2.find(b"Conexi")
if idx >= 0:
    hex_after = data2[idx+6:idx+10].hex()
    print(f"Bytes after 'Conexi': {hex_after} (want c3b3 for o-acute)")
