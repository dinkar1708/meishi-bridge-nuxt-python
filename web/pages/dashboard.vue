<template>
  <NuxtLayout name="default">
    <!-- Welcome banner -->
    <section class="relative overflow-hidden bg-gradient-to-br from-primary-700 via-primary-800 to-[#0b1538] text-white">
      <svg class="pointer-events-none absolute inset-0 w-full h-full opacity-[0.07]" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <defs>
          <pattern id="seigaiha-d" x="0" y="0" width="80" height="40" patternUnits="userSpaceOnUse">
            <path d="M0 40 A 40 40 0 0 1 80 40" fill="none" stroke="white" stroke-width="1.5"/>
            <path d="M-40 40 A 40 40 0 0 1 40 40" fill="none" stroke="white" stroke-width="1.5"/>
            <path d="M40 40 A 40 40 0 0 1 120 40" fill="none" stroke="white" stroke-width="1.5"/>
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#seigaiha-d)"/>
      </svg>
      <div class="pointer-events-none absolute -top-24 -right-24 h-80 w-80 rounded-full bg-cyan-400/20 blur-3xl"></div>
      <div class="pointer-events-none absolute -bottom-32 -left-20 h-72 w-72 rounded-full bg-fuchsia-500/20 blur-3xl"></div>

      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-16">
        <div class="text-xs tracking-[0.3em] text-primary-200 font-bold uppercase mb-3">{{ t('dashboard.title') }}</div>
        <h1 class="text-3xl sm:text-4xl font-bold mb-2">
          {{ user?.full_name ? `${user.full_name} 様` : t('dashboard.welcome') }}
        </h1>
        <p class="text-white/80">{{ t('dashboard.welcome') }}</p>
      </div>
    </section>

    <!-- Stats -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-10 relative z-10">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
        <div
          v-for="(stat, idx) in stats"
          :key="idx"
          class="group relative bg-white rounded-2xl ring-1 ring-gray-100 shadow-xl p-6 hover:-translate-y-1 hover:shadow-2xl transition overflow-hidden"
        >
          <div class="absolute -right-6 -top-6 text-7xl font-black text-gray-50 group-hover:text-primary-50 transition select-none">
            0{{ idx + 1 }}
          </div>
          <div class="relative w-11 h-11 rounded-xl bg-gradient-to-br from-primary-500 to-primary-700 text-white shadow-lg shadow-primary-500/30 flex items-center justify-center mb-4">
            <component :is="stat.icon" />
          </div>
          <div class="relative text-sm text-gray-500 font-medium">{{ t(stat.label) }}</div>
          <div class="relative mt-1 flex items-baseline gap-2">
            <span class="text-3xl font-bold text-gray-900">{{ stat.value }}</span>
            <span class="text-sm text-gray-500">{{ stat.unit }}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Cards section -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="bg-white rounded-2xl ring-1 ring-gray-100 shadow-sm">
        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 px-7 sm:px-8 py-6 border-b border-gray-100">
          <div>
            <h2 class="text-xl font-bold text-gray-900">{{ t('dashboard.myCards') }}</h2>
            <p class="text-sm text-gray-600 mt-1">{{ t('dashboard.cardCount', { count: myCards.length }) }}</p>
          </div>
          <NuxtLink
            to="/cards/new"
            class="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-primary-600 to-primary-700 hover:from-primary-700 hover:to-primary-800 text-white font-semibold px-6 py-3 rounded-lg shadow-lg shadow-primary-500/30 transition"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
            {{ t('dashboard.createNew') }}
          </NuxtLink>
        </div>

        <div class="p-7 sm:p-8">
          <!-- Loading -->
          <div v-if="loading" class="text-center py-10 text-gray-500">{{ t('common.loading') }}</div>

          <!-- Empty state -->
          <div v-else-if="myCards.length === 0" class="border border-dashed border-gray-200 rounded-xl py-14 text-center">
            <div class="mx-auto w-16 h-16 rounded-2xl bg-primary-50 text-primary-600 flex items-center justify-center mb-4">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7l9-4 9 4-9 4-9-4zm0 0v6m18-6v6M3 13l9 4 9-4M3 19l9 4 9-4"/></svg>
            </div>
            <p class="text-gray-700 font-semibold">{{ t('card.noCards') }}</p>
            <p class="text-sm text-gray-500 mt-1 mb-5">{{ t('card.noCardsHint') }}</p>
            <NuxtLink
              to="/cards/new"
              class="inline-flex items-center gap-2 bg-gradient-to-r from-primary-600 to-primary-700 hover:from-primary-700 hover:to-primary-800 text-white font-semibold px-5 py-2.5 rounded-lg shadow-lg shadow-primary-500/30 transition"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
              {{ t('dashboard.createNew') }}
            </NuxtLink>
          </div>

          <!-- Card grid -->
          <div v-else class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
            <article
              v-for="card in myCards"
              :key="card.id"
              class="group relative bg-white rounded-2xl ring-1 ring-gray-200 hover:ring-primary-300 hover:shadow-xl transition overflow-hidden"
            >
              <div class="p-5">
                <div class="flex items-start justify-between mb-3">
                  <div>
                    <div class="text-[10px] tracking-[0.25em] text-primary-600 font-semibold uppercase">Meishi</div>
                    <div class="w-8 h-0.5 bg-gradient-to-r from-primary-500 to-cyan-500 rounded-full mt-1"></div>
                  </div>
                  <span class="text-[10px] uppercase text-gray-400 font-mono">{{ card.public_slug.slice(0, 8) }}</span>
                </div>
                <div class="text-lg font-bold text-gray-900">{{ card.name }}</div>
                <div v-if="card.name_kana" class="text-xs text-gray-500">{{ card.name_kana }}</div>
                <div v-if="card.title" class="mt-2 inline-block px-2 py-0.5 rounded bg-primary-50 text-primary-700 text-[11px] font-semibold">{{ card.title }}</div>
                <div v-if="card.company" class="mt-2 text-sm text-gray-600">{{ card.company }}</div>
              </div>
              <div class="px-5 py-3 border-t border-gray-100 flex items-center justify-between gap-2 bg-gray-50">
                <button
                  @click="onDelete(card)"
                  class="text-xs text-gray-500 hover:text-red-600 transition font-medium"
                >
                  {{ t('common.delete') }}
                </button>
                <a
                  :href="`/c/${card.public_slug}`"
                  target="_blank"
                  rel="noopener"
                  class="text-xs text-primary-600 hover:text-primary-700 transition font-semibold"
                >
                  {{ t('card.viewPublic') }} →
                </a>
              </div>
            </article>
          </div>
        </div>
      </div>
    </section>
  </NuxtLayout>
</template>

<script setup lang="ts">
import { h } from 'vue'

const { t } = useI18n()
const { user, token } = useAuth()
const { cards } = useApi()
const router = useRouter()

const myCards = ref<any[]>([])
const loading = ref(true)

const iconCard = () => h('svg', { class: 'w-5 h-5', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M3 5a2 2 0 012-2h14a2 2 0 012 2v14a2 2 0 01-2 2H5a2 2 0 01-2-2V5zM7 8h10M7 12h6M7 16h4' })
])
const iconEye = () => h('svg', { class: 'w-5 h-5', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M15 12a3 3 0 11-6 0 3 3 0 016 0z' }),
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z' })
])
const iconShare = () => h('svg', { class: 'w-5 h-5', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z' })
])

const stats = computed(() => [
  { label: 'dashboard.myCards', unit: '', value: myCards.value.length, icon: iconCard },
  { label: 'dashboard.totalViews', unit: '', value: 0, icon: iconEye },
  { label: 'dashboard.totalShares', unit: '', value: 0, icon: iconShare }
])

const loadCards = async () => {
  loading.value = true
  try {
    myCards.value = await cards.list()
  } catch (err: any) {
    if (err?.statusCode === 401) {
      await router.push('/login')
      return
    }
    console.error('Failed to load cards', err)
    myCards.value = []
  } finally {
    loading.value = false
  }
}

const onDelete = async (card: any) => {
  if (!confirm(t('card.deleteConfirm'))) return
  try {
    await cards.remove(card.id)
    myCards.value = myCards.value.filter(c => c.id !== card.id)
  } catch (err) {
    console.error('Delete failed', err)
  }
}

onMounted(() => {
  if (!token.value && process.client) {
    router.push('/login')
    return
  }
  loadCards()
})
</script>
