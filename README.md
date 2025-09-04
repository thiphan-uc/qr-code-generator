# Biox Systems — QR Code Generator (CLI)

A lightweight Python app that generates a QR code from a URL.  
Tested on **macOS** with Python 3 (installed via Homebrew).

---

## Requirements
- macOS with [Homebrew](https://brew.sh/) installed  
- Python 3.10+ (`brew install python`)  
- `qrcode` (installed via pip)

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install qrcode
```
or install from the manifest

```bash
pip install -r requirements.txt
```

### 4. Generate QR from URL
```bash
python3 app.py --url "https://www.bioxsystems.com/"
```
