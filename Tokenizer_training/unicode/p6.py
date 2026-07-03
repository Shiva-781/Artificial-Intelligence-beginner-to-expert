unicode_str = input("Enter Unicode (e.g. U+1F600): ")

code = int(unicode_str[2:], 16)   # U+ हटाकर hex को int में बदलें
print(chr(code))

# Input:

# U+1F600

# Output:

# 😀