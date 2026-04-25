<template>
  <NuxtLayout name="default">
    <div class="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <!-- Header -->
      <div class="text-center">
        <h2 class="text-3xl font-bold text-gray-900">
          {{ $t('auth.registerTitle') }}
        </h2>
        <p class="mt-2 text-sm text-gray-600">
          {{ $t('auth.registerSubtitle') }}
        </p>
      </div>

      <!-- Register Form -->
      <div class="card">
        <form @submit.prevent="handleRegister" class="space-y-6">
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

          <!-- Username -->
          <div>
            <label for="username" class="label">
              {{ $t('auth.username') }}
            </label>
            <input
              id="username"
              v-model="form.username"
              type="text"
              required
              class="input"
              :class="{ 'border-red-500': errors.username }"
              :placeholder="$t('auth.usernamePlaceholder')"
            />
            <p v-if="errors.username" class="error-text">
              {{ errors.username }}
            </p>
          </div>

          <!-- Full Name -->
          <div>
            <label for="fullName" class="label">
              {{ $t('auth.fullName') }}
            </label>
            <input
              id="fullName"
              v-model="form.full_name"
              type="text"
              class="input"
              :class="{ 'border-red-500': errors.full_name }"
              :placeholder="$t('auth.fullNamePlaceholder')"
            />
            <p v-if="errors.full_name" class="error-text">
              {{ errors.full_name }}
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

          <!-- Confirm Password -->
          <div>
            <label for="confirmPassword" class="label">
              {{ $t('auth.confirmPassword') }}
            </label>
            <input
              id="confirmPassword"
              v-model="form.confirmPassword"
              type="password"
              required
              class="input"
              :class="{ 'border-red-500': errors.confirmPassword }"
              :placeholder="$t('auth.passwordPlaceholder')"
            />
            <p v-if="errors.confirmPassword" class="error-text">
              {{ errors.confirmPassword }}
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
            <span v-else>{{ $t('auth.registerButton') }}</span>
          </button>
        </form>

        <!-- Login Link -->
        <div class="mt-6 text-center">
          <p class="text-sm text-gray-600">
            {{ $t('auth.haveAccount') }}
            <NuxtLink to="/login" class="text-primary-600 hover:text-primary-700 font-medium">
              {{ $t('common.login') }}
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
const { register } = useAuth()
const router = useRouter()

// Form state
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

// Validation
const validateForm = () => {
  errors.email = ''
  errors.username = ''
  errors.full_name = ''
  errors.password = ''
  errors.confirmPassword = ''
  let isValid = true

  if (!form.email) {
    errors.email = t('auth.emailRequired')
    isValid = false
  }

  if (!form.username) {
    errors.username = t('auth.usernameRequired')
    isValid = false
  }

  if (!form.password) {
    errors.password = t('auth.passwordRequired')
    isValid = false
  } else if (form.password.length < 5) {
    errors.password = 'Password must be at least 5 characters'
    isValid = false
  }

  if (form.password !== form.confirmPassword) {
    errors.confirmPassword = t('auth.passwordsNotMatch')
    isValid = false
  }

  return isValid
}

// Handle registration
const handleRegister = async () => {
  console.log('handleRegister called')
  errorMessage.value = ''

  if (!validateForm()) {
    console.log('Form validation failed')
    return
  }

  console.log('Form validation passed, attempting registration...')
  loading.value = true

  try {
    const registerData = {
      email: form.email,
      username: form.username,
      password: form.password,
      full_name: form.full_name || undefined
    }
    console.log('Registration data:', registerData)

    const result = await register(registerData)
    console.log('Registration result:', result)

    if (result.success) {
      console.log('Registration successful, redirecting to home')
      // Redirect to home page on success
      await router.push('/')
    } else {
      console.log('Registration failed:', result.error)
      errorMessage.value = result.error || t('auth.registerError')
    }
  } catch (error) {
    console.error('Registration exception:', error)
    errorMessage.value = t('auth.registerError')
  } finally {
    loading.value = false
  }
}
</script>
