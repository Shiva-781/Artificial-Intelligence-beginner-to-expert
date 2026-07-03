# 2. UTF-8 With BOM

# Python में utf-8-sig encoding BOM जोड़ती है।

text = "Hello 😀"

utf8_bom = text.encode("utf-8-sig")

print("Bytes:", utf8_bom)
print("Hex  :", " ".join(f"{b:02X}" for b in utf8_bom))

# Output:

# Bytes: b'\xef\xbb\xbfHello \xf0\x9f\x98\x80'
# Hex  : EF BB BF 48 65 6C 6C 6F 20 F0 9F 98 80