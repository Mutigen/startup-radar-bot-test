# 🚀 Deploy Mock API NOW - Step by Step

Folge diesen Schritten, um deine Mock-API in 5 Minuten live zu bekommen!

---

## 📋 Voraussetzungen

- ✅ Du hast ein Vercel Account ([kostenlos anmelden](https://vercel.com))
- ✅ Du hast Git installiert
- ✅ Dein Code ist auf GitHub (oder lokal)

---

## 🎯 Zwei Deployment-Optionen

### Option A: Vercel Dashboard (Einfachste Methode) ⭐

**Perfekt wenn:** Du keine CLI installieren willst

1. **Gehe zu [vercel.com](https://vercel.com)**

2. **Klicke "Add New Project"**

3. **Import dein GitHub Repository:**
   - Wähle `startup-radar-bot`
   - Oder: Upload ZIP-Datei deines Projekts

4. **Configure Project:**
   ```
   Framework Preset: Other
   Root Directory: ./
   Build Command: (leave empty)
   Output Directory: (leave empty)
   ```

5. **Environment Variables (Optional):**
   - Für Mock-API NICHT nötig
   - Überspringe diesen Schritt

6. **Klicke "Deploy"** ✨

7. **Warte 1-2 Minuten**

8. **Fertig!** Du bekommst eine URL wie:
   ```
   https://startup-radar-bot-abc123.vercel.app
   ```

### Option B: Vercel CLI (Für Fortgeschrittene)

**Perfekt wenn:** Du CLI-Tools magst

```bash
# 1. Installiere Vercel CLI
npm i -g vercel

# 2. Login
vercel login

# 3. Gehe zu deinem Projekt
cd startup-radar-bot

# 4. Deploy
vercel --prod

# Folge den Prompts:
# - Set up and deploy? → Yes
# - Which scope? → [Dein Account]
# - Link to existing project? → No
# - Project name? → startup-radar-bot
# - Directory? → ./ (Enter drücken)
# - Override settings? → No

# Fertig! Du bekommst eine URL
```

---

## ✅ Nach dem Deployment

### 1. Test deine Deployment-URL

```bash
# Health Check
curl https://DEINE-URL.vercel.app/api/mock

# Voller Test
curl -X POST https://DEINE-URL.vercel.app/api/mock \
  -H "Authorization: Bearer demo-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30,"max_results":5,"min_score":40}'
```

### 2. Automatischer Test mit Skript

```bash
./test_deployment.sh https://DEINE-URL.vercel.app
```

Du solltest sehen:
```
✓ Health check passed
✓ Scan successful - Found 5 startups
✓ Filter test passed
✓ Authentication working
```

---

## 📧 Teile es mit deinem Arbeitgeber

### Template für Email/LinkedIn

```
Hallo [Name],

ich habe ein System entwickelt, das automatisch neue Tech-Startups
aus dem deutschen Handelsregister scannt und mit KI bewertet.

🔗 LIVE DEMO (sofort im Browser testen):
https://DEINE-URL.vercel.app/api/mock

Einfach ausprobieren:

curl -X POST https://DEINE-URL.vercel.app/api/mock \
  -H "Authorization: Bearer demo-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30,"max_results":5,"min_score":40}'

📖 Komplette Dokumentation & Code:
https://github.com/[username]/startup-radar-bot

Die Demo nutzt Beispieldaten - die Produktions-Version
verbindet sich mit der echten Handelsregister.ai API.

Features:
✅ 10 deutsche Städte Coverage
✅ AI-basiertes Scoring System (0-100)
✅ Make.com Workflow Automation
✅ ~€2/Monat Betriebskosten

Viele Grüße,
[Dein Name]
```

### Template für GitHub README

Füge das zu deiner README.md hinzu:

```markdown
## 🎮 Live Demo

Try the mock API without installation:

**Health Check:**
```bash
curl https://DEINE-URL.vercel.app/api/mock
```

**Test Scan:**
```bash
curl -X POST https://DEINE-URL.vercel.app/api/mock \
  -H "Authorization: Bearer demo-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30,"max_results":5,"min_score":40}'
```

**Live URL:** [https://DEINE-URL.vercel.app/api/mock](https://DEINE-URL.vercel.app/api/mock)
```

---

## 🔗 Beide APIs auf Vercel

Nach dem Deployment hast du:

| API | Endpoint | Zweck |
|-----|----------|-------|
| **Production** | `/api/scan` | Echte Daten, braucht API Keys |
| **Mock Demo** | `/api/mock` | Sample-Daten, keine Keys nötig |

**Für Arbeitgeber:** Immer `/api/mock` teilen!

---

## 🎨 Bonus: Schöne Demo-Seite erstellen

Erstelle `public/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Startup Radar Bot - Demo</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            background: white;
            border-radius: 15px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        h1 { color: #333; margin-bottom: 10px; }
        .subtitle { color: #666; margin-bottom: 30px; }
        button {
            background: #667eea;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
        }
        button:hover { background: #5568d3; transform: translateY(-2px); }
        button:disabled { background: #ccc; cursor: not-allowed; }
        .loader { display: none; margin: 20px 0; color: #667eea; }
        pre {
            background: #f5f5f5;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            margin-top: 20px;
            border-left: 4px solid #667eea;
        }
        .stats {
            display: flex;
            gap: 20px;
            margin: 20px 0;
        }
        .stat {
            flex: 1;
            background: #f9f9f9;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
        }
        .stat-value {
            font-size: 24px;
            font-weight: bold;
            color: #667eea;
        }
        .stat-label {
            color: #666;
            font-size: 12px;
            margin-top: 5px;
        }
        .badge {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            margin: 5px 5px 5px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Startup Radar Bot</h1>
        <p class="subtitle">AI-powered German startup discovery system</p>

        <button onclick="testAPI()" id="testBtn">
            🎯 Test API with Sample Data
        </button>

        <div class="loader" id="loader">Loading...</div>

        <div id="stats"></div>
        <div id="result"></div>

        <div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #eee;">
            <h3>📖 Resources</h3>
            <p style="margin: 10px 0;">
                <a href="https://github.com/your-username/startup-radar-bot"
                   style="color: #667eea;">View on GitHub</a>
            </p>
            <p style="color: #666; font-size: 14px;">
                Built with Python, Vercel, Make.com & Claude AI
            </p>
        </div>
    </div>

    <script>
        async function testAPI() {
            const btn = document.getElementById('testBtn');
            const loader = document.getElementById('loader');
            const result = document.getElementById('result');
            const stats = document.getElementById('stats');

            btn.disabled = true;
            loader.style.display = 'block';
            result.innerHTML = '';
            stats.innerHTML = '';

            try {
                const response = await fetch('/api/mock', {
                    method: 'POST',
                    headers: {
                        'Authorization': 'Bearer demo-key',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        days_back: 60,
                        max_results: 10,
                        min_score: 40
                    })
                });

                const data = await response.json();

                // Show stats
                const avgScore = data.results.reduce((sum, s) => sum + s.relevance_score, 0) / data.count;
                stats.innerHTML = `
                    <div class="stats">
                        <div class="stat">
                            <div class="stat-value">${data.count}</div>
                            <div class="stat-label">Startups Found</div>
                        </div>
                        <div class="stat">
                            <div class="stat-value">${Math.round(avgScore)}</div>
                            <div class="stat-label">Avg Score</div>
                        </div>
                        <div class="stat">
                            <div class="stat-value">${[...new Set(data.results.map(s => s.city))].length}</div>
                            <div class="stat-label">Cities</div>
                        </div>
                    </div>
                `;

                // Show results
                let html = '<h2>📊 Results</h2>';
                data.results.forEach((startup, i) => {
                    const tags = startup.tags.split(',');
                    const tagBadges = tags.map(t => `<span class="badge">${t}</span>`).join('');

                    html += `
                        <div style="margin: 20px 0; padding: 20px; background: #f9f9f9; border-radius: 8px;">
                            <h3>${i + 1}. ${startup.startup_name}</h3>
                            <p style="color: #666; margin: 10px 0;">${startup.short_description}</p>
                            <div>${tagBadges}</div>
                            <div style="margin-top: 10px; color: #888; font-size: 14px;">
                                <strong>Score:</strong> ${startup.relevance_score} |
                                <strong>City:</strong> ${startup.city} |
                                <strong>Founded:</strong> ${startup.founded_year}
                            </div>
                        </div>
                    `;
                });

                result.innerHTML = html;

            } catch (error) {
                result.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
            } finally {
                btn.disabled = false;
                loader.style.display = 'none';
            }
        }
    </script>
</body>
</html>
```

Dann ist deine Hauptseite eine schöne Demo: `https://DEINE-URL.vercel.app`

---

## 🎯 Checkliste vor dem Teilen

- [ ] Deployment erfolgreich
- [ ] Health Check funktioniert
- [ ] Scan Test funktioniert
- [ ] Test-Skript läuft durch
- [ ] GitHub Repository ist public
- [ ] README.md hat Demo-URL
- [ ] Email-Template vorbereitet

---

## 🚀 Los geht's!

1. **Deploy jetzt** (Option A oder B oben)
2. **Test deine URL** mit `test_deployment.sh`
3. **Update README** mit deiner Live-URL
4. **Teile mit Arbeitgeber** via Email/LinkedIn

**Du schaffst das! 💪**

Bei Problemen, check die Vercel Logs:
```bash
vercel logs
```

Oder im Dashboard: vercel.com → dein-projekt → Deployments → Logs
