# picoCTF Writeup: Magikarp Ground Mission

**Challenge Name:** Magikarp Ground Mission  
**Category:** General Skills  
**Difficulty:** Easy   
**Author:** syreal

---

## 📌 Challenge Description

_Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Additional details will be available after launching your challenge instance._

This introductory challenge tests basic Linux command-line navigation skills. Players must traverse different directories to locate three fragments of a flag scattered across the filesystem.

---

## 🎯 Objective

Find and combine three flag fragments hidden in different directories within the SSH environment.

---

## 🔍 Initial Analysis

Upon launching the challenge instance, we receive the following connection credentials:

- **Username:** `ctf-player`
- **Host:** `wily-courier.picoctf.net`
- **Port:** `62628`
- **Password:** `8c606eb1`

The challenge requires knowledge of basic Linux commands:

- `ssh` - Secure Shell connection
- `ls` - List directory contents
- `cd` - Change directory
- `cat` - Display file contents

---

## 🛠️ Solution Steps

### Step 1: Establish SSH Connection

Connect to the remote server using the provided credentials:

```bash
ssh ctf-player@wily-courier.picoctf.net -p 62628
```

### Step 2: Host Authentication

On first connection, SSH displays a host authenticity warning. Type `yes` to confirm and proceed with the connection.

### Step 3: Authentication

Enter the password when prompted:

```bash
ctf-player@wily-courier.picoctf.net's password: 8c606eb1
```

Upon successful authentication, you'll see the Ubuntu welcome message:

```
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 6.14.0-1012-aws x86_64)
```

### Step 4: First Flag Fragment (Home Directory)

List the contents of the current directory:

```bash
ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt
```

Read the first flag fragment:

```bash
ctf-player@pico-chall$ cat 1of3.flag.txt
picoCTF{xxsh_
```

Check the instructions for the next fragment:

```bash
ctf-player@pico-chall$ cat instructions-to-2of3.txt
Next, go to the root of all things, more succinctly `/`
```

**Fragment 1:** `picoCTF{xxsh_`

### Step 5: Second Flag Fragment (Root Directory)

Navigate to the root directory:

```bash
ctf-player@pico-chall$ cd /
```

List the directory contents:

```bash
ctf-player@pico-chall$ ls
2of3.flag.txt  boot       dev  home                      lib    media  opt   root  sbin  sys  usr
bin            challenge  etc  instructions-to-3of3.txt  lib64  mnt    proc  run   srv   tmp  var
```

Read the second flag fragment:

```bash
ctf-player@pico-chall$ cat 2of3.flag.txt
0ut_0f_//4t3r_
```

Check the next instructions:

```bash
ctf-player@pico-chall$ cat instructions-to-3of3.txt
Lastly, ctf-player, go home... more succinctly `~`
```

**Fragment 2:** `0ut_0f_//4t3r_`

### Step 6: Third Flag Fragment (Home Directory)

Navigate to the home directory using the tilde shortcut:

```bash
ctf-player@pico-chall$ cd ~
```

List the directory contents:

```bash
ctf-player@pico-chall$ ls
3of3.flag.txt  drop-in
```

Read the final flag fragment:

```bash
ctf-player@pico-chall$ cat 3of3.flag.txt
0b24fc4f}
```

**Fragment 3:** `0b24fc4f}`

### Step 7: Assemble the Complete Flag

Concatenate all three fragments in order:

```
picoCTF{xxsh_ + 0ut_0f_//4t3r_ + 0b24fc4f}
```

---

## 🚩 Flag

```
picoCTF{xxsh_0ut_0f_//4t3r_0b24fc4f}
```

---

## 💡 Key Takeaways

This challenge reinforces fundamental Linux navigation concepts:

1. **SSH Connection:** Establishing secure remote connections
2. **Directory Navigation:** Using `cd` with absolute paths (`/`) and shortcuts (`~`)
3. **File Exploration:** Listing contents with `ls` and reading files with `cat`
4. **Path Understanding:** Recognizing special directories:
   - `.` (current directory)
   - `~` (home directory)
   - `/` (root directory)

---

## 🔧 Commands Used

| Command | Purpose                  |
| ------- | ------------------------ |
| `ssh`   | Connect to remote server |
| `ls`    | List directory contents  |
| `cd`    | Change directory         |
| `cat`   | Display file contents    |

---

## 📝 Full Terminal Session

```bash
C:\Users\Acer>ssh ctf-player@wily-courier.picoctf.net -p 62628
ctf-player@wily-courier.picoctf.net's password:
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 6.14.0-1012-aws x86_64)

ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt

ctf-player@pico-chall$ cat 1of3.flag.txt
picoCTF{xxsh_

ctf-player@pico-chall$ cat instructions-to-2of3.txt
Next, go to the root of all things, more succinctly `/`

ctf-player@pico-chall$ cd /

ctf-player@pico-chall$ ls
2of3.flag.txt  boot       dev  home                      lib    media  opt   root  sbin  sys  usr
bin            challenge  etc  instructions-to-3of3.txt  lib64  mnt    proc  run   srv   tmp  var

ctf-player@pico-chall$ cat 2of3.flag.txt
0ut_0f_//4t3r_

ctf-player@pico-chall$ cat instructions-to-3of3.txt
Lastly, ctf-player, go home... more succinctly `~`

ctf-player@pico-chall$ cd ~

ctf-player@pico-chall$ ls
3of3.flag.txt  drop-in

ctf-player@pico-chall$ cat 3of3.flag.txt
0b24fc4f}
```

---

**Challenge Completed Successfully! 🎉**
