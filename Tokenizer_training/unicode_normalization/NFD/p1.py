import unicodedata

while True:
    text = input("\nEnter Unicode string (or 'exit' to quit): ")

    if text.lower() == "exit":
        break

    # NFD Normalization
    nfd = unicodedata.normalize("NFD", text)

    print("\n" + "=" * 70)
    print("Original :", repr(text))
    print("NFD      :", repr(nfd))
    print("=" * 70)

    # Original text characters
    print("\nCharacters & Code Points")
    print("-" * 70)

    for i, c in enumerate(text):
        print(
            f"[{i}] "
            f"'{c}'  "
            f"U+{ord(c):04X}  "
            f"CCC={unicodedata.combining(c):3}  "
            f"{unicodedata.name(c, 'UNKNOWN')}"
        )

    # NFD characters
    print("\nNFD Characters & Code Points")
    print("-" * 70)

    for i, c in enumerate(nfd):
        print(
            f"[{i}] "
            f"'{c}'  "
            f"U+{ord(c):04X}  "
            f"CCC={unicodedata.combining(c):3}  "
            f"{unicodedata.name(c, 'UNKNOWN')}"
        )

    print("\nUTF-8 Bytes")
    print("-" * 70)
    print("Original :", text.encode("utf-8").hex(" "))
    print("NFD      :", nfd.encode("utf-8").hex(" "))

    print("\nStatistics")
    print("-" * 70)
    print("Original Length :", len(text))
    print("NFD Length      :", len(nfd))
    print("Already NFD     :", unicodedata.is_normalized("NFD", text))
    print("Changed         :", text != nfd)





    # Test Case 1

# Input
# Ạ̊é가ﬁ①Ｆ




# Output


# ======================================================================
# Original : 'Ạ̊é가ﬁ①Ｆ'
# NFD      : 'Ạ̊é가ﬁ①Ｆ'
# ======================================================================

# Characters & Code Points
# ----------------------------------------------------------------------
# [0] 'A'  U+0041  CCC=  0  LATIN CAPITAL LETTER A
# [1] '̊'  U+030A  CCC=230  COMBINING RING ABOVE
# [2] '̣'  U+0323  CCC=220  COMBINING DOT BELOW
# [3] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [4] '́'  U+0301  CCC=230  COMBINING ACUTE ACCENT
# [5] 'ᄀ'  U+1100  CCC=  0  HANGUL CHOSEONG KIYEOK
# [6] 'ᅡ'  U+1161  CCC=  0  HANGUL JUNGSEONG A
# [7] 'ﬁ'  U+FB01  CCC=  0  LATIN SMALL LIGATURE FI
# [8] '①'  U+2460  CCC=  0  CIRCLED DIGIT ONE
# [9] 'Ｆ'  U+FF26  CCC=  0  FULLWIDTH LATIN CAPITAL LETTER F

# NFD Characters & Code Points
# ----------------------------------------------------------------------
# [0] 'A'  U+0041  CCC=  0  LATIN CAPITAL LETTER A
# [1] '̣'  U+0323  CCC=220  COMBINING DOT BELOW
# [2] '̊'  U+030A  CCC=230  COMBINING RING ABOVE
# [3] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [4] '́'  U+0301  CCC=230  COMBINING ACUTE ACCENT
# [5] 'ᄀ'  U+1100  CCC=  0  HANGUL CHOSEONG KIYEOK
# [6] 'ᅡ'  U+1161  CCC=  0  HANGUL JUNGSEONG A
# [7] 'ﬁ'  U+FB01  CCC=  0  LATIN SMALL LIGATURE FI
# [8] '①'  U+2460  CCC=  0  CIRCLED DIGIT ONE
# [9] 'Ｆ'  U+FF26  CCC=  0  FULLWIDTH LATIN CAPITAL LETTER F

# UTF-8 Bytes
# ----------------------------------------------------------------------
# Original : 41 cc 8a cc a3 65 cc 81 e1 84 80 e1 85 a1 ef ac 81 e2 91 a0 ef bc a6
# NFD      : 41 cc a3 cc 8a 65 cc 81 e1 84 80 e1 85 a1 ef ac 81 e2 91 a0 ef bc a6

# Statistics
# ----------------------------------------------------------------------
# Original Length : 10
# NFD Length      : 10
# Already NFD     : False
# Changed         : True




# Test Case 2


# Input
# à̕




# Output







# Test Case 3



# Input
# क़




# Output






# Tset case 5:





# Input

# Enter Unicode string (or 'exit' to quit): exit

# Output

# Enter Unicode string (or 'exit' to quit): exit

# Program yahin khatam ho jayega (koi aur output nahi aayega).




# Tset case 6:





# Input

# Enter Unicode string (or 'exit' to quit): EXIT

# Output

# Enter Unicode string (or 'exit' to quit): EXIT

# Program yahin khatam ho jayega (koi aur output nahi aayega).






# Test case 7:

# input 



#Hello! My name is Rahul. Café, résumé, naïve, coöperate, é 😀 🚀 ❤️ Hindi: नमस्ते Emoji: 😀😂👍 Currency: ₹ $ € Math: ∑ √ ∞



# output:





# sare input se run karke  output nikaal lo