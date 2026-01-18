# 🚀 Startup Radar Bot

> **Automated German startup discovery with AI-powered scoring** - Find newly registered tech companies from the German commercial register (Handelsregister) with intelligent relevance scoring.

[![Live Demo](https://img.shields.io/badge/Live-Demo-green?style=for-the-badge)](https://startup-radar-bot-test.vercel.app/api/mock)
[![Vercel](https://img.shields.io/badge/Deployed_on-Vercel-black?style=flat&logo=vercel)](https://vercel.com)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python)](https://www.python.org/)

---

## 🎯 What It Does

Automatically scans the German **Handelsregister** (commercial register) for newly registered tech startups across 10 major cities, scores them by relevance (0-100), and delivers actionable leads for B2B sales, investment, or partnership opportunities.

**Perfect for:** B2B SaaS companies, angel investors, VCs, business consultants, market researchers.

---

## 🎮 Try It Now

### Live Demo API

```bash
# Health check
curl https://startup-radar-bot-test.vercel.app/api/mock

# Test scan
curl -X POST https://startup-radar-bot-test.vercel.app/api/mock \
  -H "Authorization: Bearer demo-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30,"max_results":5,"min_score":40}'
```

**🌐 Interactive Demo:** [https://startup-radar-bot-test.vercel.app](https://startup-radar-bot-test.vercel.app)

> 💡 The demo uses **sample data** (15 realistic German startups). The production version connects to the real [Handelsregister.ai API](https://handelsregister.ai).

---

## ✨ Features

### 🔍 **Smart Discovery**
- Automated scanning of German commercial register via [Handelsregister.ai](https://handelsregister.ai)
- 10 major German cities: Berlin, München, Hamburg, Frankfurt, Darmstadt, Köln, Stuttgart, Düsseldorf, Leipzig, Karlsruhe
- Rotating coverage: 5 cities per run (Group A/B weekly rotation)
- Filters by legal form (GmbH, UG, AG) and tech keywords

### 🎯 **AI-Powered Scoring (0-100)**
Each startup receives a relevance score based on:
- **Company Age** (30 pts) - Newer = Higher score
- **Tech Keywords** (25 pts) - Software, AI, SaaS, FinTech, etc.
- **Regional Priority** (20 pts) - Major tech hubs prioritized
- **Legal Form** (10 pts) - GmbH/UG preferred
- **Description Quality** (15 pts)

**Priority Levels:**
- 🔴 **High** (≥70) - Immediate action
- 🟡 **Medium** (≥40) - Worth reviewing
- 🟢 **Low** (<40) - Optional follow-up

### 🤖 **Full Automation**
- Make.com workflow orchestration
- Bi-weekly automatic scans (Monday + Thursday)
- Google Sheets data export
- Claude AI integration for pain point analysis
- Zero manual intervention

### 💰 **Cost-Effective**
- **~€2/month** operational costs
- Free tiers: Vercel, Make.com (1000 ops), Handelsregister.ai (500 credits)
- Serverless architecture - no infrastructure management

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python 3.9+ |
| **Hosting** | Vercel (Serverless) |
| **Data Source** | Handelsregister.ai API |
| **Automation** | Make.com |
| **AI Analysis** | Anthropic Claude 4.5 |
| **Storage** | Google Sheets |

---

## 🚀 Quick Start

### 1. Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FMutigen%2Fstartup-radar-bot-test)

Or manually:

```bash
# Clone repository
git clone https://github.com/Mutigen/startup-radar-bot-test.git
cd startup-radar-bot-test

# Deploy with Vercel CLI
npm i -g vercel
vercel --prod
```

### 2. Set Environment Variables (Production Only)

For the **production API** (`/api/scan`), add these in Vercel:

```bash
# API Key for Make.com authentication
API_KEY=your_secure_random_api_key

# Handelsregister.ai API Key
HANDELSREGISTER_API_KEY=your_handelsregister_api_key
```

> 💡 **Mock API** (`/api/mock`) doesn't need environment variables!

### 3. Test Your Deployment

```bash
# Health check
curl https://your-deployment.vercel.app/api/mock

# Test scan
curl -X POST https://your-deployment.vercel.app/api/mock \
  -H "Authorization: Bearer demo-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":60,"max_results":10,"min_score":40}'
```

---

## 📡 API Reference

### Base URL
```
https://your-deployment.vercel.app
```

### Endpoints

#### `GET /api/mock`
Health check - returns service status.

**Response:**
```json
{
  "status": "online",
  "service": "Startup Radar Bot (MOCK DEMO)",
  "version": "2.2.0 (Mock)",
  "current_group": "B",
  "note": "This is a DEMO API with sample data."
}
```

#### `POST /api/mock`
Scan for startups (demo data).

**Request:**
```json
{
  "days_back": 90,      // Days to look back (default: 30)
  "max_results": 10,    // Max startups (default: 30)
  "min_score": 40       // Min score (default: 20)
}
```

**Response:**
```json
{
  "success": true,
  "count": 5,
  "results": [
    {
      "startup_name": "TechVision AI GmbH",
      "city": "Berlin",
      "relevance_score": 85,
      "tags": "Berlin,Software,KI/AI",
      "founded_year": "2025",
      "short_description": "AI-powered enterprise software...",
      "handelsregister_id": "HRB234567"
    }
  ]
}
```

**Full schema:** See [API Documentation](TESTING.md)

---

## 💡 Use Cases

### 1. B2B Sales Pipeline
Automated weekly delivery of qualified tech startup leads with AI-analyzed pain points.

### 2. Investor Deal Flow
Bi-weekly scans with relevance scoring for quick filtering of early-stage investment opportunities.

### 3. Market Research
Historical data collection for startup ecosystem trend analysis.

### 4. Partnership Development
Identify potential technology partners or acquisition targets by keywords and business description.

---

## 🔄 How It Works

```
Make.com Scheduler
    ↓ (Monday + Thursday, 8:00 AM)
Vercel Serverless API (/api/scan)
    ↓ (Search 5 cities)
Handelsregister.ai API
    ↓ (Calculate scores, filter)
JSON Response (top 30)
    ↓ (Iterator)
Make.com → Claude AI Analysis
    ↓ (Pain points, insights)
Google Sheets (CRM)
```

**City Rotation:**
- **Even weeks** (2, 4, 6...): Group A (Berlin, München, Hamburg, Frankfurt, Darmstadt)
- **Odd weeks** (1, 3, 5...): Group B (Köln, Stuttgart, Düsseldorf, Leipzig, Karlsruhe)

---

## 📊 Sample Output

**Mock API returns 15 realistic startups:**

| City | Example Startups | Industries |
|------|-----------------|------------|
| Berlin | TechVision AI, RoboTech | AI, Robotics |
| München | CloudFlow, GreenEnergy | SaaS, GreenTech |
| Hamburg | DataMind, FoodTech | Analytics, FoodTech |
| Frankfurt | FinTech Innovations, InsurTech | FinTech, Insurance |
| Darmstadt | SmartLogistics, SmartCity | Logistics, IoT |

**Score Range:** 40-90 points  
**Registration Dates:** Oct 2024 - Jan 2025

---

## 🧪 Testing

### Local Mock Server

```bash
# Start mock API locally
python api/mock_scan.py

# Test locally
curl -X POST http://localhost:8000/api/scan \
  -H "Authorization: Bearer test-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30,"max_results":5,"min_score":40}'
```

### Automated Tests

```bash
# Run test suite
python test_mock_api.py

# Test deployed API
./test_deployment.sh https://your-deployment.vercel.app
```

---

## 📚 Documentation

- **[Testing Guide](TESTING.md)** - Complete testing documentation
- **[Quick Start](QUICKSTART.md)** - 10-minute setup guide
- **[API Reference](#api-reference)** - Endpoint documentation

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Ideas:**
- Add more regions (Austria, Switzerland)
- Email enrichment integration
- LinkedIn profile scraping
- Notion database sync
- Web dashboard with analytics

---

## 📈 Roadmap

- [x] **v1.0** - Core functionality (Nov 2025)
- [x] **v2.0** - Multi-city expansion (10 cities)
- [x] **v2.2** - City rotation system (Jan 2025)
- [ ] **v2.3** - Email enrichment (Hunter.io/Apollo)
- [ ] **v2.4** - LinkedIn automation (Phantombuster)
- [ ] **v3.0** - Web dashboard with analytics
- [ ] **v3.1** - Expand to Austria & Switzerland

---

## 💰 Cost Breakdown

| Service | Free Tier | Monthly Cost |
|---------|-----------|--------------|
| Vercel | Unlimited deployments | **€0** |
| Handelsregister.ai | 500 credits/month | **€0-2** |
| Make.com | 1000 operations | **€0** |
| Google Sheets | Unlimited | **€0** |
| **Total** | | **~€0-2/month** |

*For typical usage: 2 scans/week, 30 results per scan*

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

- **Issues:** [GitHub Issues](https://github.com/Mutigen/startup-radar-bot-test/issues)
- **Live Demo:** [https://startup-radar-bot-test.vercel.app](https://startup-radar-bot-test.vercel.app)

---

**Built with ❤️ by [MAMIKO](https://mamiko.dev) @ MUT-i-GEN**

*Automated startup scouting for smart entrepreneurs, investors, and B2B companies.*

---

⭐ **Star this repo if you find it useful!**
