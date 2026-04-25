# 🌐 Web Frontend - Nuxt 4

**MeishiBridge Web Application**

Modern, responsive web interface built with Nuxt 4, TypeScript, and Tailwind CSS.

---

## 📋 Overview

The web frontend provides the primary user interface for MeishiBridge, featuring:
- User authentication and dashboard
- Business card editor with live preview
- Template selection and customization
- Public card sharing pages
- Analytics dashboard
- Bilingual support (日本語/English)

---

## 🛠️ Tech Stack

- **[Nuxt 4](https://nuxt.com)** - Vue.js meta-framework with SSR/SSG
- **[TypeScript](https://www.typescriptlang.org/)** - Type-safe JavaScript
- **[Tailwind CSS](https://tailwindcss.com/)** - Utility-first CSS
- **[Pinia](https://pinia.vuejs.org/)** - State management
- **[Nuxt i18n](https://i18n.nuxtjs.org/)** - Internationalization
- **[VueUse](https://vueuse.org/)** - Vue composition utilities

---

## Project Setup

This project was set up **manually** for full control over structure and dependencies. However, you can also use the Nuxt CLI to generate a starter project.

### **Option 1: Using Nuxt CLI (Recommended for New Projects)**

```bash
# Create new Nuxt project with CLI
npx nuxi init my-project
# OR
npm create nuxt@latest my-project

# Follow prompts to select:
# - Package manager: npm
# - UI framework: None (we'll add Tailwind manually)
# - Modules: Select i18n, tailwindcss, pinia

cd my-project
npm install
npm run dev
```

### **Option 2: Manual Setup (What We Did)**

This gives you more control over the exact configuration:

```bash
# 1. Create project structure
mkdir -p web/assets/css web/components/{ui,card,editor} web/composables web/layouts web/locales web/middleware web/pages/editor web/plugins web/public web/stores

# 2. Create configuration files manually:
# - package.json (dependencies)
# - nuxt.config.ts (Nuxt & i18n configuration)
# - tsconfig.json (TypeScript configuration)
# - tailwind.config.js (Tailwind CSS configuration)
# - .gitignore (Git ignore file)
# - .env.local (Environment variables)

# 3. Install dependencies
cd web
npm install

# 4. Install additional dependencies
npm install -D vue-tsc

# 5. Start development server
npm run dev
```

**Why Manual Setup?**
- Full control over dependencies and versions
- Custom project structure from the start
- No unused files or boilerplate
- Learn how Nuxt works internally

### **Key Configuration Files Created**

1. **package.json** - Dependencies and scripts
2. **nuxt.config.ts** - Nuxt configuration with i18n and Tailwind modules
3. **tailwind.config.js** - Tailwind CSS theme configuration
4. **tsconfig.json** - TypeScript configuration
5. **.env.local** - Environment variables for local development
6. **app.vue** - Main app component
7. **assets/css/main.css** - Tailwind CSS and custom styles

### **Pages Created**

- `pages/index.vue` - Home page (simple "Hello" landing page)
- `pages/login.vue` - Login page with form validation and i18n
- `pages/register.vue` - Registration page with form validation
- `pages/dashboard.vue` - Dashboard placeholder

### **Composables Created**

- `composables/useApi.ts` - API client for backend communication
- `composables/useAuth.ts` - Authentication state management

### **Localization Files**

- `locales/ja.json` - Japanese translations
- `locales/en.json` - English translations

---

## 📂 Project Structure

```
web/
├── assets/              # CSS, images, fonts
├── components/          # Vue components
│   ├── card/           # Card-related components
│   ├── editor/         # Editor components
│   └── ui/             # Reusable UI components
├── composables/         # Vue composables
│   ├── useAuth.ts      # Authentication logic
│   ├── useCard.ts      # Card operations
│   └── useApi.ts       # API client
├── layouts/             # Page layouts
│   ├── default.vue
│   └── dashboard.vue
├── locales/             # i18n translations
│   ├── ja.json         # Japanese
│   └── en.json         # English
├── middleware/          # Route middleware
│   └── auth.ts         # Auth guard
├── pages/               # File-based routing
│   ├── index.vue       # Landing page
│   ├── login.vue       # Login page
│   ├── register.vue    # Register page
│   ├── dashboard.vue   # User dashboard
│   ├── editor/
│   │   └── [id].vue   # Card editor
│   └── [username].vue  # Public card view
├── plugins/             # Nuxt plugins
├── public/              # Static files
├── stores/              # Pinia stores
│   ├── auth.ts         # Auth store
│   └── card.ts         # Card store
├── nuxt.config.ts       # Nuxt configuration
├── tailwind.config.js   # Tailwind configuration
├── tsconfig.json        # TypeScript config
├── package.json         # Dependencies
└── README.md            # This file
```

---

## 🚀 Getting Started

### **Prerequisites**
- Node.js 18 or higher
- npm or yarn

### **Installation**

```bash
# Navigate to web directory
cd web

# Install dependencies
npm install
```

---

## 🌍 Environment Configuration

The project supports **4 environments**:

| Environment | Purpose | Config File | API URL |
|-------------|---------|-------------|---------|
| **local** | Local development | `.env.local` | `http://localhost:8000` |
| **dev** | Development deployment | `.env.dev` | `https://api-dev.meishibridge.com` |
| **stg** | Staging/Testing | `.env.stg` | `https://api-stg.meishibridge.com` |
| **prod** | Production (Client) | `.env.prod` | `https://api.meishibridge.com` |

### **Setup Environment Files**

Create environment-specific files:

**`.env.local`** (Local development)
```env
NUXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NUXT_PUBLIC_APP_URL=http://localhost:3000
```

**`.env.dev`** (Development deployment)
```env
NUXT_PUBLIC_API_URL=https://meishibridge-api-dev.onrender.com/api/v1
NUXT_PUBLIC_APP_URL=https://meishibridge-dev.vercel.app
```

**`.env.stg`** (Staging deployment)
```env
NUXT_PUBLIC_API_URL=https://meishibridge-api-stg.onrender.com/api/v1
NUXT_PUBLIC_APP_URL=https://meishibridge-stg.vercel.app
```

**`.env.prod`** (Production for clients)
```env
NUXT_PUBLIC_API_URL=https://meishibridge-api.onrender.com/api/v1
NUXT_PUBLIC_APP_URL=https://meishibridge.com
```

### **Run with Environment**

```bash
# Local development
npm run dev
# Uses .env.local automatically

# Build for specific environment
npm run build -- --dotenv .env.dev
npm run build -- --dotenv .env.stg
npm run build -- --dotenv .env.prod
```

---

## 🚀 Development

```bash
# Start development server (uses .env.local)
npm run dev

# Access at http://localhost:3000
```

### **Build**

```bash
# Build for production
npm run build

# Preview production build
npm run preview

# Generate static site
npm run generate
```

### **Nuxt Config**

Key configurations in `nuxt.config.ts`:
- Modules: Tailwind, Pinia, i18n
- SSR/SSG settings
- API proxy configuration
- Meta tags and SEO

---

## 🧪 Testing (Optional for MVP)

Frontend testing is **optional for MVP** but recommended for production. Focus on critical paths.

### **Do You Need Frontend Tests?**

| Scenario | Recommendation |
|----------|---------------|
| **MVP/Interview Portfolio** | **Optional** - Focus on API tests instead |
| **Production/Client Project** | **Recommended** - Add critical path tests |
| **Team Development** | **Required** - Prevent regressions |

### **Minimal Testing Strategy for MVP**

**Priority 1: API is well tested** ✅
- If your API has 90%+ coverage, frontend tests are less critical
- Manual testing is acceptable for MVP

**Priority 2 (Optional): Component Tests**
- Test critical components only (login, card editor)
- Skip until after MVP launch

**Priority 3 (Future): E2E Tests**
- Add for production after MVP validation

### **If You Want to Add Tests:**

**Setup (Vitest + Vue Test Utils):**
```bash
# Install test dependencies
npm install -D vitest @vue/test-utils happy-dom

# Run tests
npm run test

# Run with coverage
npm run test:coverage
```

**Minimal Test Cases (Optional):**

**1. Component Tests** (`components/__tests__/`)
```javascript
// Test login form validation
test('LoginForm validates email format')

// Test card preview updates
test('CardPreview displays Japanese text correctly')
```

**2. Composable Tests** (`composables/__tests__/`)
```javascript
// Test API client
test('useApi handles authentication errors')

// Test auth state
test('useAuth stores user session')
```

**3. E2E Tests - Critical Path Only** (`e2e/`)
```javascript
// User can login
test('User login flow works')

// User can create card
test('User can create and save business card')
```

### **Recommended Approach for MVP:**

```bash
# 1. Ensure API has good tests (90%+ coverage)
cd api && pytest --cov=app

# 2. Manual testing for frontend
npm run dev
# Test login, create card, view card manually

# 3. Add frontend tests AFTER MVP launch (if needed)
```

**Coverage Target (if testing):**
- Components: 70%+ (optional)
- Composables: 80%+ (if critical logic)
- E2E: Critical user flows only

---

## 📱 Features

For complete feature list and roadmap, see **[Main README](../README.md#features)**.

---

## 🎨 Design System

### **Colors**
- Primary: Blue (#3B82F6)
- Secondary: Gray (#6B7280)
- Success: Green (#10B981)
- Error: Red (#EF4444)

### **Typography**
- Primary Font: Noto Sans JP (Japanese)
- Secondary Font: Inter (Latin)

### **Components**
Reusable UI components in `components/ui/`:
- Button
- Input
- Modal
- Card
- Dropdown

---

## 🌍 Localization (i18n)

**Supported Languages:** English & Japanese only (for now)

### **Setup (Nuxt i18n module)**

**Configuration:**
```javascript
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@nuxtjs/i18n'],

  i18n: {
    locales: [
      { code: 'en', iso: 'en-US', file: 'en.json', name: 'English' },
      { code: 'ja', iso: 'ja-JP', file: 'ja.json', name: '日本語' }
    ],
    defaultLocale: 'ja',  // Default: Japanese
    lazy: true,
    langDir: 'locales/'
  }
})
```

### **Translation Files**

**`locales/ja.json`** (Japanese)
```json
{
  "common": {
    "login": "ログイン",
    "register": "新規登録",
    "save": "保存",
    "cancel": "キャンセル"
  },
  "card": {
    "name": "氏名",
    "company": "会社名",
    "title": "役職"
  }
}
```

**`locales/en.json`** (English)
```json
{
  "common": {
    "login": "Login",
    "register": "Sign Up",
    "save": "Save",
    "cancel": "Cancel"
  },
  "card": {
    "name": "Name",
    "company": "Company",
    "title": "Title"
  }
}
```

### **Usage in Components**

```vue
<template>
  <div>
    <h1>{{ $t('common.login') }}</h1>
    <button>{{ $t('common.save') }}</button>

    <!-- Language switcher -->
    <select v-model="$i18n.locale">
      <option value="ja">日本語</option>
      <option value="en">English</option>
    </select>
  </div>
</template>
```

**Future:** More languages can be added in Phase 2/3 if needed.

---

## 📦 Dependencies

### **Core**
- nuxt: ^3.x
- vue: ^3.x
- typescript: ^5.x

### **UI & Styling**
- @nuxtjs/tailwindcss: ^6.x
- @headlessui/vue: ^1.x

### **State & Data**
- @pinia/nuxt: ^0.5.x
- @vueuse/core: ^10.x

### **i18n**
- @nuxtjs/i18n: ^8.x

### **Testing**
- vitest: ^1.x
- @vue/test-utils: ^2.x
- playwright: ^1.x

---

## 🚢 Deployment

### **Vercel (Recommended - FREE)**

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel --prod
```

**Environment Variables (Vercel Dashboard):**
- `NUXT_PUBLIC_API_URL`: Your backend API URL
- `NUXT_PUBLIC_APP_URL`: Your app URL

### **Other Options**
- Netlify
- Cloudflare Pages
- AWS Amplify

---

## 🔍 Troubleshooting

### **Build Errors**
```bash
# Clear cache
rm -rf .nuxt node_modules
npm install
```

### **Hot Reload Not Working**
Check `nuxt.config.ts` vite configuration

### **API Connection Issues**
Verify `NUXT_PUBLIC_API_URL` in `.env`

---

## 📚 Resources

- [Nuxt 4 Documentation](https://nuxt.com)
- [Vue 3 Documentation](https://vuejs.org)
- [Tailwind CSS](https://tailwindcss.com)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)

---

## 🤝 Contributing

See main [README](../README.md) for contribution guidelines.

---

**Built with Nuxt 4** ⚡
