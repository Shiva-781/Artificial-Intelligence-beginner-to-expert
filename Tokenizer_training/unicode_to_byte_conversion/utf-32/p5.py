# Without BOM (UTF-32LE)
unicode_str = input("Enter Unicode (e.g. U+1F600): ")

code = int(unicode_str[2:], 16)
ch = chr(code)

utf32 = ch.encode("utf-32-le")

print("Character :", ch)
print("Hex Bytes :", " ".join(f"{b:02X}" for b in utf32))

# Input:

# U+1F600

# Output:

# Character : 😀
# Hex Bytes : 00 F6 01 00