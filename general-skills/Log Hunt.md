# picoCTF Writeup: Log Hunt

**Challenge Name:** Log Hunt  
**Category:** General Skills  
**Difficulty:** Easy  
**Author:** Yahaya Meddy  

---

## 📌 Challenge Description

Our server appears to be leaking fragments of a secret flag through its log files. The flag is split into several parts, some of which are repeated. Your task is to analyze the logs, identify the relevant fragments, and reconstruct the complete flag.

---

## 🎯 Objective

Analyze the server log file, locate all flag fragments, and correctly assemble them to recover the full picoCTF flag.

---

## 🔍 Initial Analysis

The challenge provides a downloadable log file named `server.log`. Since this is a log-based challenge, the solution relies on text processing rather than file repair or binary analysis.

Command-line tools such as `cat` and `grep` are sufficient for this task.

---

## 🛠️ Solution Steps

### Step 1: Download the Log File

Download the provided log file using `wget`:

```bash
wget https://challenge-files.picoctf.net/c_amiable_citadel/49cec6157142f24a599f4164d5b63322c2494f801390d6f22eb91b3aa592bc66/server.log
```

---

### Step 2: Inspect the Log Contents

View the contents of the log file:

```bash
cat server.log
```

The output contains typical server log entries such as warnings and informational messages, with timestamps and log levels.

---

### Step 3: Search for Flag Fragments

Since picoCTF flags always start with `picoCTF{`, use `grep` to search for occurrences of the flag:

```bash
grep "pico" server.log
```

Output:

```
[1990-08-09 10:00:10] INFO FLAGPART: picoCTF{us3_
[1990-08-09 11:04:27] INFO FLAGPART: picoCTF{us3_
...
```

This reveals repeated and incomplete fragments of the flag.

---

### Step 4: Extract All Flag Parts

To collect all fragments, search for the keyword `FLAGPART`:

```bash
grep "FLAGPART" server.log
```

Output:

```
[1990-08-09 10:00:10] INFO FLAGPART: picoCTF{us3_
[1990-08-09 10:02:55] INFO FLAGPART: y0urlinux_
[1990-08-09 10:05:54] INFO FLAGPART: sk1lls_
[1990-08-09 10:05:55] INFO FLAGPART: sk1lls_
[1990-08-09 10:10:54] INFO FLAGPART: cedfa5fb}
```

From this output, the unique flag fragments can be identified while ignoring duplicates.

---

### Step 5: Assemble the Flag

Combine the fragments in logical order:

```
picoCTF{us3_ + y0urlinux_ + sk1lls_ + cedfa5fb}
```

---

## 🚩 Flag

```
picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}
```

---

## 💡 Key Takeaways

This challenge highlights several important skills:

1. **Log Analysis**
   Sensitive information can accidentally leak through logs if not handled carefully.

2. **Text Processing with CLI Tools**
   Simple tools like `grep` are powerful for extracting relevant data from large text files.

3. **Pattern Recognition**
   Recognizing flag formats helps quickly narrow down relevant information.

4. **Noise Filtering**
   Identifying duplicates and irrelevant entries is essential when working with real-world logs.

---

## 🔧 Tools Used

| Tool   | Purpose                           | Type |
| ------ | --------------------------------- | ---- |
| `wget` | Download the log file             | CLI  |
| `cat`  | View log file contents            | CLI  |
| `grep` | Search and extract flag fragments | CLI  |

---

**Challenge successfully completed.**