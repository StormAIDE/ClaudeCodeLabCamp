import axios from 'axios'

const api = axios.create({
  baseURL: '/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
})

export interface ChatRequest {
  message: string
  stream?: boolean
}

export interface ChatResponse {
  response: string
  tool_calls: any[]
}

export async function sendMessage(message: string): Promise<ChatResponse> {
  const response = await api.post<ChatResponse>('/agent/chat', {
    message,
    stream: false,
  })
  return response.data
}

export async function checkAgentStatus() {
  const response = await api.get('/agent/status')
  return response.data
}
