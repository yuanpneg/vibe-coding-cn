# Telegram Bot Button and Keyboard Implementation Guide

> A complete reference for developing interactive features for Telegram Bots

---

## 📋 Table of Contents

1. [Button and Keyboard Types](#button-and-keyboard-types)
2. [Implementation Comparison](#implementation-comparison)
3. [Core Code Examples](#core-code-examples)
4. [Best Practices](#best-practices)

---

## Button and Keyboard Types

### 1. Inline Keyboard

**Features**:
- Displayed below a message
- Triggers a callback when clicked, without sending a message
- Supports callback data, URLs, switch queries, etc.

**Use Cases**: Confirmation/cancellation, menu navigation, pagination control, setting options

### 2. Reply Keyboard

**Features**:
- Displayed above the input field
- Sends a text message when a button is clicked
- Can be set as persistent or one-time

**Use Cases**: Quick commands, common actions, form input, main menu

### 3. Bot Command Menu

**Features**:
- Displayed in the "/" button to the left of the input field
- Set via BotFather or the API
- Provides a list of commands and their descriptions

**Use Cases**: Function index, new user guidance, quick command access

### 4. Type Comparison

| Feature | Inline | Reply | Command Menu |
|---|---|---|---|
| Position | Below message | Above input field | "/" menu |
| Trigger | Callback query | Text message | Command |
| Persistence | With message | Configurable | Always present |
| Scenario | Temporary interaction | Resident function | Command index |

---

## Implementation Comparison

### python-telegram-bot (Recommended for Bot development)

**Advantages**:
- Officially recommended, with a complete Handler system
- Rich support for buttons and keyboards
- Excellent performance with the asynchronous version

**Installation**:
```bash
pip install python-telegram-bot==20.7
```

### Telethon (Suitable for user account automation)

**Advantages**:
- Full access to the MTProto API
- Can be used with user accounts and Bots
- Powerful message listening capabilities

**Installation**:
```bash
pip install telethon cryptg
```

---

## Core Code Examples

### 1. Inline Keyboard Implementation

**python-telegram-bot:**
```python
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Display an inline keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("📊 View Data", callback_data="view_data"),
            InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
        ],
        [
            InlineKeyboardButton("🔗 Visit Website", url="https://example.com"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button clicks"""
    query = update.callback_query
    await query.answer()  # Must be called

    if query.data == "view_data":
        await query.edit_message_text("Displaying data...")
    elif query.data == "settings":
        await query.edit_message_text("Settings options...")

# Register handlers
app = Application.builder().token("TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_callback))
app.run_polling()
```

**Telethon:**
```python
from telethon import TelegramClient, events, Button

client = TelegramClient('bot', api_id, api_hash).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    buttons = [
        [Button.inline("📊 View Data", b"view_data"), Button.inline("⚙️ Settings", b"settings")],
        [Button.url("🔗 Visit Website", "https://example.com")]
    ]
    await event.respond("Please choose:", buttons=buttons)

@client.on(events.CallbackQuery)
async def callback(event):
    if event.data == b"view_data":
        await event.edit("Displaying data...")
    elif event.data == b"settings":
        await event.edit("Settings options...")

client.run_until_disconnected()
```

### 2. Reply Keyboard Implementation

**python-telegram-bot:**
```python
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Display a reply keyboard"""
    keyboard = [
        [KeyboardButton("📊 View Data"), KeyboardButton("⚙️ Settings")],
        [KeyboardButton("📚 Help"), KeyboardButton("❌ Hide Keyboard")],
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )
    await update.message.reply_text("Menu activated", reply_markup=reply_markup)

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages"""
    text = update.message.text
    if text == "📊 View Data":
        await update.message.reply_text("Displaying data...")
    elif text == "❌ Hide Keyboard":
        await update.message.reply_text("Keyboard hidden", reply_markup=ReplyKeyboardRemove())
```

**Telethon:**
```python
@client.on(events.NewMessage(pattern='/menu'))
async def menu(event):
    buttons = [
        [Button.text("📊 View Data"), Button.text("⚙️ Settings")],
        [Button.text("📚 Help"), Button.text("❌ Hide Keyboard")]
    ]
    await event.respond("Menu activated", buttons=buttons)

@client.on(events.NewMessage)
async def handle_text(event):
    if event.text == "📊 View Data":
        await event.respond("Displaying data...")
```

### 3. Bot Command Menu Setup

**Via BotFather:**
```
1. Send /setcommands to @BotFather
2. Choose your Bot
3. Enter the list of commands (format per line: command - description)

start - Start the bot
help - Get help
menu - Display the main menu
settings - Configure settings
```

**Via API (python-telegram-bot):**
```python
from telegram import BotCommand

async def set_commands(app: Application):
    """Set the command menu"""
    commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("help", "Get help"),
        BotCommand("menu", "Display the main menu"),
        BotCommand("settings", "Configure settings"),
    ]
    await app.bot.set_my_commands(commands)

# Call on startup
app.post_init = set_commands
```

### 4. Project Structure Example

```
telegram_bot/
├── bot.py                    # Main program
├── config.py                 # Configuration management
├── requirements.txt
├── .env
├── handlers/
│   ├── command_handlers.py   # Command handlers
│   ├── callback_handlers.py  # Callback handlers
│   └── message_handlers.py   # Message handlers
├── keyboards/
│   ├── inline_keyboards.py   # Inline keyboard layouts
│   └── reply_keyboards.py    # Reply keyboard layouts
└── utils/
    ├── logger.py             # Logger
    └── database.py           # Database
```

**Modular Example (keyboards/inline_keyboards.py):**
```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_main_menu():
    """Main menu keyboard"""
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📊 Data", callback_data="data"),
            InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
        ],
        [InlineKeyboardButton("📚 Help", callback_data="help")],
    ])

def get_data_menu():
    """Data menu keyboard"""
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📈 Real-time", callback_data="data_realtime"),
            InlineKeyboardButton("📊 History", callback_data="data_history"),
        ],
        [InlineKeyboardButton("⬅️ Back", callback_data="back")],
    ])
```

---

## Best Practices

### 1. Handler Priority

```python
# Match in order of registration, from most specific to most general
app.add_handler(CommandHandler("start", start))           # 1. Specific command
app.add_handler(CallbackQueryHandler(callback))           # 2. Callback query
app.add_handler(ConversationHandler(...))                 # 3. Conversation flow
app.add_handler(MessageHandler(filters.TEXT, text_msg))   # 4. General message (last)
```

### 2. Error Handling

```python
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Global error handler"""
    logger.error(f"Update {update} caused error", exc_info=context.error)

    # Notify the user
    if update and update.effective_message:
        await update.effective_message.reply_text("Operation failed, please try again")

app.add_error_handler(error_handler)
```

### 3. Callback Data Management

```python
# Use structured callback_data
callback_data = "action:page:item"  # e.g., "view:1:product_123"

# Parse callback data
async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    parts = query.data.split(":")
    action, page, item = parts

    if action == "view":
        await show_item(query, page, item)
```

### 4. Keyboard Design Principles

- **Concise**: 2-3 buttons per row at most
- **Clear**: Use emojis to enhance recognition
- **Consistent**: Maintain a uniform layout style
- **Responsive**: Provide timely feedback to user actions

### 5. Security Considerations

```python
# Verify user permissions
ADMIN_IDS = [123456789]

async def admin_only(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("Permission denied")
        return

    # Execute admin operations
```

### 6. Deployment Solutions

**Webhook (Recommended for production):**
```python
from flask import Flask, request

app_flask = Flask(__name__)

@app_flask.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    application.update_queue.put(update)
    return "OK"

# Set webhook
bot.set_webhook(f"https://yourdomain.com/webhook")
```

**Systemd Service (Linux):**
```ini
[Unit]
Description=Telegram Bot
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/path/to/bot
ExecStart=/path/to/venv/bin/python bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

### 7. Common Library Versions

```txt
# requirements.txt
python-telegram-bot==20.7
python-dotenv==1.0.0
aiosqlite==0.19.0
httpx==0.25.2
```

---

## Quick Reference

### Inline Keyboard Button Types

```python
InlineKeyboardButton("Text", callback_data="data")     # Callback button
InlineKeyboardButton("Link", url="https://...")        # URL button
InlineKeyboardButton("Switch", switch_inline_query="")   # Inline query
InlineKeyboardButton("Login", login_url=...)            # Login button
InlineKeyboardButton("Pay", pay=True)                 # Payment button
InlineKeyboardButton("App", web_app=WebAppInfo(...))  # Mini App
```

### Common Event Types

- `events.NewMessage` - New message
- `events.CallbackQuery` - Callback query
- `events.InlineQuery` - Inline query
- `events.ChatAction` - Group action

---

**This guide covers all the core implementations of Telegram Bot buttons and keyboards!**
