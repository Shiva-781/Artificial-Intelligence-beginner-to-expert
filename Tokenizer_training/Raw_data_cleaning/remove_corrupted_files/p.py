with open(r"E:\Artificial_Inteligence\Tokenizer_training\Raw_data_cleaning\remove_corrupted_files\raw_documents\file2.txt", "wb") as f:
    f.write(b"\xff\xfe\xfa\x80")


#ye file run karne ke bad file2.txt me 胺  ye hoga aur uske bad p1 ya p2 run karne per file2.txt corrupted file hogi 
#agr ye file nhi run kar rhe direct 胺 ye file2.txt me likh kar p1 ya p2 ko run karyenge to bo valid file hogi



# kyunki

# Sirf ajeeb text likhne se file **corrupted nahi banegi**. Agar editor se save karoge to woh valid UTF-8 hi ban jayegi.  



# Case 1: Editor me text likhna (ÿþ)

# Agar tum VS Code ya Notepad me likhte ho:

# ÿþ

# aur file ko UTF-8 me save karte ho, to editor ye characters ko valid UTF-8 bytes me convert kar deta hai.

# Example:

# Character: ÿ
# UTF-8 bytes: C3 BF

# Character: þ
# UTF-8 bytes: C3 BE

# To file ke andar actual bytes hoti hain:

# C3 BF C3 BE

# Ye valid UTF-8 hai. Isliye:

# with open("file2.txt", "r", encoding="utf-8") as f:
#     f.read()

# bina error ke chal jata hai.

# Case 2: Python se binary mode (wb)

# Jab tum likhte ho:

# with open("file2.txt", "wb") as f:
#     f.write(b"\xff\xfe\xfa\x80")

# to Python encoding nahi karta.

# Ye bytes exactly file me likh deta hai:

# FF FE FA 80

# Ab jab tum UTF-8 me read karte ho:

# with open("file2.txt", "r", encoding="utf-8") as f:
#     f.read()

# Python dekhta hai:

# FF

# Lekin UTF-8 me FF kabhi valid starting byte nahi hota.

# Isliye error aata hai:

# UnicodeDecodeError

# Aur tumhari file "corrupted" maan li jati hai.

# w aur wb ka difference
# Text mode (w)
# with open("file.txt", "w", encoding="utf-8") as f:
#     f.write("ÿþ")

# Python characters ko UTF-8 me encode karega.

# File me bytes:

# C3 BF C3 BE

# ✅ Valid UTF-8

# Binary mode (wb)
# with open("file.txt", "wb") as f:
#     f.write(b"\xff\xfe")

# Python bytes ko jaise ke taise likh dega.

# File me bytes:

# FF FE

# ❌ UTF-8 ke liye invalid