<template>
  <div class="min-h-screen bg-gradient-to-br from-primary-700 via-primary-800 to-[#0b1538] text-white relative overflow-hidden">
    <!-- Background pattern -->
    <svg class="pointer-events-none absolute inset-0 w-full h-full opacity-[0.06]" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <defs>
        <pattern id="seigaiha-pub" x="0" y="0" width="80" height="40" patternUnits="userSpaceOnUse">
          <path d="M0 40 A 40 40 0 0 1 80 40" fill="none" stroke="white" stroke-width="1.5"/>
          <path d="M-40 40 A 40 40 0 0 1 40 40" fill="none" stroke="white" stroke-width="1.5"/>
          <path d="M40 40 A 40 40 0 0 1 120 40" fill="none" stroke="white" stroke-width="1.5"/>
        </pattern>
      </defs>
      <rect width="100%" height="100%" fill="url(#seigaiha-pub)"/>
    </svg>
    <div class="pointer-events-none absolute -top-32 -left-20 h-[28rem] w-[28rem] rounded-full bg-cyan-400/20 blur-3xl animate-blob"></div>
    <div class="pointer-events-none absolute -bottom-32 -right-20 h-[28rem] w-[28rem] rounded-full bg-fuchsia-500/20 blur-3xl animate-blob" style="animation-delay:-4s"></div>

    <!-- Loading -->
    <div v-if="pending" class="relative min-h-screen flex items-center justify-center">
      <div class="text-white/70">{{ t('common.loading') }}</div>
    </div>

    <!-- Not found -->
    <div v-else-if="!card" class="relative min-h-screen flex items-center justify-center px-4">
      <div class="text-center max-w-sm">
        <div class="text-7xl mb-4">🔍</div>
        <h1 class="text-2xl font-bold mb-2">{{ t('card.notFound') }}</h1>
        <NuxtLink to="/" class="inline-block mt-6 bg-white text-primary-700 px-5 py-2.5 rounded-lg font-semibold hover:bg-primary-50 transition">
          {{ t('card.back') }}
        </NuxtLink>
      </div>
    </div>

    <!-- Card -->
    <div v-else class="relative min-h-screen flex items-center justify-center px-4 py-12">
      <div class="w-full max-w-md">
        <!-- Header -->
        <div class="text-center mb-6">
          <div class="text-[10px] tracking-[0.4em] text-primary-200 font-bold uppercase">MeishiBridge</div>
        </div>

        <!-- 3D tilt card -->
        <div
          ref="cardEl"
          @mousemove="onMouseMove"
          @mouseleave="onMouseLeave"
          class="relative bg-white text-gray-900 rounded-3xl p-7 sm:p-8 shadow-2xl ring-1 ring-black/5 transition-transform duration-200 ease-out will-change-transform"
          :style="tiltStyle"
        >
          <!-- Top row -->
          <div class="flex items-start justify-between mb-6">
            <div>
              <div class="text-[11px] tracking-[0.25em] text-primary-600 font-semibold uppercase">Meishi</div>
              <div class="w-10 h-1 bg-gradient-to-r from-primary-500 to-cyan-500 rounded-full mt-1"></div>
            </div>
            <!-- Big QR -->
            <button
              type="button"
              @click="qrEnlarged = true"
              class="w-16 h-16 rounded-md bg-gray-900 grid grid-cols-7 grid-rows-7 gap-px p-1 hover:scale-105 transition cursor-zoom-in"
              :title="t('card.scanQR')"
            >
              <span v-for="i in 49" :key="i" class="bg-white" :class="qrPattern[i-1] ? '' : 'opacity-0'"></span>
            </button>
          </div>

          <!-- Identity -->
          <div class="text-3xl sm:text-4xl font-bold tracking-tight">{{ card.name }}</div>
          <div v-if="card.name_kana" class="text-sm text-gray-500 mt-1">{{ card.name_kana }}</div>
          <div v-if="card.name_en" class="text-sm text-gray-500">{{ card.name_en }}</div>
          <div v-if="card.title" class="mt-3 inline-block px-3 py-1 rounded-md bg-primary-50 text-primary-700 text-xs font-semibold">
            {{ card.title }}
          </div>
          <div v-if="card.company" class="mt-2 text-sm font-medium text-gray-700">{{ card.company }}</div>

          <div class="border-t border-gray-100 my-5"></div>

          <!-- Contact rows -->
          <div class="space-y-2">
            <ContactRow v-if="card.email"   icon="mail"  :value="card.email"   :href="`mailto:${card.email}`" :on-copy="copy" :copy-label="t('card.copy')" :copied-label="t('card.copied')" :copied-key="copiedKey" copy-key="email" />
            <ContactRow v-if="card.phone"   icon="phone" :value="card.phone"   :href="`tel:${card.phone}`"    :on-copy="copy" :copy-label="t('card.copy')" :copied-label="t('card.copied')" :copied-key="copiedKey" copy-key="phone" />
            <ContactRow v-if="card.website" icon="link"  :value="card.website" :href="websiteHref"            :on-copy="copy" :copy-label="t('card.copy')" :copied-label="t('card.copied')" :copied-key="copiedKey" copy-key="website" external />
            <ContactRow v-if="card.address" icon="pin"   :value="card.address" :href="`https://maps.google.com/?q=${encodeURIComponent(card.address)}`" :on-copy="copy" :copy-label="t('card.copy')" :copied-label="t('card.copied')" :copied-key="copiedKey" copy-key="address" external />
          </div>

          <div v-if="card.bio" class="mt-5 pt-5 border-t border-gray-100 text-sm text-gray-600 leading-relaxed whitespace-pre-line">
            {{ card.bio }}
          </div>
        </div>

        <!-- Action buttons -->
        <div class="grid grid-cols-2 gap-3 mt-5">
          <button
            @click="downloadVCard"
            class="flex items-center justify-center gap-2 bg-white text-primary-800 hover:bg-primary-50 transition px-4 py-3 rounded-xl text-sm font-semibold shadow-lg shadow-primary-900/40"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 17v1a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h9a2 2 0 012 2v1m-3 4h6m0 0l-2-2m2 2l-2 2"/></svg>
            {{ t('card.saveContact') }}
          </button>
          <button
            @click="share"
            class="flex items-center justify-center gap-2 bg-white/15 hover:bg-white/25 ring-1 ring-white/25 transition px-4 py-3 rounded-xl text-sm font-semibold backdrop-blur-sm"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"/></svg>
            {{ shareCopied ? t('card.copied') : t('card.share') }}
          </button>
        </div>

        <div class="text-center mt-8 text-xs text-white/50 tracking-wide">
          Powered by <NuxtLink to="/" class="text-white/80 hover:text-white">MeishiBridge</NuxtLink>
        </div>
      </div>

      <!-- QR enlarge overlay -->
      <div
        v-if="qrEnlarged"
        @click="qrEnlarged = false"
        class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-6 cursor-pointer animate-fade-in"
      >
        <div class="bg-white rounded-2xl p-6 max-w-xs w-full text-center" @click.stop>
          <div class="text-xs tracking-[0.3em] text-primary-600 font-bold uppercase mb-4">{{ t('card.scanQR') }}</div>
          <div class="aspect-square bg-gray-900 grid grid-cols-7 grid-rows-7 gap-px p-2 rounded">
            <span v-for="i in 49" :key="i" class="bg-white" :class="qrPattern[i-1] ? '' : 'opacity-0'"></span>
          </div>
          <div class="text-sm text-gray-700 font-bold mt-4">{{ card.name }}</div>
          <div class="text-xs text-gray-400 break-all mt-2">{{ shareUrl }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const { t } = useI18n()
const route = useRoute()
const { cards } = useApi()

definePageMeta({ layout: false })

const slug = computed(() => String(route.params.slug || ''))

const { data: card, pending } = await useAsyncData(
  `card-${slug.value}`,
  () => cards.getPublic(slug.value).catch(() => null),
  { default: () => null as any, server: false }
)

const cardEl = ref<HTMLElement | null>(null)
const tiltStyle = ref('')
const copiedKey = ref('')
const shareCopied = ref(false)
const qrEnlarged = ref(false)

const websiteHref = computed(() => {
  if (!card.value?.website) return '#'
  const w = card.value.website
  return /^https?:\/\//i.test(w) ? w : `https://${w}`
})

const shareUrl = computed(() => {
  if (process.client) return window.location.href
  return ''
})

// Deterministic mock QR pattern from slug (so each card looks unique)
const qrPattern = computed(() => {
  const s = slug.value || 'meishi'
  const out: number[] = []
  let h = 0
  for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) >>> 0
  for (let i = 0; i < 49; i++) {
    h = (h * 1103515245 + 12345 + i) >>> 0
    out.push(h & 1)
  }
  // force corners (typical QR finder pattern look)
  const corners = [0, 1, 5, 6, 7, 8, 12, 13, 14, 15, 19, 20, 28, 34, 35, 36, 41, 42, 43, 48]
  return out.map((v, i) => corners.includes(i) ? 1 : v)
})

const onMouseMove = (e: MouseEvent) => {
  const el = cardEl.value
  if (!el) return
  const rect = el.getBoundingClientRect()
  const x = (e.clientX - rect.left) / rect.width - 0.5
  const y = (e.clientY - rect.top) / rect.height - 0.5
  const rotY = x * 12
  const rotX = -y * 12
  tiltStyle.value = `transform: perspective(1000px) rotateX(${rotX}deg) rotateY(${rotY}deg) scale(1.02);`
}
const onMouseLeave = () => { tiltStyle.value = '' }

const copy = async (key: string, value: string) => {
  try {
    await navigator.clipboard.writeText(value)
    copiedKey.value = key
    setTimeout(() => { if (copiedKey.value === key) copiedKey.value = '' }, 1500)
  } catch {}
}

const share = async () => {
  const data = {
    title: card.value?.name || 'MeishiBridge',
    text: `${card.value?.name}${card.value?.title ? ' / ' + card.value.title : ''}`,
    url: shareUrl.value
  }
  if (typeof navigator !== 'undefined' && (navigator as any).share) {
    try { await (navigator as any).share(data); return } catch {}
  }
  try {
    await navigator.clipboard.writeText(shareUrl.value)
    shareCopied.value = true
    setTimeout(() => { shareCopied.value = false }, 1500)
  } catch {}
}

const downloadVCard = () => {
  const c = card.value
  if (!c) return
  const lines = [
    'BEGIN:VCARD',
    'VERSION:3.0',
    `FN:${c.name}`,
    c.name_en ? `N:${c.name_en};;;;` : '',
    c.title ? `TITLE:${c.title}` : '',
    c.company ? `ORG:${c.company}` : '',
    c.email ? `EMAIL:${c.email}` : '',
    c.phone ? `TEL:${c.phone}` : '',
    c.website ? `URL:${c.website}` : '',
    c.address ? `ADR:;;${c.address};;;;` : '',
    c.bio ? `NOTE:${c.bio.replace(/\n/g, '\\n')}` : '',
    'END:VCARD'
  ].filter(Boolean).join('\n')
  const blob = new Blob([lines], { type: 'text/vcard;charset=utf-8' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `${c.name || 'meishi'}.vcf`
  a.click()
  URL.revokeObjectURL(url)
}

useHead(() => ({
  title: card.value ? `${card.value.name} | MeishiBridge` : 'MeishiBridge',
  meta: card.value ? [
    { name: 'description', content: `${card.value.name}${card.value.title ? ' / ' + card.value.title : ''}${card.value.company ? ' / ' + card.value.company : ''}` }
  ] : []
}))

</script>

<style scoped>
@keyframes blob {
  0%, 100% { transform: translate(0,0) scale(1) }
  33%      { transform: translate(20px,-30px) scale(1.05) }
  66%      { transform: translate(-15px,20px) scale(0.95) }
}
@keyframes fade-in { from { opacity: 0 } to { opacity: 1 } }
.animate-blob { animation: blob 12s ease-in-out infinite }
.animate-fade-in { animation: fade-in .2s ease-out both }
</style>
