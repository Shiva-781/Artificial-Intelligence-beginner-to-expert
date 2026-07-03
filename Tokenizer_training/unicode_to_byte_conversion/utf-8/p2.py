# 1. UTF-8 Without BOM
text = "Hello 😀"

utf8_bytes = text.encode("utf-8")

print("Bytes:", utf8_bytes)
print("Hex  :", " ".join(f"{b:02X}" for b in utf8_bytes))

# Output:

# Bytes: b'Hello \xf0\x9f\x98\x80'
# Hex  : 48 65 6C 6C 6F 20 F0 9F 98 80