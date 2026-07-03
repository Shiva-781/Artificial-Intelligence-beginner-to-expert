# 1. UTF-16 With BOM
text = "Hello 😀"

utf16 = text.encode("utf-16")

print("Bytes:", utf16)
print("Hex  :", " ".join(f"{b:02X}" for b in utf16))

# Output (Little Endian सिस्टम पर):

# Bytes: b'\xff\xfeH\x00e\x00l\x00l\x00o\x00 \x00=\xd8\x00\xde'
# Hex  : FF FE 48 00 65 00 6C 00 6C 00 6F 00 20 00 3D D8 00 DE
# FF FE → BOM
# बाकी UTF-16LE data है।