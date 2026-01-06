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

counts = {}
total = 0

for folder, name in categories.items():
    path = f"./{folder}"
    if os.path.isdir(path):
        c = len([f for f in os.listdir(path) if f.endswith(".md")])
    else:
        c = 0
    counts[name] = c
    total += c

stats_block = f"Total Challenges Completed: {total}\n\n"
for name, count in counts.items():
    stats_block += f"- {name}: {count}\n"

with open(README, "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r"<!-- STATS_START -->(.|\n)*?<!-- STATS_END -->",
    f"<!-- STATS_START -->\n{stats_block}\n<!-- STATS_END -->",
    content,
)

with open(README, "w", encoding="utf-8") as f:
    f.write(new_content)
