# 🏦 BawaBank 🇬🇭 — Ghana Fintech Demo Bank

**Live:** https://bawabank-2.onrender.com/
**Code:** https://github.com/lil-homie97/BawaBank

BawaBank is a mobile-first digital banking app built for Ghana — with GHS ledger, MoMo-style transfers, and persistent transaction history. Built in public from Accra.

![BawaBank Screenshot](https://via.placeholder.com/600x300?text=BawaBank+Live+Demo)

### ✨ Features (Shipped)
- 💰 **GHS Balance** — persistent ledger (survives refresh / restart)
- 📥 **Deposit API** — POST /deposit
- 📤 **MoMo Transfer** — recipient name + MoMo number + validation
- 🧾 **Transactions** — deposit/transfer history with status
- 🚀 **Deployed** — auto-deploy on Render from GitHub main
- 📱 **Mobile-first UI** — dark premium banking design

### 🛠️ Tech Stack
- **Backend:** Python, Flask, Gunicorn
- **Frontend:** HTML, CSS, JavaScript (fetch API)
- **Persistence:** JSON file DB (migrating to PostgreSQL)
- **Deploy:** Render + GitHub Actions CI/CD

### 📸 Live Demo
1. Open https://bawabank-2.onrender.com/
2. Deposit GHS 100
3. Transfer to MoMo number
4. Refresh — balance stays at GHS 2500.00

> Note: Demo money only — no real MTN MoMo transaction. Safe to test with any amount.

### 🗺️ Roadmap
- [x] Live deploy on Render
- [x] Persistent balance
- [x] MoMo transfer UI
- [ ] PostgreSQL + Render Disk for true persistence
- [ ] Login / Auth
- [ ] MTN MoMo API integration
- [ ] Receipt PDF export

### 👨‍💻 Founder
**Derrick Bawa** — Aspiring Fintech Engineer | Accra, Ghana
Built in 3 days — from 42 lines to production bank.

LinkedIn: [Add your link]
Portfolio: bawabank-2.onrender.com

### 🤝 Feedback
Open an Issue or DM — what should I build next?

---
Built with ❤️ in Ghana 🇬🇭 #BuildInPublic #GhanaTech
