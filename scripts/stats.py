import os
import re

README = "README.md"

categories = {
    "general-skills": "General Skills",
    "forensics": "Forensics",
    "reverse-engineering": "Reverse Engineering",
    "web-exploitation": "Web Exploitation",
    "cryptography": "Cryptography",
    "binary-exploitation": "Binary Exploitation",
}

category_counts = {}
difficulty_counts = {
    "Easy": 0,
    "Medium": 0,
    "Hard": 0,
}

total = 0

difficulty_regex = re.compile(
    r"\*\*Difficulty:\*\*\s*(Easy|Medium|Hard)", re.IGNORECASE
)

for folder, name in categories.items():
    path = f"./{folder}"
    count = 0

    if not os.path.isdir(path):
        category_counts[name] = 0
        continue

    for file in os.listdir(path):
        if not file.endswith(".md"):
            continue

        file_path = os.path.join(path, file)
        count += 1
        total += 1

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        match = difficulty_regex.search(content)
        if match:
            diff = match.group(1).capitalize()
            if diff in difficulty_counts:
                difficulty_counts[diff] += 1

    category_counts[name] = count

# Build stats block
stats_block = ""
stats_block += f"Total Challenges Completed: {total}  \n"
stats_block += f"Total Challenges Completed (Easy): {difficulty_counts['Easy']}  \n"
stats_block += f"Total Challenges Completed (Medium): {difficulty_counts['Medium']}  \n"
stats_block += f"Total Challenges Completed (Hard): {difficulty_counts['Hard']}  \n\n"

for name, count in category_counts.items():
    stats_block += f"- {name}: {count}\n"

# Update README
with open(README, "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r"<!-- STATS_START -->(.|\n)*?<!-- STATS_END -->",
    f"<!-- STATS_START -->\n{stats_block}\n<!-- STATS_END -->",
    content,
)

with open(README, "w", encoding="utf-8") as f:
    f.write(new_content)
