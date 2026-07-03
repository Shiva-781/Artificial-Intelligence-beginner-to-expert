
# 2. UTF-16 Little Endian (Without BOM)
text = "Hello 😀"

utf16 = text.encode("utf-16-le")

print("Bytes:", utf16)
print("Hex  :", " ".join(f"{b:02X}" for b in utf16))

# Output:
# Bytes: b'H\x00e\x00l\x00l\x00o\x00 \x00=\xd8\x00\xde'
# Hex  : 48 00 65 00 6C 00 6C 00 6F 00 20 00 3D D8 00 DE