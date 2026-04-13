import { useState, useRef, useEffect } from 'react'
import { useMutation } from '@tanstack/react-query'
import { useAgentStore } from '../store/agentStore'
import { sendMessage } from '../api/agent'
import MessageList from './MessageList'
import MessageInput from './MessageInput'

export default function ChatInterface() {
  const { messages, addMessage, setStatus } = useAgentStore()
  const [input, setInput] = useState('')
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const chatMutation = useMutation({
    mutationFn: sendMessage,
    onMutate: () => {
      setStatus('loading')
      addMessage({
        role: 'user',
        content: input,
      })
      setInput('')
    },
    onSuccess: (data) => {
      addMessage({
        role: 'assistant',
        content: data.response,
      })
      setStatus('ready')
    },
    onError: (error: any) => {
      addMessage({
        role: 'assistant',
        content: `Error: ${error.message || 'Failed to get response'}`,
      })
      setStatus('error')
      setTimeout(() => setStatus('ready'), 2000)
    },
  })

  const handleSend = () => {
    if (!input.trim()) return
    chatMutation.mutate(input)
  }

  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-gray-800 rounded-lg shadow-2xl overflow-hidden">
        <MessageList messages={messages} messagesEndRef={messagesEndRef} />
        <MessageInput
          value={input}
          onChange={setInput}
          onSend={handleSend}
          disabled={chatMutation.isPending}
        />
      </div>
    </div>
  )
}
