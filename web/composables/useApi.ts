export interface CardData {
  id: number
  user_id: number
  public_slug: string
  name: string
  name_kana: string | null
  name_en: string | null
  title: string | null
  company: string | null
  email: string | null
  phone: string | null
  website: string | null
  address: string | null
  bio: string | null
  locale: string
  created_at: string
  updated_at: string
}

export interface CardInput {
  name: string
  name_kana?: string
  name_en?: string
  title?: string
  company?: string
  email?: string
  phone?: string
  website?: string
  address?: string
  bio?: string
  locale?: string
}

export const useApi = () => {
  const config = useRuntimeConfig()
  const baseURL = config.public.apiUrl

  const parseErrorMessage = (error: any): string => {
    const detail =
      error?.data?.detail ??
      error?.response?._data?.detail ??
      error?.response?._data?.message

    if (typeof detail === 'string' && detail.trim()) {
      return detail
    }

    if (Array.isArray(detail) && detail.length > 0) {
      const first = detail[0]
      if (typeof first?.msg === 'string') return first.msg
      if (typeof first === 'string') return first
    }

    if (error?.statusCode === 500) {
      return 'Server error. Please try again.'
    }

    if (typeof error?.message === 'string' && error.message.trim()) {
      return error.message
    }

    return 'Request failed. Please try again.'
  }

  const authHeader = (): Record<string, string> => {
    if (!process.client) return {}
    const token = localStorage.getItem('auth-token')
    return token ? { Authorization: `Bearer ${token}` } : {}
  }

  const apiRequest = async <T>(
    endpoint: string,
    options: RequestInit & { auth?: boolean } = {}
  ): Promise<T> => {
    const url = `${baseURL}${endpoint}`
    const { auth = false, ...rest } = options as any

    try {
      const response = await $fetch<T>(url, {
        ...rest,
        headers: {
          'Content-Type': 'application/json',
          ...(auth ? authHeader() : {}),
          ...rest.headers
        }
      })
      return response
    } catch (error: any) {
      throw {
        message: parseErrorMessage(error),
        detail: error?.data?.detail ?? error?.response?._data?.detail,
        data: error?.data ?? error?.response?._data,
        statusCode: error?.statusCode ?? error?.response?.status
      }
    }
  }

  const auth = {
    login: (email: string, password: string) =>
      apiRequest<{ access_token: string; token_type: string }>('/auth/login', {
        method: 'POST',
        body: { email, password }
      }),

    register: (data: { email: string; password: string; username: string; full_name?: string }) =>
      apiRequest<any>('/auth/register', {
        method: 'POST',
        body: data
      }),

    getCurrentUser: (token: string) =>
      apiRequest<any>('/auth/me', {
        headers: { Authorization: `Bearer ${token}` }
      })
  }

  const cards = {
    list: () => apiRequest<CardData[]>('/cards', { auth: true }),
    get: (id: number) => apiRequest<CardData>(`/cards/${id}`, { auth: true }),
    create: (data: CardInput) =>
      apiRequest<CardData>('/cards', { method: 'POST', body: data, auth: true }),
    update: (id: number, data: Partial<CardInput>) =>
      apiRequest<CardData>(`/cards/${id}`, { method: 'PATCH', body: data, auth: true }),
    remove: (id: number) =>
      apiRequest<void>(`/cards/${id}`, { method: 'DELETE', auth: true }),
    getPublic: (slug: string) => apiRequest<CardData>(`/cards/public/${slug}`)
  }

  return {
    apiRequest,
    auth,
    cards
  }
}
