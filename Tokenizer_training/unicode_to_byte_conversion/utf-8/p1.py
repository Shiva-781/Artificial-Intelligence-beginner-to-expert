unicode_str = input("Enter Unicode (e.g. U+1F600): ")

# U+ हटाकर hexadecimal को integer में बदलें
code_point = int(unicode_str[2:], 16)

# Unicode code point → Character
ch = chr(code_point)

# Character → UTF-8 bytes
utf8_bytes = ch.encode("utf-8")

print("Character :", ch)
print("UTF-8 Bytes:", utf8_bytes)

# Hex format में bytes
print("Hex Bytes :", " ".join(f"{b:02X}" for b in utf8_bytes))



# Example 1

# Input:

# U+0041

# Output:

# Character : A
# UTF-8 Bytes: b'A'
# Hex Bytes : 41



# Example 2

# Input:

# U+0915

# Output:

# Character : क
# UTF-8 Bytes: b'\xe0\xa4\x95'
# Hex Bytes : E0 A4 95



# Example 3

# Input:

# U+1F600

# Output:

# Character : 😀
# UTF-8 Bytes: b'\xf0\x9f\x98\x80'
# Hex Bytes : F0 9F 98 80





# यह conversion इस क्रम में होता है:

# U+1F600
#    ↓
# chr(0x1F600)
#    ↓
# 😀
#    ↓
# .encode("utf-8")
#    ↓
# b'\xf0\x9f\x98\x80'


#  utf-8  me  big indian aur little indian ka concept nhi hota isliye  BOM ka concept optional hai matlab use hi nhi karte