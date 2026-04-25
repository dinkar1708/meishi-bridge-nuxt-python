export const useApi = () => {
  const config = useRuntimeConfig()
  const baseURL = config.public.apiUrl

  // Generic API request function
  const apiRequest = async <T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> => {
    const url = `${baseURL}${endpoint}`

    try {
      const response = await $fetch<T>(url, {
        ...options,
        headers: {
          'Content-Type': 'application/json',
          ...options.headers
        }
      })

      return response
    } catch (error: any) {
      console.error('API Error:', error)
      console.error('API Error details:', error.data)
      // Re-throw with more details
      throw {
        message: error.message,
        data: error.data,
        statusCode: error.statusCode
      }
    }
  }

  // Auth API endpoints
  const auth = {
    login: async (email: string, password: string) => {
      return apiRequest<{ access_token: string; token_type: string }>(
        '/auth/login',
        {
          method: 'POST',
          body: { email, password }
        }
      )
    },

    register: async (data: {
      email: string
      password: string
      username: string
      full_name?: string
    }) => {
      return apiRequest<any>('/auth/register', {
        method: 'POST',
        body: data
      })
    },

    getCurrentUser: async (token: string) => {
      return apiRequest<any>('/auth/me', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
    }
  }

  return {
    apiRequest,
    auth
  }
}
