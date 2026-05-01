# MeishiBridge (メイシブリッジ)

<div align="center">

**デジタル名刺プラットフォーム | Digital Business Card Platform for Japan**

[![Nuxt 4](https://img.shields.io/badge/Nuxt-4-00DC82)](https://nuxt.com)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-latest-009688)](https://fastapi.tiangolo.com)
[![Flutter](https://img.shields.io/badge/Flutter-latest-02569B)](https://flutter.dev)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

[Live Demo](#) • [日本語](README.ja.md)

</div>

---

## Overview

MeishiBridge is a **full-stack digital business card platform** designed for Japanese business culture with QR codes, PDF export, and bilingual support (日本語/English).

**Why MeishiBridge?**
- Built for Japanese meishi (名刺) culture
- Modern tech stack (Nuxt 4, FastAPI, Flutter)
- Split deployment: Vercel frontend + Vercel backend + Neon Postgres
- AI-ready (Python backend for OCR, translation)
- Multi-platform (Web + iOS + Android)

---

## Tech Stack (Latest Stable Versions)

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| **Frontend** | Nuxt 4 | 4.4+ | Web application |
| | TypeScript | 5.x | Type safety |
| | Tailwind CSS | 3.x | Styling |
| **Backend** | Python | 3.11+ | API server |
| | FastAPI | 0.109+ | REST API framework |
| | PostgreSQL | 15+ | Database |
| **Mobile** | Flutter | 3.24+ | iOS/Android apps |
| | Dart | 3.5+ | Programming language |
| **DevOps** | Docker | Latest | Containerization |
| | Terraform | 1.x | Infrastructure as Code |

---

## Project Structure & Documentation

This project is organized into **4 independent modules**, each with detailed documentation:

| Module | Description | Tech Stack | Documentation |
|--------|-------------|------------|---------------|
| **[web/](web/)** | Frontend web application | Nuxt 4 + TypeScript + Tailwind | **[Web README](web/README.md)** |
| **[api/](api/)** | Backend REST API | Python 3.11 + FastAPI + PostgreSQL | **[API README](api/README.md)** |
| **[mobile/](mobile/)** | iOS & Android apps | Flutter 3.24+ + Dart 3.5+ | **[Mobile README](mobile/README.md)** |
| **[infra/](infra/)** | Infrastructure & DevOps | Docker + Terraform + CI/CD | **[Infra README](infra/README.md)** |

```
meishi-link-nuxt-python/
├── web/              # Frontend → See web/README.md
├── api/              # Backend → See api/README.md
├── mobile/           # Mobile Apps → See mobile/README.md
├── infra/            # Infrastructure → See infra/README.md
└── README.md         # This file (Overview)
```

> **Each module has its own detailed README** with setup, development, testing, and deployment instructions.

---

## Quick Start

### **Option 1: Docker (Recommended - Easiest)**

```bash
# Clone repository
git clone https://github.com/dinkar1708/meishi-bridge-nuxt-python.git
cd meishi-bridge-nuxt-python

# Start all services with Docker
cd infra
docker-compose up -d

# Frontend: http://localhost:3000
# API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

**More details:** See **[Infrastructure README](infra/README.md)** for Docker setup

---

### **Option 2: Run Individually**

Choose the module you want to work on:

| Module | Quick Start Command | Full Setup Guide |
|--------|-------------------|------------------|
| **Web** | `cd web && npm install && npm run dev` | **[web/README.md](web/README.md)** |
| **API** | `cd api && pip install -r requirements.txt && uvicorn app.main:app --reload` | **[api/README.md](api/README.md)** |
| **Mobile** | `cd mobile && flutter pub get && flutter run` | **[mobile/README.md](mobile/README.md)** |

> **See each module's README for detailed prerequisites, environment setup, and troubleshooting.**

---

## Features

### **Phase 1: MVP (Weeks 1-3)**
1. User authentication (JWT)
2. Business card creation (Japanese/English)
3. QR code generation
4. PDF export (91mm × 55mm)
5. Public card sharing
6. Basic analytics
7. 3-5 professional templates

### **Phase 2: Enhanced (Weeks 4-6)**
8. More templates (10+ total)
9. Advanced analytics dashboard
10. vCard export
11. User profile management

### **Phase 3: AI Integration (Weeks 7-10)**
12. OCR card scanner
13. Auto-translation (Japanese ↔ English)
14. Smart furigana generation
15. Team accounts

### **Phase 4: Mobile Apps (Weeks 11-14)**
16. iOS app (Flutter)
17. Android app (Flutter)
18. NFC support
19. Camera scanner

---

## Testing

Each module has comprehensive test coverage:

| Module | Test Command | Coverage | Full Guide |
|--------|-------------|----------|------------|
| **API** | `cd api && pytest --cov=app` | 90%+ target | [api/README.md#testing](api/README.md#testing) |
| **Web** | `cd web && npm run test` | 85%+ target | [web/README.md#testing](web/README.md#testing) |
| **Mobile** | `cd mobile && flutter test` | 80%+ target | [mobile/README.md#testing](mobile/README.md#testing) |

> **Full testing guides** (unit, integration, E2E) in each module's README.

---

## Deployment

Deployment docs are centralized in **[infra/README.md](infra/README.md)**.

- Deployment options and step-by-step:
  - [infra/README.md#-deployment-options](infra/README.md#-deployment-options)
- Deployer assignment for web/api/db:
  - [infra/README.md#-deployer-assignment-single-source-of-truth](infra/README.md#-deployer-assignment-single-source-of-truth)

---

## Module Documentation

For detailed information about each component:

| Documentation | Description |
|-----------------|-------------|
| **[Web Frontend Guide](web/README.md)** | Nuxt 4 setup, components, i18n, deployment to Vercel |
| **[API Backend Guide](api/README.md)** | FastAPI setup, endpoints, database models, deployment to Vercel |
| **[Mobile App Guide](mobile/README.md)** | Flutter setup, NFC, camera scanner, App Store deployment |
| **[Infrastructure Guide](infra/README.md)** | Docker, Terraform, CI/CD, monitoring, cost estimation |

---

## Contributing

See individual module READMEs for specific contribution guidelines.

**General workflow:**
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

## Author

**Dinakar Maurya**
- GitHub: [@dinkar1708](https://github.com/dinkar1708)

---

## Support

If this project helped you, please give it a star!

**Built with love for Japanese business culture**

---

<div align="center">

**[Star this repository](https://github.com/dinkar1708/meishi-bridge-nuxt-python)** • **[Report Bug](https://github.com/dinkar1708/meishi-bridge-nuxt-python/issues)** • **[Request Feature](https://github.com/dinkar1708/meishi-bridge-nuxt-python/issues)**

</div>

## Web DEMO

<img width="1948" height="1078" alt="Screenshot 2026-04-25 at 17 46 26" src="https://github.com/user-attachments/assets/7c404dc0-433f-4c9b-a6b9-85b8308c9b5c" />

<img width="1838" height="1067" alt="Screenshot 2026-04-25 at 17 46 43" src="https://github.com/user-attachments/assets/c49b62a1-c463-4e8e-accd-41b8acb99fd0" />
<img width="1864" height="1090" alt="Screenshot 2026-04-25 at 17 46 35" src="https://github.com/user-attachments/assets/3424e5d1-3c7d-4041-9516-53fdb3691e26" />

