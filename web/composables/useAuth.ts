export const useAuth = () => {
  const api = useApi()
  const router = useRouter()

  // State
  const token = useState<string | null>('auth-token', () => null)
  const user = useState<any>('auth-user', () => null)
  const isAuthenticated = computed(() => !!token.value)

  // Load token from localStorage on mount
  if (process.client) {
    const storedToken = localStorage.getItem('auth-token')
    if (storedToken) {
      token.value = storedToken
    }
  }

  // Login
  const login = async (email: string, password: string) => {
    try {
      console.log('Attempting login for:', email)
      const response = await api.auth.login(email, password)
      console.log('Login response:', response)
      token.value = response.access_token

      // Store token in localStorage
      if (process.client) {
        localStorage.setItem('auth-token', response.access_token)
      }

      // Fetch user data
      await fetchUser()

      return { success: true }
    } catch (error: any) {
      console.error('Login error:', error)
      const errorMessage = error.data?.detail || error.message || 'Login failed'
      console.error('Error message:', errorMessage)
      return {
        success: false,
        error: errorMessage
      }
    }
  }

  // Register
  const register = async (data: {
    email: string
    password: string
    username: string
    full_name?: string
  }) => {
    try {
      console.log('useAuth.register called with:', data)
      const response = await api.auth.register(data)
      console.log('Registration API response:', response)

      // Auto-login after registration
      console.log('Auto-login after registration...')
      return await login(data.email, data.password)
    } catch (error: any) {
      console.error('Registration error:', error)
      console.error('Registration error details:', error.data)
      const errorMessage = error.data?.detail || error.message || 'Registration failed'
      console.error('Error message:', errorMessage)
      return {
        success: false,
        error: errorMessage
      }
    }
  }

  // Fetch current user
  const fetchUser = async () => {
    if (!token.value) {
      console.log('fetchUser: No token, skipping')
      return
    }

    try {
      console.log('fetchUser: Fetching user with token:', token.value.substring(0, 20) + '...')
      const userData = await api.auth.getCurrentUser(token.value)
      console.log('fetchUser: User data received:', userData)
      user.value = userData
    } catch (error) {
      console.error('Fetch user error:', error)
      logout()
    }
  }

  // Logout
  const logout = () => {
    token.value = null
    user.value = null

    if (process.client) {
      localStorage.removeItem('auth-token')
    }

    router.push('/login')
  }

  return {
    token,
    user,
    isAuthenticated,
    login,
    register,
    logout,
    fetchUser
  }
}
