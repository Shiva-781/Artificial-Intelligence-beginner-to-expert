# Without BOM (UTF-16BE)
unicode_str = input("Enter Unicode: ")

code = int(unicode_str[2:], 16)
ch = chr(code)

utf16 = ch.encode("utf-16-be")

print("Character :", ch)
print("Hex Bytes :", " ".join(f"{b:02X}" for b in utf16))

# Input:

# U+1F600

# Output:

# Character : 😀
# Hex Bytes : D8 3D DE 00



# Note:  UTF-16 LE  me poora ulta nhi likha jaata  balki do box hot hai dono box apni jagah per hi rhte hai unka order nhi badlta box me bits bharne ke bad dono ke box apne hi andar 8-8 bit ke pair ka order change kar lete hai


# utf-32 LE   me  pura 8-8 bit ke pair ke order ko ulta likhte hai


# Encoding                  	BOM           	            Example (😀)
# utf-16	              ✅ FF FE (या FE FF)	         FF FE 3D D8 00 DE
# utf-16-le	                ❌	                           3D D8 00 DE
# utf-16-be	                ❌	                           D8 3D DE 00





# //jab  utf-16  me 4 byte character ho to bha surrogate pair ka role aata hai

# Surrogate Pair UTF-16 की एक तकनीक है, जिसका उपयोग उन Unicode characters को स्टोर करने के लिए किया जाता है जिनका code point U+10000 से बड़ा होता है।

# क्यों ज़रूरत पड़ती है?

# UTF-16 में एक code unit 16 bits (2 bytes) का होता है।

# U+0000 से U+FFFF तक के characters → 1 code unit (2 bytes) में आ जाते हैं।
# U+10000 से U+10FFFF तक के characters → 1 code unit में नहीं आते, इसलिए 2 code units (4 bytes) का उपयोग किया जाता है। इन्हीं दो code units को Surrogate Pair कहते हैं।
# उदाहरण 1: A

# Unicode:

# U+0041

# UTF-16:

# 41 00

# यह surrogate pair नहीं है क्योंकि U+0041 < U+10000।

# उदाहरण 2: क

# Unicode:

# U+0915

# UTF-16:

# 15 09

# यह भी surrogate pair नहीं है।

# उदाहरण 3: 😀 (Emoji)

# Unicode:

# U+1F600

# यह U+10000 से बड़ा है, इसलिए UTF-16 इसे दो 16-bit values में बदलता है:

# High Surrogate = D83D
# Low Surrogate = DE00

# UTF-16BE:

# D8 3D DE 00

# UTF-16LE:

# 3D D8 00 DE

# इसी जोड़ी (D83D + DE00) को Surrogate Pair कहते हैं।





# UTF-8 vs UTF-16 vs UTF-32

# Encoding	               😀 (U+1F600)
# UTF-8	                    F0 9F 98 80 (4 bytes)
# UTF-16                	D8 3D    DE 00 (Surrogate Pair)
# UTF-32                 	00 01 F6 00 (4 bytes, सीधे code point)


# याद रखने की ट्रिक
# UTF-8 → Surrogate Pair नहीं।
# UTF-16 → U+10000 और उससे बड़े code points के लिए Surrogate Pair।
# UTF-32 → Surrogate Pair नहीं, क्योंकि हर character 4 bytes में सीधे स्टोर होता है।