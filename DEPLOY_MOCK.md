# 🚀 Mock API Deployment Guide

Deploy the mock API to Vercel so anyone can test it without installation!

---

## 🎯 Why Deploy Mock API?

✅ **For Employers:** They can test immediately in browser
✅ **No Installation:** Just send them a URL
✅ **No API Keys Needed:** Uses sample data
✅ **Professional:** Shows your deployment skills

---

## 📦 What You're Deploying

**File:** `api/mock.py`
- Mock version of the Startup Radar Bot
- 15 realistic German startup samples
- Same scoring logic as production
- **No API credits consumed**

---

## 🚀 Deployment Steps

### Option 1: Deploy Mock Only (Recommended for Demo)

This creates a separate deployment just for the mock API.

```bash
# 1. Make sure you're in the project directory
cd startup-radar-bot

# 2. Deploy to Vercel
vercel --prod

# When prompted:
# - Project name: startup-radar-bot-demo (or similar)
# - Directory: ./
# - Override settings: No
```

### Option 2: Deploy Both (Production + Mock)

The mock API will be available at `/api/mock` alongside your production API.

```bash
# Just deploy normally
vercel --prod
```

Your APIs will be:
- **Production:** `https://your-app.vercel.app/api/scan`
- **Mock Demo:** `https://your-app.vercel.app/api/mock`

---

## ✅ Test Your Deployment

### 1. Health Check

```bash
# Replace with your actual Vercel URL
curl https://your-app.vercel.app/api/mock
```

**Expected Response:**
```json
{
  "status": "online",
  "service": "Startup Radar Bot (MOCK DEMO)",
  "version": "2.2.0 (Mock)",
  "note": "This is a DEMO API with sample data...",
  "demo_usage": {
    "method": "POST",
    "headers": {
      "Authorization": "Bearer demo-key",
      "Content-Type": "application/json"
    },
    "body": {
      "days_back": 30,
      "max_results": 5,
      "min_score": 40
    }
  }
}
```

### 2. Test Scan

```bash
curl -X POST https://your-app.vercel.app/api/mock \
  -H "Authorization: Bearer demo-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30,"max_results":5,"min_score":40}'
```

**Expected:** JSON with 5 German startups

---

## 📧 Share with Employers

### Email Template

```
Subject: Startup Radar Bot - Live Demo

Hi [Name],

I've built an automated system that scans German company registries
for new tech startups and scores them with AI.

🔗 LIVE DEMO (no installation needed):
https://your-app.vercel.app/api/mock

Try it:
→ Open URL in browser for instructions
→ Or use curl:

curl -X POST https://your-app.vercel.app/api/mock \
  -H "Authorization: Bearer demo-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30,"max_results":5,"min_score":40}'

📖 Full Documentation:
https://github.com/your-username/startup-radar-bot

This demo uses sample data - the production version connects
to the real German Handelsregister API.

Best regards,
[Your Name]
```

---

## 🎨 Create a Demo Page (Optional)

Create a simple HTML page to showcase the API:

```html
<!-- Create: public/demo.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Startup Radar Bot - Demo</title>
    <style>
        body { font-family: Arial; max-width: 800px; margin: 50px auto; padding: 20px; }
        button { background: #0070f3; color: white; padding: 10px 20px; border: none; cursor: pointer; }
        pre { background: #f4f4f4; padding: 15px; overflow-x: auto; }
    </style>
</head>
<body>
    <h1>🚀 Startup Radar Bot - Live Demo</h1>
    <p>Click to test the API with sample data:</p>
    <button onclick="testAPI()">Test API</button>
    <div id="result"></div>

    <script>
        async function testAPI() {
            const response = await fetch('/api/mock', {
                method: 'POST',
                headers: {
                    'Authorization': 'Bearer demo-key',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    days_back: 30,
                    max_results: 5,
                    min_score: 40
                })
            });

            const data = await response.json();
            document.getElementById('result').innerHTML =
                '<h2>Results:</h2><pre>' + JSON.stringify(data, null, 2) + '</pre>';
        }
    </script>
</body>
</html>
```

---

## 🔍 Compare: Mock vs Production

| Feature | Mock API | Production API |
|---------|----------|----------------|
| **Endpoint** | `/api/mock` | `/api/scan` |
| **Auth** | Any Bearer token | Specific API key |
| **Data** | 15 samples | Real Handelsregister |
| **Cost** | €0 | ~€2/month |
| **Credits** | None used | Uses API credits |
| **Use Case** | Demo/Testing | Real leads |

---

## 📊 What Employers Will See

When they test your mock API, they'll see:

1. **Professional JSON Response:**
   - Clean data structure
   - Realistic German startup data
   - Proper HTTP status codes

2. **Smart Scoring System:**
   - 0-100 relevance score
   - Multiple scoring factors
   - Priority classification

3. **Production-Ready Code:**
   - Error handling
   - CORS support
   - Well-documented

4. **Technical Skills:**
   - Python/Vercel
   - API design
   - Data processing
   - Scoring algorithms

---

## 🎯 Best Practices

### DO:
✅ Include GitHub link in API response
✅ Add clear "DEMO DATA" labels
✅ Show usage examples in health check
✅ Keep mock data realistic

### DON'T:
❌ Remove demo labels (be transparent)
❌ Use same endpoint for mock and production
❌ Forget to test after deployment
❌ Share without testing first

---

## 🐛 Troubleshooting

### Deployment Fails

```bash
# Check Vercel logs
vercel logs

# Redeploy
vercel --prod --force
```

### 404 Not Found

Make sure `api/mock.py` exists and has the `handler` class.

### CORS Errors

The mock API includes CORS headers. If you still have issues:
- Check browser console
- Test with `curl` first
- Verify Vercel deployment

---

## 🚀 Quick Commands

```bash
# Deploy mock API
vercel --prod

# Get deployment URL
vercel ls

# View logs
vercel logs

# Test deployment
curl https://$(vercel ls --json | jq -r '.[0].url')/api/mock
```

---

## 📈 Next Steps

After deployment:

1. **Test thoroughly** with all endpoints
2. **Update GitHub README** with demo URL
3. **Share with employers** via email/LinkedIn
4. **Monitor usage** in Vercel dashboard

---

**Your Mock API is now live! 🎉**

Share it confidently - it shows real technical skills without exposing sensitive data.
