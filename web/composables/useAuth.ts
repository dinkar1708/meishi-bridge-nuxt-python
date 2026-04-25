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
      const response = await api.auth.login(email, password)
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
      return {
        success: false,
        error: error.data?.detail || 'Login failed'
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
      await api.auth.register(data)

      // Auto-login after registration
      return await login(data.email, data.password)
    } catch (error: any) {
      console.error('Registration error:', error)
      return {
        success: false,
        error: error.data?.detail || 'Registration failed'
      }
    }
  }

  // Fetch current user
  const fetchUser = async () => {
    if (!token.value) return

    try {
      const userData = await api.auth.getCurrentUser(token.value)
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
