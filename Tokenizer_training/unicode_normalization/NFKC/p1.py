import unicodedata

while True:
    text = input("\nEnter Unicode string (or 'exit' to quit): ")

    if text.lower() == "exit":
        break

    # NFKC Normalization
    nfkc = unicodedata.normalize("NFKC", text)

    print("\n" + "=" * 70)
    print("Original :", repr(text))
    print("NFKC     :", repr(nfkc))
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

    # NFKC characters
    print("\nNFKC Characters & Code Points")
    print("-" * 70)

    for i, c in enumerate(nfkc):
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
    print("NFKC     :", nfkc.encode("utf-8").hex(" "))

    print("\nStatistics")
    print("-" * 70)
    print("Original Length :", len(text))
    print("NFKC Length     :", len(nfkc))
    print("Already NFKC    :", unicodedata.is_normalized("NFKC", text))
    print("Changed         :", text != nfkc)


#nfkc   and nfkd  ke notes pado   fir  enke test cases dekhna   