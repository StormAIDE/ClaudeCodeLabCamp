import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import axios from 'axios'
import type { ChatResponse } from './agent'

describe('agent API', () => {
  const mockPost = vi.fn()
  const mockGet = vi.fn()

  beforeEach(() => {
    // Mock axios.create to return our mock instance
    vi.spyOn(axios, 'create').mockReturnValue({
      post: mockPost,
      get: mockGet,
    } as any)

    // Reset all mocks
    vi.clearAllMocks()
  })

  afterEach(() => {
    vi.restoreAllMocks()
  })

  describe('sendMessage', () => {
    it('should send a message and return response', async () => {
      const mockResponse = {
        data: {
          response: 'Hello! How can I help you?',
          tool_calls: [],
        },
      }

      mockPost.mockResolvedValue(mockResponse)

      // Dynamically import to use the mocked axios
      const module = await import('./agent?t=' + Date.now())
      const result = await module.sendMessage('Hello')

      expect(result.response).toBe('Hello! How can I help you?')
      expect(result.tool_calls).toEqual([])
    })

    it('should handle API errors', async () => {
      mockPost.mockRejectedValue(new Error('Network error'))

      const module = await import('./agent?t=' + Date.now())
      await expect(module.sendMessage('Hello')).rejects.toThrow('Network error')
    })
  })

  describe('checkAgentStatus', () => {
    it('should check agent status', async () => {
      const mockStatus = {
        data: {
          status: 'ready',
          model: 'claude-4',
        },
      }

      mockGet.mockResolvedValue(mockStatus)

      const module = await import('./agent?t=' + Date.now())
      const result = await module.checkAgentStatus()

      expect(result.status).toBe('ready')
      expect(result.model).toBe('claude-4')
    })
  })
})
