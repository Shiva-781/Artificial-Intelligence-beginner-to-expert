# 3. UTF-16 Big Endian (Without BOM)
text = "Hello 😀"

utf16 = text.encode("utf-16-be")

print("Bytes:", utf16)
print("Hex  :", " ".join(f"{b:02X}" for b in utf16))

# Output:
# Bytes: b'\x00H\x00e\x00l\x00l\x00o\x00 \xd8=\xde\x00'
# Hex  : 00 48 00 65 00 6C 00 6C 00 6F 00 20 D8 3D DE 00