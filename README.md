# Wiper Script

A python script that erases the content of files matching a pattern, recursively through directories(Downloads directory in this case).

---

## How to do it

- Iterate through all files matching the pattern recursively
- Use `.glob(file_pattern)` for a single directory, or `.rglob(file_pattern)` for recursive search
- Ensure it's a file and not a directory
- Open the file in write mode (`'w'`) which overwrites existing content

> **Be careful, this will erase the original content of all matching files!**

---

## Building the Executable

The script was packaged into a  `.exe` using **PyInstaller**.

**Install PyInstaller:**
```bash
pip install pyinstaller
```

**Build the executable:**
```bash
python -m PyInstaller --onefile wiper.py
```

The `.exe` will be generated in the `dist/` folder.

---

## Download

> [Download wiper.exe](https://www.mediafire.com/file/mg5etbayux7p0g5/wiper.exe/file)

---

## ⚠️ Warning

**I am not responsible** for any data loss or damage caused by using this tool. Use it at your own risk(clicking the .exe file when downloaded will erase your folder content).
