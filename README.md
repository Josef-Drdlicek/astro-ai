# 🔮 Astro AI – Osobní astrologický průvodce

Interaktivní webová aplikace v Pythonu (Flask), která kombinuje astrologii a AI generování textů.  
Umožňuje zobrazit **denní horoskop, osobní výklad i detailní profil znamení** s důrazem na estetiku a plynulý UX.

---

## 🌠 Funkce

✨ **Denní horoskop pro všechna znamení** – generovaný pseudonáhodně na základě data a jména.  
🧠 **Personalizovaný výklad** – podle zadaného jména a životní oblasti (láska, práce, zdraví).  
🌈 **Kompletní profil znamení** – element, planeta, silné stránky, výzvy, afirmace a slavné osobnosti.  
🎨 **Moderní design** – čisté barvy, plynulé animace, responzivní layout.  
🪶 **Plně offline** – nevyužívá žádné API, běží lokálně přes Flask.

---

## 🖼️ Náhledy

| Domovská stránka | Detail znamení |
|------------------|----------------|

---

## 🧩 Instalace a spuštění

### 1️⃣ Klonování repozitáře
```bash
git clone https://github.com/Josef-Drdlicek/astro-ai.git
cd astro-ai
2️⃣ Aktivace virtuálního prostředí
bash
Zkopírovat kód
python -m venv .venv
.venv\Scripts\activate
3️⃣ Instalace závislostí
bash
Zkopírovat kód
pip install -r requirements.txt
4️⃣ Spuštění aplikace
bash
Zkopírovat kód
python run.py
Aplikace poběží na: 👉 http://127.0.0.1:5000

🏗️ Struktura projektu
csharp
Zkopírovat kód
astro-ai/
│
├── app/
│   ├── __init__.py          # Inicializace Flask aplikace
│   ├── routes.py            # Hlavní routy (home, sign detail)
│   ├── templates/           # HTML šablony (Jinja2)
│   ├── static/              # CSS, obrázky, fonty
│   └── services/
│       ├── horoscope.py     # Generování horoskopů
│       └── sign_profiles.py # Datový profil znamení
│
├── requirements.txt
├── run.py
└── README.md
⚙️ Použité technologie
🐍 Python 3.11+

🌐 Flask

🎨 HTML + CSS (Jinja2 templating)

🔢 Dataclasses & random

💫 Responzivní design, moderní UI

🌟 Budoucí plány
 Integrace s OpenAI API pro reálné AI výklady

 Ukládání uživatelských profilů (SQLite)

 Temný režim 🌙

 Sdílení denního horoskopu přes URL

 Export do PDF s osobní zprávou

👨‍💻 Autor
Josef Drdlíček
IT Consultant & AI Enthusiast
LinkedIn · GitHub

🧘‍♂️ „Astrologie není o předvídání budoucnosti. Je o porozumění sobě.“

yaml
Zkopírovat kód

---

Teď to jen dej:  
```bash
git add README.md
git commit -m "📝 Add README"
git push origin main
