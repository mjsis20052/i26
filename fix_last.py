#!/usr/bin/env python3
# fix_last.py — últimas correcciones puntuales

import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

file_path = r"C:\Users\mjsis\OneDrive\Desktop\web de 2do soft\2do\clase-php-mysql-I26.html"
with open(file_path, "rb") as f:
    raw = f.read()
text = raw.decode("utf-8")

pairs = [
    # Hero badge
    ("🎓 2do año ?? I26",        "🎓 2do año · I26"),
    # Table comment operators
    ("// ??mismo valor Y tipo?", "// ¿mismo valor Y tipo?"),
    ("// ??a es mayor?",         "// ¿a es mayor?"),
    ("// ??a es menor?",         "// ¿a es menor?"),
    ("// ??a es mayor o igual?", "// ¿a es mayor o igual?"),
    ("// ??a es menor o igual?", "// ¿a es menor o igual?"),
    # Connection data separators
    ('localhost</code> ?? usuario',          'localhost</code> · usuario'),
    ('root</code> ?? contraseña',            'root</code> · contraseña'),
    ('(vacía) ?? puerto',                    '(vacía) · puerto'),
    # Code comments
    ("Si se envi?? el formulario",           "Si se envió el formulario"),
    ("(m??todo POST)",                       "(método POST)"),
    ("WHERE es CR??TICO",                    "WHERE es CRÍTICO"),
    ("sin ??l actualizar??a",                "sin él actualizaría"),
    ("sin ??l borra",                        "sin él borra"),
    ("Siempre sanitiz?? los datos",          "Siempre sanitizá los datos"),
    ("previene inyecci??n",                  "previene inyección"),
    # SQL section
    ("programaci??n general",                "programación general"),
    ("le dec??s",                            "le decís"),
    ("qué quer??s",                          "qué querés"),
    ("hoja de c??lculo",                     "hoja de cálculo"),
    ("inscripci??n con valor",               "inscripción con valor"),
    # type-desc in SQL section
    ("N??mero entero. Rango",                "Número entero. Rango"),
    ("99.99 ?? 1500.50",                     "99.99 · 1500.50"),
    ("sin l??mite",                          "sin límite"),
    ("cu??ndo ocurri??",                     "cuándo ocurrió"),
    ("fila espec??fica",                     "fila específica"),
    # Index
    (">??ndice automático",                  ">Índice automático"),
    ("MySQL crea un ??ndice",               "MySQL crea un índice"),
    # VS Code card  
    ('"dl-icon">═══?</div>',                '"dl-icon">💻</div>'),
    # online-icon leftover
    ('"online-icon">???</div>',             '"online-icon">🌐</div>'),
    # leftover ??? as generic arrow
]

fixed = text
count = 0
for broken, correct in pairs:
    n = fixed.count(broken)
    if n:
        fixed = fixed.replace(broken, correct)
        count += n

remaining = len(re.findall(r'\?\?', fixed))
print(f"Fixed: {count} occurrences")
print(f"Remaining '??' patterns: {remaining}")

if remaining > 0:
    ctxs = [(m.start(), fixed[max(0,m.start()-30):m.start()+35])
            for m in re.finditer(r'\?\?', fixed)]
    for pos, ctx in ctxs[:15]:
        print(f"  {repr(ctx)}")

encoded = fixed.encode("utf-8")
with open(file_path, "wb") as f:
    f.write(encoded)
print(f"Saved ({len(encoded)} bytes)")
