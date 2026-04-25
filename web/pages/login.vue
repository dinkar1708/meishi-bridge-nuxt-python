<template>
  <NuxtLayout name="default">
    <div class="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <!-- Header -->
      <div class="text-center">
        <h2 class="text-3xl font-bold text-gray-900">
          {{ $t('auth.loginTitle') }}
        </h2>
        <p class="mt-2 text-sm text-gray-600">
          {{ $t('auth.loginSubtitle') }}
        </p>
      </div>

      <!-- Login Form -->
      <div class="card">
        <form @submit.prevent="handleLogin" class="space-y-6">
          <!-- Email -->
          <div>
            <label for="email" class="label">
              {{ $t('auth.email') }}
            </label>
            <input
              id="email"
              v-model="form.email"
              type="email"
              required
              class="input"
              :class="{ 'border-red-500': errors.email }"
              :placeholder="$t('auth.emailPlaceholder')"
            />
            <p v-if="errors.email" class="error-text">
              {{ errors.email }}
            </p>
          </div>

          <!-- Password -->
          <div>
            <label for="password" class="label">
              {{ $t('auth.password') }}
            </label>
            <input
              id="password"
              v-model="form.password"
              type="password"
              required
              class="input"
              :class="{ 'border-red-500': errors.password }"
              :placeholder="$t('auth.passwordPlaceholder')"
            />
            <p v-if="errors.password" class="error-text">
              {{ errors.password }}
            </p>
          </div>

          <!-- Error Message -->
          <div v-if="errorMessage" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
            {{ errorMessage }}
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="loading"
            class="w-full btn btn-primary"
          >
            <span v-if="loading">{{ $t('common.loading') }}</span>
            <span v-else>{{ $t('auth.loginButton') }}</span>
          </button>
        </form>

        <!-- Register Link -->
        <div class="mt-6 text-center">
          <p class="text-sm text-gray-600">
            {{ $t('auth.noAccount') }}
            <NuxtLink to="/register" class="text-primary-600 hover:text-primary-700 font-medium">
              {{ $t('common.register') }}
            </NuxtLink>
          </p>
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

// Form state
const form = reactive({
  email: '',
  password: ''
})

const errors = reactive({
  email: '',
  password: ''
})

const loading = ref(false)
const errorMessage = ref('')

// Validation
const validateForm = () => {
  errors.email = ''
  errors.password = ''
  let isValid = true

  if (!form.email) {
    errors.email = t('auth.emailRequired')
    isValid = false
  }

  if (!form.password) {
    errors.password = t('auth.passwordRequired')
    isValid = false
  } else if (form.password.length < 8) {
    errors.password = t('auth.passwordMinLength')
    isValid = false
  }

  return isValid
}

// Handle login
const handleLogin = async () => {
  errorMessage.value = ''

  if (!validateForm()) {
    return
  }

  loading.value = true

  try {
    const result = await login(form.email, form.password)

    if (result.success) {
      // Redirect to dashboard on success
      router.push('/dashboard')
    } else {
      errorMessage.value = result.error || t('auth.loginError')
    }
  } catch (error) {
    errorMessage.value = t('auth.loginError')
  } finally {
    loading.value = false
  }
}
</script>
