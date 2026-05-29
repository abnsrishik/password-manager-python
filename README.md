# Password Manager

A desktop password manager built with Python and Tkinter.
Generates strong passwords, saves credentials per website, and lets you search them instantly — all stored locally in JSON.

## Features

- **Password generator** — creates randomised passwords with letters, numbers, and symbols
- **Auto-copy** — generated password copied to clipboard automatically (via pyperclip)
- **Save credentials** — stores website, email, and password in `data.json`
- **Search** — retrieve saved credentials by website name instantly
- **Confirmation dialog** — review before saving, prevents accidental entries
- **Persistent storage** — data survives app close, new entries merge with existing

## How to Run

```bash
git clone https://github.com/abnsrishik/password-manager-python
cd password-manager-python
pip install pyperclip
python main.py
```

## Project Structure

```
password-manager-python/
├── main.py                  # GUI + save/search/generate logic
├── password_generator.py    # PasswordGenerator class
├── logo.png                 # App icon
└── data.json                # Auto-generated, stores all credentials
```

## Architecture

| File | Class / Role | Responsibility |
|---|---|---|
| `password_generator.py` | `PasswordGenerator` | Generates randomised passwords using letters, numbers, symbols |
| `main.py` | — | Tkinter GUI, save/search logic, JSON read/write |

## Data Storage Format

Credentials saved as JSON:

```json
{
    "github": {
        "email": "user@example.com",
        "password": "aX3!kR9#"
    },
    "netflix": {
        "email": "user@example.com",
        "password": "mZ7$bQ2!"
    }
}
```

## Requirements

- Python 3.x
- pyperclip (`pip install pyperclip`)
- tkinter (included with standard Python)

## What I Learned

- Tkinter GUI — Entry, Button, Label, Canvas, messagebox, grid layout
- JSON file handling — read, write, update, error handling
- Separation of concerns — password logic in its own class/file
- Try/except/else/finally for robust file operations
- pyperclip for clipboard integration
