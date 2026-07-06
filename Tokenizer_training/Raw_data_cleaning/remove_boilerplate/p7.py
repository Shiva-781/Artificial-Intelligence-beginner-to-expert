# Method 7 — Frequency Based Boilerplate Removal

# Idea

# Agar koi line

# Privacy Policy

# 10000 documents me repeat ho rahi hai

# ↓

# Boilerplate.

# Code
from collections import Counter

documents = [

"Home\nPython",

"Home\nMachine Learning",

"Home\nArtificial Intelligence"

]

counter = Counter()

for doc in documents:

    for line in doc.splitlines():

        counter[line] += 1

print(counter)





# Output

# Counter({
# 'Home':3,
# 'Python':1,
# 'Machine Learning':1,
# 'Artificial Intelligence':1
# })




# Ab

# Home

# sab documents me aa raha hai

# ↓

# Remove.