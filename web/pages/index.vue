<template>
  <NuxtLayout name="default">
    <!-- ░░░ HERO ░░░ -->
    <section class="relative overflow-hidden bg-gradient-to-br from-primary-700 via-primary-800 to-[#0b1538] text-white">
      <!-- Seigaiha (青海波) wave pattern overlay -->
      <svg class="pointer-events-none absolute inset-0 w-full h-full opacity-[0.07]" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <defs>
          <pattern id="seigaiha" x="0" y="0" width="80" height="40" patternUnits="userSpaceOnUse">
            <path d="M0 40 A 40 40 0 0 1 80 40" fill="none" stroke="white" stroke-width="1.5"/>
            <path d="M-40 40 A 40 40 0 0 1 40 40" fill="none" stroke="white" stroke-width="1.5"/>
            <path d="M40 40 A 40 40 0 0 1 120 40" fill="none" stroke="white" stroke-width="1.5"/>
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#seigaiha)"/>
      </svg>

      <!-- Glowing accents -->
      <div class="pointer-events-none absolute inset-0">
        <div class="absolute -top-32 -left-20 h-[28rem] w-[28rem] rounded-full bg-primary-400/30 blur-3xl"></div>
        <div class="absolute top-1/3 -right-24 h-[22rem] w-[22rem] rounded-full bg-fuchsia-500/20 blur-3xl"></div>
        <div class="absolute bottom-0 left-1/3 h-72 w-72 rounded-full bg-cyan-400/15 blur-3xl"></div>
      </div>

      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 md:pt-28 pb-24 md:pb-32">
        <div class="grid lg:grid-cols-12 gap-10 lg:gap-12 items-center">
          <!-- Copy -->
          <div class="lg:col-span-7 text-center lg:text-left">
            <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/10 ring-1 ring-white/20 backdrop-blur-sm text-xs sm:text-sm tracking-wide mb-6 animate-fade-in">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
              {{ t('home.tagline') }}
            </span>

            <h1 class="font-bold leading-[1.1] tracking-tight mb-6 animate-fade-in-up">
              <span class="block text-3xl sm:text-4xl lg:text-5xl text-white/90">
                {{ t('home.heroTitle') }}
              </span>
              <span class="block text-4xl sm:text-5xl lg:text-6xl mt-1 text-transparent bg-clip-text bg-gradient-to-r from-white via-primary-100 to-cyan-200">
                {{ t('home.heroTitle2') }}
              </span>
            </h1>

            <p class="text-base sm:text-lg text-white/75 leading-relaxed max-w-xl mx-auto lg:mx-0 mb-8 animate-fade-in-up" style="animation-delay:.1s">
              {{ t('home.heroDescription') }}
            </p>

            <div class="flex flex-col sm:flex-row gap-3 justify-center lg:justify-start mb-10 animate-fade-in-up" style="animation-delay:.2s">
              <NuxtLink
                to="/register"
                class="group inline-flex items-center justify-center gap-2 bg-white text-primary-800 hover:bg-primary-50 transition px-7 py-3.5 rounded-lg text-base font-bold shadow-xl shadow-primary-900/40"
              >
                {{ t('home.getStarted') }}
                <svg class="w-4 h-4 transition-transform group-hover:translate-x-0.5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"/></svg>
              </NuxtLink>
              <a
                href="#features"
                class="inline-flex items-center justify-center bg-white/10 hover:bg-white/20 ring-1 ring-white/25 transition px-7 py-3.5 rounded-lg text-base font-medium backdrop-blur-sm"
              >
                {{ t('home.learnMore') }}
              </a>
            </div>

            <!-- Trust strip -->
            <ul class="flex flex-wrap gap-x-6 gap-y-2 justify-center lg:justify-start text-sm text-white/70 animate-fade-in-up" style="animation-delay:.3s">
              <li class="flex items-center gap-1.5"><span class="text-emerald-400">✓</span>{{ t('home.trustFree') }}</li>
              <li class="flex items-center gap-1.5"><span class="text-emerald-400">✓</span>{{ t('home.trustNoCard') }}</li>
              <li class="flex items-center gap-1.5"><span class="text-emerald-400">✓</span>{{ t('home.trustJa') }}</li>
              <li class="flex items-center gap-1.5"><span class="text-emerald-400">✓</span>{{ t('home.trustQR') }}</li>
            </ul>
          </div>

          <!-- Meishi card preview -->
          <div class="lg:col-span-5 relative animate-fade-in-up" style="animation-delay:.15s">
            <!-- Stacked back card -->
            <div class="absolute inset-0 bg-white/10 rounded-2xl rotate-[-6deg] translate-x-4 translate-y-4 backdrop-blur-sm ring-1 ring-white/10"></div>
            <!-- Front meishi -->
            <div class="relative bg-white text-gray-900 rounded-2xl p-7 sm:p-8 shadow-2xl rotate-[2deg] hover:rotate-0 transition-transform duration-500 ring-1 ring-black/5">
              <div class="flex items-start justify-between mb-6">
                <div>
                  <div class="text-[11px] tracking-[0.25em] text-primary-600 font-semibold uppercase">Meishi</div>
                  <div class="w-10 h-1 bg-gradient-to-r from-primary-500 to-cyan-500 rounded-full mt-1"></div>
                </div>
                <!-- QR mock -->
                <div class="w-14 h-14 rounded-md bg-gray-900 grid grid-cols-5 grid-rows-5 gap-px p-1">
                  <span v-for="i in 25" :key="i" class="bg-white" :class="qrPattern[i-1] ? '' : 'opacity-0'"></span>
                </div>
              </div>

              <div class="text-2xl sm:text-3xl font-bold tracking-tight">山田 太郎</div>
              <div class="text-sm text-gray-500 mt-0.5">YAMADA Taro</div>
              <div class="mt-3 inline-block px-2.5 py-1 rounded-md bg-primary-50 text-primary-700 text-xs font-semibold">プロダクトデザイナー</div>

              <div class="border-t border-gray-100 my-5"></div>

              <div class="space-y-1.5 text-sm text-gray-600">
                <div class="flex items-center gap-2"><span class="w-4 text-primary-500">✉</span>yamada@meishibridge.jp</div>
                <div class="flex items-center gap-2"><span class="w-4 text-primary-500">☎</span>+81 90-1234-5678</div>
                <div class="flex items-center gap-2"><span class="w-4 text-primary-500">⌘</span>株式会社メイシブリッジ</div>
                <div class="flex items-center gap-2"><span class="w-4 text-primary-500">⊕</span>東京都渋谷区</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom fade into next section -->
      <div class="absolute bottom-0 inset-x-0 h-12 bg-gradient-to-b from-transparent to-white"></div>
    </section>

    <!-- ░░░ FEATURES ░░░ -->
    <section id="features" class="py-20 lg:py-28 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-14">
          <div class="text-xs sm:text-sm tracking-[0.3em] text-primary-600 font-bold uppercase mb-3">Features</div>
          <h2 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">{{ t('home.features') }}</h2>
          <div class="w-16 h-1 bg-gradient-to-r from-primary-500 to-cyan-500 mx-auto rounded-full"></div>
        </div>

        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-5">
          <div
            v-for="(f, idx) in features"
            :key="idx"
            class="group relative p-7 rounded-2xl ring-1 ring-gray-200 hover:ring-primary-300 hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 bg-white overflow-hidden"
          >
            <div class="absolute -right-6 -top-6 text-7xl font-black text-gray-50 group-hover:text-primary-50 transition select-none">
              0{{ idx + 1 }}
            </div>
            <div class="relative w-12 h-12 rounded-xl bg-gradient-to-br from-primary-500 to-primary-700 text-white shadow-lg shadow-primary-500/30 flex items-center justify-center mb-5">
              <component :is="f.icon" />
            </div>
            <h3 class="relative text-lg font-bold text-gray-900 mb-2">{{ t(f.title) }}</h3>
            <p class="relative text-sm text-gray-600 leading-relaxed">{{ t(f.desc) }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ░░░ HOW IT WORKS ░░░ -->
    <section class="py-20 lg:py-28 bg-gradient-to-b from-gray-50 to-white relative overflow-hidden">
      <!-- Asanoha-inspired decorative dots -->
      <div class="absolute inset-0 opacity-40 pointer-events-none" style="background-image: radial-gradient(circle, #c7d2fe 1px, transparent 1px); background-size: 28px 28px;"></div>

      <div class="relative max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-16">
          <div class="text-xs sm:text-sm tracking-[0.3em] text-primary-600 font-bold uppercase mb-3">3 Steps</div>
          <h2 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">{{ t('home.howItWorks') }}</h2>
          <div class="w-16 h-1 bg-gradient-to-r from-primary-500 to-cyan-500 mx-auto rounded-full"></div>
        </div>

        <div class="grid md:grid-cols-3 gap-10 relative">
          <!-- Connector line -->
          <div class="hidden md:block absolute top-9 left-[16%] right-[16%] h-0.5 bg-gradient-to-r from-primary-200 via-primary-400 to-primary-200"></div>
          <div
            v-for="(step, idx) in steps"
            :key="idx"
            class="relative text-center"
          >
            <div class="relative z-10 w-[72px] h-[72px] mx-auto rounded-2xl bg-white text-primary-700 text-2xl font-black flex items-center justify-center shadow-xl ring-1 ring-primary-100 mb-5 rotate-3 hover:rotate-0 transition-transform">
              <span class="text-3xl tracking-tight">0{{ idx + 1 }}</span>
            </div>
            <h3 class="text-xl font-bold text-gray-900">{{ t(step) }}</h3>
          </div>
        </div>
      </div>
    </section>

    <!-- ░░░ FINAL CTA ░░░ -->
    <section class="relative py-20 lg:py-24 bg-gradient-to-br from-primary-700 via-primary-800 to-[#0b1538] text-white overflow-hidden">
      <!-- Subtle wave pattern -->
      <svg class="pointer-events-none absolute inset-0 w-full h-full opacity-[0.06]" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <rect width="100%" height="100%" fill="url(#seigaiha)"/>
      </svg>
      <div class="pointer-events-none absolute -top-20 -left-20 h-80 w-80 rounded-full bg-cyan-400/20 blur-3xl"></div>
      <div class="pointer-events-none absolute -bottom-20 -right-20 h-80 w-80 rounded-full bg-fuchsia-500/20 blur-3xl"></div>

      <div class="relative max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-bold mb-4 leading-tight">{{ t('home.cta') }}</h2>
        <p class="text-base sm:text-lg text-white/80 mb-10 max-w-2xl mx-auto">{{ t('home.ctaDescription') }}</p>
        <NuxtLink
          to="/register"
          class="group inline-flex items-center gap-2 bg-white text-primary-800 hover:bg-primary-50 transition px-10 py-4 rounded-lg text-lg font-bold shadow-2xl"
        >
          {{ t('home.getStarted') }}
          <svg class="w-5 h-5 transition-transform group-hover:translate-x-1" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"/></svg>
        </NuxtLink>
        <div class="mt-6 text-sm text-white/60">
          <span class="text-emerald-400">✓</span> {{ t('home.trustNoCard') }}
        </div>
      </div>
    </section>
  </NuxtLayout>
</template>

<script setup lang="ts">
import { h } from 'vue'

const { t } = useI18n()

useHead({
  title: 'MeishiBridge — デジタル名刺プラットフォーム',
  meta: [
    { name: 'description', content: '日本のビジネス文化に最適化されたデジタル名刺。QRコード、PDF出力、日英バイリンガル対応で、出会いを次のステップへ。' }
  ]
})

const iconPencil = () => h('svg', { class: 'w-6 h-6', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z' })
])
const iconTemplate = () => h('svg', { class: 'w-6 h-6', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M4 5a1 1 0 011-1h14a1 1 0 011 1v3a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z' })
])
const iconShare = () => h('svg', { class: 'w-6 h-6', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z' })
])
const iconGlobe = () => h('svg', { class: 'w-6 h-6', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z' })
])

const features = [
  { title: 'home.feature1Title', desc: 'home.feature1Description', icon: iconPencil },
  { title: 'home.feature2Title', desc: 'home.feature2Description', icon: iconTemplate },
  { title: 'home.feature3Title', desc: 'home.feature3Description', icon: iconShare },
  { title: 'home.feature4Title', desc: 'home.feature4Description', icon: iconGlobe }
]

const steps = ['home.step1', 'home.step2', 'home.step3']

const qrPattern = [
  1,1,1,0,1,
  1,0,1,1,0,
  0,1,1,0,1,
  1,1,0,1,1,
  1,0,1,1,0
]
</script>

<style scoped>
@keyframes fade-in {
  from { opacity: 0 }
  to   { opacity: 1 }
}
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(12px) }
  to   { opacity: 1; transform: translateY(0) }
}
.animate-fade-in     { animation: fade-in .6s ease-out both }
.animate-fade-in-up  { animation: fade-in-up .7s ease-out both }
</style>
