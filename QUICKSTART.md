# ⚡ Quick Start Guide

Get your Startup Radar Bot up and running in 10 minutes!

## 📋 Prerequisites

- Python 3.9+ installed
- Git installed
- Accounts on:
  - [Vercel](https://vercel.com) (free)
  - [Handelsregister.ai](https://handelsregister.ai) (500 free credits)
  - [Make.com](https://www.make.com) (optional - for automation)

---

## 🚀 Step 1: Local Testing with Mock API

### Clone the Repository

```bash
git clone https://github.com/your-username/startup-radar-bot.git
cd startup-radar-bot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Mock Server

```bash
python api/mock_scan.py
```

You should see:
```
🚀 Startup Radar Bot - Mock API Server
Server running on http://localhost:8000
```

### Test the Mock API

**In a new terminal:**

```bash
# Health check
curl http://localhost:8000/api/scan

# Test scan
curl -X POST http://localhost:8000/api/scan \
  -H "Authorization: Bearer test-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30,"max_results":5,"min_score":40}'
```

### Run Automated Tests

```bash
python test_mock_api.py
```

Expected output:
```
✅ Health Check
✅ Basic Scan
✅ High Score Filter
...
PASSED: 6/6
```

---

## 🌐 Step 2: Deploy to Vercel

### Install Vercel CLI

```bash
npm i -g vercel
```

### Login to Vercel

```bash
vercel login
```

### Deploy

```bash
vercel --prod
```

Follow the prompts:
- **Set up and deploy?** → Yes
- **Which scope?** → Your account
- **Link to existing project?** → No
- **Project name?** → startup-radar-bot
- **Directory?** → `./` (press Enter)
- **Override settings?** → No

You'll get a URL like: `https://startup-radar-bot-xyz.vercel.app`

---

## 🔐 Step 3: Configure Environment Variables

### Generate Secure API Key

```bash
# On Mac/Linux
openssl rand -hex 32

# On Windows (PowerShell)
[Convert]::ToBase64String((1..32 | ForEach-Object { Get-Random -Maximum 256 }))
```

Copy the output (e.g., `1a581897-4e57-4dbf-bace-c618967d60fb`)

### Get Handelsregister.ai API Key

1. Go to [handelsregister.ai](https://handelsregister.ai)
2. Sign up for free account
3. Navigate to API settings
4. Copy your API key

### Add to Vercel

```bash
# Add API Key
vercel env add API_KEY
# Paste your generated key when prompted

# Add Handelsregister API Key
vercel env add HANDELSREGISTER_API_KEY
# Paste your handelsregister.ai key when prompted
```

### Redeploy with Environment Variables

```bash
vercel --prod
```

---

## ✅ Step 4: Test Production API

### Health Check

```bash
curl https://your-deployment.vercel.app/api/scan
```

Expected:
```json
{
  "status": "online",
  "service": "Startup Radar Bot",
  "version": "2.2.0 (Rotation)",
  ...
}
```

### Test Real Scan

```bash
curl -X POST https://your-deployment.vercel.app/api/scan \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"days_back":90,"max_results":5,"min_score":40}'
```

**⚠️ This will consume 5-10 API credits from Handelsregister.ai**

---

## 🤖 Step 5: Automate with Make.com (Optional)

### Create Make.com Account

1. Go to [make.com](https://www.make.com)
2. Sign up for free (1000 operations/month)

### Create New Scenario

1. Click **Create a new scenario**
2. Search for **Schedule** module
3. Configure:
   - **Interval:** Weekly
   - **Days:** Monday, Thursday
   - **Time:** 08:00

### Add HTTP Module

1. Click **+** → Search **HTTP**
2. Select **Make a request**
3. Configure:
   - **URL:** `https://your-deployment.vercel.app/api/scan`
   - **Method:** POST
   - **Headers:**
     ```
     Authorization: Bearer YOUR_API_KEY
     Content-Type: application/json
     ```
   - **Body:**
     ```json
     {
       "days_back": 7,
       "max_results": 30,
       "min_score": 40
     }
     ```

### Add Iterator

1. Click **+** → **Iterator**
2. **Array:** `{{results}}`

### Add Google Sheets

1. Click **+** → **Google Sheets**
2. Select **Add a row**
3. Map fields from iterator output
4. Save scenario

### Test & Activate

1. Click **Run once** to test
2. Check Google Sheets for results
3. Click **ON** to activate

---

## 📊 What's Next?

### Monitor Usage

- **Vercel:** Check deployment logs at [vercel.com/dashboard](https://vercel.com/dashboard)
- **Handelsregister.ai:** Monitor API credits in your dashboard
- **Make.com:** View scenario execution history

### Customize Scoring

Edit `api/scan.py` to adjust:
- City priorities
- Keyword weights
- Score thresholds

### Add Features

- Email enrichment (Hunter.io)
- LinkedIn scraping (Phantombuster)
- Notion integration
- Custom webhooks

### Join Community

- Report issues on GitHub
- Share improvements
- Request features

---

## 🆘 Troubleshooting

### Mock Server Won't Start

```bash
# Check if port is in use
lsof -i :8000

# Use different port
python -c "from api.mock_scan import run_server; run_server(port=8001)"
```

### Vercel Deployment Fails

```bash
# Check Python version
python --version  # Should be 3.9+

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Try again
vercel --prod
```

### 401 Unauthorized on Production

- Verify API_KEY environment variable is set in Vercel
- Check Authorization header format: `Bearer YOUR_KEY`
- Regenerate API key if compromised

### No Results from Real API

- Check Handelsregister.ai API credits
- Increase `days_back` parameter (try 90 or 180)
- Lower `min_score` (try 20 instead of 40)
- Verify cities have new registrations

---

## 💰 Cost Breakdown

### Free Tier Limits

| Service | Free Tier | Estimated Monthly Cost |
|---------|-----------|------------------------|
| Vercel | Unlimited | €0 |
| Handelsregister.ai | 500 credits | €0-2 (if exceeded) |
| Make.com | 1000 operations | €0 |
| Google Sheets | Unlimited | €0 |

**Total: ~€0-2/month** for typical usage (2 scans/week)

### Paid Plans (Optional)

- **Handelsregister.ai Pro:** €49/month (10,000 credits)
- **Make.com Core:** €9/month (10,000 operations)
- **Vercel Pro:** €20/month (unlimited deployments)

---

## 📚 Learn More

- [Full Documentation](README_EN.md)
- [Testing Guide](TESTING.md)
- [API Reference](README_EN.md#-api-reference)

---

**Ready to find your next startup lead? Let's go! 🚀**
