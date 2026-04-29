#!/usr/bin/env python3
# fix_lineas.py - Repara los ?? restantes en clase-php-mysql-I26.html
# Lee línea por línea y aplica reemplazos exactos de línea

file_path = r"C:\Users\mjsis\OneDrive\Desktop\web de 2do soft\2do\clase-php-mysql-I26.html"

with open(file_path, "rb") as f:
    raw = f.read()

text = raw.decode("utf-8")
lines = text.splitlines(keepends=True)

# Mapa de reemplazos: (stripped_line_to_match, replacement_stripped)
# Los emojis se asignan por el contexto de la línea vecina
# Trabajamos con un approach de ventana: reemplazamos líneas según lo que viene antes

# Primero hacemos los reemplazos simples que no dependen del contexto
simple = [
    # type-card icons (por type-name siguiente)
    ('        <div class="type-icon">????</div>', None),  # placeholder, handled below
    # Accent missing still
    ("N??meros enteros", "Números enteros"),
    ("N??meros con parte decimal", "Números con parte decimal"),
    ("Funci??n para ver el tipo", "Función para ver el tipo"),
    ("Operadores L??gicos", "Operadores Lógicos"),
    ("Operadores Aritm??ticos", "Operadores Aritméticos"),
    ("Operadores de Asignaci??n", "Operadores de Asignación"),
    ("Operadores de Comparaci??n", "Operadores de Comparación"),
    ("M??dulo", "Módulo"),
    ("S??mbolo", "Símbolo"),
    ("s??mbolos", "símbolos"),
    ("entre s??.", "entre sí."),
    # switch section
    ("PHP ??? if / elseif / else", "PHP — if / elseif / else"),
    ("PHP ??? switch", "PHP — switch"),
    ("switch ??? Cuando", "switch — Cuando"),
    ("\"??Casi fin de semana!\"", '"¡Casi fin de semana!"'),
    ("\"s??bado\"", '"sábado"'),
    ("\"D??a de semana\"", '"Día de semana"'),
    # connections / crud
    ("SECCIÓN 07 ??? CONEXIÓN", "SECCIÓN 07 — CONEXIÓN"),
    ("SECCIÓN 08 ??? CRUD", "SECCIÓN 08 — CRUD"),
    ("Conexión PHP ??? MySQL", "Conexión PHP → MySQL"),
    ("Flujo de conexión PHP ??? MySQL", "Flujo de conexión PHP → MySQL"),
    ("Paso 1 ??? Crear", "Paso 1 → Crear"),
    ("Paso 2 ??? Archivo", "Paso 2 → Archivo"),
    ("Paso 3 ??? Usar", "Paso 3 → Usar"),
    ("PHP ??? conexion.php", "PHP → conexion.php"),
    ("PHP ??? cualquier archivo", "PHP → cualquier archivo"),
    ("conexión fue exitosa ???", "conexión fue exitosa ✓"),
    ("// Establecer charset (importante para tildes y ??)", "// Establecer charset (importante para tildes y ñ)"),
    ("host = <code", "host = <code"),  # vacáa -> vacía
    ("vacáa)", "vacía)"),
    ("Contraseña (XAMPP default = vacáa)", "Contraseña (XAMPP default = vacía)"),
    ("Inici?? XAMPP", "Iniciá XAMPP"),
    ("y escribió:", "y escribís:"),
    # crud sections
    ("C ??? CREATE", "C → CREATE"),
    ("R ??? READ", "R → READ"),
    ("D ??? DELETE", "D → DELETE"),
    ("C ??? CREATE ??? Formulario", "C — CREATE — Formulario"),
    ("HTML ??? form_agregar.html", "HTML — form_agregar.html"),
    ("PHP ??? agregar.php", "PHP — agregar.php"),
    ("PHP ??? leer.php", "PHP — leer.php"),
    ("PHP ??? editar.php", "PHP — editar.php"),
    ("PHP ??? eliminar.php", "PHP — eliminar.php"),
    ("PHP ??? actualizar.php", "PHP — actualizar.php"),
    ("READ ??? Listado", "READ — Listado"),
    ("UPDATE ??? Formulario", "UPDATE — Formulario"),
    ("DELETE ??? Eliminar", "DELETE → Eliminar"),
    # SQL section  
    ("SECCIÓN 09 ??? SQL", "SECCIÓN 09 — SQL"),
    ("SQL ??? Lenguaje", "SQL — Lenguaje"),
    ("SQL ??? CREATE TABLE", "SQL — CREATE TABLE"),
    ("SQL ??? INSERT", "SQL — INSERT"),
    ("SQL ??? SELECT", "SQL — SELECT"),
    ("SQL ??? UPDATE", "SQL — UPDATE"),
    ("SQL ??? DELETE", "SQL — DELETE"),
    ("SQL ??? WHERE", "SQL — WHERE"),
    ("SQL ??? claves", "SQL — claves"),
    ("SQL ??? ORDER", "SQL — ORDER"),
    # more switch
    ("\"??Casi", '"¡Casi'),
    # feature-icon in steps
    # The numbered steps (1️⃣, 2°????, 3°????)
    ("2°????", "2°"),
    ("3°????", "3°"),
    # VS code card
    ("VS Code ??? Editor", "VS Code — Editor"),
    ("code.visualstudio.com ?? Gratis", "code.visualstudio.com — Gratis"),
    ("Practicá PHP online ??? sin instalar", "Practicá PHP online — sin instalar"),
    # online-card icon broken
    # misc CRUD arrows
    ("El usuario llena un formulario ??? PHP", "El usuario llena un formulario → PHP"),
    ("El usuario edita datos ??? PHP", "El usuario edita datos → PHP"),
    # SQL descriptions
    ("??? clic en <strong>", "→ clic en <strong>"),
    ("??? Escribís el nombre:", "→ Escribís el nombre:"),
    ("??? Collation:", "→ Collation:"),
    ("utf8mb4_unicode_ci ??? <strong>Crear", "utf8mb4_unicode_ci → <strong>Crear"),
    # buenas practicas arrow
    ("buena práctica ??? libera", "buena práctica — libera"),
    # Remaining accent words
    ("acr??nimo:", "acrónimo:"),
    ("\"Multiplataforma\" ??? and??", '"Multiplataforma" — andá'),
    ("???", "→"),   # generic fallback for remaining triple-?
    # index badge 2?? year
]

# Apply simple text replacements across the whole text
fixed = text
count = 0
for broken, correct in simple:
    if correct is None:
        continue
    n = fixed.count(broken)
    if n > 0:
        fixed = fixed.replace(broken, correct)
        count += n

# ─── Context-aware line-by-line fix for type/feature/box icons ───────────────
# We need to look at the NEXT meaningful line to decide which emoji to assign

lines2 = fixed.splitlines(keepends=True)
result = []
i = 0

# Map: next div class/content → emoji for ????
# type-icon: determined by type-name next
type_icon_map = {
    "String":    "📝",
    "Integer":   "🔢",
    "Float":     "🔣",
    "Boolean":   "☑️",
    "Array":     "📚",
    "NULL":      "🚫",
    "Object":    "🧩",
    "gettype()": "🔍",
}

# feature-icon: determined by h4 content
feature_icon_map = {
    "Base de datos relacional": "🗄️",
    "Se consulta con SQL":      "📋",
    "phpMyAdmin":               "🖥️",
    "PHP + MySQL":              "🔗",
    "Abrir phpMyAdmin":         "🖥️",
    "Crear la base de datos":   "🗃️",
    "Crear la tabla":           "📋",
}

# box-icon: determined by box-label
box_icon_map = {
    "Navegador":       "🌐",
    "Apache + PHP":    "⚙️",
    "MySQL":           "🗄️",
    "HTML":            "📄",
    "conexion.php":    "📄",
    "new mysqli()":    "⚙️",
    "$conexion":       "✅",
}

while i < len(lines2):
    line = lines2[i]
    stripped = line.strip()

    # Fix type-icon ????
    if '????</div>' in line and 'type-icon' in line:
        # look ahead for type-name
        emoji = "📌"
        for j in range(i+1, min(i+4, len(lines2))):
            nxt = lines2[j].strip()
            if 'type-name' in nxt:
                for key, val in type_icon_map.items():
                    if key in nxt:
                        emoji = val
                        break
                break
        line = line.replace('????</div>', f'{emoji}</div>')

    # Fix feature-icon ????
    elif '????</div>' in line and 'feature-icon' in line:
        emoji = "💡"
        for j in range(i+1, min(i+5, len(lines2))):
            nxt = lines2[j].strip()
            if '<h4>' in nxt or '<h4 ' in nxt:
                for key, val in feature_icon_map.items():
                    if key in nxt:
                        emoji = val
                        break
                break
        line = line.replace('????</div>', f'{emoji}</div>')

    # Fix box-icon ????
    elif '????</div>' in line and 'box-icon' in line:
        emoji = "📦"
        for j in range(i+1, min(i+4, len(lines2))):
            nxt = lines2[j].strip()
            if 'box-label' in nxt:
                for key, val in box_icon_map.items():
                    if key in nxt:
                        emoji = val
                        break
                break
        line = line.replace('????</div>', f'{emoji}</div>')

    # Fix callout-icon ????
    elif '????</div>' in line and 'callout-icon' in line:
        # look at callout class
        emoji = "💡"
        for j in range(i-3, i):
            if j >= 0:
                prev = lines2[j]
                if 'callout warn' in prev:
                    emoji = "⚠️"
                    break
                elif 'callout tip' in prev:
                    emoji = "💡"
                    break
                elif 'callout info' in prev:
                    emoji = "ℹ️"
                    break
        line = line.replace('????</div>', f'{emoji}</div>')

    # Fix online-icon ???
    elif '???</div>' in line and 'online-icon' in line:
        line = line.replace('???</div>', '🌐</div>')

    # Fix dl-icon ════? (leftover)
    elif '═══?</div>' in line and 'dl-icon' in line:
        line = line.replace('═══?</div>', '💻</div>')

    # Fix box-icon ════?
    elif '═══?</div>' in line and 'box-icon' in line:
        emoji = "🗄️"
        for j in range(i+1, min(i+4, len(lines2))):
            nxt = lines2[j].strip()
            if 'box-label' in nxt:
                if 'MySQL' in nxt:
                    emoji = "🗄️"
                break
        line = line.replace('═══?</div>', f'{emoji}</div>')

    # Fix feature-icon ════?
    elif '═══?</div>' in line and 'feature-icon' in line:
        emoji = "📋"
        for j in range(i+1, min(i+5, len(lines2))):
            nxt = lines2[j].strip()
            if '<h4>' in nxt or '<h4 ' in nxt:
                if 'Base de datos' in nxt:
                    emoji = "🗄️"
                elif 'phpMyAdmin' in nxt:
                    emoji = "🖥️"
                break
        line = line.replace('═══?</div>', f'{emoji}</div>')

    # Fix box-icon ════ (the apache+php box that got turned into three ═══)  
    elif '═══</div>' in line and 'box-icon' in line:
        emoji = "⚙️"
        for j in range(i+1, min(i+4, len(lines2))):
            nxt = lines2[j].strip()
            if 'box-label' in nxt:
                if 'Apache' in nxt or 'mysqli' in nxt:
                    emoji = "⚙️"
                elif 'conexion' in nxt:
                    emoji = "📄"
                break
        line = line.replace('═══</div>', f'{emoji}</div>')

    # Fix callout-icon ════ 
    elif '═══</div>' in line and 'callout-icon' in line:
        emoji = "💡"
        for j in range(i-3, i):
            if j >= 0:
                prev = lines2[j]
                if 'callout warn' in prev:
                    emoji = "⚠️"
                    break
                elif 'callout tip' in prev:
                    emoji = "💡"
                    break
                elif 'callout info' in prev:
                    emoji = "ℹ️"
                    break
        line = line.replace('═══</div>', f'{emoji}</div>')

    result.append(line)
    i += 1

fixed2 = "".join(result)

# ─── Final remaining single-char fixes ────────────────────────────────────────
# ??? remaining three-? 
import re
# Only if they are standalone separators (not part of longer sequences)
# At this point most ??? should be arrows we already fixed
# Count remaining
remaining_count = len(re.findall(r'\?\?', fixed2))

# Save
encoded = fixed2.encode("utf-8")
with open(file_path, "wb") as f:
    f.write(encoded)

print(f"Simple replacements: {count}")
remaining_count = len(re.findall(r'\?\?', fixed2))
print(f"Remaining ?? after all fixes: {remaining_count}")
print(f"Saved: {len(encoded)} bytes")
