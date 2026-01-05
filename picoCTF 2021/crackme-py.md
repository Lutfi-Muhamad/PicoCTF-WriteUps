# picoCTF Writeup: crackme-py

**Challenge Name:** crackme-py  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Author:** syreal

---

## 📌 Challenge Description

*crackme-py: Reverse Engineering Challenge*

**File provided:** `crackme_gen.py`

This challenge presents a Python script that appears to be a simple number comparison program, but contains hidden functionality that reveals the flag when properly analyzed and executed.

---

## 🎯 Objective

Analyze the provided Python code to discover and extract the hidden flag through reverse engineering techniques.

---

## 🔍 Initial Analysis

The challenge provides a downloadable Python script:

- **Filename:** `crackme_gen.py`
- **Download URL:** [crackme_gen.py](https://challenge-files.picoctf.net/c_wily_courier/1f719c049ec6e9a090f9c507eb75df0217faa62f246ffeaef252cdd270075986/crackme_gen.py)

**Required Skills:**
- Python code analysis
- Understanding of ROT47 cipher
- Basic reverse engineering
- Code flow analysis
- Function call manipulation

---

## 📄 Code Analysis

The provided script contains the following key components:

```python
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`>0c0Abc?FE0g`\_47fgaagg6ffN"

# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
           "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def decode_secret(secret):
    """ROT47 decode
    
    NOTE: encode and decode are the same operation in the ROT cipher family.
    """
    # Encryption key
    rotate_const = 47
    
    # Storage for decoded secret
    decoded = ""
    
    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]
    
    print(decoded)

def choose_greatest():
    """Echo the largest of the two numbers given by the user to the program
    
    Warning: this function was written quickly and needs proper error handling
    """
    user_value_1 = input("What's your first number? ")
    user_value_2 = input("What's your second number? ")
    greatest_value = user_value_1
    
    if user_value_1 > user_value_2:
        greatest_value = user_value_1
    elif user_value_1 < user_value_2:
        greatest_value = user_value_2
    
    print("The number with largest positive magnitude is " + str(greatest_value))

choose_greatest()
```

**Key Observations:**
1. There's an encrypted string stored in `bezos_cc_secret`
2. A `decode_secret()` function exists but is **never called**
3. The `choose_greatest()` function is a decoy that serves no purpose for finding the flag
4. The cipher used is **ROT47** (a rotation cipher)

---

## 🛠️ Solution Steps

### Step 1: Download the Python Script

Download the script file using your browser or command-line tools:

**Using wget:**
```bash
wget https://challenge-files.picoctf.net/c_wily_courier/1f719c049ec6e9a090f9c507eb75df0217faa62f246ffeaef252cdd270075986/crackme_gen.py
```

**Using curl:**
```bash
curl -O https://challenge-files.picoctf.net/c_wily_courier/1f719c049ec6e9a090f9c507eb75df0217faa62f246ffeaef252cdd270075986/crackme_gen.py
```

### Step 2: Initial Program Execution

Run the script normally to understand its apparent functionality:

```bash
python crackme_gen.py
```

**Output:**
```
What's your first number? 10
What's your second number? 11
The number with largest positive magnitude is 11
```

The program appears to be a simple number comparison tool—this is the **decoy functionality**.

### Step 3: Code Analysis and Discovery

Upon analyzing the code, we discover:

1. **Encrypted Secret:** `bezos_cc_secret = "A:4@r%uL`>0c0Abc?FE0g`\_47fgaagg6ffN"`
2. **Unused Function:** The `decode_secret()` function exists but is never called
3. **ROT47 Cipher:** The comment explicitly states this is ROT47 encoding
4. **Decoy Function:** `choose_greatest()` is just a distraction

The key insight: **We need to call the `decode_secret()` function with the encrypted string.**

### Step 4: Solution Method 1 - Call the Decode Function

Modify the script to call the `decode_secret()` function:

**Modified Code:**
```python
# Add this line at the end of the script
decode_secret(bezos_cc_secret)
```

**Full modified execution flow:**
```python
# ... (original code) ...

choose_greatest()
decode_secret(bezos_cc_secret)  # Add this line
```

**Run the modified script:**
```bash
python crackme_gen.py
```

**Output:**
```
What's your first number? 1
What's your second number? 2
The number with largest positive magnitude is 2
picoCTF{1m_4_p34nut_810cf782288e77}
```

### Step 5: Solution Method 2 - Clean Execution

Remove the decoy function and only execute the decode function:

**Cleaned Code:**
```python
# Encrypted secret
bezos_cc_secret = "A:4@r%uL`>0c0Abc?FE0g`\_47fgaagg6ffN"

# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
           "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def decode_secret(secret):
    """ROT47 decode"""
    rotate_const = 47
    decoded = ""
    
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]
    
    print(decoded)

# Call the decode function
decode_secret(bezos_cc_secret)
```

**Run the cleaned script:**
```bash
python crackme_gen.py
```

**Output:**
```
picoCTF{1m_4_p34nut_810cf782288e77}
```

### Step 6: Alternative Solution - Online ROT47 Decoder

You can also decode the encrypted string using online tools:

1. Visit [dCode ROT47 Decoder](https://www.dcode.fr/rot-47-cipher)
2. Paste the encrypted string: `A:4@r%uL`>0c0Abc?FE0g`\_47fgaagg6ffN`
3. Click "Decrypt"
4. The flag is revealed: `picoCTF{1m_4_p34nut_810cf782288e77}`

### Step 7: Alternative Solution - Python One-Liner

You can also solve this with a Python one-liner:

```python
python -c "
secret = 'A:4@r%uL\`>0c0Abc?FE0g\`\_47fgaagg6ffN'
alphabet = '!\"#\$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\\\]^_\`abcdefghijklmnopqrstuvwxyz{|}~'
print(''.join(alphabet[(alphabet.find(c) + 47) % len(alphabet)] for c in secret))
"
```

---

## 🚩 Flag

```
picoCTF{1m_4_p34nut_810cf782288e77}
```

---

## 💡 Key Takeaways

This challenge reinforces fundamental reverse engineering concepts:

1. **Code Flow Analysis:** Understanding which functions are called and which are not—identifying unused code that contains the actual solution
2. **Decoy Recognition:** Recognizing distraction code (the number comparison function) that diverts attention from the real objective
3. **Cipher Identification:** Understanding classic ciphers like ROT47 and how they work
4. **Function Manipulation:** Learning to modify code execution flow by calling uncalled functions or removing unnecessary code
5. **Comment Analysis:** Reading code comments carefully—they often contain hints about encryption methods or hidden functionality
6. **Multiple Solution Paths:** Understanding there are often multiple ways to solve a challenge (modify code, use online tools, create one-liners)

---

## 🔧 Tools & Techniques Used

| Tool/Technique | Purpose | Method |
|----------------|---------|--------|
| Python Interpreter | Execute and test the script | Command-line |
| Code Editor | Modify the Python script | Local |
| Text Analysis | Identify unused functions | Manual |
| ROT47 Cipher | Understand the encryption method | Cryptography |
| dCode.fr | Alternative decryption method | Online |
| Python One-Liner | Quick script execution | Command-line |

---

**Challenge Completed Successfully! 🎉**