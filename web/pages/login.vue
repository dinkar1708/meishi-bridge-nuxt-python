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
          <div v-if="errorMessage" class="bg-red-100 border-2 border-red-500 text-red-900 px-6 py-4 rounded-lg mb-4">
            <p class="font-bold text-lg">❌ Login Failed</p>
            <p class="mt-2">{{ errorMessage }}</p>
          </div>

          <!-- Success Message -->
          <div v-if="successMessage" class="bg-green-100 border-2 border-green-500 text-green-900 px-6 py-4 rounded-lg mb-4">
            <p class="font-bold text-lg">✅ Login Successful!</p>
            <p class="mt-2">{{ successMessage }}</p>
          </div>

          <!-- Submit Button -->
          <button
            type="button"
            @click="handleLogin"
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
// Test if script is loading
console.log('LOGIN PAGE SCRIPT LOADED!')

const { t } = useI18n()
const { login } = useAuth()
const router = useRouter()

console.log('useAuth loaded:', !!login)
console.log('router loaded:', !!router)

// Form state (pre-filled with test account for easy testing)
const form = reactive({
  email: 'test@example.com',
  password: 'test123'
})

const errors = reactive({
  email: '',
  password: ''
})

const loading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

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
  } else if (form.password.length < 5) {
    errors.password = 'Password must be at least 5 characters'
    isValid = false
  }

  return isValid
}

// Handle login
const handleLogin = async () => {
  console.log('🔥 LOGIN BUTTON CLICKED!')
  alert('Login button clicked! Check console.')

  errorMessage.value = ''
  successMessage.value = ''

  if (!validateForm()) {
    errorMessage.value = 'Please fill in all required fields'
    console.log('❌ Validation failed')
    return
  }

  console.log('✅ Validation passed')
  loading.value = true

  try {
    console.log('📞 Calling login API...')
    const result = await login(form.email, form.password)
    console.log('📥 Login result:', result)

    if (result.success) {
      successMessage.value = 'Redirecting to dashboard...'
      console.log('✅ Login successful!')
      // Small delay to show success message
      setTimeout(async () => {
        await router.push('/dashboard')
      }, 500)
    } else {
      errorMessage.value = result.error || 'Login failed. Please check your credentials.'
      console.log('❌ Login failed:', result.error)
    }
  } catch (error: any) {
    errorMessage.value = error?.message || 'Network error. Please try again.'
    console.log('💥 Error:', error)
  } finally {
    loading.value = false
  }
}
</script>
