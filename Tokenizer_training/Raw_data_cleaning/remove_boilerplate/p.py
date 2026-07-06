import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FOLDER = os.path.join(BASE_DIR, "raw_documents")

os.makedirs(INPUT_FOLDER, exist_ok=True)

files = {

    "article1.txt": """Home
About
Privacy Policy

Python is one of the most popular programming languages.

It is widely used in AI and Machine Learning.

Contact
""",

    "article2.txt": """Subscribe
Login

Artificial Intelligence is transforming industries.

Machine Learning is a subset of AI.

Terms of Service
""",

    "article3.txt": """Home
About
Contact
Privacy Policy
Terms of Service
Cookie Policy
Subscribe
Login

Tokenizer training requires a clean dataset.

Duplicate documents should be removed.

Privacy Policy
""",

    "article4.txt": """Python Programming

Data Science

Deep Learning

Machine Learning
""",

    "article5.txt": """Privacy Policy
Terms of Service
Cookie Policy
Home
About
Contact
Subscribe
Login
""",

    "article6.txt": """Home

Python

About

Machine Learning

Contact

Artificial Intelligence

Privacy Policy
""",

    "article7.txt": """Login
Subscribe
Welcome to our website.

Today's article is about NLP.

Cookie Policy
""",

    "article8.txt": """Privacy Policy

Privacy Policy

Privacy Policy

Python is awesome.

Privacy Policy
""",

}

for filename, content in files.items():

    with open(
        os.path.join(INPUT_FOLDER, filename),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(content)

print("Boilerplate test files created successfully.")