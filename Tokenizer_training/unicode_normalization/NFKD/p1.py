import unicodedata

while True:
    text = input("\nEnter Unicode string (or 'exit' to quit): ")

    if text.lower() == "exit":
        break

    # NFKD Normalization
    nfkd = unicodedata.normalize("NFKD", text)

    print("\n" + "=" * 70)
    print("Original :", repr(text))
    print("NFKD     :", repr(nfkd))
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

    # NFKD characters
    print("\nNFKD Characters & Code Points")
    print("-" * 70)

    for i, c in enumerate(nfkd):
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
    print("NFKD     :", nfkd.encode("utf-8").hex(" "))

    print("\nStatistics")
    print("-" * 70)
    print("Original Length :", len(text))
    print("NFKD Length     :", len(nfkd))
    print("Already NFKD    :", unicodedata.is_normalized("NFKD", text))
    print("Changed         :", text != nfkd)