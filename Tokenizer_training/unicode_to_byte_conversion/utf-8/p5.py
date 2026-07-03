# Unicode Input (U+XXXX) से UTF-8 में Convert
# With BOM
unicode_str = input("Enter Unicode (e.g. U+1F600): ")

code_point = int(unicode_str[2:], 16)
ch = chr(code_point)

utf8 = ch.encode("utf-8-sig")

print("Character :", ch)
print("UTF-8 Hex :", " ".join(f"{b:02X}" for b in utf8))

# Input:

# U+1F600

# Output:

# Character : 😀
# UTF-8 Hex : EF BB BF F0 9F 98 80
# ध्यान दें
# utf-8 → BOM नहीं जोड़ता।
# utf-8-sig → शुरुआत में EF BB BF (UTF-8 BOM) जोड़ता है।
# UTF-8 में Big Endian या Little Endian नहीं होता; BOM केवल फ़ाइल को UTF-8 के रूप में पहचानने के लिए उपयोग किया जाता है।