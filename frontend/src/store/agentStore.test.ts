import { describe, it, expect, beforeEach } from 'vitest'
import { useAgentStore } from './agentStore'

describe('agentStore', () => {
  beforeEach(() => {
    // Reset the store before each test
    useAgentStore.setState({ messages: [], status: 'ready' })
  })

  it('should have initial state', () => {
    const state = useAgentStore.getState()

    expect(state.messages).toEqual([])
    expect(state.status).toBe('ready')
  })

  it('should add a message', () => {
    const { addMessage } = useAgentStore.getState()

    addMessage({
      role: 'user',
      content: 'Hello',
    })

    const state = useAgentStore.getState()

    expect(state.messages).toHaveLength(1)
    expect(state.messages[0].role).toBe('user')
    expect(state.messages[0].content).toBe('Hello')
    expect(state.messages[0].id).toBeDefined()
    expect(state.messages[0].timestamp).toBeInstanceOf(Date)
  })

  it('should add multiple messages', () => {
    const { addMessage } = useAgentStore.getState()

    addMessage({ role: 'user', content: 'Hello' })
    addMessage({ role: 'assistant', content: 'Hi there!' })
    addMessage({ role: 'user', content: 'How are you?' })

    const state = useAgentStore.getState()

    expect(state.messages).toHaveLength(3)
    expect(state.messages[0].role).toBe('user')
    expect(state.messages[1].role).toBe('assistant')
    expect(state.messages[2].role).toBe('user')
  })

  it('should generate unique IDs for messages', () => {
    const { addMessage } = useAgentStore.getState()

    addMessage({ role: 'user', content: 'Message 1' })
    addMessage({ role: 'user', content: 'Message 2' })

    const state = useAgentStore.getState()

    expect(state.messages[0].id).not.toBe(state.messages[1].id)
  })

  it('should set status', () => {
    const { setStatus } = useAgentStore.getState()

    setStatus('loading')
    expect(useAgentStore.getState().status).toBe('loading')

    setStatus('error')
    expect(useAgentStore.getState().status).toBe('error')

    setStatus('ready')
    expect(useAgentStore.getState().status).toBe('ready')
  })

  it('should clear messages', () => {
    const { addMessage, clearMessages } = useAgentStore.getState()

    addMessage({ role: 'user', content: 'Message 1' })
    addMessage({ role: 'user', content: 'Message 2' })

    expect(useAgentStore.getState().messages).toHaveLength(2)

    clearMessages()

    expect(useAgentStore.getState().messages).toEqual([])
  })

  it('should preserve status when clearing messages', () => {
    const { addMessage, clearMessages, setStatus } = useAgentStore.getState()

    addMessage({ role: 'user', content: 'Test' })
    setStatus('loading')

    clearMessages()

    const state = useAgentStore.getState()
    expect(state.messages).toEqual([])
    expect(state.status).toBe('loading')
  })
})
