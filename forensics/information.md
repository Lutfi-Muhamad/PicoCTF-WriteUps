# picoCTF Writeup: Information

**Challenge Name:** Information  
**Category:** Forensics  
**Difficulty:** Easy  
**Author:** susie

---

## 📌 Challenge Description

_Files can always be changed in a secret way. Can you find the flag?_

**File provided:** `cat.jpg`

This challenge introduces players to basic digital forensics and metadata analysis. Information can be hidden within file properties that aren't immediately visible when viewing the file normally.

---

## 🎯 Objective

Extract the hidden flag from the metadata of an image file named `cat.jpg`.

---

## 🔍 Initial Analysis

The challenge provides a downloadable image file:

- **Filename:** `cat.jpg`
- **Download URL:** [cat.jpg](https://challenge-files.picoctf.net/c_wily_courier/76e95e3e6ee69b4f82b3cea25051f5a9a5918b57809a1f90b29b06b776c73bc7/cat.jpg)
  ![alt text](https://challenge-files.picoctf.net/c_wily_courier/76e95e3e6ee69b4f82b3cea25051f5a9a5918b57809a1f90b29b06b776c73bc7/cat.jpg)

The challenge hint suggests that files can be "changed in a secret way," pointing toward metadata manipulation or steganography techniques.

**Required Skills:**

- Basic forensics analysis
- Metadata examination
- Base64 encoding/decoding
- Steganography awareness

---

## 🛠️ Solution Steps

### Step 1: Download the Image

Download the image file using your browser or command-line tools:

**Using wget:**

```bash
wget https://challenge-files.picoctf.net/c_wily_courier/76e95e3e6ee69b4f82b3cea25051f5a9a5918b57809a1f90b29b06b776c73bc7/cat.jpg
```

**Or using curl:**

```bash
curl -O https://challenge-files.picoctf.net/c_wily_courier/76e95e3e6ee69b4f82b3cea25051f5a9a5918b57809a1f90b29b06b776c73bc7/cat.jpg
```

### Step 2: Initial Analysis - Steganography Check

First approach: Check for hidden data using steganography tools.

**Attempt with steghide:**

```bash
steghide extract -sf cat.jpg
```

This approach yielded no results, indicating the flag isn't hidden using traditional steganography methods.

### Step 3: Metadata Examination

The second approach involves examining the image's metadata, which contains information about the file such as camera settings, creation date, author, and custom fields.

**Method 1: Online Tool**

Use [Metadata2Go](https://www.metadata2go.com):

1. Upload `cat.jpg` to the website
2. Review all metadata fields
3. Look for unusual or suspicious entries

**Method 2: Command-Line Tools (Alternative)**

```bash
# Using exiftool (if available)
exiftool cat.jpg

# Using strings, base64, and grep command
strings cat.jpg | base64 -d 2>/dev/null | grep -i "pico"
```

### Step 4: Discovering the Encoded Flag

In the metadata (Still encrypted version), a suspicious entry is found in the **License** field:

```
License: cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
```

This string appears to be encoded data rather than a typical license identifier.

### Step 5: Identifying the Encoding

To identify the encoding method, use cipher identification tools:

**Using dCode.fr:**

1. Visit [dCode Cipher Identifier](https://www.dcode.fr/cipher-identifier)
2. Paste the string: `cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9`
3. The tool identifies it as **Base64 encoding**

**Recognizing Base64:**

- Typically contains alphanumeric characters and `+`, `/`, `=`
- Often ends with one or two `=` padding characters
- Character set: `A-Z`, `a-z`, `0-9`, `+`, `/`

### Step 6: Decoding the Flag

Decode the Base64 string to reveal the flag:

**Using online decoder:**
Visit [Base64 Decode](https://www.base64decode.org/) and paste the string.

**Using command-line:**

```bash
echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d
```

**Result:**

```
picoCTF{the_m3tadata_1s_modified}
```

---

## 🚩 Flag

```
picoCTF{the_m3tadata_1s_modified}
```

---

## 💡 Key Takeaways

This challenge reinforces fundamental digital forensics concepts:

1. **Metadata Analysis:** Understanding that files contain hidden information beyond their visible content
2. **Multiple Attack Vectors:** Trying different approaches (steganography vs. metadata) when initial methods fail
3. **Encoding Recognition:** Identifying common encoding schemes like Base64
4. **Forensics Tools:** Using both online and command-line tools for file analysis:
   - Online: Metadata2Go, dCode, Base64 decoders
   - CLI: `exiftool`, `strings`, `base64`, `steghide`

---

## 🔧 Tools Used

| Tool                    | Purpose                            | Method       |
| ----------------------- | ---------------------------------- | ------------ |
| `wget` / `curl`         | Download the challenge file        | Command-line |
| `steghide`              | Check for steganographic content   | Command-line |
| Metadata2Go             | Extract image metadata             | Online       |
| `exiftool`              | View EXIF/metadata (alternative)   | Command-line |
| dCode Cipher Identifier | Identify encoding type             | Online       |
| Base64 Decoder          | Decode Base64 string               | Online/CLI   |
| `strings`               | Extract readable strings from file | Command-line |

---

**Challenge Completed Successfully! 🎉**












