# 🏗️ Infrastructure

**MeishiBridge Infrastructure & DevOps**

Docker, Terraform, CI/CD, and deployment configurations.

---

## 📋 Overview

This directory contains infrastructure configurations:
- **FREE Manual Deployment** (Vercel + Render + Supabase) - $0/month
- **GCP with Terraform** (Cloud Run + Cloud SQL) - ~$15/month
- Docker Compose for local development
- CI/CD pipelines (GitHub Actions)

---

## 🚀 Deployment Options

### **Option 1: FREE Manual Deployment** (Recommended for MVP)

**Stack:** Vercel + Render + Supabase = **$0/month**

#### **Quick Setup (15 minutes):**

**1. Frontend (Vercel):**
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
cd web
vercel --prod
```
Or connect GitHub repo at [vercel.com](https://vercel.com) for auto-deploy.

**2. Backend (Render):**
- Go to [render.com](https://render.com)
- New Web Service → Connect GitHub repo
- Build: `pip install -r requirements.txt`
- Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- Add environment variables (see below)

**3. Database (Supabase):**
- Create project at [supabase.com](https://supabase.com)
- Get connection string from Settings → Database
- Create storage bucket: `cards`

**Environment Variables:**
```env
# Render (Backend)
DATABASE_URL=<from Supabase>
SECRET_KEY=<random string>
SUPABASE_URL=<from Supabase>
SUPABASE_KEY=<from Supabase>
FRONTEND_URL=https://your-app.vercel.app

# Vercel (Frontend)
NUXT_PUBLIC_API_URL=https://your-api.onrender.com/api/v1
NUXT_PUBLIC_APP_URL=https://your-app.vercel.app
```

**Done!** 🎉 Total cost: $0/month

---

### **Option 2: GCP with Terraform** (For Production)

**Stack:** Cloud Run + Cloud SQL = **~$15/month**

Deploy everything on GCP using Terraform:
- Cloud Run (Frontend container)
- Cloud Run (Backend container)
- Cloud SQL PostgreSQL
- Cloud Storage

```bash
cd infra/terraform/gcp
terraform init
terraform plan
terraform apply
```

Full guide below in [GCP Terraform Setup](#gcp-terraform-setup) section.

---

## 📂 Structure

```
infra/
├── docker/
│   ├── docker-compose.yml          # Local development
│   ├── docker-compose.prod.yml     # Production-like local
│   ├── Dockerfile.api              # API image
│   └── Dockerfile.web              # Web image
│
├── terraform/                       # Infrastructure as Code
│   ├── aws/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   └── modules/
│   │       ├── vpc/
│   │       ├── rds/
│   │       ├── ecs/
│   │       └── s3/
│   │
│   ├── gcp/
│   │   ├── main.tf
│   │   └── ...
│   │
│   └── environments/
│       ├── dev.tfvars
│       ├── staging.tfvars
│       └── prod.tfvars
│
├── k8s/                            # Kubernetes configs
│   ├── deployments/
│   ├── services/
│   ├── ingress/
│   └── configmaps/
│
├── .github/
│   └── workflows/
│       ├── api-ci.yml             # API CI/CD
│       ├── web-ci.yml             # Web CI/CD
│       ├── mobile-ci.yml          # Mobile CI/CD
│       └── terraform-apply.yml    # Infrastructure deployment
│
├── scripts/                        # Utility scripts
│   ├── backup-db.sh
│   ├── restore-db.sh
│   ├── deploy.sh
│   └── health-check.sh
│
└── README.md                       # This file
```

---

## 🐳 Docker Setup

### **Local Development (Docker Compose)**

**Start all services:**
```bash
cd infra/docker
docker-compose up -d

# Services:
# - PostgreSQL: localhost:5432
# - API: localhost:8000
# - Web: localhost:3000
# - pgAdmin: localhost:5050 (optional)
```

**Stop services:**
```bash
docker-compose down

# With volume cleanup:
docker-compose down -v
```

**View logs:**
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f api
docker-compose logs -f web
```

### **Docker Compose Configuration**

**`docker-compose.yml`** - Development setup
```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    container_name: meishibridge-db
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: meishibridge
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  api:
    build:
      context: ../../api
      dockerfile: ../infra/docker/Dockerfile.api
    container_name: meishibridge-api
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    volumes:
      - ../../api:/app
    ports:
      - "8000:8000"
    env_file:
      - ../../api/.env
    depends_on:
      postgres:
        condition: service_healthy

  web:
    build:
      context: ../../web
      dockerfile: ../infra/docker/Dockerfile.web
    container_name: meishibridge-web
    command: npm run dev
    volumes:
      - ../../web:/app
      - /app/node_modules
    ports:
      - "3000:3000"
    env_file:
      - ../../web/.env
    depends_on:
      - api

volumes:
  postgres_data:
```

---

## ☁️ GCP Terraform Setup

### **Simple GCP Deployment** (~$15/month)

**Architecture:**
```
User → Cloud Run (Frontend) → Cloud Run (Backend) → Cloud SQL
                                                   → Cloud Storage
```

**Prerequisites:**
- GCP account with billing enabled
- `gcloud` CLI installed
- Terraform installed

**Quick Setup:**

```bash
# 1. Create GCP project
gcloud projects create meishi-link-prod

# 2. Enable APIs
gcloud services enable run.googleapis.com
gcloud services enable sql-component.googleapis.com
gcloud services enable storage.googleapis.com

# 3. Deploy with Terraform
cd infra/terraform/gcp
terraform init
terraform plan
terraform apply
```

**Cost Breakdown:**
- Cloud Run (Frontend): ~$5/mo
- Cloud Run (Backend): ~$5/mo
- Cloud SQL (PostgreSQL): ~$10/mo
- Cloud Storage: ~$2/mo
- **Total: ~$22/month**

**Terraform Files:**
```
terraform/gcp/
├── main.tf           # Main infrastructure
├── variables.tf      # Configuration variables
├── outputs.tf        # Output values
└── terraform.tfvars  # Your settings
```

> 💡 **Note:** Full Terraform examples available in `infra/terraform/gcp/` directory

---

## 🚀 CI/CD Pipelines

### **GitHub Actions Workflows**

**`.github/workflows/api-ci.yml`**
- Trigger: Push to `main` or PR
- Steps:
  1. Lint code (black, flake8)
  2. Run tests (pytest)
  3. Build Docker image
  4. Push to registry
  5. Deploy to Render

**`.github/workflows/web-ci.yml`**
- Trigger: Push to `main` or PR
- Steps:
  1. Lint code (ESLint)
  2. Type check (TypeScript)
  3. Run tests (Vitest)
  4. Build production
  5. Deploy to Vercel

**`.github/workflows/mobile-ci.yml`**
- Trigger: Push to `main` or PR
- Steps:
  1. Lint code (Dart)
  2. Run tests (Flutter test)
  3. Build APK/IPA
  4. Deploy to TestFlight/Play Store

---

## 🔐 Environment Variables

### **Development (.env.local)**
```bash
# API
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/meishibridge
SECRET_KEY=dev-secret-key
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_KEY=dev-key
FRONTEND_URL=http://localhost:3000

# Web
NUXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NUXT_PUBLIC_APP_URL=http://localhost:3000
```

### **Production (.env.prod)**
```bash
# API
DATABASE_URL=postgresql://user:pass@db.supabase.co:5432/postgres
SECRET_KEY=<strong-random-key>
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_KEY=<prod-key>
FRONTEND_URL=https://meishibridge.com

# Web
NUXT_PUBLIC_API_URL=https://api.meishibridge.com/api/v1
NUXT_PUBLIC_APP_URL=https://meishibridge.com
```

---

## 📊 Monitoring & Logging

### **Application Monitoring**
- **Sentry**: Error tracking
- **Datadog**: APM and metrics
- **LogRocket**: Session replay

### **Infrastructure Monitoring**
- **CloudWatch** (AWS)
- **Cloud Monitoring** (GCP)
- **Grafana**: Custom dashboards
- **Prometheus**: Metrics collection

### **Uptime Monitoring**
- **UptimeRobot**: Free tier
  - Monitor API health endpoint
  - Ping every 5 minutes
  - Prevents cold starts

---

## 🔄 Database Management

### **Backups**

**Automated (Supabase):**
- Daily backups (free tier: 7 days retention)
- Point-in-time recovery (paid tiers)

**Manual Backup:**
```bash
# Backup
pg_dump $DATABASE_URL > backup_$(date +%Y%m%d).sql

# Restore
psql $DATABASE_URL < backup_20240124.sql
```

**Backup Script:**
```bash
./infra/scripts/backup-db.sh
```

### **Migrations**

```bash
# Create migration
cd api
alembic revision --autogenerate -m "description"

# Apply migration
alembic upgrade head

# Rollback
alembic downgrade -1
```

---

## 🧪 Testing Environments

### **Local**
- Docker Compose
- Local PostgreSQL
- Hot reload enabled

### **Development**
- Deploy to `dev` branch
- Separate Supabase project
- Test new features

### **Staging**
- Production-like environment
- Pre-release testing
- Same infrastructure as prod

### **Production**
- Main branch only
- Manual deployment approval
- Zero downtime deployment

---

## 📦 Container Registry

### **Docker Hub**
```bash
# Build
docker build -t username/meishibridge-api:latest .

# Push
docker push username/meishibridge-api:latest
```

### **GitHub Container Registry**
```bash
# Login
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin

# Tag
docker tag meishibridge-api ghcr.io/username/meishibridge-api:latest

# Push
docker push ghcr.io/username/meishibridge-api:latest
```

---

## 🔧 Utility Scripts

### **Health Check**
```bash
./scripts/health-check.sh

# Checks:
# - API health endpoint
# - Database connection
# - Storage availability
```

### **Database Backup**
```bash
./scripts/backup-db.sh

# Creates timestamped backup
# Uploads to S3 (optional)
```

### **Deploy**
```bash
./scripts/deploy.sh <environment>

# Environments: dev, staging, prod
```

---

## 📊 Cost Comparison

| Deployment | Stack | Monthly Cost | Best For |
|------------|-------|--------------|----------|
| **FREE (Manual)** | Vercel + Render + Supabase | **$0** | MVP, demos, interviews |
| **GCP (Terraform)** | Cloud Run + Cloud SQL | **~$15-22** | Production, scaling |
| **Multi-Cloud Premium** | Vercel Pro + Render Standard | **~$70** | If staying multi-cloud |

**FREE Tier Limits:**
- ~1,000 users
- 500MB database
- 1GB file storage
- Cold starts (30s after 15min idle)

---

## 🔍 Troubleshooting

### **Docker Issues**
```bash
# Clean everything
docker-compose down -v
docker system prune -a

# Rebuild
docker-compose up -d --build
```

### **Port Conflicts**
```bash
# Find process using port
lsof -i :8000

# Kill process
kill -9 <PID>
```

### **Permission Issues**
```bash
# Fix Docker socket permissions
sudo chmod 666 /var/run/docker.sock
```

---

## 📚 Resources

- [Docker Documentation](https://docs.docker.com)
- [Terraform Documentation](https://www.terraform.io/docs)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Vercel Documentation](https://vercel.com/docs)
- [Render Documentation](https://render.com/docs)
- [Supabase Documentation](https://supabase.com/docs)

---

## 🤝 Contributing

See main [README](../README.md) for contribution guidelines.

---

**Infrastructure as Code** 🏗️
