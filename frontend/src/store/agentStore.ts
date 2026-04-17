import { create } from 'zustand'

export interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  timestamp: Date
}

interface AgentState {
  messages: Message[]
  status: 'ready' | 'loading' | 'error'
  sources: any[]
  addMessage: (message: Omit<Message, 'id' | 'timestamp'>) => void
  setStatus: (status: 'ready' | 'loading' | 'error') => void
  setSources: (sources: any[]) => void
  clearMessages: () => void
}

export const useAgentStore = create<AgentState>((set) => ({
  messages: [],
  status: 'ready',
  sources: [],

  addMessage: (message) => set((state) => ({
    messages: [
      ...state.messages,
      {
        ...message,
        id: crypto.randomUUID(),
        timestamp: new Date(),
      },
    ],
  })),

  setStatus: (status) => set({ status }),

  setSources: (sources) => set({ sources }),

  clearMessages: () => set({ messages: [], sources: [] }),
}))
