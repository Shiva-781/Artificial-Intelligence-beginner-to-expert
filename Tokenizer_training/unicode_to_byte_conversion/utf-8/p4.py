# Unicode Input (U+XXXX) से UTF-8 में Convert
# Without BOM
unicode_str = input("Enter Unicode (e.g. U+1F600): ")

code_point = int(unicode_str[2:], 16)
ch = chr(code_point)

utf8 = ch.encode("utf-8")

print("Character :", ch)
print("UTF-8 Hex :", " ".join(f"{b:02X}" for b in utf8))

# Input:

# U+1F600

# Output:

# Character : 😀
# UTF-8 Hex : F0 9F 98 80