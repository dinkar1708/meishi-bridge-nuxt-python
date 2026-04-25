<template>
  <NuxtLayout name="default">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="mb-8">
        <h1 class="text-3xl font-bold text-gray-900">Dashboard</h1>
        <p class="text-gray-600 mt-2">Welcome to MeishiBridge</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="card">
          <h3 class="text-lg font-semibold text-gray-900 mb-2">My Cards</h3>
          <p class="text-gray-600">You have 0 business cards</p>
        </div>

        <div class="card">
          <h3 class="text-lg font-semibold text-gray-900 mb-2">Views</h3>
          <p class="text-gray-600">0 total views</p>
        </div>

        <div class="card">
          <h3 class="text-lg font-semibold text-gray-900 mb-2">Shares</h3>
          <p class="text-gray-600">0 total shares</p>
        </div>
      </div>

      <div class="mt-8">
        <button class="btn btn-primary">
          Create New Card
        </button>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
// Dashboard placeholder
</script>
