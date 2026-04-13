import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import { createRef } from 'react'
import MessageList from './MessageList'
import type { Message } from '../store/agentStore'

describe('MessageList', () => {
  it('should render empty state when no messages', () => {
    const ref = createRef<HTMLDivElement>()

    render(<MessageList messages={[]} messagesEndRef={ref} />)

    expect(screen.getByText(/start a conversation/i)).toBeInTheDocument()
  })

  it('should render messages', () => {
    const ref = createRef<HTMLDivElement>()
    const messages: Message[] = [
      {
        id: '1',
        role: 'user',
        content: 'Hello',
        timestamp: new Date(),
      },
      {
        id: '2',
        role: 'assistant',
        content: 'Hi there!',
        timestamp: new Date(),
      },
    ]

    render(<MessageList messages={messages} messagesEndRef={ref} />)

    expect(screen.getByText('Hello')).toBeInTheDocument()
    expect(screen.getByText('Hi there!')).toBeInTheDocument()
  })

  it('should distinguish between user and assistant messages', () => {
    const ref = createRef<HTMLDivElement>()
    const messages: Message[] = [
      {
        id: '1',
        role: 'user',
        content: 'User message',
        timestamp: new Date(),
      },
      {
        id: '2',
        role: 'assistant',
        content: 'Assistant message',
        timestamp: new Date(),
      },
    ]

    render(<MessageList messages={messages} messagesEndRef={ref} />)

    expect(screen.getByText('User message')).toBeInTheDocument()
    expect(screen.getByText('Assistant message')).toBeInTheDocument()
  })

  it('should render multiple messages in order', () => {
    const ref = createRef<HTMLDivElement>()
    const messages: Message[] = [
      { id: '1', role: 'user', content: 'First', timestamp: new Date() },
      { id: '2', role: 'assistant', content: 'Second', timestamp: new Date() },
      { id: '3', role: 'user', content: 'Third', timestamp: new Date() },
    ]

    render(<MessageList messages={messages} messagesEndRef={ref} />)

    const messageTexts = screen.getAllByText(/First|Second|Third/)
    expect(messageTexts).toHaveLength(3)
  })
})
