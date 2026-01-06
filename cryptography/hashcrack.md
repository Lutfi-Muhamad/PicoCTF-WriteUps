# picoCTF Writeup: hashcrack

**Challenge Name:** hashcrack
**Category:** Cryptography
**Difficulty:** Easy
**Author:** Nana Ama Atombo-Sackey

---

## 📌 Challenge Description

A company stored a secret message on a server which was breached due to the admin using weakly hashed passwords.
Can you gain access to the secret stored on the server?

Access the server using:

```
nc verbal-sleep.picoctf.net 53323
```

---

## 🎯 Objective

Crack a series of weak password hashes in order to retrieve the final flag.

---

## 🔍 Initial Analysis

The challenge provides access to a remote service via **netcat**.
Once connected, the server presents hashed passwords one by one.
Each hash uses a different hashing algorithm and corresponds to a very common, weak password.

**Required Skills:**

- Hash identification (MD5, SHA-1, SHA-256)
- Basic understanding of password hashing
- Use of online hash cracking tools or hash databases
- Familiarity with netcat

---

## 🛠️ Solution Steps

### Step 1: Connect to the Remote Server

I connected to the challenge server using netcat:

```bash
nc verbal-sleep.picoctf.net 53323
```

The server displays a welcome message and provides the first hash:

```
Welcome!! Looking For the Secret?

We have identified a hash:
482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash:
```

---

### Step 2: Identify and Crack the First Hash

The hash provided:

```
482c811da5d5b4bc6d497ffa98491e38
```

Using an online hash identifier, the hash was recognized as **MD5**.

After cracking the hash using a public hash database, the plaintext password was revealed as:

```
password123
```

---

### Step 3: Submit the First Password

I entered the cracked password:

```
password123
```

The server confirmed success and provided the second hash:

```
Correct! You've cracked the MD5 hash with no secret found!

Flag is yet to be revealed!!
Crack this hash:
b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
```

---

### Step 4: Identify and Crack the Second Hash

The second hash:

```
b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
```

This hash is **40 characters long**, which strongly indicates **SHA-1**.

After cracking the SHA-1 hash, the password was found to be:

```
letmein
```

---

### Step 5: Submit the Second Password

I entered the password:

```
letmein
```

The server responded with the final hash:

```
Correct! You've cracked the SHA-1 hash with no secret found!

Almost there!!
Crack this hash:
916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
```

---

### Step 6: Identify and Crack the Third Hash

The final hash:

```
916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
```

This hash is **64 characters long**, which matches **SHA-256**.

Cracking the hash reveals the password:

```
qwerty098
```

---

### Step 7: Retrieve the Flag

After entering the final password:

```
qwerty098
```

The server reveals the flag:

```
Correct! You've cracked the SHA-256 hash with a secret found.
The flag is:
picoCTF{UseStr0nG_h@shEs_&PaSswDs!_eb2f8459}
```

---

## 🚩 Flag

```
picoCTF{UseStr0nG_h@shEs_&PaSswDs!_eb2f8459}
```

---

## 💡 Key Takeaways

This challenge highlights several important security concepts:

1. **Weak Passwords Are Dangerous**
   Common passwords like `password123`, `letmein`, and `qwerty098` are trivial to crack.

2. **Hashing Alone Is Not Enough**
   Unsalted hashes are highly vulnerable to rainbow tables and public hash databases.

3. **Hash Length Matters**
   The length of a hash often reveals the hashing algorithm:

   - MD5: 32 hex characters
   - SHA-1: 40 hex characters
   - SHA-256: 64 hex characters

4. **Defense Requires Proper Hashing Practices**
   Secure systems should use modern password hashing algorithms like bcrypt, scrypt, or Argon2 with salting.

---

## 🔧 Tools & Techniques Used

| Tool / Technique    | Purpose                              |
| ------------------- | ------------------------------------ |
| Netcat (nc)         | Connect to the remote service        |
| Hash Identifier     | Determine hash algorithms            |
| Online Hash DB      | Crack weak password hashes           |
| SHA / MD5 Knowledge | Identify hashes by length and format |

---

**Challenge completed successfully.**
