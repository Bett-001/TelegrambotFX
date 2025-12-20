# TelegrambotFX
# 🚀 Tonnyfx Academy Telegram Bot

A professional Telegram automation bot designed for **Tonnyfx Academy**. This bot streamlines the process of onboarding new VIP members, providing automated payment instructions, and handling transaction verification screenshots.



## 🌟 Features

* **Custom Menu Keyboard:** User-friendly buttons for navigation (Join VIP, About, Contact).
* **VIP Subscription Management:** Detailed instructions for users to pay a $30 fee via Send Money.
* **Proof of Payment Forwarding:** Automatically forwards transaction screenshots from users directly to the Admin.
* **Smart Responses:** Handles common questions about the academy and signals.
* **Admin Alerts:** Notifies the admin with the user's name, ID, and username when a payment proof is submitted.

## 🛠 Tech Stack

* **Language:** Python 3.8+
* **Library:** [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) (v20+)
* **Framework:** Asynchronous (asyncio)

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/Telegrambot.git](https://github.com/yourusername/Telegrambot.git)
   cd Telegrambot
Install dependencies:

Bash

pip install python-telegram-bot
Configure the Bot: Open main.py and update the following variables:

TOKEN: Your bot token from @BotFather.

ADMIN_USERNAME: Your Telegram username (e.g., @FxwithTonny).

Run the bot:

Bash

python main.py

Command,Description
/start,Initializes the bot and displays the main menu keyboard.
/vip,Provides payment details ($30) and verification steps.
/about,Displays information about Tonnyfx Academy signals and mentorship.
/contact,Provides a direct link to the Admin for support.
/help,Shows a list of available commands.

🛡 Security & Verification
The bot acts as a bridge. Users send screenshots of their Send Money (0743399462) transactions. These images are forwarded to the Admin for manual verification. Once verified, the Admin can manually share the VIP link with the user.

👤 Author
Tonny Bett Lead Developer & Founder of Tonnyfx Academy Telegram: @FxwithTonny

© 2025 Tonnyfx Academy. All rights reserved.