# 2. UTF-32 Little Endian (Without BOM)
text = "Hello 😀"

utf32 = text.encode("utf-32-le")

print("Hex  :", " ".join(f"{b:02X}" for b in utf32))

# Output:

# 48 00 00 00
# 65 00 00 00
# 6C 00 00 00
# 6C 00 00 00
# 6F 00 00 00
# 20 00 00 00
# 00 F6 01 00