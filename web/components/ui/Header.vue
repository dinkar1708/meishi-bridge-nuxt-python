<template>
  <header class="bg-white shadow-sm">
    <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <div class="flex items-center">
          <NuxtLink to="/" class="flex items-center space-x-2">
            <div class="w-10 h-10 bg-primary-600 rounded-lg flex items-center justify-center">
              <span class="text-white font-bold text-xl">M</span>
            </div>
            <span class="text-xl font-bold text-gray-900">MeishiBridge</span>
          </NuxtLink>
        </div>

        <!-- Navigation & Language Switcher -->
        <div class="flex items-center space-x-4">
          <!-- User Greeting (if logged in) -->
          <div v-if="user" class="hidden md:flex items-center space-x-4">
            <span class="text-gray-700">
              Hello, {{ user.username }}!
            </span>
            <button @click="handleLogout" class="text-gray-700 hover:text-primary-600 px-3 py-2">
              {{ t('common.logout') }}
            </button>
          </div>

          <!-- Navigation Links (if not logged in) -->
          <div v-else class="hidden md:flex items-center space-x-4">
            <NuxtLink to="/login" class="text-gray-700 hover:text-primary-600 px-3 py-2">
              {{ t('common.login') }}
            </NuxtLink>
            <NuxtLink to="/register" class="btn btn-primary text-sm">
              {{ t('common.register') }}
            </NuxtLink>
          </div>

          <!-- Language Switcher -->
          <div class="flex items-center">
            <select
              @change="onLocaleChange"
              class="text-sm border border-gray-300 rounded-md px-3 py-1.5 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            >
              <option value="ja" :selected="locale === 'ja'">🇯🇵 日本語</option>
              <option value="en" :selected="locale === 'en'">🇬🇧 English</option>
            </select>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup lang="ts">
const { t, locale } = useI18n()
const { user, logout } = useAuth()

const onLocaleChange = (event: Event) => {
  const next = (event.target as HTMLSelectElement).value
  document.cookie = `i18n_redirected=${next}; path=/; max-age=31536000; samesite=lax`
  window.location.reload()
}

const handleLogout = () => {
  logout()
}
</script>
