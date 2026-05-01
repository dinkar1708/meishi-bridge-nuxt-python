<template>
  <NuxtLayout name="default">
    <div class="grid lg:grid-cols-2 min-h-[calc(100vh-4rem)]">
      <!-- ░░░ LEFT: brand panel ░░░ -->
      <aside class="hidden lg:flex relative items-center justify-center overflow-hidden bg-gradient-to-br from-primary-700 via-primary-800 to-[#0b1538] text-white p-12">
        <svg class="pointer-events-none absolute inset-0 w-full h-full opacity-[0.07]" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <defs>
            <pattern id="seigaiha-l" x="0" y="0" width="80" height="40" patternUnits="userSpaceOnUse">
              <path d="M0 40 A 40 40 0 0 1 80 40" fill="none" stroke="white" stroke-width="1.5"/>
              <path d="M-40 40 A 40 40 0 0 1 40 40" fill="none" stroke="white" stroke-width="1.5"/>
              <path d="M40 40 A 40 40 0 0 1 120 40" fill="none" stroke="white" stroke-width="1.5"/>
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#seigaiha-l)"/>
        </svg>
        <div class="pointer-events-none absolute -top-24 -left-24 h-[28rem] w-[28rem] rounded-full bg-primary-400/30 blur-3xl"></div>
        <div class="pointer-events-none absolute -bottom-24 -right-24 h-[24rem] w-[24rem] rounded-full bg-cyan-400/15 blur-3xl"></div>

        <div class="relative max-w-md">
          <div class="text-xs tracking-[0.3em] text-primary-200 font-bold uppercase mb-4">MeishiBridge</div>
          <h2 class="text-4xl font-bold leading-tight mb-4">{{ t('auth.heroTitle') }}</h2>
          <p class="text-white/80 leading-relaxed mb-10">{{ t('auth.heroSubtitle') }}</p>

          <!-- Mini meishi -->
          <div class="bg-white/95 text-gray-900 rounded-xl p-5 shadow-2xl ring-1 ring-white/20 rotate-[-2deg] max-w-xs">
            <div class="flex items-center justify-between mb-3">
              <div class="text-[10px] tracking-[0.25em] text-primary-600 font-semibold uppercase">Meishi</div>
              <div class="w-9 h-9 rounded bg-gray-900 grid grid-cols-4 grid-rows-4 gap-px p-0.5">
                <span v-for="i in 16" :key="i" class="bg-white" :class="qrPattern[i-1] ? '' : 'opacity-0'"></span>
              </div>
            </div>
            <div class="text-lg font-bold">山田 太郎</div>
            <div class="text-xs text-gray-500">YAMADA Taro</div>
            <div class="mt-2 inline-block px-2 py-0.5 rounded bg-primary-50 text-primary-700 text-[11px] font-semibold">プロダクトデザイナー</div>
          </div>
        </div>
      </aside>

      <!-- ░░░ RIGHT: form ░░░ -->
      <div class="flex items-center justify-center py-12 px-4 sm:px-6 lg:px-12 bg-gray-50">
        <div class="max-w-md w-full">
          <div class="text-center lg:text-left mb-8">
            <h1 class="text-3xl font-bold text-gray-900">{{ $t('auth.loginTitle') }}</h1>
            <p class="mt-2 text-sm text-gray-600">{{ $t('auth.loginSubtitle') }}</p>
          </div>

          <div class="bg-white rounded-2xl shadow-xl ring-1 ring-gray-100 p-7 sm:p-8">
            <form @submit.prevent="handleLogin" class="space-y-5">
              <div>
                <label for="email" class="label">{{ $t('auth.email') }}</label>
                <input
                  id="email"
                  v-model="form.email"
                  type="email"
                  required
                  class="input"
                  :class="{ 'border-red-500': errors.email }"
                  :placeholder="$t('auth.emailPlaceholder')"
                />
                <p v-if="errors.email" class="error-text">{{ errors.email }}</p>
              </div>

              <div>
                <label for="password" class="label">{{ $t('auth.password') }}</label>
                <input
                  id="password"
                  v-model="form.password"
                  type="password"
                  required
                  class="input"
                  :class="{ 'border-red-500': errors.password }"
                  :placeholder="$t('auth.passwordPlaceholder')"
                />
                <p v-if="errors.password" class="error-text">{{ errors.password }}</p>
              </div>

              <div v-if="errorMessage" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm">
                {{ errorMessage }}
              </div>
              <div v-if="successMessage" class="bg-emerald-50 border border-emerald-200 text-emerald-700 px-4 py-3 rounded-lg text-sm">
                {{ successMessage }}
              </div>

              <button
                type="submit"
                :disabled="loading"
                class="w-full inline-flex items-center justify-center gap-2 bg-gradient-to-r from-primary-600 to-primary-700 hover:from-primary-700 hover:to-primary-800 text-white font-semibold py-3 rounded-lg shadow-lg shadow-primary-500/30 transition disabled:opacity-60"
              >
                <span v-if="loading">{{ $t('common.loading') }}</span>
                <span v-else>{{ $t('auth.loginButton') }}</span>
              </button>
            </form>

            <div class="mt-6 text-center text-sm text-gray-600">
              {{ $t('auth.noAccount') }}
              <NuxtLink to="/register" class="text-primary-600 hover:text-primary-700 font-semibold ml-1">
                {{ $t('common.register') }}
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
const { t } = useI18n()
const { login } = useAuth()
const router = useRouter()

const form = reactive({
  email: 'test@example.com',
  password: 'test123'
})
const errors = reactive({ email: '', password: '' })
const loading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const qrPattern = [
  1,1,0,1,
  1,0,1,1,
  0,1,1,0,
  1,0,1,1
]

const validateForm = () => {
  errors.email = ''
  errors.password = ''
  let isValid = true
  if (!form.email) { errors.email = t('auth.emailRequired'); isValid = false }
  if (!form.password) {
    errors.password = t('auth.passwordRequired'); isValid = false
  } else if (form.password.length < 5) {
    errors.password = 'Password must be at least 5 characters'; isValid = false
  }
  return isValid
}

const handleLogin = async () => {
  errorMessage.value = ''
  successMessage.value = ''
  if (!validateForm()) return
  loading.value = true
  try {
    const result = await login(form.email, form.password)
    if (result.success) {
      successMessage.value = t('auth.loginSuccess')
      setTimeout(() => router.push('/dashboard'), 400)
    } else {
      errorMessage.value = result.error || t('auth.loginError')
    }
  } catch (error: any) {
    errorMessage.value = error?.message || t('error.network')
  } finally {
    loading.value = false
  }
}
</script>
