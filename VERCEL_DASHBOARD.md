# 🎯 Vercel Dashboard Deployment (OHNE CLI)

Schritt-für-Schritt Anleitung zum Deployen über das Vercel Dashboard.

---

## 📋 **Voraussetzungen**

✅ Projekt ist auf GitHub gepusht (siehe `GIT_SETUP.md`)
✅ Du hast einen Vercel Account (kostenlos: https://vercel.com/signup)

---

## 🚀 **Schritt 1: Vercel Account verbinden**

### **1a) Anmelden:**
- Gehe zu: https://vercel.com/login
- Klicke **"Continue with GitHub"**
- Authorisiere Vercel (Zugriff auf deine Repos)

### **1b) Falls schon eingeloggt:**
- Dashboard: https://vercel.com/dashboard
- Weiter zu Schritt 2

---

## 📦 **Schritt 2: Neues Projekt erstellen**

1. **Klicke:** "Add New..." → "Project"
   - Oder direkt: https://vercel.com/new

2. **Import Git Repository:**
   - Du siehst eine Liste deiner GitHub Repos
   - Suche: `startup-radar-bot`
   - Klicke **"Import"** daneben

3. **Falls Repo nicht sichtbar:**
   - Klicke "Adjust GitHub App Permissions"
   - Gib Vercel Zugriff auf das Repository
   - Gehe zurück und importiere

---

## ⚙️ **Schritt 3: Project Settings konfigurieren**

Du siehst jetzt ein Formular:

### **Framework Preset:**
```
Other
```
(Vercel erkennt Python automatisch)

### **Root Directory:**
```
./
```
(Projekt-Root, nicht ändern)

### **Build Command:**
```
[Leer lassen]
```
(Nicht nötig für Serverless Functions)

### **Output Directory:**
```
[Leer lassen]
```

### **Install Command:**
```
[Leer lassen]
```
(Vercel installiert aus requirements.txt automatisch)

---

## 🔐 **Schritt 4: Environment Variables (OPTIONAL)**

⚠️ **NUR für Production API (`/api/scan`) - NICHT für Mock API!**

Die Mock API (`/api/mock`) braucht KEINE Environment Variables!

**Wenn du auch Production API nutzen willst:**

1. **Klicke:** "Environment Variables" ausklappen

2. **Füge hinzu:**
   ```
   Name: API_KEY
   Value: [dein-generierter-key]
   ```
   (Generiere mit: `openssl rand -hex 32`)

3. **Füge hinzu:**
   ```
   Name: HANDELSREGISTER_API_KEY
   Value: [dein-handelsregister-key]
   ```

**Für Demo nur Mock API:** Überspringe diesen Schritt komplett! ✅

---

## 🚀 **Schritt 5: Deploy!**

1. **Klicke:** "Deploy" Button (unten rechts)

2. **Warte ~1-2 Minuten:**
   - Du siehst einen Build-Log
   - Fortschritt wird angezeigt
   - Es sollte durchlaufen: Building → Deploying → Ready

3. **Erfolg!** 🎉
   - Du siehst: "Congratulations!" oder "Your project is ready"
   - Deine URL erscheint: `https://startup-radar-bot-xyz.vercel.app`

---

## ✅ **Schritt 6: Testen**

### **6a) Im Browser:**

Öffne deine Deployment-URL:
```
https://startup-radar-bot-xyz.vercel.app/api/mock
```

**Du solltest sehen:**
```json
{
  "status": "online",
  "service": "Startup Radar Bot (MOCK DEMO)",
  ...
}
```

### **6b) Mit curl:**

```bash
# Ersetze mit deiner echten URL!
curl https://startup-radar-bot-xyz.vercel.app/api/mock

# Test Scan
curl -X POST https://startup-radar-bot-xyz.vercel.app/api/mock \
  -H "Authorization: Bearer demo-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30,"max_results":5,"min_score":40}'
```

### **6c) Mit Test-Skript:**

```bash
# In deinem Projekt-Verzeichnis:
./test_deployment.sh https://startup-radar-bot-xyz.vercel.app
```

**Erwartete Ausgabe:**
```
✓ Health check passed
✓ Scan successful - Found 5 startups
✓ Filter test passed
✓ Authentication working
```

---

## 📝 **Schritt 7: Production Domain (optional)**

Vercel gibt dir automatisch:
- `https://startup-radar-bot-xyz.vercel.app`

**Willst du eine eigene Domain?**

1. Gehe zu: Project → Settings → Domains
2. Klicke "Add Domain"
3. Folge den Anweisungen

Für Demo/Arbeitgeber ist die Vercel-URL perfekt! ✅

---

## 🔄 **Automatische Updates**

**Das Beste:** Jeder Git Push deployed automatisch neu!

```bash
# Mache Änderungen in deinem Code
git add .
git commit -m "Update documentation"
git push

# Vercel deployed automatisch in ~1 Minute! 🚀
```

Du siehst alle Deployments im Vercel Dashboard.

---

## 📧 **Schritt 8: Mit Arbeitgeber teilen**

Kopiere deine Mock-API URL:
```
https://startup-radar-bot-xyz.vercel.app/api/mock
```

**Email-Template:**

```
Betreff: Startup Radar Bot - Live Demo

Hallo [Name],

ich habe ein automatisiertes System entwickelt, das neue Tech-Startups
aus dem deutschen Handelsregister scannt und mit AI bewertet.

🔗 LIVE DEMO (sofort im Browser testen):
https://startup-radar-bot-xyz.vercel.app/api/mock

Test-Befehl:
curl -X POST https://startup-radar-bot-xyz.vercel.app/api/mock \
  -H "Authorization: Bearer demo-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30,"max_results":5,"min_score":40}'

📖 Kompletter Code & Dokumentation:
https://github.com/dein-username/startup-radar-bot

Die Demo nutzt Beispieldaten. Die Produktions-Version
verbindet sich mit der echten Handelsregister.ai API.

Tech Stack:
✅ Python 3.9 + Vercel Serverless
✅ AI-basiertes Scoring (0-100)
✅ Make.com Automation
✅ ~€2/Monat Betriebskosten

Viele Grüße,
[Dein Name]
```

---

## 📊 **Dashboard Features**

Im Vercel Dashboard siehst du:

- **Deployments:** Alle Versionen
- **Analytics:** Wie oft wurde API aufgerufen
- **Logs:** Runtime Logs von deiner API
- **Domains:** URL-Verwaltung
- **Settings:** Environment Variables, etc.

---

## 🐛 **Troubleshooting**

### **"Build failed"**
→ Check Logs im Dashboard:
1. Klicke auf fehlgeschlagenes Deployment
2. Lies Build Log
3. Meist: Missing dependency in `requirements.txt`

**Fix:**
```bash
# Lokal:
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Fix: Update requirements.txt"
git push
```

### **"404 on /api/mock"**
→ Prüfe:
1. Ist `api/mock.py` im GitHub Repo?
2. Hat die Datei die `handler` Klasse?
3. Redeploy: Dashboard → Deployments → ... → Redeploy

### **"CORS Error"**
→ Sollte nicht passieren (Mock-API hat CORS)
→ Teste zuerst mit `curl` statt Browser

### **"Function timeout"**
→ Mock API ist schnell, sollte nicht passieren
→ Check Logs im Dashboard

---

## 🎯 **Zusammenfassung**

```
1. Vercel.com → Login with GitHub
2. Add New Project
3. Import "startup-radar-bot"
4. Framework: Other
5. Environment Variables: [Skip für Mock]
6. Deploy!
7. Teste: https://deine-url.vercel.app/api/mock
8. Teile mit Arbeitgeber! 🚀
```

**Zeit:** ~5 Minuten
**Kosten:** €0 (Free tier)
**Auto-Deploy:** Bei jedem Git Push ✅

---

## 🎉 **Geschafft!**

Deine Mock-API ist jetzt live und du kannst sie mit jedem teilen!

**Nächste Schritte:**
- ✅ README auf GitHub updaten mit Live-URL
- ✅ Email an Arbeitgeber schicken
- ✅ LinkedIn Post machen

---

## 📸 **Screenshots-Referenz**

Falls du visuelle Hilfe brauchst:

1. **Import Screen:**
   - "Import Git Repository" → Liste der Repos

2. **Configure Screen:**
   - Framework Preset Dropdown
   - Build/Output Command Felder
   - Environment Variables Section

3. **Deploy Screen:**
   - Build Log
   - Progress Bar
   - Success Confetti 🎊

4. **Dashboard:**
   - Deployments Liste
   - Visit Button → Deine Live-URL

---

**Viel Erfolg! 🚀**

Bei Problemen: Check die Vercel Docs oder die Logs im Dashboard.
