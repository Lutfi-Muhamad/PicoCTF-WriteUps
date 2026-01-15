# picoCTF Writeup: Hidden in Plainsight

**Challenge Name:** Hidden in Plainsight  
**Category:** Forensics  
**Difficulty:** Easy  
**Author:** Yahaya Meddy  

---

## 📌 Challenge Description

You are given a seemingly ordinary JPG image. However, something is hidden inside the file beyond what is visually visible. Your task is to analyze the image, uncover the hidden payload, and extract the flag.

---

## 🎯 Objective

Analyze the provided image file, identify any hidden data or metadata, and extract the embedded flag using appropriate forensic techniques and tools.

---

## 🔍 Initial Analysis

The challenge provides a download link to a file named `img.jpg`. At first glance, the image appears normal and does not reveal anything suspicious when viewed directly.

To proceed, the challenge requires basic knowledge of Linux command-line tools and digital forensics concepts.

Relevant tools include:

* `wget` – Download files from the internet
* `exiftool` – Inspect metadata inside files
* `base64` – Decode Base64-encoded strings
* `steghide` – Extract hidden data from images
* `cat` – Display file contents

---

## 🛠️ Solution Steps

### Step 1: Download the Image

First, download the image using `wget`:

```bash
wget https://challenge-files.picoctf.net/c_amiable_citadel/31f5b3c0759eba6f7632fcb2eca20424a40c6f066e52c07eabedafafb800d87e/img.jpg
```

---

### Step 2: Visual Inspection

Opening the image normally does not reveal any visible clue or anomaly. This indicates that the hidden data is not embedded visually and requires further forensic analysis.

![alt text](https://challenge-files.picoctf.net/c_amiable_citadel/31f5b3c0759eba6f7632fcb2eca20424a40c6f066e52c07eabedafafb800d87e/img.jpg)

---

### Step 3: Inspect Metadata Using ExifTool

Next, analyze the image metadata:

```bash
exiftool img.jpg
```

Output full:

```
ExifTool Version Number         : 13.36
File Name                       : img.jpg
Directory                       : .
File Size                       : 74 kB
File Modification Date/Time     : 2026:01:12 11:58:23+07:00
File Access Date/Time           : 2026:01:12 11:58:25+07:00
File Inode Change Date/Time     : 2026:01:12 11:58:23+07:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Comment                         : c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9
Image Width                     : 640
Image Height                    : 640
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 640x640
Megapixels                      : 0.410

```

The `Comment` field contains a suspicious string that does not resemble normal text. This strongly suggests an encoded payload.

---

### Step 4: Decode the Base64 Comment

The string appears to be Base64-encoded. Decode it using:

```bash
echo "c3RlZ2hpZGU6Y0VGNmVuZHZjbVE=" | base64 -d
```

Result:

```
steghide:cEF6endvcmQ
```

This output provides two important clues:

1. The keyword `steghide`, indicating the tool required for extraction
2. Another Base64-encoded string: `cEF6endvcmQ`

Decode the second string:

```bash
echo -n "cEF6endvcmQ" | base64 -d
```

Result:

```
pAzzword
```

This string is the password needed to extract the hidden data.

---

### Step 5: Extract Hidden Data with Steghide

Using `steghide` and the discovered password:

```bash
steghide extract -sf img.jpg -p pAzzword
```

Output:

```
wrote extracted data to "flag.txt".
```

This confirms that hidden data has been successfully extracted.

---

### Step 6: Read the Flag

Finally, display the contents of the extracted file:

```bash
cat flag.txt
```

Output:

```
picoCTF{h1dd3n_1n_1m4g3_92f08d7c}
```

---

## 🚩 Flag

```
picoCTF{h1dd3n_1n_1m4g3_92f08d7c}
```

---

## 💡 Key Takeaways

This challenge reinforces several fundamental digital forensics concepts:

1. **Metadata Analysis**
   Files often contain hidden information beyond their visible content.

2. **Encoding Recognition**
   Identifying common encodings such as Base64 is essential in forensic analysis.

3. **Steganography Techniques**
   Tools like `steghide` can embed and extract hidden payloads inside media files.

4. **Systematic Investigation**
   When one approach fails, pivot to another method instead of guessing blindly.

---

## 🔧 Tools Used

| Tool       | Purpose                             | Type |
| ---------- | ----------------------------------- | ---- |
| `wget`     | Download the challenge file         | CLI  |
| `exiftool` | Inspect metadata inside the image   | CLI  |
| `base64`   | Decode Base64-encoded strings       | CLI  |
| `steghide` | Extract steganographic data         | CLI  |
| `cat`      | Display extracted file contents     | CLI  |

---

**Challenge successfully completed.**
