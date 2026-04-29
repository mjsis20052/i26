import sys

# Read the file in binary
with open(r"C:\Users\mjsis\OneDrive\Desktop\web de 2do soft\2do\clase-php-mysql-I26.html", "rb") as f:
    data = f.read()

# Detect what encoding the file really is
# Try to decode as utf-8 - if it fails, find the bad sequences

print("File size:", len(data))
print("First 3 bytes:", data[:3].hex())  # Check for BOM

# Try reading as latin-1 and check for patterns
try:
    text_latin1 = data.decode("latin-1")
    # Count suspicious sequences (Ã followed by another char = double-encoded UTF-8)
    count_double = text_latin1.count("Ã")
    print(f"Occurrences of 'Ã' (double-encoding indicator): {count_double}")
except Exception as e:
    print(f"Error reading as latin-1: {e}")

# Check a known broken sequence
idx = data.find(b"Conexi")
if idx >= 0:
    print(f"Bytes after 'Conexi' at pos {idx}: {data[idx+6:idx+12].hex()}")
    print(f"Expected for 'ón': c3b3 6e")
