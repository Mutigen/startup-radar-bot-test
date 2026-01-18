# 🚀 Startup Radar Bot

> **Automated startup discovery system for the Rhein-Main region** - Find, score, and analyze newly registered German startups with AI-powered insights.

[![Vercel](https://img.shields.io/badge/deployed%20on-Vercel-black?style=flat&logo=vercel)](https://radar.mamiko.dev)
[![Python](https://img.shields.io/badge/python-3.9+-blue?style=flat&logo=python)](https://www.python.org/)
[![Make.com](https://img.shields.io/badge/automation-Make.com-6B46C1?style=flat)](https://www.make.com)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat)](LICENSE)

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Quick Start](#-quick-start)
- [Documentation](#-documentation)
- [Tech Stack](#-tech-stack)
- [API Reference](#-api-reference)
- [Use Cases](#-use-cases)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**Startup Radar Bot** automatically scans the German commercial register (Handelsregister) for newly registered tech startups in the Rhein-Main region (Darmstadt, Frankfurt, Offenbach, Wiesbaden). It uses AI to analyze business potential and generates outreach-ready data for sales, investment, or partnership opportunities.

**Perfect for:**
- 🏢 B2B SaaS companies targeting early-stage startups
- 💼 Business consultants and agencies
- 💰 Angel investors and VCs
- 📊 Market researchers

**Live API:** [https://radar.mamiko.dev/api/scan](https://radar.mamiko.dev/api/scan)

---

## ✨ Features

### 🔍 **Smart Discovery**
- Automated scanning of German Handelsregister via [handelsregister.ai](https://handelsregister.ai)
- Filters by region, legal form (GmbH, UG, AG), and tech keywords
- Configurable lookback periods (30-365 days)

### 🎯 **AI-Powered Scoring**
- **0-100 relevance score** based on:
  - Company age (30 points)
  - Tech keywords (25 points)  
  - Regional priority (20 points)
  - Legal form (10 points)
  - Business description quality (15 points)

### 🤖 **Claude AI Integration**
- Automatic pain point analysis
- Business challenge identification
- Industry-specific insights

### 📊 **Full Automation**
- Make.com workflow orchestration
- Bi-weekly automatic scans (Monday + Thursday)
- Google Sheets data export
- Zero manual intervention required

### 💰 **Cost-Effective**
- ~€0.50-2/month operational costs
- Free tiers: Vercel, Make.com (1000 ops), Handelsregister.ai (500 credits)
- No infrastructure management

---

## 🔄 How It Works

```
┌─────────────────┐
│   Make.com      │  ← Triggers bi-weekly (Mon + Thu, 8:00 AM)
│   Scheduler     │
└────────┬────────┘
         │
         ↓ HTTP POST
┌─────────────────────────────────────────┐
│   Vercel Serverless API                 │
│   radar.mamiko.dev/api/scan             │
│                                         │
│   1. Search Handelsregister             │
│   2. Calculate relevance scores         │
│   3. Filter & rank startups             │
│   4. Return JSON                        │
└────────┬────────────────────────────────┘
         │
         ↓ JSON Response
┌─────────────────┐      ┌──────────────┐
│   Make.com      │─────→│ Claude AI    │
│   Iterator      │      │ Analysis     │
└────────┬────────┘      └──────┬───────┘
         │                      │
         ↓                      ↓
┌────────────────────────────────────────┐
│         Google Sheets                  │
│  ┌──────────────┐  ┌─────────────────┐│
│  │Startup_Radar │  │Outreach_Queue   ││
│  │(All Data)    │  │(AI Insights)    ││
│  └──────────────┘  └─────────────────┘│
└────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites

- [Vercel Account](https://vercel.com) (free)
- [Make.com Account](https://www.make.com) (free tier)
- [Handelsregister.ai API Key](https://handelsregister.ai) (500 free credits)
- [Anthropic API Key](https://console.anthropic.com) (pay-as-you-go)

### 1. Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FMutigen%2Fstartup-radar-bot)

Or manually:

```bash
# Clone repository
git clone https://github.com/Mutigen/startup-radar-bot.git
cd startup-radar-bot

# Install Vercel CLI
npm i -g vercel

# Deploy
vercel login
vercel --prod
```

### 2. Set Environment Variables

```bash
# API Key for Make.com authentication
vercel env add API_KEY
# Enter: your_secure_api_key

# Handelsregister.ai API Key
vercel env add HANDELSREGISTER_API_KEY  
# Enter: your_handelsregister_api_key
```

### 3. Test the API

```bash
# Health check
curl https://your-deployment.vercel.app/api/scan

# Test scan
curl -X POST https://your-deployment.vercel.app/api/scan \
  -H "Authorization: Bearer your_secure_api_key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":365,"max_results":5,"min_score":10}'
```

### 4. Setup Make.com Automation

See [📚 Full Documentation](DOCUMENTATION.md) for complete Make.com setup guide.

---

## 📚 Documentation

- **[Complete Documentation](DOCUMENTATION.md)** - Full setup guide with screenshots
- **[API Reference](#-api-reference)** - Endpoint documentation below
- **[Handelsregister.ai API](https://handelsregister.ai/api)** - Data source documentation

---

## 🛠 Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Python 3.9 | Serverless function |
| **Hosting** | Vercel | Serverless deployment |
| **Data Source** | Handelsregister.ai | German company registry |
| **Automation** | Make.com | Workflow orchestration |
| **AI Analysis** | Anthropic Claude 4.5 | Pain point identification |
| **Storage** | Google Sheets | Data management & CRM |

---

## 📡 API Reference

### Base URL

```
https://radar.mamiko.dev/api/scan
```

### Authentication

All POST requests require Bearer token authentication:

```bash
Authorization: Bearer YOUR_API_KEY
```

### Endpoints

#### `GET /api/scan`

Health check endpoint.

**Response:**
```json
{
  "status": "online",
  "service": "Startup Radar Bot",
  "version": "1.0.0",
  "timestamp": "2025-11-29T20:00:00"
}
```

#### `POST /api/scan`

Main scanning endpoint for startup discovery.

**Request Body:**
```json
{
  "days_back": 365,      // Optional: Days to look back (default: 30)
  "max_results": 10,     // Optional: Max startups (default: 20)
  "min_score": 10        // Optional: Min relevance score (default: 30)
}
```

**Response:**
```json
{
  "success": true,
  "timestamp": "2025-11-29T20:00:00",
  "count": 3,
  "results": [
    {
      "startup_id": "abc123...",
      "startup_name": "Example GmbH",
      "legal_name": "Example GmbH",
      "city": "Darmstadt",
      "founded_year": "2025",
      "relevance_score": 75,
      "tags": "Darmstadt,Software,KI/AI",
      "industry": "Tech",
      "sub_industry": "Software",
      "stage": "Pre-Seed",
      "handelsregister_id": "HRB123456",
      "short_description": "AI-powered software solutions...",
      "notes": "Priority: High, Score: 75, Region: Darmstadt",
      "website": "",
      "linkedin_company_url": "",
      "country": "DE",
      "handelsregister_source": "handelsregister.ai",
      "source": "RadarBot v1",
      "created_at": "2025-11-29T20:00:00",
      "processed": false,
      "founder_name": "",
      "founder_linkedin_url": ""
    }
  ]
}
```

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `startup_id` | string | Unique identifier (entity_id from Handelsregister) |
| `startup_name` | string | Company name |
| `city` | string | Company location |
| `founded_year` | string | Year of registration |
| `relevance_score` | integer | 0-100 score based on multiple factors |
| `tags` | string | Comma-separated tags (Region, Tech keywords) |
| `handelsregister_id` | string | Official register number (e.g. HRB123456) |
| `short_description` | string | Business purpose (first 200 chars) |
| `notes` | string | Priority level and scoring details |

---

## 💡 Use Cases

### 1. B2B Sales Pipeline
**Problem:** Finding newly registered tech companies manually is time-consuming.  
**Solution:** Automated weekly delivery of qualified leads with AI-analyzed pain points.

### 2. Investor Deal Flow
**Problem:** Missing early-stage investment opportunities in specific regions.  
**Solution:** Bi-weekly scans with relevance scoring for quick filtering.

### 3. Market Research
**Problem:** Tracking startup ecosystem trends requires constant monitoring.  
**Solution:** Historical data collection in Google Sheets for trend analysis.

### 4. Partnership Development
**Problem:** Identifying potential technology partners or acquisition targets.  
**Solution:** Filtered results by tech keywords and business description analysis.

---

## 📊 Scoring System

Startups receive a **0-100 relevance score** based on:

### 1. Company Age (30 points)
- ≤30 days: 30 points
- ≤90 days: 25 points
- ≤180 days: 15 points
- ≤365 days: 10 points

### 2. Tech Keywords (25 points)
- 3 points per keyword match
- Keywords: software, AI, SaaS, cloud, data, analytics, app, platform, digital, innovation, tech, engineering, logistics

### 3. Regional Priority (20 points)
- Darmstadt: 20 points
- Frankfurt: 15 points
- Offenbach: 12 points
- Wiesbaden: 10 points

### 4. Legal Form (10 points)
- GmbH/UG: 10 points
- AG: 8 points

### 5. Description Quality (15 points)
- >50 characters: 15 points
- >20 characters: 10 points

**Priority Levels:**
- 🔴 High: Score ≥70
- 🟡 Medium: Score ≥40
- 🟢 Low: Score <40

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions

- [ ] Add more regions (Berlin, München, Hamburg)
- [ ] Email finder integration
- [ ] LinkedIn profile scraping
- [ ] Notion database sync
- [ ] Additional scoring factors
- [ ] Multi-language support
- [ ] Web dashboard

---

## 📈 Roadmap

- [x] **v1.0** - Core functionality (Nov 2025)
- [ ] **v1.1** - Email enrichment via Hunter.io/Apollo
- [ ] **v1.2** - LinkedIn automation with Phantombuster
- [ ] **v1.3** - Notion CRM integration
- [ ] **v2.0** - Web dashboard with analytics
- [ ] **v2.1** - Multi-region expansion (DE, AT, CH)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Handelsregister.ai](https://handelsregister.ai) - German company registry API
- [Anthropic](https://www.anthropic.com) - Claude AI for analysis
- [Make.com](https://www.make.com) - Workflow automation
- [Vercel](https://vercel.com) - Serverless hosting

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/Mutigen/startup-radar-bot/issues)
- **Discussions:** [GitHub Discussions](https://github.com/Mutigen/startup-radar-bot/discussions)
- **Documentation:** [Complete Guide](DOCUMENTATION.md)

---

**Built with ❤️ by [MAMIKO](https://mamiko.dev) @ MUT-i-GEN**

*Automated startup scouting for smart entrepreneurs*

---

⭐ **Star this repo if you find it useful!**
