# API Documentation

Complete documentation for the MeishiBridge API.

---

## Documentation Structure

```
docs/
├── README.md                    # This file - Documentation index
├── setup/                       # Installation and setup
├── development/                 # Development guides
├── testing/                     # Testing guide and best practices
├── database/                    # Database migrations and management
├── api-reference/              # API endpoints reference
├── architecture/               # System architecture
└── guides/                     # Step-by-step tutorials

Note: Deployment documentation is in /infra/ (not here)
```

---

## Quick Access

### **Getting Started**

#### **[setup/installation.md](setup/installation.md)** - Complete Setup Guide
**Start here!** Complete step-by-step guide for setting up the API locally:
- Prerequisites and installation
- Virtual environment setup
- Environment configuration (local/dev/stg/prod)
- Database setup (Docker/Local PostgreSQL)
- Running migrations
- Starting development server
- Troubleshooting

### **[setup/](setup/)** - Setup & Configuration
All setup-related documentation:
- Installation guide
- Configuration options
- Environment setup
- Docker setup
- VS Code configuration

---

## Documentation Categories

### **1. [setup/](setup/)** - Setup & Installation
Get the API running locally
- Installation guide
- Configuration
- Database setup
- Environment variables
- VS Code setup

### **2. [development/](development/)** - Development Guides
Learn how to develop with the API
- Architecture overview
- Project structure
- Creating endpoints
- Database models
- Coding standards

### **3. [testing/](testing/)** - Testing Guide
Complete testing documentation
- Running tests (Docker method)
- Test structure and organization
- Writing tests
- Coverage reports
- Test best practices
- CI/CD integration

### **4. [database/](database/)** - Database Management
Database operations and migrations
- Alembic migrations guide
- Creating migrations
- Applying migrations
- Troubleshooting database issues

### **5. [api-reference/](api-reference/)** - API Reference
Complete API documentation
- Authentication endpoints
- Business card endpoints
- User endpoints
- Request/response schemas
- Error responses

### **6. [architecture/](architecture/)** - Architecture
System design and patterns
- Architecture overview
- Tech stack decisions
- Design patterns
- Component design
- Security architecture

### **7. [guides/](guides/)** - How-To Guides
Step-by-step tutorials
- Quick start guide
- Creating your first endpoint
- Working with database
- QR code generation
- PDF generation
- Common troubleshooting

### **8. Deployment** -> See [/infra/](../../infra/)
All deployment, Docker, CI/CD, and infrastructure documentation is maintained in the `/infra/` folder at the project root.

---

## By Use Case

### **I want to get started quickly**
-> [setup/installation.md](setup/installation.md)

### **I want to understand the codebase**
-> [architecture/](architecture/)

### **I want to add a new feature**
-> [development/](development/)

### **I want to run tests**
-> [testing/](testing/)

### **I need to create database migrations**
-> [database/](database/)

### **I want to deploy to production**
-> [/infra/](../../infra/) (Deployment docs are in infra folder)

### **I want to see all API endpoints**
-> [api-reference/](api-reference/)

### **I need help with a specific task**
-> [guides/](guides/)

---

## Contributing to Documentation

We welcome documentation improvements! When adding new documentation:

1. Place it in the appropriate folder
2. Update the relevant README.md
3. Follow the existing format and style
4. Include code examples where helpful

---

## Documentation Status

| Section | Status | Files |
|---------|--------|-------|
| **Setup** | Ready | Installation guide |
| **Development** | Coming Soon | Planned |
| **Testing** | Ready | Testing guide with Docker commands |
| **Database** | Ready | Migrations guide |
| **API Reference** | Coming Soon | Planned |
| **Architecture** | Partial | Service layer organization guide |
| **Guides** | Coming Soon | Planned |
| **Deployment** | See /infra/ | Maintained separately |

---

## Need Help?

- **Setup issues?** Check [setup/installation.md](setup/installation.md)
- **Project overview?** See main [README.md](../README.md)
- **API docs?** Visit http://localhost:8000/docs when running locally
- **Report issues:** Create an issue on GitHub

---

## External Resources

- [FastAPI Official Docs](https://fastapi.tiangolo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [Alembic Docs](https://alembic.sqlalchemy.org/)
