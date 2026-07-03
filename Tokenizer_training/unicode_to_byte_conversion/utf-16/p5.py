# Without BOM (UTF-16LE)
unicode_str = input("Enter Unicode: ")

code = int(unicode_str[2:], 16)
ch = chr(code)

utf16 = ch.encode("utf-16-le")

print("Character :", ch)
print("Hex Bytes :", " ".join(f"{b:02X}" for b in utf16))

# Input:

# U+1F600

# Output:

# Character : 😀
# Hex Bytes : 3D D8 00 DE