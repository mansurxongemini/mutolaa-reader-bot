# 📚 Mutolaa Reader Service

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Async-45ba4b.svg?logo=playwright&logoColor=white)](https://playwright.dev/python/)
[![aiohttp](https://img.shields.io/badge/aiohttp-3.9-2C5BB4.svg?logo=python&logoColor=white)](https://docs.aiohttp.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Mutolaa Reader Service** is an automated educational session runner and reading companion built with asynchronous Python, Playwright browser automation, and an aiohttp monitoring health-check server.

---

## 🌟 Features
- **⚡ Asynchronous Automation**: High-efficiency headless browser sessions using **Playwright**.
- **📉 Resource Optimized**: Blocks non-essential media & tracking requests to minimize memory footprint.
- **🩺 Health Check Web Server**: Integrated lightweight **aiohttp** HTTP endpoint for cloud liveness probing.
- **🔒 Secure Authentication**: Dynamic credentials loading via environment variables.

---

## 🚀 Getting Started

### 1. Installation
```bash
git clone https://github.com/mansurxongemini/mutolaa-reader-bot.git
cd mutolaa-reader-bot

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

### 2. Configuration
Create a `.env` file (or export environment variables):
```bash
export MUTOLAA_ACCESS_TOKEN="your_token_here"
export MUTOLAA_DEVICE_ID="your_device_id_here"
export MUTOLAA_BOOK_URL="https://mutolaa.com/uz/reader/..."
```

### 3. Run
```bash
python bot.py
```

---

## 📜 License
Distributed under the **MIT License**.
