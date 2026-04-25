# Architecture Documentation

System architecture and design decisions.

---

## Available Documentation

### **[Service Layer Organization](service-layer-organization.md)**
**Complete guide for organizing services as your API grows:**
- Evolution stages: Flat -> Domain-Driven -> Layered
- Best practices for each stage (1-10, 10-30, 30+ services)
- Real code examples for each pattern
- Migration guide from flat to domain-driven structure
- Recommended structure for MeishiBridge
- When to use repository pattern, caching layer, validators
- Anti-patterns to avoid

---

## Coming Soon

### **System Design**
- **overview.md** - High-level architecture overview
- **tech-stack.md** - Technology choices and rationale
- **design-patterns.md** - Design patterns used
- **folder-structure.md** - Project organization

### **Components**
- **routers.md** - Router layer (controllers)
- **models.md** - Data models (ORM)
- **schemas.md** - Pydantic schemas (DTOs)
- **middleware.md** - Middleware components
- **dependencies.md** - FastAPI dependencies

### **Database**
- **database-design.md** - Database architecture
- **migrations.md** - Migration strategy
- **orm-patterns.md** - SQLAlchemy patterns

### **Security**
- **security-overview.md** - Security architecture
- **authentication-flow.md** - Auth implementation
- **data-protection.md** - Data security measures

### **Performance**
- **caching-strategy.md** - Caching approach
- **async-patterns.md** - Async/await usage
- **optimization.md** - Performance optimizations
