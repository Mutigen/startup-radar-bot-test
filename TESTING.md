# 🧪 Testing Guide

## Mock API Testing (No API Credits Required)

The mock API allows you to test the entire system without consuming Handelsregister.ai API credits.

### 1. Start Mock Server

```bash
# From project root
python api/mock_scan.py
```

The server will start on `http://localhost:8000`

### 2. Test Health Check

```bash
curl http://localhost:8000/api/scan
```

**Expected Response:**
```json
{
  "status": "online",
  "service": "Startup Radar Bot (MOCK)",
  "version": "2.2.0 (Mock)",
  "coverage": "5 cities per run",
  "current_week": 3,
  "current_group": "B",
  "timestamp": "2025-01-18T20:00:00",
  "note": "This is a mock API for testing. No real API calls are made."
}
```

### 3. Test Scan Endpoint

**Basic Test:**
```bash
curl -X POST http://localhost:8000/api/scan \
  -H "Authorization: Bearer test-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30,"max_results":5,"min_score":20}'
```

**High-Score Filter:**
```bash
curl -X POST http://localhost:8000/api/scan \
  -H "Authorization: Bearer test-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":90,"max_results":10,"min_score":60}'
```

**Long Lookback Period:**
```bash
curl -X POST http://localhost:8000/api/scan \
  -H "Authorization: Bearer test-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":365,"max_results":20,"min_score":30}'
```

### 4. Test with Python

Create a test script:

```python
# test_mock_api.py
import requests
import json

BASE_URL = "http://localhost:8000/api/scan"
API_KEY = "test-key"

def test_health_check():
    """Test health check endpoint"""
    response = requests.get(BASE_URL)
    print("Health Check:", json.dumps(response.json(), indent=2))
    return response.status_code == 200

def test_scan():
    """Test scan endpoint"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "days_back": 60,
        "max_results": 5,
        "min_score": 40
    }

    response = requests.post(BASE_URL, headers=headers, json=payload)
    data = response.json()

    print(f"\n✅ Found {data['count']} startups")
    print("\nTop Results:")
    for startup in data['results'][:3]:
        print(f"  - {startup['startup_name']} ({startup['city']}) - Score: {startup['relevance_score']}")

    return response.status_code == 200

if __name__ == "__main__":
    print("🧪 Testing Mock API\n")

    if test_health_check():
        print("✅ Health check passed\n")
    else:
        print("❌ Health check failed\n")

    if test_scan():
        print("\n✅ Scan test passed")
    else:
        print("\n❌ Scan test failed")
```

Run it:
```bash
python test_mock_api.py
```

---

## Production API Testing

### 1. Test with Vercel Deployment

**Health Check:**
```bash
curl https://your-deployment.vercel.app/api/scan
```

**Authenticated Scan:**
```bash
curl -X POST https://your-deployment.vercel.app/api/scan \
  -H "Authorization: Bearer YOUR_REAL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30,"max_results":5,"min_score":40}'
```

### 2. Test Make.com Integration

1. Set up a test scenario in Make.com
2. Add HTTP module pointing to mock API first
3. Test the entire workflow
4. Once working, switch to production API

---

## Mock Data Overview

The mock API includes 15 realistic German startups across 10 cities:

| City | Startups | Industries |
|------|----------|------------|
| Berlin | 2 | AI, Robotics |
| München | 2 | SaaS, GreenTech |
| Hamburg | 2 | Analytics, FoodTech |
| Frankfurt | 2 | FinTech, InsurTech |
| Darmstadt | 2 | Logistics, SmartCity |
| Köln | 1 | HealthTech |
| Stuttgart | 1 | Mobility |
| Düsseldorf | 1 | Cybersecurity |
| Leipzig | 1 | PropTech |
| Karlsruhe | 1 | EdTech |

**Registration Dates:** Between Oct 2024 - Jan 2025

**Score Range:** 40-90 (varies by keywords, city, age)

---

## Troubleshooting

### Mock Server Won't Start
```bash
# Check if port 8000 is already in use
lsof -i :8000

# Kill existing process
kill -9 <PID>

# Or use different port
python -c "from mock_scan import run_server; run_server(port=8001)"
```

### 401 Unauthorized Error
- Check that you're including `Authorization: Bearer <token>` header
- Token can be any value for mock API (e.g., "test-key")

### No Results Returned
- Check `days_back` parameter - mock data is from Oct 2024 - Jan 2025
- Lower `min_score` parameter (try 20-30)
- Increase `max_results` parameter

---

## CI/CD Testing

Add to your GitHub Actions workflow:

```yaml
# .github/workflows/test.yml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt

    - name: Start mock server
      run: |
        python api/mock_scan.py &
        sleep 2

    - name: Test API
      run: |
        curl -f http://localhost:8000/api/scan || exit 1
        curl -f -X POST http://localhost:8000/api/scan \
          -H "Authorization: Bearer test" \
          -H "Content-Type: application/json" \
          -d '{"days_back":30}' || exit 1
```

---

## Best Practices

1. **Always test with mock API first** before deploying to production
2. **Use version control** for your test scripts
3. **Document any issues** you find in GitHub Issues
4. **Test edge cases** (empty results, high scores, long lookbacks)
5. **Monitor API usage** in production to avoid exceeding limits

---

**Happy Testing! 🚀**
