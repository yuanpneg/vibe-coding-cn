---
name: telegram-dev
description: A full-stack guide to Telegram ecosystem development - covering Bot API, Mini Apps (Web Apps), and MTProto client development. Includes complete development resources for message handling, payments, inline mode, webhooks, authentication, storage, sensor APIs, and more.
---

# Telegram Ecosystem Development Skill

A comprehensive guide to Telegram development, covering the full technology stack for Bot development, Mini Apps (Web Apps), and client development.

## When to Use This Skill

Use this skill when you need help with the following:
- Developing a Telegram Bot (message bot)
- Creating Telegram Mini Apps
- Building a custom Telegram client
- Integrating Telegram payments and business features
- Implementing webhooks and long polling
- Using Telegram authentication and storage
- Handling messages, media, and files
- Implementing inline mode and keyboards

## Overview of the Telegram Development Ecosystem

### Three Core APIs

1.  **Bot API** - For creating bot programs
    -   Simple to use HTTP interface
    -   Automatically handles encryption and communication
    -   Suitable for: chatbots, automation tools

2.  **Mini Apps API** (Web Apps) - For creating web applications
    -   JavaScript interface
    -   Runs inside Telegram
    -   Suitable for: mini-apps, games, e-commerce

3.  **Telegram API & TDLib** - For creating clients
    -   Full implementation of the Telegram protocol
    -   Supports all platforms
    -   Suitable for: custom clients, enterprise applications

## Bot API Development

### Quick Start

**API Endpoint:**
```
https://api.telegram.org/bot<TOKEN>/METHOD_NAME
```

**Get a Bot Token:**
1.  Talk to @BotFather
2.  Send `/newbot`
3.  Follow the prompts to set a name
4.  Get the token

**First Bot (Python):**
```python
import requests

BOT_TOKEN = "your_bot_token_here"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# Send a message
def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    return requests.post(url, json=data)

# Get updates (long polling)
def get_updates(offset=None):
    url = f"{API_URL}/getUpdates"
    params = {"offset": offset, "timeout": 30}
    return requests.get(url, params=params).json()

# Main loop
offset = None
while True:
    updates = get_updates(offset)
    for update in updates.get("result", []):
        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"]
        
        # Reply to the message
        send_message(chat_id, f"You said: {text}")
        
        offset = update["update_id"] + 1
```

### Core API Methods

**Update Management:**
- `getUpdates` - Get updates via long polling
- `setWebhook` - Set a webhook
- `deleteWebhook` - Delete a webhook
- `getWebhookInfo` - Query webhook status

**Message Operations:**
- `sendMessage` - Send a text message
- `sendPhoto` / `sendVideo` / `sendDocument` - Send media
- `sendAudio` / `sendVoice` - Send audio
- `sendLocation` / `sendVenue` - Send a location
- `editMessageText` - Edit a message
- `deleteMessage` - Delete a message
- `forwardMessage` / `copyMessage` - Forward/copy a message

**Interactive Elements:**
- `sendPoll` - Send a poll (up to 12 options)
- Inline Keyboard (InlineKeyboardMarkup)
- Reply Keyboard (ReplyKeyboardMarkup)
- `answerCallbackQuery` - Respond to a callback query

**File Operations:**
- `getFile` - Get file information
- `downloadFile` - Download a file
- Supports files up to 2GB (in local Bot API mode)

**Payment Features:**
- `sendInvoice` - Send an invoice
- `answerPreCheckoutQuery` - Process a payment
- Telegram Stars payment (up to 10,000 Stars)

### Webhook Configuration

**Set a Webhook:**
```python
import requests

BOT_TOKEN = "your_token"
WEBHOOK_URL = "https://yourdomain.com/webhook"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook",
    json={"url": WEBHOOK_URL}
)
```

**Flask Webhook Example:**
```python
from flask import Flask, request
import requests

app = Flask(__name__)
BOT_TOKEN = "your_token"

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    
    chat_id = update["message"]["chat"]["id"]
    text = update["message"]["text"]
    
    # Send a reply
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": f"Received: {text}"}
    )
    
    return "OK"

if __name__ == '__main__':
    app.run(port=5000)
```

**Webhook Requirements:**
- Must use HTTPS
- Supports TLS 1.2+
- Ports: 443, 80, 88, 8443
- Publicly accessible URL

### Inline Keyboard

**Create an Inline Keyboard:**
```python
def send_inline_keyboard(chat_id):
    keyboard = {
        "inline_keyboard": [
            [
                {"text": "Button 1", "callback_data": "btn1"},
                {"text": "Button 2", "callback_data": "btn2"}
            ],
            [
                {"text": "Open Link", "url": "https://example.com"}
            ]
        ]
    }
    
    requests.post(
        f"{API_URL}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": "Choose an option:",
            "reply_markup": keyboard
        }
    )
```

**Handle Callbacks:**
```python
def handle_callback_query(callback_query):
    query_id = callback_query["id"]
    data = callback_query["data"]
    chat_id = callback_query["message"]["chat"]["id"]
    
    # Respond to the callback
    requests.post(
        f"{API_URL}/answerCallbackQuery",
        json={"callback_query_id": query_id, "text": f"You clicked {data}"}
    )
    
    # Update the message
    requests.post(
        f"{API_URL}/editMessageText",
        json={
            "chat_id": chat_id,
            "message_id": callback_query["message"]["message_id"],
            "text": f"You chose: {data}"
        }
    )
```

### Inline Mode

**Configure Inline Mode:**
Talk to @BotFather and send `/setinline`

**Handle Inline Queries:**
```python
def handle_inline_query(inline_query):
    query_id = inline_query["id"]
    query_text = inline_query["query"]
    
    # Create results
    results = [
        {
            "type": "article",
            "id": "1",
            "title": "Result 1",
            "input_message_content": {
                "message_text": f"You searched for: {query_text}"
            }
        }
    ]
    
    requests.post(
        f"{API_URL}/answerInlineQuery",
        json={"inline_query_id": query_id, "results": results}
    )
```

## Mini Apps (Web Apps) Development

### Initialize a Mini App

**HTML Template:**
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <title>My Mini App</title>
</head>
<body>
    <h1>Telegram Mini App</h1>
    <button id="mainBtn">Main Button</button>
    
    <script>
        // Get the Telegram WebApp object
        const tg = window.Telegram.WebApp;
        
        // Notify Telegram that the app is ready
        tg.ready();
        
        // Expand to full screen
        tg.expand();
        
        // Display user information
        const user = tg.initDataUnsafe?.user;
        if (user) {
            console.log("Username:", user.first_name);
            console.log("User ID:", user.id);
        }
        
        // Configure the main button
        tg.MainButton.text = "Submit";
        tg.MainButton.show();
        tg.MainButton.onClick(() => {
            // Send data to the Bot
            tg.sendData(JSON.stringify({action: "submit"}));
        });
        
        // Add a back button
        tg.BackButton.show();
        tg.BackButton.onClick(() => {
            tg.close();
        });
    </script>
</body>
</html>
```

### Mini App Core API

**WebApp Object Main Properties:**
```javascript
// Initialization data
tg.initData           // Raw initialization string
tg.initDataUnsafe     // Parsed object

// User and theme
tg.initDataUnsafe.user       // User information
tg.themeParams                // Theme colors
tg.colorScheme                // 'light' or 'dark'

// Status
tg.isExpanded         // Whether it's full screen
tg.isFullscreen       // Whether it's full screen
tg.viewportHeight     // Viewport height
tg.platform           // Platform type

// Version
tg.version            // WebApp version
```

**Main Methods:**
```javascript
// Window control
tg.ready()            // Mark the app as ready
tg.expand()           // Expand to full height
tg.close()            // Close the Mini App
tg.requestFullscreen() // Request full screen

// Data sending
tg.sendData(data)     // Send data to the Bot

// Navigation
tg.openLink(url)      // Open an external link
tg.openTelegramLink(url) // Open a Telegram link

// Dialogs
tg.showPopup(params, callback)  // Show a popup
tg.showAlert(message)           // Show an alert
tg.showConfirm(message)         // Show a confirmation

// Sharing
tg.shareMessage(message)        // Share a message
tg.shareUrl(url)                // Share a link
```

### UI Controls

**Main Button (MainButton):**
```javascript
tg.MainButton.setText("Click Me");
tg.MainButton.show();
tg.MainButton.enable();
tg.MainButton.showProgress();  // Show loading
tg.MainButton.hideProgress();

tg.MainButton.onClick(() => {
    console.log("Main button clicked");
});
```

**Secondary Button (SecondaryButton):**
```javascript
tg.SecondaryButton.setText("Cancel");
tg.SecondaryButton.show();
tg.SecondaryButton.onClick(() => {
    tg.close();
});
```

**Back Button (BackButton):**
```javascript
tg.BackButton.show();
tg.BackButton.onClick(() => {
    // Back logic
});
```

**Haptic Feedback:**
```javascript
tg.HapticFeedback.impactOccurred('light');  // light, medium, heavy
tg.HapticFeedback.notificationOccurred('success'); // success, warning, error
tg.HapticFeedback.selectionChanged();
```

### Storage API

**Cloud Storage:**
```javascript
// Save data
tg.CloudStorage.setItem('key', 'value', (error, success) => {
    if (success) console.log('Saved successfully');
});

// Get data
tg.CloudStorage.getItem('key', (error, value) => {
    console.log('Value:', value);
});

// Delete data
tg.CloudStorage.removeItem('key');

// Get all keys
tg.CloudStorage.getKeys((error, keys) => {
    console.log('All keys:', keys);
});
```

**Local Storage:**
```javascript
// Normal local storage
localStorage.setItem('key', 'value');
const value = localStorage.getItem('key');

// Secure storage (requires biometrics)
tg.SecureStorage.setItem('secret', 'value', callback);
tg.SecureStorage.getItem('secret', callback);
```

### Biometric Authentication

```javascript
const bioManager = tg.BiometricManager;

// Initialize
bioManager.init(() => {
    if (bioManager.isInited) {
        console.log('Supported type:', bioManager.biometricType);
        // 'finger', 'face', 'unknown'
        
        if (bioManager.isAccessGranted) {
            // Already authorized, can be used
        } else {
            // Request authorization
            bioManager.requestAccess({reason: 'Need to verify identity'}, (success) => {
                if (success) {
                    console.log('Authorization successful');
                }
            });
        }
    }
});

// Perform authentication
bioManager.authenticate({reason: 'Confirm action'}, (success, token) => {
    if (success) {
        console.log('Authentication successful, token:', token);
    }
});
```

### Location and Sensors

**Get Location:**
```javascript
tg.LocationManager.init(() => {
    if (tg.LocationManager.isInited) {
        tg.LocationManager.getLocation((location) => {
            console.log('Latitude:', location.latitude);
            console.log('Longitude:', location.longitude);
        });
    }
});
```

**Accelerometer:**
```javascript
tg.Accelerometer.start({refresh_rate: 100}, (started) => {
    if (started) {
        tg.Accelerometer.onEvent((event) => {
            console.log('Acceleration:', event.x, event.y, event.z);
        });
    }
});

// Stop
tg.Accelerometer.stop();
```

**Gyroscope:**
```javascript
tg.Gyroscope.start({refresh_rate: 100}, callback);
tg.Gyroscope.onEvent((event) => {
    console.log('Rotation speed:', event.x, event.y, event.z);
});
```

**Device Orientation:**
```javascript
tg.DeviceOrientation.start({refresh_rate: 100}, callback);
tg.DeviceOrientation.onEvent((event) => {
    console.log('Orientation:', event.absolute, event.alpha, event.beta, event.gamma);
});
```

### Payment Integration

**Initiate a Payment (Telegram Stars):**
```javascript
tg.openInvoice('https://t.me/$invoice_link', (status) => {
    if (status === 'paid') {
        console.log('Payment successful');
    } else if (status === 'cancelled') {
        console.log('Payment cancelled');
    } else if (status === 'failed') {
        console.log('Payment failed');
    }
});
```

### Data Validation

**Server-side Validation of initData (Python):**
```python
import hmac
import hashlib
from urllib.parse import parse_qs

def validate_init_data(init_data, bot_token):
    # Parse the data
    parsed = parse_qs(init_data)
    received_hash = parsed.get('hash', [''])[0]
    
    # Remove the hash
    data_check_arr = []
    for key, value in parsed.items():
        if key != 'hash':
            data_check_arr.append(f"{key}={value[0]}")
    
    # Sort
    data_check_arr.sort()
    data_check_string = '\n'.join(data_check_arr)
    
    # Calculate the secret key
    secret_key = hmac.new(
        b"WebAppData",
        bot_token.encode(),
        hashlib.sha256
    ).digest()
    
    # Calculate the hash
    calculated_hash = hmac.new(
        secret_key,
        data_check_string.encode(),
        hashlib.sha256
    ).hexdigest()
    
    return calculated_hash == received_hash
```

### Launching a Mini App

**From a Keyboard Button:**
```python
keyboard = {
    "keyboard": [[ 
        {
            "text": "Open App",
            "web_app": {"url": "https://yourdomain.com/app"}
        }
    ]],
    "resize_keyboard": True
}

requests.post(
    f"{API_URL}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": "Click the button to open the app",
        "reply_markup": keyboard
    }
)
```

**From an Inline Button:**
```python
keyboard = {
    "inline_keyboard": [[
        {
            "text": "Launch App",
            "web_app": {"url": "https://yourdomain.com/app"}
        }
    ]]
}
```

**From the Menu Button:**
Talk to @BotFather:
```
/setmenubutton
→ Choose your Bot
→ Provide URL: https://yourdomain.com/app
```

## Client Development (TDLib)

### Using TDLib

**Python Example (python-telegram):**
```python
from telegram.client import Telegram

tg = Telegram(
    api_id='your_api_id',
    api_hash='your_api_hash',
    phone='+1234567890',
    database_encryption_key='changeme1234',
)

tg.login()

# Send a message
result = tg.send_message(
    chat_id=123456789,
    text='Hello from TDLib!'
)

# Get chat list
result = tg.get_chats()
result.wait()
chats = result.update

print(chats)

tg.stop()
```

### MTProto Protocol

**Features:**
- End-to-end encryption
- High performance
- Supports all Telegram features
- Requires API ID/Hash (from https://my.telegram.org)

## Best Practices

### Bot Development

1.  **Error Handling**
    ```python
    try:
        response = requests.post(url, json=data, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    ```

2.  **Rate Limiting**
    -   Group messages: max 20/minute
    -   Private messages: max 30/second
    -   Global limits: avoid being too frequent

3.  **Use Webhooks instead of Long Polling**
    -   More efficient
    -   Lower latency
    -   Better scalability

4.  **Data Validation**
    -   Always validate initData
    -   Don't trust client-side data
    -   Server-side validation for all operations

### Mini Apps Development

1.  **Responsive Design**
    ```javascript
    // Listen for theme changes
    tg.onEvent('themeChanged', () => {
        document.body.style.backgroundColor = tg.themeParams.bg_color;
    });
    
    // Listen for viewport changes
    tg.onEvent('viewportChanged', () => {
        console.log('New height:', tg.viewportHeight);
    });
    ```

2.  **Performance Optimization**
    -   Minimize JavaScript bundle size
    -   Use lazy loading
    -   Optimize images and resources

3.  **User Experience**
    -   Adapt to dark/light themes
    -   Use native UI controls (MainButton, etc.)
    -   Provide haptic feedback
    -   Respond quickly to user actions

4.  **Security Considerations**
    -   HTTPS is mandatory
    -   Validate initData
    -   Don't store sensitive information on the client
    -   Use SecureStorage for secrets

## Common Libraries and Tools

### Python
- `python-telegram-bot` - A powerful Bot framework
- `aiogram` - An asynchronous Bot framework
- `telethon` / `pyrogram` - MTProto clients

### Node.js
- `node-telegram-bot-api` - Bot API wrapper
- `telegraf` - Modern Bot framework
- `grammy` - Lightweight framework

### Other Languages
- PHP: `telegram-bot-sdk`
- Go: `telegram-bot-api`
- Java: `TelegramBots`
- C#: `Telegram.Bot`

## Reference Resources

### Official Documentation
- Bot API: https://core.telegram.org/bots/api
- Mini Apps: https://core.telegram.org/bots/webapps
- Mini Apps Platform: https://docs.telegram-mini-apps.com
- Telegram API: https://core.telegram.org

### GitHub Repositories
- Bot API Server: https://github.com/tdlib/telegram-bot-api
- Android Client: https://github.com/DrKLO/Telegram
- Desktop Client: https://github.com/telegramdesktop/tdesktop
- Official Organization: https://github.com/orgs/TelegramOfficial/repositories

### Tools
- @BotFather - Create and manage Bots
- https://my.telegram.org - Get API ID/Hash
- Telegram Web App test environment

## Reference Files

This skill includes a detailed index of Telegram development resources and complete implementation templates:

- **index.md** - A complete index of resources and quick navigation
- **Telegram_Bot_按钮和键盘实现模板.md** - An implementation guide for interactive buttons and keyboards (404 lines, 12 KB)
  - Detailed explanation of three button types (Inline/Reply/Command Menu)
  - Comparison of implementations with python-telegram-bot and Telethon
  - Complete ready-to-use code examples and project structure
  - Handler system, error handling, and deployment方案
- **动态视图对齐实现文档.md** - A guide to data display in Telegram (407 lines, 12 KB)
  - Intelligent dynamic alignment algorithm (three-step method, O(n×m) complexity)
  - Perfect alignment solution for monospaced font environments
  - Intelligent numerical formatting system (automatic B/M/K abbreviation)
  - Professional display for leaderboards and data tables

These concise guides provide core solutions for Telegram Bot development:
- All implementation methods for button and keyboard interaction
- Professional formatting and display of messages and data
- Practical best practices and quick references

---

**Master full-stack development of the Telegram ecosystem with this skill!**