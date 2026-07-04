import unicodedata

while True:
    text = input("\nEnter Unicode string (or 'exit' to quit): ")

    if text.lower() == "exit":
        break

    nfc = unicodedata.normalize("NFC", text)

    print("\n" + "=" * 70)
    #original text
    print("Original :", repr(text))
    #normalized text
    print("NFC      :", repr(nfc))
    print("=" * 70)



#  loop ki help se  original text ke ek ek character ka unicode ,ccc value , uska official unicode name

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


#  loop ki help se normalized test ke ek ek character ka unicode ,ccc value , uska official unicode name
    print("\nNFC Characters & Code Points")
    print("-" * 70)

    for i, c in enumerate(nfc):
        print(
            f"[{i}] "
            f"'{c}'  "
            f"U+{ord(c):04X}  "
            f"CCC={unicodedata.combining(c):3}  " #-----> ye ccc  value batata hai jisse pta chalta hai ki character   starter(normal char)  hai  ya  combining mark 
            f"{unicodedata.name(c, 'UNKNOWN')}"  #----->
        )
#  loop me  i--->index  hai   c---> character

    print("\nUTF-8 Bytes")
    print("-" * 70)
    print("Original :", text.encode("utf-8").hex(" "))# ye string ko unicode ka use karke byte me convert kar deta hai
    print("NFC      :", nfc.encode("utf-8").hex(" "))

    print("\nStatistics")
    print("-" * 70)
    print("Original Length :", len(text))
    print("NFC Length      :", len(nfc))
    print("Already NFC     :", unicodedata.is_normalized("NFC", text))# ----->ye check karta given  string aur char  nfc ya other unicode normalization me normalized hai ya nhi  agr hai to true  nhi hai to false
    print("Changed         :", text != nfc)# agr  equal hua to change nhi hua false output



# Test Case 1

# Input
# Ạ̊é가ﬁ①Ｆ




# Output




# ======================================================================
# Original : 'Ạ̊é가ﬁ①Ｆ'
# NFC      : 'Ạ̊é가ﬁ①Ｆ'
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

# NFC Characters & Code Points
# ----------------------------------------------------------------------
# [0] 'Ạ'  U+1EA0  CCC=  0  LATIN CAPITAL LETTER A WITH DOT BELOW
# [1] '̊'  U+030A  CCC=230  COMBINING RING ABOVE
# [2] 'é'  U+00E9  CCC=  0  LATIN SMALL LETTER E WITH ACUTE
# [3] '가'  U+AC00  CCC=  0  HANGUL SYLLABLE GA
# [4] 'ﬁ'  U+FB01  CCC=  0  LATIN SMALL LIGATURE FI
# [5] '①'  U+2460  CCC=  0  CIRCLED DIGIT ONE
# [6] 'Ｆ'  U+FF26  CCC=  0  FULLWIDTH LATIN CAPITAL LETTER F

# UTF-8 Bytes
# ----------------------------------------------------------------------
# Original : 41 cc 8a cc a3 65 cc 81 e1 84 80 e1 85 a1 ef ac 81 e2 91 a0 ef bc a6
# NFC      : e1 ba a0 cc 8a c3 a9 ea b0 80 ef ac 81 e2 91 a0 ef bc a6

# Statistics
# ----------------------------------------------------------------------
# Original Length : 10
# NFC Length      : 7
# Already NFC     : False
# Changed         : True









# Test Case 2


# Input
# à̕




# Output




# ======================================================================
# Original : 'à̕'
# NFC      : 'à̕'
# ======================================================================

# Characters & Code Points
# ----------------------------------------------------------------------
# [0] 'a'  U+0061  CCC=  0  LATIN SMALL LETTER A
# [1] '̕'  U+0315  CCC=232  COMBINING COMMA ABOVE RIGHT
# [2] '̀'  U+0300  CCC=230  COMBINING GRAVE ACCENT

# NFC Characters & Code Points
# ----------------------------------------------------------------------
# [0] 'à'  U+00E0  CCC=  0  LATIN SMALL LETTER A WITH GRAVE
# [1] '̕'  U+0315  CCC=232  COMBINING COMMA ABOVE RIGHT

# UTF-8 Bytes
# ----------------------------------------------------------------------
# Original : 61 cc 95 cc 80
# NFC      : c3 a0 cc 95

# Statistics
# ----------------------------------------------------------------------
# Original Length : 3
# NFC Length      : 2
# Already NFC     : False
# Changed         : True





# Test Case 3



# Input
# क़




# Output



# ======================================================================
# Original : 'क़'
# NFC      : 'क़'
# ======================================================================

# Characters & Code Points
# ----------------------------------------------------------------------
# [0] 'क़'  U+0958  CCC=  0  DEVANAGARI LETTER QA

# NFC Characters & Code Points
# ----------------------------------------------------------------------
# [0] 'क़'  U+0958  CCC=  0  DEVANAGARI LETTER QA

# UTF-8 Bytes
# ----------------------------------------------------------------------
# Original : e0 a5 98
# NFC      : e0 a5 98

# Statistics
# ----------------------------------------------------------------------
# Original Length : 1
# NFC Length      : 1
# Already NFC     : True
# Changed         : False





# Test case 4





# Input
# नमस्ते



# Output



# ======================================================================
# Original : 'नमस्ते'
# NFC      : 'नमस्ते'
# ======================================================================

# Characters & Code Points
# ----------------------------------------------------------------------
# [0] 'न'  U+0928  CCC=  0  DEVANAGARI LETTER NA
# [1] 'म'  U+092E  CCC=  0  DEVANAGARI LETTER MA
# [2] 'स'  U+0938  CCC=  0  DEVANAGARI LETTER SA
# [3] '्'  U+094D  CCC=  9  DEVANAGARI SIGN VIRAMA
# [4] 'त'  U+0924  CCC=  0  DEVANAGARI LETTER TA
# [5] 'े'  U+0947  CCC=  0  DEVANAGARI VOWEL SIGN E

# NFC Characters & Code Points
# ----------------------------------------------------------------------
# [0] 'न'  U+0928  CCC=  0  DEVANAGARI LETTER NA
# [1] 'म'  U+092E  CCC=  0  DEVANAGARI LETTER MA
# [2] 'स'  U+0938  CCC=  0  DEVANAGARI LETTER SA
# [3] '्'  U+094D  CCC=  9  DEVANAGARI SIGN VIRAMA
# [4] 'त'  U+0924  CCC=  0  DEVANAGARI LETTER TA
# [5] 'े'  U+0947  CCC=  0  DEVANAGARI VOWEL SIGN E

# UTF-8 Bytes
# ----------------------------------------------------------------------
# Original : e0 a4 a8 e0 a4 ae e0 a4 b8 e0 a5 8d e0 a4 a4 e0 a5 87
# NFC      : e0 a4 a8 e0 a4 ae e0 a4 b8 e0 a5 8d e0 a4 a4 e0 a5 87

# Statistics
# ----------------------------------------------------------------------
# Original Length : 6
# NFC Length      : 6
# Already NFC     : True
# Changed         : False






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



# Enter Unicode string (or 'exit' to quit): Hello! My name is Rahul. Café, résumé, naïve, coöperate, é 😀 🚀 ❤️ Hindi: नमस्ते Emoji: 😀😂👍 Currency: ₹ $ € Math: ∑ √ ∞



# output:


# ======================================================================
# Original : 'Hello! My name is Rahul. Café, résumé, naïve, coöperate, é 😀 🚀 ❤️ Hindi: नमस्ते Emoji: 😀😂👍 Currency: ₹ $ € Math: ∑ √ ∞'
# NFC      : 'Hello! My name is Rahul. Café, résumé, naïve, coöperate, é 😀 🚀 ❤️ Hindi: नमस्ते Emoji: 😀😂👍 Currency: ₹ $ € Math: ∑ √ ∞'
# ======================================================================

# Characters & Code Points
# ----------------------------------------------------------------------
# [0] 'H'  U+0048  CCC=  0  LATIN CAPITAL LETTER H
# [1] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [2] 'l'  U+006C  CCC=  0  LATIN SMALL LETTER L
# [3] 'l'  U+006C  CCC=  0  LATIN SMALL LETTER L
# [4] 'o'  U+006F  CCC=  0  LATIN SMALL LETTER O
# [5] '!'  U+0021  CCC=  0  EXCLAMATION MARK
# [6] ' '  U+0020  CCC=  0  SPACE
# [7] 'M'  U+004D  CCC=  0  LATIN CAPITAL LETTER M
# [8] 'y'  U+0079  CCC=  0  LATIN SMALL LETTER Y
# [9] ' '  U+0020  CCC=  0  SPACE
# [10] 'n'  U+006E  CCC=  0  LATIN SMALL LETTER N
# [11] 'a'  U+0061  CCC=  0  LATIN SMALL LETTER A
# [12] 'm'  U+006D  CCC=  0  LATIN SMALL LETTER M
# [13] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [14] ' '  U+0020  CCC=  0  SPACE
# [15] 'i'  U+0069  CCC=  0  LATIN SMALL LETTER I
# [16] 's'  U+0073  CCC=  0  LATIN SMALL LETTER S
# [17] ' '  U+0020  CCC=  0  SPACE
# [18] 'R'  U+0052  CCC=  0  LATIN CAPITAL LETTER R
# [19] 'a'  U+0061  CCC=  0  LATIN SMALL LETTER A
# [20] 'h'  U+0068  CCC=  0  LATIN SMALL LETTER H
# [21] 'u'  U+0075  CCC=  0  LATIN SMALL LETTER U
# [22] 'l'  U+006C  CCC=  0  LATIN SMALL LETTER L
# [23] '.'  U+002E  CCC=  0  FULL STOP
# [24] ' '  U+0020  CCC=  0  SPACE
# [25] 'C'  U+0043  CCC=  0  LATIN CAPITAL LETTER C
# [26] 'a'  U+0061  CCC=  0  LATIN SMALL LETTER A
# [27] 'f'  U+0066  CCC=  0  LATIN SMALL LETTER F
# [28] 'é'  U+00E9  CCC=  0  LATIN SMALL LETTER E WITH ACUTE
# [29] ','  U+002C  CCC=  0  COMMA
# [30] ' '  U+0020  CCC=  0  SPACE
# [31] 'r'  U+0072  CCC=  0  LATIN SMALL LETTER R
# [32] 'é'  U+00E9  CCC=  0  LATIN SMALL LETTER E WITH ACUTE
# [33] 's'  U+0073  CCC=  0  LATIN SMALL LETTER S
# [34] 'u'  U+0075  CCC=  0  LATIN SMALL LETTER U
# [35] 'm'  U+006D  CCC=  0  LATIN SMALL LETTER M
# [36] 'é'  U+00E9  CCC=  0  LATIN SMALL LETTER E WITH ACUTE
# [37] ','  U+002C  CCC=  0  COMMA
# [38] ' '  U+0020  CCC=  0  SPACE
# [39] 'n'  U+006E  CCC=  0  LATIN SMALL LETTER N
# [40] 'a'  U+0061  CCC=  0  LATIN SMALL LETTER A
# [41] 'ï'  U+00EF  CCC=  0  LATIN SMALL LETTER I WITH DIAERESIS
# [42] 'v'  U+0076  CCC=  0  LATIN SMALL LETTER V
# [43] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [44] ','  U+002C  CCC=  0  COMMA
# [45] ' '  U+0020  CCC=  0  SPACE
# [46] 'c'  U+0063  CCC=  0  LATIN SMALL LETTER C
# [47] 'o'  U+006F  CCC=  0  LATIN SMALL LETTER O
# [48] 'ö'  U+00F6  CCC=  0  LATIN SMALL LETTER O WITH DIAERESIS
# [49] 'p'  U+0070  CCC=  0  LATIN SMALL LETTER P
# [50] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [51] 'r'  U+0072  CCC=  0  LATIN SMALL LETTER R
# [52] 'a'  U+0061  CCC=  0  LATIN SMALL LETTER A
# [53] 't'  U+0074  CCC=  0  LATIN SMALL LETTER T
# [54] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [55] ','  U+002C  CCC=  0  COMMA
# [56] ' '  U+0020  CCC=  0  SPACE
# [57] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [58] '́'  U+0301  CCC=230  COMBINING ACUTE ACCENT
# [59] ' '  U+0020  CCC=  0  SPACE
# [60] '😀'  U+1F600  CCC=  0  GRINNING FACE
# [61] ' '  U+0020  CCC=  0  SPACE
# [62] '🚀'  U+1F680  CCC=  0  ROCKET
# [63] ' '  U+0020  CCC=  0  SPACE
# [64] '❤'  U+2764  CCC=  0  HEAVY BLACK HEART
# [65] '️'  U+FE0F  CCC=  0  VARIATION SELECTOR-16
# [66] ' '  U+0020  CCC=  0  SPACE
# [67] 'H'  U+0048  CCC=  0  LATIN CAPITAL LETTER H
# [68] 'i'  U+0069  CCC=  0  LATIN SMALL LETTER I
# [69] 'n'  U+006E  CCC=  0  LATIN SMALL LETTER N
# [70] 'd'  U+0064  CCC=  0  LATIN SMALL LETTER D
# [71] 'i'  U+0069  CCC=  0  LATIN SMALL LETTER I
# [72] ':'  U+003A  CCC=  0  COLON
# [73] ' '  U+0020  CCC=  0  SPACE
# [74] 'न'  U+0928  CCC=  0  DEVANAGARI LETTER NA
# [75] 'म'  U+092E  CCC=  0  DEVANAGARI LETTER MA
# [76] 'स'  U+0938  CCC=  0  DEVANAGARI LETTER SA
# [77] '्'  U+094D  CCC=  9  DEVANAGARI SIGN VIRAMA
# [78] 'त'  U+0924  CCC=  0  DEVANAGARI LETTER TA
# [79] 'े'  U+0947  CCC=  0  DEVANAGARI VOWEL SIGN E
# [80] ' '  U+0020  CCC=  0  SPACE
# [81] 'E'  U+0045  CCC=  0  LATIN CAPITAL LETTER E
# [82] 'm'  U+006D  CCC=  0  LATIN SMALL LETTER M
# [83] 'o'  U+006F  CCC=  0  LATIN SMALL LETTER O
# [84] 'j'  U+006A  CCC=  0  LATIN SMALL LETTER J
# [85] 'i'  U+0069  CCC=  0  LATIN SMALL LETTER I
# [86] ':'  U+003A  CCC=  0  COLON
# [87] ' '  U+0020  CCC=  0  SPACE
# [88] '😀'  U+1F600  CCC=  0  GRINNING FACE
# [89] '😂'  U+1F602  CCC=  0  FACE WITH TEARS OF JOY
# [90] '👍'  U+1F44D  CCC=  0  THUMBS UP SIGN
# [91] ' '  U+0020  CCC=  0  SPACE
# [92] 'C'  U+0043  CCC=  0  LATIN CAPITAL LETTER C
# [93] 'u'  U+0075  CCC=  0  LATIN SMALL LETTER U
# [94] 'r'  U+0072  CCC=  0  LATIN SMALL LETTER R
# [95] 'r'  U+0072  CCC=  0  LATIN SMALL LETTER R
# [96] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [97] 'n'  U+006E  CCC=  0  LATIN SMALL LETTER N
# [98] 'c'  U+0063  CCC=  0  LATIN SMALL LETTER C
# [99] 'y'  U+0079  CCC=  0  LATIN SMALL LETTER Y
# [100] ':'  U+003A  CCC=  0  COLON
# [101] ' '  U+0020  CCC=  0  SPACE
# [102] '₹'  U+20B9  CCC=  0  INDIAN RUPEE SIGN
# [103] ' '  U+0020  CCC=  0  SPACE
# [104] '$'  U+0024  CCC=  0  DOLLAR SIGN
# [105] ' '  U+0020  CCC=  0  SPACE
# [106] '€'  U+20AC  CCC=  0  EURO SIGN
# [107] ' '  U+0020  CCC=  0  SPACE
# [108] 'M'  U+004D  CCC=  0  LATIN CAPITAL LETTER M
# [109] 'a'  U+0061  CCC=  0  LATIN SMALL LETTER A
# [110] 't'  U+0074  CCC=  0  LATIN SMALL LETTER T
# [111] 'h'  U+0068  CCC=  0  LATIN SMALL LETTER H
# [112] ':'  U+003A  CCC=  0  COLON
# [113] ' '  U+0020  CCC=  0  SPACE
# [114] '∑'  U+2211  CCC=  0  N-ARY SUMMATION
# [115] ' '  U+0020  CCC=  0  SPACE
# [116] '√'  U+221A  CCC=  0  SQUARE ROOT
# [117] ' '  U+0020  CCC=  0  SPACE
# [118] '∞'  U+221E  CCC=  0  INFINITY

# NFC Characters & Code Points
# ----------------------------------------------------------------------
# [0] 'H'  U+0048  CCC=  0  LATIN CAPITAL LETTER H
# [1] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [2] 'l'  U+006C  CCC=  0  LATIN SMALL LETTER L
# [3] 'l'  U+006C  CCC=  0  LATIN SMALL LETTER L
# [4] 'o'  U+006F  CCC=  0  LATIN SMALL LETTER O
# [5] '!'  U+0021  CCC=  0  EXCLAMATION MARK
# [6] ' '  U+0020  CCC=  0  SPACE
# [7] 'M'  U+004D  CCC=  0  LATIN CAPITAL LETTER M
# [8] 'y'  U+0079  CCC=  0  LATIN SMALL LETTER Y
# [9] ' '  U+0020  CCC=  0  SPACE
# [10] 'n'  U+006E  CCC=  0  LATIN SMALL LETTER N
# [11] 'a'  U+0061  CCC=  0  LATIN SMALL LETTER A
# [12] 'm'  U+006D  CCC=  0  LATIN SMALL LETTER M
# [13] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [14] ' '  U+0020  CCC=  0  SPACE
# [15] 'i'  U+0069  CCC=  0  LATIN SMALL LETTER I
# [16] 's'  U+0073  CCC=  0  LATIN SMALL LETTER S
# [17] ' '  U+0020  CCC=  0  SPACE
# [18] 'R'  U+0052  CCC=  0  LATIN CAPITAL LETTER R
# [19] 'a'  U+0061  CCC=  0  LATIN SMALL LETTER A
# [20] 'h'  U+0068  CCC=  0  LATIN SMALL LETTER H
# [21] 'u'  U+0075  CCC=  0  LATIN SMALL LETTER U
# [22] 'l'  U+006C  CCC=  0  LATIN SMALL LETTER L
# [23] '.'  U+002E  CCC=  0  FULL STOP
# [24] ' '  U+0020  CCC=  0  SPACE
# [25] 'C'  U+0043  CCC=  0  LATIN CAPITAL LETTER C
# [26] 'a'  U+0061  CCC=  0  LATIN SMALL LETTER A
# [27] 'f'  U+0066  CCC=  0  LATIN SMALL LETTER F
# [28] 'é'  U+00E9  CCC=  0  LATIN SMALL LETTER E WITH ACUTE
# [29] ','  U+002C  CCC=  0  COMMA
# [30] ' '  U+0020  CCC=  0  SPACE
# [31] 'r'  U+0072  CCC=  0  LATIN SMALL LETTER R
# [32] 'é'  U+00E9  CCC=  0  LATIN SMALL LETTER E WITH ACUTE
# [33] 's'  U+0073  CCC=  0  LATIN SMALL LETTER S
# [34] 'u'  U+0075  CCC=  0  LATIN SMALL LETTER U
# [35] 'm'  U+006D  CCC=  0  LATIN SMALL LETTER M
# [36] 'é'  U+00E9  CCC=  0  LATIN SMALL LETTER E WITH ACUTE
# [37] ','  U+002C  CCC=  0  COMMA
# [38] ' '  U+0020  CCC=  0  SPACE
# [39] 'n'  U+006E  CCC=  0  LATIN SMALL LETTER N
# [40] 'a'  U+0061  CCC=  0  LATIN SMALL LETTER A
# [41] 'ï'  U+00EF  CCC=  0  LATIN SMALL LETTER I WITH DIAERESIS
# [42] 'v'  U+0076  CCC=  0  LATIN SMALL LETTER V
# [43] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [44] ','  U+002C  CCC=  0  COMMA
# [45] ' '  U+0020  CCC=  0  SPACE
# [46] 'c'  U+0063  CCC=  0  LATIN SMALL LETTER C
# [47] 'o'  U+006F  CCC=  0  LATIN SMALL LETTER O
# [48] 'ö'  U+00F6  CCC=  0  LATIN SMALL LETTER O WITH DIAERESIS
# [49] 'p'  U+0070  CCC=  0  LATIN SMALL LETTER P
# [50] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [51] 'r'  U+0072  CCC=  0  LATIN SMALL LETTER R
# [52] 'a'  U+0061  CCC=  0  LATIN SMALL LETTER A
# [53] 't'  U+0074  CCC=  0  LATIN SMALL LETTER T
# [54] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [55] ','  U+002C  CCC=  0  COMMA
# [56] ' '  U+0020  CCC=  0  SPACE
# [57] 'é'  U+00E9  CCC=  0  LATIN SMALL LETTER E WITH ACUTE
# [58] ' '  U+0020  CCC=  0  SPACE
# [59] '😀'  U+1F600  CCC=  0  GRINNING FACE
# [60] ' '  U+0020  CCC=  0  SPACE
# [61] '🚀'  U+1F680  CCC=  0  ROCKET
# [62] ' '  U+0020  CCC=  0  SPACE
# [63] '❤'  U+2764  CCC=  0  HEAVY BLACK HEART
# [64] '️'  U+FE0F  CCC=  0  VARIATION SELECTOR-16
# [65] ' '  U+0020  CCC=  0  SPACE
# [66] 'H'  U+0048  CCC=  0  LATIN CAPITAL LETTER H
# [67] 'i'  U+0069  CCC=  0  LATIN SMALL LETTER I
# [68] 'n'  U+006E  CCC=  0  LATIN SMALL LETTER N
# [69] 'd'  U+0064  CCC=  0  LATIN SMALL LETTER D
# [70] 'i'  U+0069  CCC=  0  LATIN SMALL LETTER I
# [71] ':'  U+003A  CCC=  0  COLON
# [72] ' '  U+0020  CCC=  0  SPACE
# [73] 'न'  U+0928  CCC=  0  DEVANAGARI LETTER NA
# [74] 'म'  U+092E  CCC=  0  DEVANAGARI LETTER MA
# [75] 'स'  U+0938  CCC=  0  DEVANAGARI LETTER SA
# [76] '्'  U+094D  CCC=  9  DEVANAGARI SIGN VIRAMA
# [77] 'त'  U+0924  CCC=  0  DEVANAGARI LETTER TA
# [78] 'े'  U+0947  CCC=  0  DEVANAGARI VOWEL SIGN E
# [79] ' '  U+0020  CCC=  0  SPACE
# [80] 'E'  U+0045  CCC=  0  LATIN CAPITAL LETTER E
# [81] 'm'  U+006D  CCC=  0  LATIN SMALL LETTER M
# [82] 'o'  U+006F  CCC=  0  LATIN SMALL LETTER O
# [83] 'j'  U+006A  CCC=  0  LATIN SMALL LETTER J
# [84] 'i'  U+0069  CCC=  0  LATIN SMALL LETTER I
# [85] ':'  U+003A  CCC=  0  COLON
# [86] ' '  U+0020  CCC=  0  SPACE
# [87] '😀'  U+1F600  CCC=  0  GRINNING FACE
# [88] '😂'  U+1F602  CCC=  0  FACE WITH TEARS OF JOY
# [89] '👍'  U+1F44D  CCC=  0  THUMBS UP SIGN
# [90] ' '  U+0020  CCC=  0  SPACE
# [91] 'C'  U+0043  CCC=  0  LATIN CAPITAL LETTER C
# [92] 'u'  U+0075  CCC=  0  LATIN SMALL LETTER U
# [93] 'r'  U+0072  CCC=  0  LATIN SMALL LETTER R
# [94] 'r'  U+0072  CCC=  0  LATIN SMALL LETTER R
# [95] 'e'  U+0065  CCC=  0  LATIN SMALL LETTER E
# [96] 'n'  U+006E  CCC=  0  LATIN SMALL LETTER N
# [97] 'c'  U+0063  CCC=  0  LATIN SMALL LETTER C
# [98] 'y'  U+0079  CCC=  0  LATIN SMALL LETTER Y
# [99] ':'  U+003A  CCC=  0  COLON
# [100] ' '  U+0020  CCC=  0  SPACE
# [101] '₹'  U+20B9  CCC=  0  INDIAN RUPEE SIGN
# [102] ' '  U+0020  CCC=  0  SPACE
# [103] '$'  U+0024  CCC=  0  DOLLAR SIGN
# [104] ' '  U+0020  CCC=  0  SPACE
# [105] '€'  U+20AC  CCC=  0  EURO SIGN
# [106] ' '  U+0020  CCC=  0  SPACE
# [107] 'M'  U+004D  CCC=  0  LATIN CAPITAL LETTER M
# [108] 'a'  U+0061  CCC=  0  LATIN SMALL LETTER A
# [109] 't'  U+0074  CCC=  0  LATIN SMALL LETTER T
# [110] 'h'  U+0068  CCC=  0  LATIN SMALL LETTER H
# [111] ':'  U+003A  CCC=  0  COLON
# [112] ' '  U+0020  CCC=  0  SPACE
# [113] '∑'  U+2211  CCC=  0  N-ARY SUMMATION
# [114] ' '  U+0020  CCC=  0  SPACE
# [115] '√'  U+221A  CCC=  0  SQUARE ROOT
# [116] ' '  U+0020  CCC=  0  SPACE
# [117] '∞'  U+221E  CCC=  0  INFINITY

# UTF-8 Bytes
# ----------------------------------------------------------------------
# Original : 48 65 6c 6c 6f 21 20 4d 79 20 6e 61 6d 65 20 69 73 20 52 61 68 75 6c 2e 20 43 61 66 c3 a9 2c 20 72 c3 a9 73 75 6d c3 a9 2c 20 6e 61 c3 af 76 65 2c 20 63 6f c3 b6 70 65 72 61 74 65 2c 20 65 cc 81 20 f0 9f 98 80 20 f0 9f 9a 80 20 e2 9d a4 ef b8 8f 20 48 69 6e 64 69 3a 20 e0 a4 a8 e0 a4 ae e0 a4 b8 e0 a5 8d e0 a4 a4 e0 a5 87 20 45 6d 6f 6a 69 3a 20 f0 9f 98 80 f0 9f 98 82 f0 9f 91 8d 20 43 75 72 72 65 6e 63 79 3a 20 e2 82 b9 20 24 20 e2 82 ac 20 4d 61 74 68 3a 20 e2 88 91 20 e2 88 9a 20 e2 88 9e
# NFC      : 48 65 6c 6c 6f 21 20 4d 79 20 6e 61 6d 65 20 69 73 20 52 61 68 75 6c 2e 20 43 61 66 c3 a9 2c 20 72 c3 a9 73 75 6d c3 a9 2c 20 6e 61 c3 af 76 65 2c 20 63 6f c3 b6 70 65 72 61 74 65 2c 20 c3 a9 20 f0 9f 98 80 20 f0 9f 9a 80 20 e2 9d a4 ef b8 8f 20 48 69 6e 64 69 3a 20 e0 a4 a8 e0 a4 ae e0 a4 b8 e0 a5 8d e0 a4 a4 e0 a5 87 20 45 6d 6f 6a 69 3a 20 f0 9f 98 80 f0 9f 98 82 f0 9f 91 8d 20 43 75 72 72 65 6e 63 79 3a 20 e2 82 b9 20 24 20 e2 82 ac 20 4d 61 74 68 3a 20 e2 88 91 20 e2 88 9a 20 e2 88 9e

# Statistics
# ----------------------------------------------------------------------
# Original Length : 119
# NFC Length      : 118
# Already NFC     : False
# Changed         : True