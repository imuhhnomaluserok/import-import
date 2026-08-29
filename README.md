# `import import`

> **What the hell is this program...?**

A weird little puzzle game made with **Python + Pygame**.

The goal is simple:

> **Make `import` import `import`.**

That's it.

I don't know why I made this.

---

## 📦 Requirements

You need:

* **Python 3.12.1**
* **Pygame**

### Install Pygame

```powershell
py -3.12 -m pip install pygame
```

---

## ▶️ How to Start

Open PowerShell in the folder containing `game.py` and run:

```powershell
py -3.12 game.py
```

### 📋 Copy this

```text
py -3.12 game.py
```

Press **Enter** and the game will start.

---

# 🎮 How to Play

You are given a Python-like command prompt.

Your mission is to make this command work:

```text
import import
```

Obviously, it doesn't work at first.

So... let's fix that.

---

# 🔑 Walkthrough

Enter the following commands **in order** and press **Enter** after each one.

### 1. Try `import import`

Type:

```text
import import
```

You will get an error.

That's normal.

```text
'import' は、内部コマンドまたは外部コマンド、
操作可能なプログラムまたはバッチ ファイルとして認識されていません。
```

---

### 2. Check the PATH

Type:

```text
path
```

You should see something like:

```text
PATH=C:\Windows\system32;C:\Windows;C:\Python314
```

There is a hidden `core` directory that needs to be added to the PATH.

---

### 3. Add `core` to the PATH

This is the important part.

Type:

```text
set path=core
```

If successful, you will see:

```text
[NOTICE] A hidden directory 'core' has been linked to the system PATH.
```

The hack is complete. 🕵️

---

### 4. Try `import import` again

Now type:

```text
import import
```

And...

```text
[CRITICAL] ACCESS GRANTED.
[SYSTEM] Patching Python vocabulary rules...
[SUCCESS] 'import' successfully imported into 'import'!
```

🎉 **You win!**

---

# 🛠️ Customize It

Feel free to modify the code and make your own version!

For example, the prompt currently shows:

```text
C:\Users\arks2_dc4cden>
```

That's just the path from the developer's computer.

You can change it to whatever you want by editing `game.py`.

**Go crazy.**

---

# 🇯🇵 日本語

Python + Pygameで作った、**Python風CUIの謎解きゲーム**です。

目的：

> **`import`を`import`させる。**

それだけです。

俺は何をしたかったんだろう。

なんでこんなのを作ったんだ。

---

## 📜 License

See `LICENSE.txt`.

This project is released under the **MIT License**.

...Why does this thing even need a license?

I don't know.

---

# 🦆 Have Fun!

Feel free to modify, break, improve, or completely destroy the game.

**Make your own weird version.**

That's what it's here for.

> `import import`
>
> **It just works.**
