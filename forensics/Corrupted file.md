# picoCTF Writeup: Corrupted File

**Challenge Name:** Corrupted File  
**Category:** Forensics  
**Difficulty:** Easy  
**Author:** Yahaya Meddy  

---

## 📌 Challenge Description

This file seems broken… or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?

You are given a file with no clear extension. The goal is to identify the file type, repair the corrupted bytes, and recover the flag.

---

## 🎯 Objective

Analyze the corrupted file at the byte level, repair its header, restore the original file format, and extract the flag from the recovered content.

---

## 🔍 Initial Analysis

The challenge provides a downloadable file named `file` without any extension. Attempting to open it directly does not reveal meaningful information.

This suggests that the file header may be corrupted or intentionally modified, requiring manual inspection.

Basic knowledge of file signatures (magic bytes) and hex-level analysis is required.

---

## 🛠️ Solution Steps

### Step 1: Download the File

Download the provided file using `wget`:

```bash
wget https://challenge-files.picoctf.net/c_amiable_citadel/bdd976098377529fe779dbd31b424f69e51327b5ba68fd247dfcc074f0684141/file
```

---

### Step 2: Attempt Basic Inspection

Viewing the file using `cat` produces unreadable output:

```bash
cat file
```

This confirms the file is binary and not meant to be interpreted as plain text.

---

### Step 3: Inspect the File Using a Hex Editor

Given the challenge hint about corrupted bytes, a hex editor is the appropriate tool:

```bash
hexeditor file
```

Inspecting the first few bytes reveals that the file header does not match any common file signature.

---

### Step 4: Identify the Correct File Signature

According to standard file signatures:

* JPEG files always begin with the bytes:

```
FF D8 FF E0
```

However, the file starts with:

```
5C 78 FF E0
```

This indicates that the first two bytes are corrupted.

---

### Step 5: Repair the File Header

Using the hex editor, replace the first four bytes:

**Before:**

```
5C 78 FF E0
```

**After:**

```
FF D8 FF E0
```

Save the corrected file and rename it with a JPEG extension:

```bash
mv file file.jpeg
```

---

### Step 6: Open the Repaired Image

Open the recovered JPEG file:

```bash
open file.jpeg
```

The image now opens successfully and visibly displays the flag.

---

## 🚩 Flag

```
picoCTF{r3st0r1ng_th3_by73s_249e4e3c}
```

---

## 💡 Key Takeaways

This challenge reinforces several core digital forensics concepts:

1. **File Signature Analysis**
   File types are identified by magic bytes, not file extensions.

2. **Hex-Level Repair**
   Even a small corruption in the header can make a file unreadable.

3. **Tool Selection Matters**
   Hex editors are essential when dealing with corrupted or malformed files.

4. **Think Before Brute Force**
   Understanding file formats saves time compared to random trial-and-error.

---

## 🔧 Tools Used

| Tool         | Purpose                          | Type |
| ------------ | -------------------------------- | ---- |
| `wget`       | Download the challenge file      | CLI  |
| `hexeditor`  | Inspect and modify file bytes    | CLI  |
| `cat`        | Verify binary nature of the file | CLI  |
| Image Viewer | View the recovered JPEG image    | GUI  |

---

**Challenge successfully completed.**