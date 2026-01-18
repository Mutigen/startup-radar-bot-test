# 🚀 Git Setup - Schritt für Schritt

Folge diesen Commands **genau in dieser Reihenfolge**!

---

## ✅ **Schritt 1: Git Status prüfen**

```bash
cd ~/startup-radar-bot
git status
```

**Du solltest sehen:**
- Neue Dateien (grün/rot)
- Keine Konflikte

---

## 📝 **Schritt 2: Aktuelles Git-Repo entfernen (WICHTIG!)**

Da du das Projekt kopiert hast, hat es noch das alte Git-History.
Wir starten frisch:

```bash
# Altes .git Verzeichnis entfernen
rm -rf .git

# Neues Git initialisieren
git init

# Main Branch erstellen
git branch -M main
```

**✅ Jetzt hast du ein frisches Git-Repository ohne alte History!**

---

## 📦 **Schritt 3: Alle Dateien hinzufügen**

```bash
# Alle Dateien zum Staging hinzufügen
git add .

# Status prüfen (optional)
git status
```

**Du solltest sehen:**
```
Changes to be committed:
  new file:   .env.example
  new file:   .gitignore
  new file:   DEPLOY_MOCK.md
  new file:   DEPLOY_NOW.md
  ...
  new file:   api/mock.py
  new file:   api/scan.py
  ...
```

**⚠️ Wichtig:** Stelle sicher, dass `.env` NICHT dabei ist!
(Sollte von `.gitignore` ausgeschlossen sein)

---

## 💾 **Schritt 4: Ersten Commit erstellen**

```bash
git commit -m "Initial commit: Startup Radar Bot with Mock API

- Production API (api/scan.py) for real Handelsregister data
- Mock API (api/mock.py) for testing without API credits
- English documentation (README_EN.md)
- Deployment guides for Vercel
- Automated testing scripts
- Make.com integration ready"
```

---

## 🌐 **Schritt 5: GitHub Repository erstellen**

### **5a) Gehe zu GitHub:**
- Öffne: https://github.com/new
- **Repository name:** `startup-radar-bot` (oder anderer Name)
- **Description:** `Automated German startup discovery with AI-powered scoring`
- **Visibility:** Public (damit Arbeitgeber es sehen können)
- **❌ NICHT** "Initialize with README" anklicken!
- **❌ NICHT** .gitignore oder License hinzufügen!
- Klicke **"Create repository"**

### **5b) GitHub zeigt dir jetzt Commands:**

GitHub zeigt dir eine Seite mit Commands. **IGNORIERE die ersten Commands!**

Wir nutzen nur diese:

```bash
# Ersetze 'dein-username' mit deinem GitHub Username!
git remote add origin https://github.com/dein-username/startup-radar-bot.git

# Beispiel:
# git remote add origin https://github.com/levan/startup-radar-bot.git
```

---

## 🚀 **Schritt 6: Zu GitHub pushen**

```bash
# Push zu GitHub (main branch)
git push -u origin main
```

**Beim ersten Mal wirst du nach Login gefragt:**
- Username: [dein GitHub username]
- Password: **NICHT dein Passwort!** → Verwende einen **Personal Access Token**

### **Personal Access Token erstellen (falls noch nicht gemacht):**

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. "Generate new token (classic)"
3. Name: `Vercel Deployment`
4. Scopes: ✅ `repo` (voller Zugriff)
5. Generate token
6. **KOPIERE den Token sofort!** (erscheint nur einmal)
7. Nutze diesen Token als "Password" beim `git push`

**Oder einfacher:** Nutze GitHub Desktop oder GitHub CLI für automatischen Login.

---

## ✅ **Schritt 7: Verifizieren**

Gehe zu: `https://github.com/dein-username/startup-radar-bot`

**Du solltest sehen:**
- ✅ Alle Dateien
- ✅ README_EN.md wird angezeigt
- ✅ Ordner: `api/`
- ✅ Alle Markdown Docs

---

## 🎉 **Fertig!**

Dein Repository ist jetzt auf GitHub!

**Nächster Schritt:** Öffne `VERCEL_DASHBOARD.md` um es mit Vercel zu verbinden.

---

## 🔧 **Troubleshooting**

### **"Permission denied (publickey)"**
→ Nutze HTTPS statt SSH:
```bash
git remote set-url origin https://github.com/dein-username/startup-radar-bot.git
```

### **"Updates were rejected"**
→ Force push (OK bei neuem Repo):
```bash
git push -u origin main --force
```

### **".env file wird gepusht"**
→ Sollte nicht passieren! Prüfe:
```bash
git rm --cached .env
echo ".env" >> .gitignore
git add .gitignore
git commit -m "Fix: Ignore .env file"
git push
```

### **"Repository already exists"**
→ Lösche auf GitHub und erstelle neu, ODER nutze anderen Namen

---

## 📋 **Zusammenfassung der Commands:**

```bash
# 1. Git neu initialisieren
rm -rf .git
git init
git branch -M main

# 2. Dateien hinzufügen
git add .
git commit -m "Initial commit: Startup Radar Bot with Mock API"

# 3. GitHub verbinden (ersetze dein-username!)
git remote add origin https://github.com/dein-username/startup-radar-bot.git

# 4. Pushen
git push -u origin main
```

**Zeit:** ~5-10 Minuten

**Danach:** → `VERCEL_DASHBOARD.md` öffnen! 🚀
