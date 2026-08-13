📋 Prerequisites
Python 3.10+ installed on your system.

A Telegram Bot Token obtained from @BotFather.

A Gemini API Key obtained from Google AI Studio.

⚙️ Local Setup
Clone the repository:

Bash
git clone git@github.com:EstebanPastor/Telegram-assistant-bot.git
cd Telegram-assistant-bot
Create and activate a virtual environment:

Bash
# Windows
python -m venv .venv
.venv\\Scripts\\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Configure environment variables:
Create a .env file in the root directory:

Fragmento de código
TELEGRAM_TOKEN=your_telegram_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
Run the bot:

Bash
python main.py
☁️ 24/7 Deployment (Render)
This bot is configured to run as a Background Worker on Render.

Push your repository to GitHub (ensure .env is listed in .gitignore):

Bash
git remote add origin git@github.com:EstebanPastor/Telegram-assistant-bot.git
git branch -M main
git push -u origin main
Log in to Render and create a New Background Worker.

Connect your GitHub repository (EstebanPastor/Telegram-assistant-bot).

Set the build and start commands:

Build Command: pip install -r requirements.txt

Start Command: python main.py

Add the environment variables under Environment Variables:

TELEGRAM_TOKEN

GEMINI_API_KEY

Click Create Background Worker.

📜 License
This project is open-source and available under the MIT License.
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content)

print("README.md updated with correct remote origin.")


```text?code_stdout&code_event_index=1
README.md updated with correct remote origin.

Your README file is ready
[file-tag: code-generated-file-3e716be6-1ba2-4e10-a731-231037d85a19]

Acá tenés el README.md actualizado con tu repositorio exacto (EstebanPastor/Telegram-assistant-bot.git):

Markdown
# AI Telegram Bot

A lightweight, asynchronous Telegram bot powered by Google's **Gemini AI** (`gemini-2.5-flash`). Built with Python using `python-telegram-bot` and `google-genai`.

---

## 🚀 Features

- **Gemini AI Integration:** Fast and intelligent text generation using Google's official SDK.
- **Asynchronous Execution:** Built with `python-telegram-bot` for smooth handling of user messages.
- **Environment Variable Protection:** Uses `python-dotenv` to keep sensitive API keys secure.
- **Cloud Ready:** Designed for continuous 24/7 deployment on platforms like Render or Railway.

---

## 🛠️ Project Structure

```text
├── main.py              # Main application script
├── requirements.txt      # Project dependencies
├── .env                 # Environment variables (not committed to git)
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
📋 Prerequisites
Python 3.10+ installed on your system.

A Telegram Bot Token obtained from @BotFather.

A Gemini API Key obtained from Google AI Studio.

⚙️ Local Setup
Clone the repository:

Bash
git clone git@github.com:EstebanPastor/Telegram-assistant-bot.git
cd Telegram-assistant-bot
Create and activate a virtual environment:

Bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Configure environment variables:
Create a .env file in the root directory:

Fragmento de código
TELEGRAM_TOKEN=your_telegram_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
Run the bot:

Bash
python main.py
☁️ 24/7 Deployment (Render)
This bot is configured to run as a Background Worker on Render.

Push your repository to GitHub (ensure .env is listed in .gitignore):

Bash
git remote add origin git@github.com:EstebanPastor/Telegram-assistant-bot.git
git branch -M main
git push -u origin main
Log in to Render and create a New Background Worker.

Connect your GitHub repository (EstebanPastor/Telegram-assistant-bot).

Set the build and start commands:

Build Command: pip install -r requirements.txt

Start Command: python main.py

Add the environment variables under Environment Variables:

TELEGRAM_TOKEN

GEMINI_API_KEY

Click Create Background Worker.

📜 License
This project is open-source and available under the MIT License.git add 