# 🚩 picoCTF Writeups

A collection of detailed writeups for picoCTF challenges, documenting solutions, methodologies, and learning outcomes for various cybersecurity challenges.

[![picoCTF](https://img.shields.io/badge/picoCTF-Challenges-blue)](https://picoctf.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Table of Contents

- [About](#about)
- [Challenge Categories](#challenge-categories)
- [Writeup Structure](#writeup-structure)
- [Challenges Solved](#challenges-solved)
- [Tools Used](#tools-used)
- [How to Use This Repository](#how-to-use-this-repository)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [Contact](#contact)

---

## 🎯 About

This repository contains comprehensive writeups for [picoCTF](https://picoctf.org/) challenges. Each writeup includes:

- **Detailed solution steps** with explanations
- **Command-line examples** and code snippets
- **Tool recommendations** and alternatives
- **Learning outcomes** and key takeaways
- **Screenshots and proof of completion**

The goal is to help others learn cybersecurity concepts while documenting my problem-solving approach and methodology.

---

## 📚 Challenge Categories

picoCTF challenges are organized into various categories:

| Category | Description | Challenges Solved |
|----------|-------------|-------------------|
| 🔍 **Forensics** | Digital forensics, steganography, metadata analysis | 1 |
| 🔄 **Reverse Engineering** | Binary analysis, code decompilation, algorithm understanding | 1 |
| 🌐 **Web Exploitation** | Web vulnerabilities, injection attacks, session management | 0 |
| 🔐 **Cryptography** | Encryption, encoding, cipher breaking | 0 |
| 💻 **Binary Exploitation** | Buffer overflows, shellcode, memory corruption | 0 |
| 🛠️ **General Skills** | Linux commands, scripting, basic tools | 1 |

---

## 📝 Writeup Structure

Each writeup follows a consistent format for easy navigation:

```markdown
# Challenge Name

**Category:** [Category]
**Difficulty:** [Easy/Medium/Hard]
**Points:** [Points]

## 📌 Challenge Description
## 🎯 Objective
## 🔍 Initial Analysis
## 🛠️ Solution Steps
## 🚩 Flag
## 💡 Key Takeaways
## 🔧 Tools Used
```

---

## 🏆 Challenges Solved

### General Skills

| Challenge | Difficulty | Points | Writeup |
|-----------|------------|--------|---------|
| Magikarp Ground Mission | Easy | 30 | [📄 Writeup](./general-skills/magikarp-ground-mission.md) |

### Forensics

| Challenge | Difficulty | Points | Writeup |
|-----------|------------|--------|---------|
| Information | Easy | 10 | [📄 Writeup](./forensics/information.md) |

### Reverse Engineering

| Challenge | Difficulty | Points | Writeup |
|-----------|------------|--------|---------|
| crackme-py | Medium | 30 | [📄 Writeup](./reverse-engineering/crackme-py.md) |

### Web Exploitation

| Challenge | Difficulty | Points | Writeup |
|-----------|------------|--------|---------|
| Coming soon... | - | - | - |

### Cryptography

| Challenge | Difficulty | Points | Writeup |
|-----------|------------|--------|---------|
| Coming soon... | - | - | - |

### Binary Exploitation

| Challenge | Difficulty | Points | Writeup |
|-----------|------------|--------|---------|
| Coming soon... | - | - | - |

---

## 🔧 Tools Used

This section lists common tools used across multiple challenges:

### Command-Line Tools
- `ssh` - Secure Shell for remote connections
- `ls`, `cd`, `cat` - Basic Linux navigation
- `wget`, `curl` - Download files from URLs
- `strings` - Extract readable strings from files
- `grep` - Search for patterns in text
- `base64` - Encode/decode Base64
- `exiftool` - Read and write metadata
- `steghide` - Steganography tool
- `binwalk` - Firmware analysis tool
- `file` - Determine file type

### Online Tools
- [CyberChef](https://gchq.github.io/CyberChef/) - Data transformation
- [dCode](https://www.dcode.fr/) - Cipher identification and decoding
- [Metadata2Go](https://www.metadata2go.com/) - Online metadata viewer
- [Base64 Decode](https://www.base64decode.org/) - Base64 decoder

### Programming Languages
- Python 3 - Scripting and automation
- Bash - Shell scripting

---

## 📖 How to Use This Repository

### For Learning

1. **Try the challenge yourself first** before reading the writeup
2. If stuck, read only the "Initial Analysis" section for hints
3. Use the writeup as a reference to understand different approaches
4. Check the "Key Takeaways" section to consolidate learning

### For Reference

1. Navigate to the appropriate category folder
2. Find the challenge writeup by name
3. Follow the step-by-step solution
4. Adapt the methodology to similar challenges

### Repository Structure

```
picoctf-writeups/
├── README.md
├── general-skills/
│   ├── magikarp-ground-mission.md
│   └── ...
├── forensics/
│   ├── information.md
│   └── ...
├── reverse-engineering/
│   ├── crackme-py.md
│   └── ...
├── web-exploitation/
│   └── ...
├── cryptography/
│   └── ...
├── binary-exploitation/
│   └── ...
└── assets/
    └── images/
```

---

## ⚠️ Disclaimer

**Educational Purpose Only**

These writeups are created for **educational purposes** to help others learn cybersecurity concepts and problem-solving techniques. 

- ✅ Use these writeups to **learn and understand** CTF methodologies
- ✅ Try challenges on your own **before** reading solutions
- ✅ Use the techniques in **authorized environments** only
- ❌ Do **not** use these methods for unauthorized access or malicious purposes
- ❌ Do **not** submit these solutions as your own work in competitions

**Respect the CTF Spirit:** Capture The Flag competitions are designed for learning. Try to solve challenges independently before consulting writeups.

---

## 📊 Progress Tracker

```
Total Challenges Completed: 3
├── General Skills:        1/XX ░░░░░░░░░░ 
├── Forensics:            1/XX ░░░░░░░░░░
├── Reverse Engineering:  1/XX ░░░░░░░░░░
├── Web Exploitation:     0/XX ░░░░░░░░░░
├── Cryptography:         0/XX ░░░░░░░░░░
└── Binary Exploitation:  0/XX ░░░░░░░░░░
```

---

## 🎓 Learning Resources

### Recommended Resources for CTF Beginners

- [picoCTF Practice](https://play.picoctf.org/practice) - Official practice platform
- [CTF101](https://ctf101.org/) - Introduction to CTFs
- [OverTheWire](https://overthewire.org/wargames/) - Security wargames
- [HackTheBox](https://www.hackthebox.com/) - Penetration testing labs
- [TryHackMe](https://tryhackme.com/) - Guided cybersecurity learning

### Useful Documentation

- [Bash Scripting Guide](https://www.gnu.org/software/bash/manual/)
- [Python Documentation](https://docs.python.org/3/)
- [Linux Command Reference](https://man7.org/linux/man-pages/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

---

## 📞 Contact

**Author:** [Muhamad Lutfi]  
**GitHub:** [@Lutfi-Muhamad](https://https://github.com/Lutfi-Muhamad)  
**Email:** muhamad.ltfi10@gmail.com

---

---

## 📈 Statistics

<!--![GitHub stars](https://img.shields.io/github/stars/Lutfi-Muhamad/picoctf-writeups?style=social)
![GitHub forks](https://img.shields.io/github/forks/Lutfi-Muhamad/picoctf-writeups?style=social) -->
 ![GitHub issues](https://img.shields.io/github/issues/Lutfi-Muhamad/picoctf-writeups)
![Last commit](https://img.shields.io/github/last-commit/Lutfi-Muhamad/picoctf-writeups) 

---

<div align="center">

**Happy Hacking! 🔐**

*Remember: The journey of learning is more important than the destination.*

[⬆ Back to Top](#-picoctf-writeups)

</div>
