# 🚀 Startup Radar Bot

> **Automated startup discovery system for the German market** - Find, score, and analyze newly registered German startups with AI-powered insights.

[![Vercel](https://img.shields.io/badge/deployed%20on-Vercel-black?style=flat&logo=vercel)](https://vercel.com)
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

**Startup Radar Bot** automatically scans the German commercial register (Handelsregister) for newly registered tech startups across 10 major German cities. It uses AI to analyze business potential and generates outreach-ready data for sales, investment, or partnership opportunities.

**Perfect for:**
- 🏢 B2B SaaS companies targeting early-stage startups
- 💼 Business consultants and agencies
- 💰 Angel investors and VCs
- 📊 Market researchers

**Coverage:** Berlin, München, Hamburg, Frankfurt, Darmstadt, Köln, Stuttgart, Düsseldorf, Leipzig, Karlsruhe

---

## ✨ Features

### 🔍 **Smart Discovery**
- Automated scanning of German Handelsregister via [handelsregister.ai](https://handelsregister.ai)
- Rotating coverage: 5 cities per week (Group A/B rotation)
- Filters by legal form (GmbH, UG, AG) and tech keywords
- Configurable lookback periods (30-365 days)

### 🎯 **AI-Powered Scoring**
- **0-100 relevance score** based on:
  - Company age (30 points) - Fresher startups score higher
  - Tech keywords (25 points) - Software, AI, SaaS, FinTech, etc.
  - Regional priority (20 points) - Major tech hubs prioritized
  - Legal form (10 points) - GmbH/UG preferred
  - Business description quality (15 points)

### 🤖 **Claude AI Integration**
- Automatic pain point analysis
- Business challenge identification
- Industry-specific insights
- Personalized outreach recommendations

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
│   Scheduler     │     Group A: Even weeks | Group B: Odd weeks
└────────┬────────┘
         │
         ↓ HTTP POST
┌─────────────────────────────────────────┐
│   Vercel Serverless API                 │
│   /api/scan                             │
│                                         │
│   1. Determine city group (A or B)      │
│   2. Search Handelsregister (5 cities)  │
│   3. Calculate relevance scores         │
│   4. Filter & rank startups             │
│   5. Return JSON                        │
└────────┬────────────────────────────────┘
         │
         ↓ JSON Response (top 30)
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

**City Rotation System:**
- **Week 2, 4, 6...** (Even) → Group A: Berlin, München, Hamburg, Frankfurt, Darmstadt
- **Week 1, 3, 5...** (Odd) → Group B: Köln, Stuttgart, Düsseldorf, Leipzig, Karlsruhe

---

## 🚀 Quick Start

### Prerequisites

- [Vercel Account](https://vercel.com) (free tier)
- [Make.com Account](https://www.make.com) (free - 1000 operations/month)
- [Handelsregister.ai API Key](https://handelsregister.ai) (500 free credits/month)
- [Anthropic API Key](https://console.anthropic.com) (optional - for AI analysis)

### 1. Deploy to Vercel

**Option A: One-Click Deploy**

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fyour-username%2Fstartup-radar-bot)

**Option B: Manual Deploy**

```bash
# Clone repository
git clone https://github.com/your-username/startup-radar-bot.git
cd startup-radar-bot

# Install Vercel CLI
npm i -g vercel

# Deploy
vercel login
vercel --prod
```

### 2. Set Environment Variables

In your Vercel project dashboard, add these environment variables:

```bash
# API Key for Make.com authentication (generate a secure random key)
API_KEY=your_secure_random_api_key_here

# Handelsregister.ai API Key (get from https://handelsregister.ai)
HANDELSREGISTER_API_KEY=your_handelsregister_api_key
```

**Generate a secure API key:**
```bash
# On Mac/Linux
openssl rand -hex 32

# Or use a password generator
# Example: 1a581897-4e57-4dbf-bace-c618967d60fb
```

### 3. Test the API

```bash
# Health check (no authentication required)
curl https://your-deployment.vercel.app/api/scan

# Test scan with authentication
curl -X POST https://your-deployment.vercel.app/api/scan \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "days_back": 90,
    "max_results": 10,
    "min_score": 40
  }'
```

### 4. Setup Make.com Automation

1. **Create a new scenario in Make.com**
2. **Add a Schedule trigger** (twice per week: Monday + Thursday, 8:00 AM)
3. **Add HTTP module** with POST request to your Vercel endpoint
4. **Add Iterator** to process results
5. **Add Google Sheets** module to save data
6. **(Optional) Add Anthropic Claude** module for AI analysis

For detailed setup instructions, see the [Documentation](#-documentation) section.

---

## 📚 Documentation

### Mock API for Testing

For local development and testing without consuming API credits, use the included mock API:

```bash
# Start mock server
python api/mock_scan.py

# Test mock endpoint
curl -X POST http://localhost:8000/api/scan \
  -H "Authorization: Bearer test-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30,"max_results":5,"min_score":20}'
```

The mock API returns realistic sample data without making real API calls to Handelsregister.ai.

### Project Structure

```
startup-radar-bot/
├── api/
│   ├── scan.py           # Main serverless function
│   └── mock_scan.py      # Mock API for testing
├── .env.example          # Environment variables template
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
├── README.md            # German documentation
├── README_EN.md         # English documentation (this file)
└── LICENSE              # MIT License
```

---

## 🛠 Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Python 3.9+ | Serverless function |
| **Hosting** | Vercel | Serverless deployment |
| **Data Source** | Handelsregister.ai | German company registry API |
| **Automation** | Make.com | Workflow orchestration |
| **AI Analysis** | Anthropic Claude 4.5 | Pain point identification |
| **Storage** | Google Sheets | Data management & CRM |

---

## 📡 API Reference

### Base URL

```
https://your-deployment.vercel.app/api/scan
```

### Authentication

All POST requests require Bearer token authentication:

```bash
Authorization: Bearer YOUR_API_KEY
```

### Endpoints

#### `GET /api/scan`

Health check endpoint - returns service status and current city rotation group.

**Response:**
```json
{
  "status": "online",
  "service": "Startup Radar Bot",
  "version": "2.2.0 (Rotation)",
  "coverage": "5 cities per run",
  "current_week": 3,
  "current_group": "B",
  "timestamp": "2025-01-18T20:00:00"
}
```

#### `POST /api/scan`

Main scanning endpoint for startup discovery.

**Request Body:**
```json
{
  "days_back": 90,       // Optional: Days to look back (default: 30)
  "max_results": 20,     // Optional: Max startups to return (default: 30)
  "min_score": 40        // Optional: Min relevance score (default: 20)
}
```

**Response:**
```json
{
  "success": true,
  "timestamp": "2025-01-18T20:00:00",
  "count": 15,
  "results": [
    {
      "startup_id": "abc123def456",
      "created_at": "2025-01-18T20:00:00",
      "processed": false,
      "relevance_score": 85,
      "tags": "Berlin,Software,KI/AI",
      "startup_name": "TechVision AI GmbH",
      "legal_name": "TechVision AI GmbH",
      "website": "https://techvision.ai",
      "linkedin_company_url": "",
      "country": "DE",
      "city": "Berlin",
      "industry": "Tech",
      "sub_industry": "Software, KI/AI",
      "founded_year": "2025",
      "stage": "Pre-Seed",
      "handelsregister_source": "handelsregister.ai",
      "handelsregister_id": "HRB123456",
      "short_description": "Development of AI-powered enterprise software solutions for process automation and data analytics...",
      "source": "RadarBot v2.2",
      "notes": "Priority: High, Score: 85",
      "founder_name": "",
      "founder_linkedin_url": ""
    }
  ]
}
```

### Response Schema

| Field | Type | Description |
|-------|------|-------------|
| `startup_id` | string | Unique identifier from Handelsregister |
| `created_at` | string | ISO timestamp of when record was created |
| `processed` | boolean | Processing status (always false on creation) |
| `relevance_score` | integer | 0-100 score based on multiple factors |
| `tags` | string | Comma-separated tags (City, Tech keywords) |
| `startup_name` | string | Company name |
| `legal_name` | string | Official legal name |
| `website` | string | Company website (if available) |
| `linkedin_company_url` | string | LinkedIn profile (empty - for enrichment) |
| `country` | string | Country code (always "DE") |
| `city` | string | Company location |
| `industry` | string | Primary industry (usually "Tech") |
| `sub_industry` | string | Specific tech categories |
| `founded_year` | string | Year of registration |
| `stage` | string | Company stage (usually "Pre-Seed") |
| `handelsregister_source` | string | Data source identifier |
| `handelsregister_id` | string | Official register number (e.g. HRB123456) |
| `short_description` | string | Business purpose (first 200 characters) |
| `source` | string | Data source version |
| `notes` | string | Priority level and scoring details |
| `founder_name` | string | Founder name (empty - for enrichment) |
| `founder_linkedin_url` | string | Founder LinkedIn (empty - for enrichment) |

---

## 💡 Use Cases

### 1. B2B Sales Pipeline
**Problem:** Finding newly registered tech companies manually is time-consuming.
**Solution:** Automated bi-weekly delivery of qualified leads with AI-analyzed pain points.

**Example:** A SaaS company targeting startups receives 20-30 new qualified leads every week, complete with relevance scores and business insights.

### 2. Investor Deal Flow
**Problem:** Missing early-stage investment opportunities in specific regions.
**Solution:** Bi-weekly scans with relevance scoring for quick filtering.

**Example:** A VC fund focusing on FinTech startups in Berlin receives alerts for all new FinTech registrations with scores above 70.

### 3. Market Research
**Problem:** Tracking startup ecosystem trends requires constant monitoring.
**Solution:** Historical data collection in Google Sheets for trend analysis.

**Example:** Research analyzing which tech sectors are growing fastest in different German cities over time.

### 4. Partnership Development
**Problem:** Identifying potential technology partners or acquisition targets.
**Solution:** Filtered results by tech keywords and business description analysis.

**Example:** An enterprise software company finding complementary startups for potential partnerships or acquisitions.

---

## 📊 Scoring System

Startups receive a **0-100 relevance score** based on:

### 1. Company Age (30 points)
- ≤30 days: **30 points** (Brand new)
- ≤90 days: **25 points** (Very fresh)
- ≤180 days: **15 points** (Recent)
- ≤365 days: **10 points** (This year)

### 2. Tech Keywords (25 points)
Each keyword match adds **2 points** (max 25):
- **Core Tech:** software, AI, SaaS, cloud, data, analytics, app, platform, digital, tech, engineering
- **Specialized:** FinTech, HealthTech, PropTech, EdTech, mobility, robotics, automation, blockchain, IoT, cybersecurity, machine learning

### 3. Regional Priority (20 points)
Based on tech ecosystem strength:
- Berlin: **20 points**
- München: **19 points**
- Hamburg: **18 points**
- Frankfurt: **17 points**
- Darmstadt: **17 points**
- Köln: **16 points**
- Stuttgart: **15 points**
- Karlsruhe: **14 points**
- Düsseldorf: **14 points**
- Leipzig: **13 points**

### 4. Legal Form (10 points)
- GmbH/UG (haftungsbeschränkt): **10 points**
- AG (Aktiengesellschaft): **8 points**

### 5. Description Quality (15 points)
- >50 characters: **15 points** (Detailed description)
- >20 characters: **10 points** (Basic description)

**Priority Levels:**
- 🔴 **High:** Score ≥70 (Highly relevant, immediate action)
- 🟡 **Medium:** Score ≥40 (Relevant, worth reviewing)
- 🟢 **Low:** Score <40 (Less relevant, optional)

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions

- [ ] Add more German cities
- [ ] Email finder integration (Hunter.io, Apollo)
- [ ] LinkedIn profile scraping (Phantombuster)
- [ ] Notion database sync
- [ ] Additional scoring factors (funding signals, team size)
- [ ] Multi-language support (English, German)
- [ ] Web dashboard with analytics
- [ ] Export to other CRMs (HubSpot, Salesforce)
- [ ] Webhook notifications for high-priority leads

---

## 📈 Roadmap

- [x] **v1.0** - Core functionality (Nov 2025)
- [x] **v2.0** - Multi-city expansion (10 cities)
- [x] **v2.2** - City rotation system (Dec 2025)
- [ ] **v2.3** - Email enrichment via Hunter.io/Apollo
- [ ] **v2.4** - LinkedIn automation with Phantombuster
- [ ] **v2.5** - Notion CRM integration
- [ ] **v3.0** - Web dashboard with analytics
- [ ] **v3.1** - Expand to Austria & Switzerland
- [ ] **v3.2** - Machine learning for score optimization

---

## 🔒 Security & Privacy

### API Security
- Bearer token authentication required for all write operations
- API keys stored as environment variables (never in code)
- Rate limiting via Handelsregister.ai (prevents abuse)

### Data Privacy
- Only publicly available company registry data is collected
- No personal data or GDPR-protected information
- All data sourced from official Handelsregister.ai API

### Environment Variables
Never commit sensitive data. Use `.env.example` as template:

```bash
# .env.example
API_KEY=your_secure_api_key_here
HANDELSREGISTER_API_KEY=your_handelsregister_api_key
```

Add your actual credentials to `.env` (git-ignored):

```bash
# .env (NOT committed to git)
API_KEY=1a581897-4e57-4dbf-bace-c618967d60fb
HANDELSREGISTER_API_KEY=sk-abc123def456...
```

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

- **Issues:** [GitHub Issues](https://github.com/your-username/startup-radar-bot/issues)
- **Discussions:** [GitHub Discussions](https://github.com/your-username/startup-radar-bot/discussions)

---

## 💼 Commercial Use

This project is open source (MIT License) and can be used commercially. However, please note:

- **Handelsregister.ai API** has usage limits (500 free credits/month)
- **Make.com** free tier allows 1000 operations/month
- **Anthropic Claude API** is pay-as-you-go

For high-volume commercial use, consider upgrading to paid tiers.

---

## 🌟 Show Your Support

If you find this project useful, please consider:

- ⭐ **Starring this repository**
- 🐦 **Sharing on social media**
- 🤝 **Contributing improvements**
- 💰 **Sponsoring development** (if you use it commercially)

---

**Built with ❤️ for the German startup ecosystem**

*Automated startup scouting for smart entrepreneurs, investors, and B2B companies*
