<template>
  <NuxtLayout name="default">
    <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary-500 to-primary-700 -mt-16">
      <div class="text-center px-4">
        <h1 class="text-6xl font-bold text-white mb-4">
          {{ t('home.title') }}
        </h1>
        <p class="text-xl text-white/90 mb-8">
          {{ t('home.subtitle') }}
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <NuxtLink
            to="/register"
            class="btn btn-primary bg-white text-primary-600 hover:bg-gray-100 px-8 py-3 text-lg"
          >
            {{ t('home.getStarted') }}
          </NuxtLink>
          <NuxtLink
            to="/login"
            class="btn bg-white/20 text-white hover:bg-white/30 border border-white/50 px-8 py-3 text-lg"
          >
            {{ t('common.login') }}
          </NuxtLink>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
const { t } = useI18n()
</script>
