# ⚡ Skills Library

> Modular skills collection for AI-assisted development

---

## 📁 Directory Structure

```
skills/
├── 00-meta-skills/       # Meta skills (skills that generate skills)
│   └── claude-skills/    # Claude skills generator
├── 01-ai-tools/          # AI CLI tools
│   ├── claude-code-guide/
│   └── claude-cookbooks/
├── 02-databases/         # Database skills
│   ├── postgresql/
│   └── timescaledb/
├── 03-crypto/            # Cryptocurrency & quantitative trading
│   ├── ccxt/
│   ├── coingecko/
│   ├── cryptofeed/
│   ├── hummingbot/
│   └── polymarket/
└── 04-dev-tools/         # Development tools
    ├── telegram-dev/
    ├── twscrape/
    ├── snapdom/
    └── proxychains/
```

---

## 🗂️ Categories

### 00-meta-skills
Skills for generating other skills.
- **claude-skills**: Meta skill for creating new SKILL.md files

### 01-ai-tools
AI CLI tools and guides.
- **claude-code-guide**: Claude Code usage guide
- **claude-cookbooks**: Claude best practices

### 02-databases
Database-related skills.
- **postgresql**: PostgreSQL operations
- **timescaledb**: Time-series database

### 03-crypto
Cryptocurrency and quantitative trading.
- **ccxt**: Crypto exchange library
- **coingecko**: Market data API
- **cryptofeed**: Real-time data feeds
- **hummingbot**: Trading bot framework
- **polymarket**: Prediction markets

### 04-dev-tools
General development tools.
- **telegram-dev**: Telegram bot development
- **twscrape**: Twitter scraping
- **snapdom**: DOM snapshot tool
- **proxychains**: Proxy configuration

---

## 📖 Skill Format

Each skill follows this structure:
```
skill-name/
├── SKILL.md        # Main skill document
├── references/     # Reference materials
├── scripts/        # Utility scripts
└── assets/         # Images and resources
```

---

## 🔗 Related Resources

- [Prompts Library](../prompts/)
- [Documents](../documents/)
- [Main README](../../../README.md)

---

[← Back](../README.md)
