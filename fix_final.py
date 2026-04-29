#!/usr/bin/env python3
# fix_final.py — Reparación completa de clase-php-mysql-I26.html
# Arregla acentos faltantes Y restaura emojis por contexto exacto

import re

file_path = r"C:\Users\mjsis\OneDrive\Desktop\web de 2do soft\2do\clase-php-mysql-I26.html"

with open(file_path, "rb") as f:
    raw = f.read()

text = raw.decode("utf-8")

# ─── 1. PALABRAS CON ACENTO (patrón broken?? → correcto) ────────────────────
accent_pairs = [
    # ó  (on)
    ("Conexi??n",        "Conexión"),
    ("CONEXI??N",        "CONEXIÓN"),
    ("conexi??n",        "conexión"),
    ("Documentaci??n",   "Documentación"),
    ("documentaci??n",   "documentación"),
    ("creaci??n",        "creación"),
    ("SECCI??N",         "SECCIÓN"),
    ("Secci??n",         "Sección"),
    ("secci??n",         "sección"),
    ("informaci??n",     "información"),
    ("propagaci??n",     "propagación"),
    ("verificaci??n",    "verificación"),
    ("Acci??n",          "Acción"),
    ("acci??n",          "acción"),
    ("Relaci??n",        "Relación"),
    ("relaci??n",        "relación"),
    ("protecci??n",      "protección"),
    ("inserci??n",       "inserción"),
    ("abstracci??n",     "abstracción"),
    ("opci??n",          "opción"),
    ("operaci??n",       "operación"),
    ("definici??n",      "definición"),
    ("configuraci??n",   "configuración"),
    ("comunicaci??n",    "comunicación"),
    ("aplicaci??n",      "aplicación"),
    ("validaci??n",      "validación"),
    ("denominaci??n",    "denominación"),
    ("implementaci??n",  "implementación"),
    ("producci??n",      "producción"),
    ("soluci??n",        "solución"),
    ("elecci??n",        "elección"),
    ("descripci??n",     "descripción"),
    ("gesti??n",         "gestión"),
    ("autentificaci??n", "autentificación"),
    ("Concatenaci??n",   "Concatenación"),
    ("Asignaci??n",      "Asignación"),
    ("Asignaci??n",      "Asignación"),
    ("Comparaci??n",     "Comparación"),
    ("Funci??n",         "Función"),
    ("Decisi??n",        "Decisión"),
    ("decisi??n",        "decisión"),
    ("Multiplicaci??n",  "Multiplicación"),
    ("divisi??n",        "división"),
    ("Divisi??n",        "División"),
    ("condici??n",       "condición"),
    ("acr??nimo",        "acrónimo"),
    ("C??mo",            "Cómo"),
    ("c??mo",            "cómo"),
    ("d??o",             "dúo"),
    # ú
    ("n??mero",          "número"),
    ("n??meros",         "números"),
    ("??nico",           "único"),
    ("??nica",           "única"),
    ("??ltimo",          "último"),
    ("??ltima",          "última"),
    # á
    ("m??s",             "más"),
    ("Adem??s",          "Además"),
    ("adem??s",          "además"),
    ("est??ndar",        "estándar"),
    ("autom??tico",      "automático"),
    ("autom??ticamente", "automáticamente"),
    ("pr??ctica",        "práctica"),
    ("pr??ctico",        "práctico"),
    ("b??sica",          "básica"),
    ("b??sico",          "básico"),
    ("p??gina",          "página"),
    ("m??xima",          "máxima"),
    ("m??ximo",          "máximo"),
    ("car??cter",        "carácter"),
    ("acr??nimo",        "acrónimo"),
    # é
    ("tambi??n",         "también"),
    ("Tambi??n",         "También"),
    ("despu??s",         "después"),
    ("Despu??s",         "Después"),
    ("p??rdida",         "pérdida"),
    # í
    ("m??nimo",          "mínimo"),
    ("expl??citamente",  "explícitamente"),
    # a with tilde (vos forms)
    ("pod??s",           "podés"),
    ("Pod??s",           "Podés"),
    ("Abr??",            "Abrí"),
    ("abr??s",           "abrís"),
    ("intent??s",        "intentás"),
    ("escrib??s",        "escribís"),
    ("escrib??",         "escribió"),
    ("Escrib??s",        "Escribís"),
    ("Us??",             "Usá"),
    ("us??",             "usá"),
    ("peg??",            "pegá"),
    ("and??",            "andá"),
    ("guard??",          "guardá"),
    ("Inici??",          "Inició"),
    ("fall??",           "falló"),
    ("Practic??",        "Practicá"),
    ("Entr??s",          "Entrás"),
    ("necesit??s",       "necesitás"),
    ("pesta??a",         "pestaña"),
    ("contrase??a",      "contraseña"),
    ("Contrase??a",      "Contraseña"),
    ("seg??n",           "según"),
    ("ning??n",          "ningún"),
    ("qu??",             "qué"),
    ("Qu??",             "Qué"),
    ("est??",            "está"),
    ("est??n",           "están"),
    ("gr??fica",         "gráfica"),
    ("din??mico",        "dinámico"),
    ("v??lido",          "válido"),
    ("v??lida",          "válida"),
    ("Id??ntico",        "Idéntico"),
    ("s??mbolos",        "símbolos"),
    ("S??mbolo",         "Símbolo"),
    ("b??squedas",       "búsquedas"),
    ("env??e",           "envíe"),
    # ñ
    ("a??os",            "años"),
    ("a??o",             "año"),
    # inverted punctuation / questions
    ("??Qu?? ",          "¿Qué "),
    ("??Por",            "¿Por"),
    ("??Cu??ndo",        "¿Cuándo"),
    ("??D??nde",         "¿Dónde"),
    ("??C??mo",          "¿Cómo"),
    ("??son",            "¿son"),
    # ° degree symbol (2?? year badge)
    ("2??",              "2°"),
    ("3??",              "3°"),
]

# ─── 2. EMOJIS / CARACTERES ESPECIALES ─────────────────────────────────────
# Restauramos por coincidencia exacta de contexto del HTML
emoji_pairs = [
    # Title / hero
    ("PHP + MySQL + XAMPP ??? Desarrollo",  "PHP + MySQL + XAMPP — Desarrollo"),
    ("Desarrollo de Software ?? 2do a",     "Desarrollo de Software 🎓 2do a"),
    # Arrows in server diagram
    ('<div class="arrow">???</div>',         '<div class="arrow">→</div>'),
    # Nav brand
    (' I26 ?? Software',                     ' I26 · Software'),
    # Nav portal link icon
    ('>???? <span>Portal</span>',            '>🏠 <span>Portal</span>'),
    # Callout icons
    ('"callout-icon">????</div>',            '"callout-icon">⚠️</div>'),  # warn callout (¿Por qué servidor?)
    ('"callout-icon">????</div>',            '"callout-icon">💡</div>'),  # tip callout (punto concatenar)
    ('"callout-icon">????</div>',            '"callout-icon">🛡️</div>'),  # security callout
    ('"callout-icon">????</div>',            '"callout-icon">✅</div>'),  # success callout
    # Server diagram box icons
    ('"box-icon">????</div>\n          <div class="box-label">Navegador',
     '"box-icon">🌐</div>\n          <div class="box-label">Navegador'),
    ('"box-icon">??????</div>\n          <div class="box-label">Apache',
     '"box-icon">⚙️</div>\n          <div class="box-label">Apache'),
    ('"box-icon">???????</div>\n          <div class="box-label">MySQL',
     '"box-icon">🗄️</div>\n          <div class="box-label">MySQL'),
    ('"box-icon">????</div>\n          <div class="box-label">HTML',
     '"box-icon">📄</div>\n          <div class="box-label">HTML'),
    # Feature icons (numbered)
    ('"feature-icon">1??????</div>',         '"feature-icon">1️⃣</div>'),
    ('"feature-icon">2??????</div>',         '"feature-icon">2️⃣</div>'),
    ('"feature-icon">3??????</div>',         '"feature-icon">3️⃣</div>'),
    # Feature item icons (database, SQL, phpMyAdmin, PHP+MySQL)
    ('"feature-icon">???????</div>\n        <div class="feature-content">\n          <h4>Base de datos',
     '"feature-icon">🗄️</div>\n        <div class="feature-content">\n          <h4>Base de datos'),
    ('"feature-icon">????</div>\n        <div class="feature-content">\n          <h4>Se consulta',
     '"feature-icon">📝</div>\n        <div class="feature-content">\n          <h4>Se consulta'),
    ('"feature-icon">???????</div>\n        <div class="feature-content">\n          <h4>phpMyAdmin',
     '"feature-icon">🖥️</div>\n        <div class="feature-content">\n          <h4>phpMyAdmin'),
    ('"feature-icon">????</div>\n        <div class="feature-content">\n          <h4>PHP + MySQL',
     '"feature-icon">🔗</div>\n        <div class="feature-content">\n          <h4>PHP + MySQL'),
    # PHP section title arrow
    ('PHP ??? Variables',                    'PHP → Variables'),
    ('PHP ??? Tipos de datos',               'PHP → Tipos de datos'),
    # Type card icons
    ('"type-icon">????</div>\n        <div class="type-name">String',
     '"type-icon">📝</div>\n        <div class="type-name">String'),
    ('"type-icon">????</div>\n        <div class="type-name">Integer',
     '"type-icon">🔢</div>\n        <div class="type-name">Integer'),
    ('"type-icon">????</div>\n        <div class="type-name">Float',
     '"type-icon">🔣</div>\n        <div class="type-name">Float'),
    ('"type-icon">???</div>\n        <div class="type-name">Boolean',
     '"type-icon">✅</div>\n        <div class="type-name">Boolean'),
    ('"type-icon">????</div>\n        <div class="type-name">Array',
     '"type-icon">📚</div>\n        <div class="type-name">Array'),
    ('"type-icon">????</div>\n        <div class="type-name">NULL',
     '"type-icon">🚫</div>\n        <div class="type-name">NULL'),
    ('"type-icon">????</div>\n        <div class="type-name">Object',
     '"type-icon">🧩</div>\n        <div class="type-name">Object'),
    ('"type-icon">????</div>\n        <div class="type-name">gettype',
     '"type-icon">🔍</div>\n        <div class="type-name">gettype'),
    # dl-card icon  
    ('"dl-icon">????</div>',                 '"dl-icon">⬇️</div>'),
    ('"dl-icon">????</div>',                 '"dl-icon">💻</div>'),
    # online-card icons
    ('"online-icon">????</div>',             '"online-icon">🌐</div>'),
    # inline within type-ex: separators
    ('42 ?? -7 ?? 0',                        '42 · -7 · 0'),
    ('3.14 ?? 8.5',                          '3.14 · 8.5'),
    ('true ?? false',                        'true · false'),
    # AND/OR/NOT indicators
    ('AND (y) ??? ambas',                    'AND (y) — ambas'),
    ('OR (o) ??? al menos',                  'OR (o) — al menos'),
    ('NOT (no) ??? niega',                   'NOT (no) — niega'),
    # concatenation comment
    ('Concatenación ??? unir textos',        'Concatenación → unir textos'),
    # phpMyAdmin interface steps
    ('??? clic en',                          '→ clic en'),
    ('??? nombre:',                          '→ nombre:'),
    ('utf8mb4_unicode_ci ??? <strong>Crear', 'utf8mb4_unicode_ci → <strong>Crear'),
    # Gratis label
    ('apachefriends.org ?? Gratis',          'apachefriends.org ✔ Gratis'),
    # Online tool label  
    ('Prácticá PHP online ??? sin instalar', 'Practicá PHP online — sin instalar'),
    # WHERE crítico
    ('WHERE es CRÍTICO ??? sin',             'WHERE es CRÍTICO → sin'),
    ('sin él actualizar??a TODO',            'sin él actualizaría TODO'),
    # CRUD section labels
    ('U ??? UPDATE',                         'U → UPDATE'),
    ('DELETE ??? Eliminar',                  'DELETE → Eliminar'),
    # dl-card ::after arrow  
    ("content: '???'",                       "content: '→'"),
    # comment dividers (CSS/HTML comments with many ??)
    # We'll handle these with regex below
    # Folder tree
    ('/\n          ????????? conexion.php',  '/\n          └── conexion.php'),
    # Section nav markers
    ('<!-- ????????? CLASE NAV',             '<!-- ═══ CLASE NAV'),
    # phpMyAdmin section
    ("phpMyAdmin ??? La interfaz gr",        "phpMyAdmin — La interfaz gr"),
    # c??digo
    ("c??digo",                              "código"),
    ("C??digo",                              "Código"),
]

fixed = text

# Apply accent fixes
accent_count = 0
for broken, correct in accent_pairs:
    n = fixed.count(broken)
    if n:
        fixed = fixed.replace(broken, correct)
        accent_count += n

# Apply emoji/special char fixes
emoji_count = 0
for broken, correct in emoji_pairs:
    n = fixed.count(broken)
    if n:
        fixed = fixed.replace(broken, correct)
        emoji_count += n

# ─── 3. REGEX FIXES ──────────────────────────────────────────────────────────
# Remove long sequences of ?? used as comment decorators in HTML comments
# e.g. <!-- ??????????????? SECTION --> → <!-- ══════════════ SECTION -->
def replace_long_qmarks(m):
    qmarks = m.group(0)
    n = len(qmarks) // 2
    return '═' * n

before_regex = fixed
fixed = re.sub(r'(?:\?\?){3,}', replace_long_qmarks, fixed)
regex_count = len(re.findall(r'═{2,}', fixed)) - len(re.findall(r'═{2,}', before_regex))

# ─── 4. REMAINING ?? REPORT ──────────────────────────────────────────────────
remaining = re.findall(r'\?\?', fixed)
print(f"[OK] Accent fixes applied: {accent_count}")
print(f"[OK] Emoji/special fixes applied: {emoji_count}")
print(f"[OK] Regex (long sequences) replaced")
print(f"[..] Remaining '??' patterns: {len(remaining)}")

if remaining and len(remaining) <= 50:
    contexts = [(m.start(), fixed[max(0,m.start()-20):m.start()+25])
                for m in re.finditer(r'\?\?', fixed)]
    for pos, ctx in contexts[:30]:
        print(f"  {repr(ctx)}")

# ─── 5. SAVE ─────────────────────────────────────────────────────────────────
encoded = fixed.encode("utf-8")
with open(file_path, "wb") as f:
    f.write(encoded)

print(f"\nGuardado como UTF-8 ({len(encoded)} bytes)")

# Verify Conexion
with open(file_path, "rb") as f:
    data2 = f.read()
idx = data2.find(b"Conexi")
if idx >= 0:
    hex_after = data2[idx+6:idx+10].hex()
    ok = "CORRECTO" if hex_after.startswith("c3b3") else "AUN ROTO"
    print(f"Verificacion 'Conexion': {hex_after} -> {ok}")
