<template>
  <NuxtLayout name="default">
    <div class="grid lg:grid-cols-2 min-h-[calc(100vh-4rem)]">
      <!-- ░░░ LEFT: brand panel ░░░ -->
      <aside class="hidden lg:flex relative items-center justify-center overflow-hidden bg-gradient-to-br from-primary-700 via-primary-800 to-[#0b1538] text-white p-12">
        <svg class="pointer-events-none absolute inset-0 w-full h-full opacity-[0.07]" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <defs>
            <pattern id="seigaiha-r" x="0" y="0" width="80" height="40" patternUnits="userSpaceOnUse">
              <path d="M0 40 A 40 40 0 0 1 80 40" fill="none" stroke="white" stroke-width="1.5"/>
              <path d="M-40 40 A 40 40 0 0 1 40 40" fill="none" stroke="white" stroke-width="1.5"/>
              <path d="M40 40 A 40 40 0 0 1 120 40" fill="none" stroke="white" stroke-width="1.5"/>
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#seigaiha-r)"/>
        </svg>
        <div class="pointer-events-none absolute -top-24 -left-24 h-[28rem] w-[28rem] rounded-full bg-fuchsia-500/20 blur-3xl"></div>
        <div class="pointer-events-none absolute -bottom-24 -right-24 h-[24rem] w-[24rem] rounded-full bg-primary-300/25 blur-3xl"></div>

        <div class="relative max-w-md">
          <div class="text-xs tracking-[0.3em] text-primary-200 font-bold uppercase mb-4">Join MeishiBridge</div>
          <h2 class="text-4xl font-bold leading-tight mb-4">{{ t('auth.heroTitle') }}</h2>
          <p class="text-white/80 leading-relaxed mb-10">{{ t('auth.heroSubtitle') }}</p>

          <ul class="space-y-3 text-sm text-white/85">
            <li class="flex items-start gap-2"><span class="text-emerald-400 mt-0.5">✓</span>{{ t('home.trustFree') }}</li>
            <li class="flex items-start gap-2"><span class="text-emerald-400 mt-0.5">✓</span>{{ t('home.trustNoCard') }}</li>
            <li class="flex items-start gap-2"><span class="text-emerald-400 mt-0.5">✓</span>{{ t('home.trustJa') }}</li>
            <li class="flex items-start gap-2"><span class="text-emerald-400 mt-0.5">✓</span>{{ t('home.trustQR') }}</li>
          </ul>
        </div>
      </aside>

      <!-- ░░░ RIGHT: form ░░░ -->
      <div class="flex items-center justify-center py-12 px-4 sm:px-6 lg:px-12 bg-gray-50">
        <div class="max-w-md w-full">
          <div class="text-center lg:text-left mb-8">
            <h1 class="text-3xl font-bold text-gray-900">{{ $t('auth.registerTitle') }}</h1>
            <p class="mt-2 text-sm text-gray-600">{{ $t('auth.registerSubtitle') }}</p>
          </div>

          <div class="bg-white rounded-2xl shadow-xl ring-1 ring-gray-100 p-7 sm:p-8">
            <form @submit.prevent="handleRegister" class="space-y-5">
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
                <label for="username" class="label">{{ $t('auth.username') }}</label>
                <input
                  id="username"
                  v-model="form.username"
                  type="text"
                  required
                  class="input"
                  :class="{ 'border-red-500': errors.username }"
                  :placeholder="$t('auth.usernamePlaceholder')"
                />
                <p v-if="errors.username" class="error-text">{{ errors.username }}</p>
              </div>

              <div>
                <label for="fullName" class="label">{{ $t('auth.fullName') }}</label>
                <input
                  id="fullName"
                  v-model="form.full_name"
                  type="text"
                  class="input"
                  :placeholder="$t('auth.fullNamePlaceholder')"
                />
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

              <div>
                <label for="confirmPassword" class="label">{{ $t('auth.confirmPassword') }}</label>
                <input
                  id="confirmPassword"
                  v-model="form.confirmPassword"
                  type="password"
                  required
                  class="input"
                  :class="{ 'border-red-500': errors.confirmPassword }"
                  :placeholder="$t('auth.passwordPlaceholder')"
                />
                <p v-if="errors.confirmPassword" class="error-text">{{ errors.confirmPassword }}</p>
              </div>

              <div v-if="errorMessage" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm">
                {{ errorMessage }}
              </div>

              <button
                type="submit"
                :disabled="loading"
                class="w-full inline-flex items-center justify-center gap-2 bg-gradient-to-r from-primary-600 to-primary-700 hover:from-primary-700 hover:to-primary-800 text-white font-semibold py-3 rounded-lg shadow-lg shadow-primary-500/30 transition disabled:opacity-60"
              >
                <span v-if="loading">{{ $t('common.loading') }}</span>
                <span v-else>{{ $t('auth.registerButton') }}</span>
              </button>
            </form>

            <div class="mt-6 text-center text-sm text-gray-600">
              {{ $t('auth.haveAccount') }}
              <NuxtLink to="/login" class="text-primary-600 hover:text-primary-700 font-semibold ml-1">
                {{ $t('common.login') }}
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
const { register } = useAuth()
const router = useRouter()

const form = reactive({
  email: '',
  username: '',
  full_name: '',
  password: '',
  confirmPassword: ''
})
const errors = reactive({
  email: '',
  username: '',
  full_name: '',
  password: '',
  confirmPassword: ''
})
const loading = ref(false)
const errorMessage = ref('')

const validateForm = () => {
  errors.email = ''
  errors.username = ''
  errors.full_name = ''
  errors.password = ''
  errors.confirmPassword = ''
  let isValid = true

  if (!form.email) { errors.email = t('auth.emailRequired'); isValid = false }
  if (!form.username) { errors.username = t('auth.usernameRequired'); isValid = false }
  if (!form.password) {
    errors.password = t('auth.passwordRequired'); isValid = false
  } else if (form.password.length < 5) {
    errors.password = 'Password must be at least 5 characters'; isValid = false
  }
  if (form.password !== form.confirmPassword) {
    errors.confirmPassword = t('auth.passwordsNotMatch'); isValid = false
  }
  return isValid
}

const handleRegister = async () => {
  errorMessage.value = ''
  if (!validateForm()) return
  loading.value = true
  try {
    const result = await register({
      email: form.email,
      username: form.username,
      password: form.password,
      full_name: form.full_name || undefined
    })
    if (result.success) {
      await router.push('/dashboard')
    } else {
      errorMessage.value = result.error || t('auth.registerError')
    }
  } catch (error) {
    errorMessage.value = t('auth.registerError')
  } finally {
    loading.value = false
  }
}
</script>
