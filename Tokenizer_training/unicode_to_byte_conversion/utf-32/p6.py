# Without BOM (UTF-32BE)
unicode_str = input("Enter Unicode (e.g. U+1F600): ")

code = int(unicode_str[2:], 16)
ch = chr(code)

utf32 = ch.encode("utf-32-be")

print("Character :", ch)
print("Hex Bytes :", " ".join(f"{b:02X}" for b in utf32))

# Input:

# U+1F600

# Output:

# Character : 😀
# Hex Bytes : 00 01 F6 00

# Encoding	                BOM	                        😀 (U+1F600)
# utf-32	               ✅ FF FE 00 00 (LE)          FF FE 00 00 00 F6 01 00
# utf-32-le	                 ❌	                         00 F6 01 00
# utf-32-be	                 ❌	                         00 01 F6 00