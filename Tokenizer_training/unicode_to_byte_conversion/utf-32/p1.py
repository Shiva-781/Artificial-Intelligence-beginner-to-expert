# 1. UTF-32 With BOM
text = "Hello 😀"

utf32 = text.encode("utf-32")

print("Bytes:", utf32)
print("Hex  :", " ".join(f"{b:02X}" for b in utf32))

# Output (Little Endian सिस्टम पर):

# Hex  : FF FE 00 00
# 48 00 00 00
# 65 00 00 00
# 6C 00 00 00
# 6C 00 00 00
# 6F 00 00 00
# 20 00 00 00
# 00 F6 01 00




# FF FE 00 00 → BOM
# बाकी UTF-32LE data है।