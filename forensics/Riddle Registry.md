# picoCTF Writeup: Riddle Registry

**Challenge Name:** Riddle Registry
**Category:** Forensics
**Difficulty:** Easy
**Author:** Prince Niyonshuti N.

---

## 📌 Challenge Description

You are given a seemingly ordinary PDF document filled with censored and meaningless content. At first glance, there is nothing useful inside the visible text. However, the real objective is to look beyond what is rendered on the screen.

The flag is hidden inside the **metadata** of the PDF file.

---

## 🎯 Objective

Analyze the PDF file and extract hidden information stored in its metadata in order to recover the flag.

---

## 🔍 Initial Analysis

After downloading and opening the file, the document appears unremarkable. The visible content contains no flag, no suspicious strings, and no hidden text layers.

This strongly suggests a **forensics-style challenge**, where the solution lies in examining the file structure rather than its visible content.

**Skills required:**

* Understanding of PDF structure
* Metadata analysis
* Familiarity with forensic tools
* Ability to recognize encoded data formats

---

## 🛠️ Solution Steps

### Step 1: Download the Provided File

The PDF file is downloaded using `wget`:

```bash
wget https://challenge-files.picoctf.net/c_amiable_citadel/5618b8a659b50b6ac50c1cb90bb61d75775299df46921871cd8cdc7888c9d509/confidential.pdf
```

This produces a file named:

```
confidential.pdf
```

---

### Step 2: Inspect the PDF Content

Opening the PDF normally reveals only censored or meaningless text. There is no visible flag or hidden message in the document body.

At this point, content-based analysis is exhausted, so metadata analysis becomes the next logical step.

---

### Step 3: Extract PDF Metadata

To inspect the internal structure and metadata of the PDF, `pdf-parser` is used:

```bash
pdf-parser confidential.pdf
```

Relevant output:

```
obj 2 0
  <<
    /Producer (PyPDF2)
    /Author '(cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jOGY5MWQ2OH0\\075)'
  >>
```

The `/Author` field contains a suspicious string that does not resemble a normal author name. This is a strong indicator of encoded data.

---

### Step 4: Identify the Encoding

The string:

```
cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jOGY5MWQ2OH0=
```

Matches the character pattern of **Base64 encoding**. This can be confirmed using a cipher identification tool such as dCode.

---

### Step 5: Decode the Metadata Value

The encoded string is decoded using `base64`:

```bash
echo "cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jOGY5MWQ2OH0=" | base64 -d
```

Output:

```
picoCTF{puzzl3d_m3tadata_f0und!_c8f91d68}
```

---

## 🚩 Flag

```
picoCTF{puzzl3d_m3tadata_f0und!_c8f91d68}
```

---

## 💡 Key Takeaways

1. **Metadata Is Part of the Evidence**
   Files often contain hidden or overlooked metadata that can store sensitive information.

2. **Visible Content Is Not the Whole Story**
   In forensic challenges, what you see is often irrelevant compared to the file’s internal structure.

3. **PDF Files Are Structured Objects**
   Fields such as `/Author`, `/Producer`, and `/Creator` are common places to hide data.

4. **Recognizing Encodings Is Essential**
   Quickly identifying Base64 saves time and avoids unnecessary brute-force approaches.

---

## 🔧 Tools Used

| Tool       | Purpose                            |
| ---------- | ---------------------------------- |
| wget       | Download challenge file            |
| pdf-parser | Inspect PDF structure and metadata |
| base64     | Decode encoded metadata            |
| dCode      | Identify encoding format           |

---

**Challenge successfully solved using basic digital forensics techniques.**
