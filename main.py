import logging
from typing import Final
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application, 
    CommandHandler, 
    MessageHandler, 
    filters, 
    ContextTypes
)

# --- Configuration ---
TOKEN: Final = "8028162834:AAFKI2uu_E-Lq3oIpMMDsdDs9aG1vTGHie8"
BOT_USERNAME: Final = "@Tonnysbot_bot"
ADMIN_USERNAME: Final = "@FxwithTonny"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- Keyboards ---
def main_menu_keyboard():
    keyboard = [
        ['💎 Join VIP', '📝 About Academy'],
        ['📞 Contact Admin', '❓ Help']
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# --- Handlers: Commands ---

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_msg = (
        f"Welcome to *Tonnyfx Academy*! 🚀\n\n"
        "I am here to help you get started with our professional signals.\n"
        "Use the buttons below to navigate."
    )
    await update.message.reply_text(
        welcome_msg, 
        parse_mode='Markdown', 
        reply_markup=main_menu_keyboard()
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "❓ *How can I help you?*\n\n"
        "💎 /vip - Get payment details for VIP\n"
        "📝 /about - Learn about Tonnyfx Academy\n"
        "📞 /contact - Contact Tonny directly\n"
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = (
        "📈 *Tonnyfx Academy* is a premier trading community.\n\n"
        "We offer:\n"
        "• 90% Accurate Forex Signals\n"
        "• Weekly Market Analysis\n"
        "• Direct Mentorship from Tonny (The Forex Master)\n"
        "• Lifetime access to our trading resources."
    )
    await update.message.reply_text(about_text, parse_mode='Markdown')

async def vip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    vip_msg = (
        "💎 *JOIN THE TONNYFX VIP GROUP* 💎\n\n"
        "Join for exclusive signals and mentorship!\n\n"
        "💵 *Subscription Fee:* $30\n"
        "🏦 *Payment Method:* Send Money\n"
        "📱 *Phone Number:* `0743399462`\n\n"
        "📋 *HOW TO VERIFY:*\n"
        "1️⃣ Send the $30 to the number above.\n"
        "2️⃣ Take a clear **screenshot** of the transaction.\n"
        "3️⃣ **Upload the photo right here to this bot.**\n\n"
        "Verification is fast! Once confirmed, you will receive the VIP link.\n\n"
        "👨‍💻 *Admin:* @FxwithTonny"
    )
    await update.message.reply_text(vip_msg, parse_mode='Markdown')

async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Need help? Contact @FxwithTonny directly.")

# --- Handlers: Messages & Media ---

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Map buttons to functions
    if text == '💎 Join VIP':
        return await vip_command(update, context)
    if text == '📝 About Academy':
        return await about_command(update, context)
    if text == '📞 Contact Admin':
        return await contact_command(update, context)
    if text == '❓ Help':
        return await help_command(update, context)

    # General text responses
    processed = text.lower()
    if "hello" in processed or "hi" in processed:
        response = "Hello! Use the menu below to explore our services."
    elif "pay" in processed or "price" in processed:
        response = "The VIP fee is $30. Click '💎 Join VIP' for payment details."
    else:
        response = "I'm not sure about that. Try using the menu buttons below!"
    
    await update.message.reply_text(response, reply_markup=main_menu_keyboard())

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type != 'private':
        return

    user = update.message.from_user
    username = f"@{user.username}" if user.username else f"ID: {user.id}"

    try:
        # Forward to Admin
        await context.bot.send_message(
            chat_id=ADMIN_USERNAME, 
            text=f"🚨 *NEW PAYMENT PROOF*\nFrom: {user.first_name} ({username})",
            parse_mode='Markdown'
        )
        await update.message.forward(chat_id=ADMIN_USERNAME)

        # Confirm to User
        await update.message.reply_text(
            "✅ *Screenshot Received!*\n\n"
            "Forwarded to Tonny. We will send you the VIP link once verified!",
            parse_mode='Markdown'
        )
    except Exception as e:
        await update.message.reply_text(f"❌ Error. Send directly to {ADMIN_USERNAME}")

# --- Main Entry Point ---

if __name__ == '__main__':
    print("Initializing Tonnyfx Bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("vip", vip_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("contact", contact_command))

    # Photo Handler
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    # Text Handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is now live and polling...")
    app.run_polling(poll_interval=1.0)