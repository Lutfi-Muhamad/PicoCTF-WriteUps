# picoCTF Writeup: Verify

**Challenge Name:** Verify
**Category:** Forensics
**Difficulty:** Easy
**Author:** Jeffery John

---

## 📌 Challenge Description

People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.
Additional details will be available after launching your challenge instance.

Access is provided via SSH:

- **Host:** rhea.picoctf.net
- **Port:** 52760
- **Username:** ctf-player
- **Password:** 1db87a14

Once connected, we are instructed to verify file hashes and decrypt the correct file.

---

## 🎯 Objective

Identify the file whose SHA-256 hash matches the provided checksum, then decrypt it to retrieve the legitimate picoCTF flag.

---

## 🔍 Initial Analysis

After connecting to the remote host, we are given:

- A checksum file containing the expected SHA-256 hash
- A decryption script
- A directory containing multiple encrypted files

Only **one file** should match the provided checksum.

---

## 🛠️ Solution Steps

### Step 1: Connect to the Remote Host

```bash
ssh -p 52760 ctf-player@rhea.picoctf.net
```

After entering the password, list the directory contents:

```bash
ls
```

Output:

```
checksum.txt  decrypt.sh  files
```

---

### Step 2: Inspect the Provided Checksum

```bash
cat checksum.txt
```

Output:

```
55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a
```

This hash is the reference value we need to match.

---

### Step 3: Generate SHA-256 Hashes for All Files

To calculate the checksum for each file in the `files` directory:

```bash
sha256sum files/*
```

This produces a large list of hashes, one per file.

---

### Step 4: Identify the Matching File Using `grep`

To efficiently locate the correct file, we pipe the output into `grep`:

```bash
sha256sum files/* | grep "55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a"
```

Output:

```
55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a  files/2cdcb2de
```

Only one file matches the provided checksum.

---

### Step 5: Decrypt the Verified File

Using the provided decryption script:

```bash
./decrypt.sh files/2cdcb2de
```

Output:

```
picoCTF{trust_but_verify_2cdcb2de}
```

---

## 🚩 Flag

```
picoCTF{trust_but_verify_2cdcb2de}
```

---

## 💡 Key Insights

- **Checksum verification ensures data integrity**
  Hashes allow us to confirm that a file has not been modified or replaced.

- **SHA-256 is deterministic and collision-resistant**
  Identical inputs always produce the same output, making it reliable for verification.

- **Command-line pipelines improve efficiency**
  Combining `sha256sum` with `grep` avoids manual inspection of large outputs.

- **Verification before decryption is critical**
  Only trusted and verified data should be processed further.

---

## 🔧 Tools & Techniques Used

| Tool / Technique | Purpose                            |
| ---------------- | ---------------------------------- |
| SSH              | Remote system access               |
| `sha256sum`      | Generate SHA-256 checksums         |
| `grep`           | Filter and match specific hashes   |
| Bash scripting   | Execute provided decryption script |

---

**Challenge completed successfully.**
