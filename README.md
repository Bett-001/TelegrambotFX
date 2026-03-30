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

### Local Run
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Set env var:**
   ```bash
   export BOT_TOKEN="your_bot_token_from_botfather"
   ```
3. **Test healthcheck (new tab):**
   ```bash
   curl http://localhost:10000/health  # Should return "OK"
   ```
4. **Run:**
   ```bash
   python main.py
   ```

### Auto-Run with systemd
...

### Render.com Deployment (Cloud - Always On)
1. **Push to GitHub** (main branch).
2. **Connect repo** at render.com/dashboard.
3. **Set env var** BOT_TOKEN in Render dashboard.
4. **Deploy** using `infra/render.yaml` Blueprint (auto-detected).
5. **Healthcheck**: Render pings /health automatically.
6. **Logs/Metrics**: Available in Render dashboard.

**Free tier works for low-traffic bots!**


### Auto-Run with systemd (Recommended - Always On)
1. **Service created**: `~/.config/systemd/user/telegrambot.service`
2. **Reload & Enable** (one-time):
   ```bash
   systemctl --user daemon-reload
   systemctl --user enable --now telegrambot
   ```
3. **Status/Logs**:
   ```bash
   systemctl --user status telegrambot
   journalctl --user -u telegrambot -f
   ```
4. **Stop**:
   ```bash
   systemctl --user stop telegrambot
   ```

**Auto-starts on login/boot, restarts on crash!**
Install dependencies:

Bash

pip install python-telegram-bot
Configure the Bot: Open main.py and update the following variables:

TOKEN: Your bot token from @BotFather.

ADMIN_USERNAME: Your Telegram username (e.g., @FxwithTonny).



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