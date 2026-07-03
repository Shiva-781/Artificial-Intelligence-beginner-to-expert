# 3. UTF-32 Big Endian (Without BOM)
text = "Hello 😀"

utf32 = text.encode("utf-32-be")

print("Hex  :", " ".join(f"{b:02X}" for b in utf32))

# Output:

# 00 00 00 48
# 00 00 00 65
# 00 00 00 6C
# 00 00 00 6C
# 00 00 00 6F
# 00 00 00 20
# 00 01 F6 00