import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FOLDER = os.path.join(BASE_DIR, "raw_documents")

os.makedirs(INPUT_FOLDER, exist_ok=True)

files = {
    "multiple_spaces.txt":
"""Hello      World

Python         is      awesome.

Tokenizer          Training
""",

    "multiple_tabs.txt":
"""Hello\t\t\tWorld

Python\t\tProgramming

OpenAI\t\t\tChatGPT
""",

    "spaces_and_tabs.txt":
"""Hello      \t\t World

Python   \t\t is    awesome

Tokenizer    \t Training
""",

    "multiple_blank_lines.txt":
"""Hello World



Python




OpenAI







Tokenizer
""",

    "leading_trailing_spaces.txt":
"""     Hello World

      Python Programming

OpenAI     

Tokenizer Training      
""",

    "all_problems.txt":
"""        Hello          World



Python\t\t\tProgramming



OpenAI       ChatGPT




Tokenizer\t\tTraining






Artificial       Intelligence
""",

    "only_spaces.txt":
"""         

     

        

""",

    "only_tabs.txt":
"""\t\t\t\t

\t\t\t

\t
""",

    "mixed_whitespace.txt":
"""   Hello\t\tWorld


Python     Programming



\t\tOpenAI


ChatGPT
""",

    "normal.txt":
"""Hello World
Python Programming
OpenAI ChatGPT
Tokenizer Training
"""
}

for filename, content in files.items():
    with open(os.path.join(INPUT_FOLDER, filename), "w", encoding="utf-8", newline="") as f:
        f.write(content)

print("All normalization test files created successfully.")

#  ye sirf  file while banane ke liiye jinhe normalize karna hai