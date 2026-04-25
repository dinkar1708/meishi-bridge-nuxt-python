<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary-500 to-primary-700">
    <div class="text-center">
      <h1 class="text-6xl font-bold text-white mb-4">
        Hello
      </h1>
      <p class="text-xl text-white/90 mb-8">
        Welcome to MeishiBridge
      </p>
      <div class="flex gap-4 justify-center">
        <NuxtLink
          to="/login"
          class="btn btn-primary bg-white text-primary-600 hover:bg-gray-100"
        >
          {{ t('common.login') }}
        </NuxtLink>
        <NuxtLink
          to="/register"
          class="btn bg-white/20 text-white hover:bg-white/30 border border-white/50"
        >
          {{ t('common.register') }}
        </NuxtLink>
      </div>

      <!-- Language switcher -->
      <div class="mt-8">
        <select
          :value="locale"
          @change="changeLanguage"
          class="bg-white/20 text-white border border-white/50 rounded px-3 py-2"
        >
          <option value="ja">日本語</option>
          <option value="en">English</option>
        </select>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const { t, locale, setLocale } = useI18n()

const changeLanguage = (event: Event) => {
  const target = event.target as HTMLSelectElement
  setLocale(target.value)
}
</script>
