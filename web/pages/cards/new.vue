<template>
  <NuxtLayout name="default">
    <!-- Header banner -->
    <section class="relative overflow-hidden bg-gradient-to-br from-primary-700 via-primary-800 to-[#0b1538] text-white">
      <svg class="pointer-events-none absolute inset-0 w-full h-full opacity-[0.07]" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <defs>
          <pattern id="seigaiha-c" x="0" y="0" width="80" height="40" patternUnits="userSpaceOnUse">
            <path d="M0 40 A 40 40 0 0 1 80 40" fill="none" stroke="white" stroke-width="1.5"/>
            <path d="M-40 40 A 40 40 0 0 1 40 40" fill="none" stroke="white" stroke-width="1.5"/>
            <path d="M40 40 A 40 40 0 0 1 120 40" fill="none" stroke="white" stroke-width="1.5"/>
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#seigaiha-c)"/>
      </svg>
      <div class="pointer-events-none absolute -top-24 -right-24 h-80 w-80 rounded-full bg-cyan-400/20 blur-3xl"></div>
      <div class="pointer-events-none absolute -bottom-32 -left-20 h-72 w-72 rounded-full bg-fuchsia-500/20 blur-3xl"></div>

      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-14">
        <div class="text-xs tracking-[0.3em] text-primary-200 font-bold uppercase mb-3">{{ t('nav.cards') }}</div>
        <h1 class="text-3xl sm:text-4xl font-bold mb-2">{{ t('card.createTitle') }}</h1>
        <p class="text-white/80">{{ t('card.createSubtitle') }}</p>
      </div>
    </section>

    <!-- Main: form + live preview -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-8 pb-16 relative z-10">
      <div class="grid lg:grid-cols-5 gap-6">
        <!-- Form (3 cols) -->
        <form @submit.prevent="handleSubmit" class="lg:col-span-3 bg-white rounded-2xl ring-1 ring-gray-100 shadow-xl p-7 sm:p-8 space-y-5">
          <div class="grid sm:grid-cols-2 gap-5">
            <div>
              <label class="label">{{ t('card.name') }} <span class="text-red-500">*</span></label>
              <input v-model="form.name" type="text" required class="input" :placeholder="t('card.namePlaceholder')" />
            </div>
            <div>
              <label class="label">{{ t('card.nameKana') }}</label>
              <input v-model="form.name_kana" type="text" class="input" :placeholder="t('card.nameKanaPlaceholder')" />
            </div>
            <div>
              <label class="label">{{ t('card.nameEn') }}</label>
              <input v-model="form.name_en" type="text" class="input" :placeholder="t('card.nameEnPlaceholder')" />
            </div>
            <div>
              <label class="label">{{ t('card.title') }}</label>
              <input v-model="form.title" type="text" class="input" :placeholder="t('card.titlePlaceholder')" />
            </div>
            <div class="sm:col-span-2">
              <label class="label">{{ t('card.company') }}</label>
              <input v-model="form.company" type="text" class="input" :placeholder="t('card.companyPlaceholder')" />
            </div>
            <div>
              <label class="label">{{ t('card.email') }}</label>
              <input v-model="form.email" type="email" class="input" placeholder="email@example.com" />
            </div>
            <div>
              <label class="label">{{ t('card.phone') }}</label>
              <input v-model="form.phone" type="tel" class="input" :placeholder="t('card.phonePlaceholder')" />
            </div>
            <div>
              <label class="label">{{ t('card.website') }}</label>
              <input v-model="form.website" type="url" class="input" :placeholder="t('card.websitePlaceholder')" />
            </div>
            <div>
              <label class="label">{{ t('card.address') }}</label>
              <input v-model="form.address" type="text" class="input" :placeholder="t('card.addressPlaceholder')" />
            </div>
            <div class="sm:col-span-2">
              <label class="label">{{ t('card.bio') }}</label>
              <textarea v-model="form.bio" rows="3" class="input resize-none" :placeholder="t('card.bioPlaceholder')"></textarea>
            </div>
          </div>

          <div v-if="errorMessage" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm">
            {{ errorMessage }}
          </div>

          <div class="flex gap-3 pt-2">
            <NuxtLink
              to="/dashboard"
              class="inline-flex items-center justify-center px-5 py-3 rounded-lg ring-1 ring-gray-200 text-gray-700 hover:bg-gray-50 transition font-medium"
            >
              {{ t('common.cancel') }}
            </NuxtLink>
            <button
              type="submit"
              :disabled="saving || !form.name"
              class="flex-1 inline-flex items-center justify-center gap-2 bg-gradient-to-r from-primary-600 to-primary-700 hover:from-primary-700 hover:to-primary-800 text-white font-semibold py-3 rounded-lg shadow-lg shadow-primary-500/30 transition disabled:opacity-60 disabled:cursor-not-allowed"
            >
              <svg v-if="!saving" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
              {{ saving ? t('card.saving') : t('card.save') }}
            </button>
          </div>
        </form>

        <!-- Preview (2 cols) -->
        <aside class="lg:col-span-2">
          <div class="lg:sticky lg:top-6">
            <div class="text-xs tracking-[0.3em] text-primary-600 font-bold uppercase mb-3">{{ t('card.preview') }}</div>
            <div
              ref="previewEl"
              @mousemove="onMouseMove"
              @mouseleave="onMouseLeave"
              :style="tiltStyle"
              class="bg-white text-gray-900 rounded-2xl p-6 shadow-2xl ring-1 ring-black/5 transition-transform duration-200 ease-out will-change-transform"
            >
              <div class="flex items-start justify-between mb-5">
                <div>
                  <div class="text-[11px] tracking-[0.25em] text-primary-600 font-semibold uppercase">Meishi</div>
                  <div class="w-10 h-1 bg-gradient-to-r from-primary-500 to-cyan-500 rounded-full mt-1"></div>
                </div>
                <div class="w-12 h-12 rounded-md bg-gray-900 grid grid-cols-5 grid-rows-5 gap-px p-1">
                  <span v-for="i in 25" :key="i" class="bg-white" :class="qrPattern[i-1] ? '' : 'opacity-0'"></span>
                </div>
              </div>

              <div class="text-2xl font-bold tracking-tight">
                {{ form.name || t('card.namePlaceholder') }}
              </div>
              <div v-if="form.name_kana" class="text-xs text-gray-500 mt-0.5">{{ form.name_kana }}</div>
              <div v-if="form.name_en" class="text-sm text-gray-500 mt-0.5">{{ form.name_en }}</div>
              <div v-if="form.title" class="mt-3 inline-block px-2.5 py-1 rounded-md bg-primary-50 text-primary-700 text-xs font-semibold">
                {{ form.title }}
              </div>

              <div class="border-t border-gray-100 my-4"></div>

              <div class="space-y-1.5 text-sm text-gray-600">
                <div v-if="form.company" class="flex items-center gap-2"><span class="w-4 text-primary-500">⌘</span>{{ form.company }}</div>
                <div v-if="form.email" class="flex items-center gap-2"><span class="w-4 text-primary-500">✉</span>{{ form.email }}</div>
                <div v-if="form.phone" class="flex items-center gap-2"><span class="w-4 text-primary-500">☎</span>{{ form.phone }}</div>
                <div v-if="form.website" class="flex items-center gap-2"><span class="w-4 text-primary-500">⌗</span>{{ form.website }}</div>
                <div v-if="form.address" class="flex items-center gap-2"><span class="w-4 text-primary-500">⊕</span>{{ form.address }}</div>
              </div>

              <div v-if="form.bio" class="mt-4 pt-4 border-t border-gray-100 text-sm text-gray-600 leading-relaxed whitespace-pre-line">
                {{ form.bio }}
              </div>
            </div>
          </div>
        </aside>
      </div>
    </section>
  </NuxtLayout>
</template>

<script setup lang="ts">
const { t, locale } = useI18n()
const { cards } = useApi()
const router = useRouter()

const form = reactive({
  name: '',
  name_kana: '',
  name_en: '',
  title: '',
  company: '',
  email: '',
  phone: '',
  website: '',
  address: '',
  bio: '',
  locale: locale.value
})

const saving = ref(false)
const errorMessage = ref('')

const previewEl = ref<HTMLElement | null>(null)
const tiltStyle = ref('')
const onMouseMove = (e: MouseEvent) => {
  const el = previewEl.value
  if (!el) return
  const rect = el.getBoundingClientRect()
  const x = (e.clientX - rect.left) / rect.width - 0.5
  const y = (e.clientY - rect.top) / rect.height - 0.5
  tiltStyle.value = `transform: perspective(1000px) rotateX(${-y * 8}deg) rotateY(${x * 8}deg);`
}
const onMouseLeave = () => { tiltStyle.value = '' }

const qrPattern = [
  1,1,1,0,1,
  1,0,1,1,0,
  0,1,1,0,1,
  1,1,0,1,1,
  1,0,1,1,0
]

const handleSubmit = async () => {
  errorMessage.value = ''
  if (!form.name.trim()) {
    errorMessage.value = t('auth.fullNameRequired')
    return
  }
  saving.value = true
  try {
    const payload: any = { name: form.name, locale: form.locale }
    for (const k of ['name_kana','name_en','title','company','email','phone','website','address','bio'] as const) {
      if (form[k]) payload[k] = form[k]
    }
    await cards.create(payload)
    await router.push('/dashboard')
  } catch (err: any) {
    errorMessage.value = err?.data?.detail || err?.message || t('common.error')
  } finally {
    saving.value = false
  }
}
</script>
