import { useState, useRef, useEffect } from 'react'
import { useMutation } from '@tanstack/react-query'
import { useAgentStore } from '../store/agentStore'
import { sendMessage } from '../api/agent'
import MessageList from './MessageList'
import MessageInput from './MessageInput'

export default function ChatInterface() {
  const { messages, addMessage, setStatus, clearMessages } = useAgentStore()
  const [input, setInput] = useState('')
  const messageListRef = useRef<HTMLDivElement | null>(null)

  const scrollToBottom = () => {
    if (messageListRef.current) {
      messageListRef.current.scrollTop = messageListRef.current.scrollHeight
    }
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
    <div className="max-w-5xl mx-auto">
      <div className="bg-white/[0.05] backdrop-blur-xl border border-white/[0.12] rounded-2xl shadow-[0_20px_60px_-15px_rgba(0,0,0,0.5)] hover:shadow-[0_25px_70px_-15px_rgba(0,0,0,0.6)] transition-shadow duration-300 overflow-hidden ring-1 ring-white/[0.08]">
        {/* Chat header with glass morphism effect */}
        <div className="bg-gradient-to-r from-slate-800/50 to-slate-700/50 backdrop-blur-sm border-b border-white/[0.08] px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
                <svg className="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
              </div>
              <div>
                <h3 className="text-white font-semibold text-sm">Chat Assistant</h3>
                <p className="text-slate-300 text-xs">Claude 4 • Strands SDK</p>
              </div>
            </div>

            <div className="flex items-center gap-2">
              {messages.length > 0 && (
                <button
                  onClick={clearMessages}
                  className="text-slate-400 hover:text-white transition-colors p-2 hover:bg-white/[0.05] rounded-lg"
                  title="Clear conversation"
                >
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                  </svg>
                </button>
              )}
              <div className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></div>
            </div>
          </div>
        </div>

        <MessageList messages={messages} containerRef={messageListRef} isLoading={chatMutation.isPending} />
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
