# 🌸 KawaiiGPT - Cute AI Chat Assistant 🌸

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-FF69B4?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Tkinter-GUI-FFB6D9?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/GPT-Powered-D5A6FF?style=for-the-badge&logo=openai&logoColor=white" alt="GPT">
  <img src="https://img.shields.io/badge/Style-Kawaii-A6E9FF?style=for-the-badge" alt="Kawaii">
</p>

<p align="center">
  <b>✨ Your adorable AI chat companion with a beautiful pastel interface ✨</b>
</p>

---

## 🎀 What is KawaiiGPT?

KawaiiGPT is a delightful desktop chat application that brings the power of AI conversation to your computer with a cute, Kawaii-inspired aesthetic. Designed for users who appreciate both functionality and beautiful design!

### Why You'll Love It

- 💖 **Adorable Interface** - Soft pastel colors that are easy on the eyes
- 🌈 **Mood Boosting** - Chatting has never been this cute!
- 🧠 **Powerful AI** - Advanced language model integration
- 📝 **Full-Featured** - Complete chat management system
- 🔒 **Secure** - Encrypted communication and local storage

## ✨ Features

### Beautiful UI Design

| Color | Hex | Usage |
|-------|-----|-------|
| 🌸 Primary | `#FFB6D9` | Headers, accents |
| 💜 Secondary | `#D5A6FF` | Sidebar, highlights |
| 💙 Accent | `#A6E9FF` | Focus indicators |
| 🤍 Background | `#FFF0F7` | Main background |
| 💕 Button | `#FF9ACF` | Interactive elements |

### Core Features

- 💬 **Smart Chat Interface**
  - Real-time AI responses
  - Message history
  - Typing indicators
  - Emoji support

- 📂 **Chat Management**
  - New chat creation
  - Save conversations
  - Export/Import functionality
  - Chat history browser

- ⚙️ **Customization**
  - Model selection
  - Temperature control
  - Response length settings
  - Theme options

- 🔧 **Developer Tools**
  - API integration
  - Custom prompts
  - Debug mode
  - Logging system

### Menu Structure

```
📁 File                    ✏️ Edit
├── New Chat               ├── Copy
├── Open History           ├── Paste
├── Save Chat              ├── Clear Chat
├── ─────────              └── Settings
├── Export                 
├── Import                 🤖 Model
└── Exit                   ├── Select Model
                           ├── Model Settings
❓ Help                    └── Download Models
├── Documentation
├── API Reference
├── Check Updates
└── About
```

## 📷 Preview

```
┌─────────────────────────────────────────────────────────────────┐
│  🌸 KawaiiGPT 🌸              Your Kawaii AI Assistant ✨  🟢   │
├───────────────┬─────────────────────────────────────────────────┤
│ 💫 Controls   │                                                 │
│               │  ┌─────────────────────────────────────────┐   │
│ [New Chat]    │  │ 🤖 KawaiiGPT                            │   │
│ [Settings]    │  │ Hello! How can I help you today? ♡     │   │
│ [History]     │  │                                         │   │
│               │  │ 👤 You                                  │   │
│ ─────────     │  │ What's the weather like?                │   │
│               │  │                                         │   │
│ Model:        │  │ 🤖 KawaiiGPT                            │   │
│ [GPT-4 ▼]     │  │ I'd be happy to help! Let me check...  │   │
│               │  └─────────────────────────────────────────┘   │
│ Temperature:  │                                                 │
│ [====0.7===]  │  ┌─────────────────────────────────┐ [Send 💕] │
│               │  │ Type your message here...       │           │
│ Max Tokens:   │  └─────────────────────────────────┘           │
│ [2048]        │                                                 │
├───────────────┴─────────────────────────────────────────────────┤
│  Status: Connected ✓                        Messages: 4         │
└─────────────────────────────────────────────────────────────────┘
```
## **Setup Instructions:** 
The following guide is for manual installation on Windows and macOS. Alternatively, macOS users can install via the [DMG download](../../releases).

## 🚀 Installation

### Requirements

- Python 3.8 or higher
- Tkinter (usually included with Python)
- Internet connection for AI features

### Quick Start

```bash
# Clone the repository
git clone https://github.com/unknown-person00lie/KawaiiGPT.git
cd KawaiiGPT

# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch the application
python main.py
```

### Dependencies

```
requests          # HTTP client
urllib3           # URL handling
cryptography      # Secure encryption
pycryptodome      # Crypto primitives
python-dateutil   # Date utilities
pytz              # Timezone support
colorama          # Terminal colors
numpy             # Numerical operations
torch             # Deep learning (optional)
transformers      # Model inference (optional)
openai            # OpenAI API client
```

## 📖 Usage Guide

### Getting Started

1. **Launch Application**
   ```bash
   python main.py
   ```

2. **Configure API Key**
   - Go to `Edit → Settings`
   - Enter your API key
   - Click "Save"

3. **Start Chatting!**
   - Type your message in the input box
   - Click "Send 💕" or press Enter
   - Wait for the cute AI response!

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Send message |
| `Ctrl+N` | New chat |
| `Ctrl+S` | Save chat |
| `Ctrl+O` | Open history |
| `Ctrl+C` | Copy selected |
| `Ctrl+V` | Paste |
| `Ctrl+Q` | Exit |

### Chat Tips

- 💡 Use clear, specific questions for better responses
- 🔄 Click "New Chat" to start fresh conversations
- 💾 Save important conversations for later reference
- 📤 Export chats as JSON or text files

## 🏗️ Project Structure

```
KawaiiGPT/
├── main.py                    # Application entry point
├── requirements.txt           # Dependencies
├── ai_engine/
│   ├── __init__.py
│   ├── gpt_client.py         # API client implementation
│   ├── model_loader.py       # Model management
│   └── prompt_handler.py     # Prompt engineering
├── core/
│   ├── __init__.py
│   ├── config.py             # App configuration
│   ├── database.py           # Local storage
│   └── session.py            # Session management
├── ui/
│   ├── __init__.py
│   ├── main_window.py        # Main GUI window
│   ├── chat_widget.py        # Chat display widget
│   └── settings_dialog.py    # Settings interface
├── utils/
│   ├── __init__.py
│   ├── logger.py             # Logging utilities
│   ├── network.py            # Network helpers
│   └── validator.py          # Input validation
└── logs/                     # Application logs
```

## ⚙️ Configuration

### Available Models

| Model | Description | Best For |
|-------|-------------|----------|
| kawaii-gpt-4-turbo | Latest & most capable | General chat |
| kawaii-gpt-3.5 | Fast & efficient | Quick responses |
| kawaii-local | Offline model | Privacy-focused |

### Settings Options

```python
settings = {
    'model': 'kawaii-gpt-4-turbo',
    'temperature': 0.7,        # 0.0 - 1.0 (creativity)
    'max_tokens': 2048,        # Response length
    'top_p': 1.0,             # Nucleus sampling
    'frequency_penalty': 0.0,  # Repetition control
    'presence_penalty': 0.0    # Topic diversity
}
```

## 🔒 Security Features

- 🔐 API key encryption
- 🛡️ Secure HTTPS communication
- ✅ Request signature verification
- 🔏 Local data encryption
- 📋 No telemetry or tracking

## 🤝 Contributing

We welcome kawaii contributions! 

1. 🍴 Fork the repository
2. 🌿 Create feature branch (`git checkout -b feature/kawaii-feature`)
3. ✨ Make your changes
4. ✅ Test thoroughly
5. 📝 Commit (`git commit -m 'Add kawaii feature'`)
6. 📤 Push (`git push origin feature/kawaii-feature`)
7. 💖 Open Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use type hints where possible
- Write descriptive docstrings
- Keep functions small and focused

## 🐛 Troubleshooting

### Application won't start?

```bash
# Ensure Tkinter is installed
python -c "import tkinter; print('OK')"

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Can't connect to API?

- Check internet connection
- Verify API key is correct
- Check firewall settings

### Slow responses?

- Try a faster model (GPT-3.5)
- Reduce max_tokens setting
- Check network speed

## 📄 License

This project is licensed under the MIT License.

## 💖 Acknowledgments

- OpenAI for language model technology
- Python Tkinter community
- All our kawaii contributors!

---

<p align="center">
  <b>Made with 💖 by the KawaiiGPT Team</b>
  <br><br>
  ⭐ Star if you think AI can be cute! ⭐
  <br>
  <sub>🌸 Spread the kawaii vibes 🌸</sub>
</p>