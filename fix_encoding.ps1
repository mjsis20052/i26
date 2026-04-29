# fix_encoding_final.ps1
# Nuclear option: replace known broken byte sequences directly in the byte array

$file = "C:\Users\mjsis\OneDrive\Desktop\web de 2do soft\2do\clase-php-mysql-I26.html"
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

# Read as raw bytes
$bytes = [System.IO.File]::ReadAllBytes($file)

# Build list of (broken-sequence -> correct-sequence) byte replacements
# All these are UTF-8 representations of the broken text
# 
# The pattern we see is C3 83 not C3 B3 - it's been shifted
# Let's try: convert the whole file treating it as CP1252 (Windows-1252) -> UTF-8

$cp1252 = [System.Text.Encoding]::GetEncoding(1252)
$text1252 = $cp1252.GetString($bytes)
# Now encode to UTF-8
$fixedBytes = $utf8NoBom.GetBytes($text1252)
[System.IO.File]::WriteAllBytes($file, $fixedBytes)

Write-Host "Applied CP1252 fix"

$b2 = [System.IO.File]::ReadAllBytes($file)
for ($i = 0; $i -lt ($b2.Length - 10); $i++) {
    if ($b2[$i] -eq 67 -and $b2[$i+1] -eq 111 -and $b2[$i+2] -eq 110 -and $b2[$i+3] -eq 101 -and $b2[$i+4] -eq 120 -and $b2[$i+5] -eq 105) {
        $h6 = [string]::Format("{0:X2}", $b2[$i+6])
        $h7 = [string]::Format("{0:X2}", $b2[$i+7])
        Write-Host "After Conexi: $h6 $h7  (want C3 B3 for utf8 o-acute)"
        break
    }
}

# Also show what the text looks like around that area as string
$asText = $utf8NoBom.GetString($b2)
$idx = $asText.IndexOf("Conexi")
if ($idx -ge 0) {
    Write-Host "Text: '$($asText.Substring($idx, 20))'"
}
