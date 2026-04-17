import { useState } from 'react'
import ChatInterface from './components/ChatInterface'
import { NewsFeed } from './components/NewsFeed'
import { useAgentStore } from './store/agentStore'

function App() {
  const { status, messages } = useAgentStore()
  const [selectedTopic, setSelectedTopic] = useState<string>('All')

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 relative overflow-hidden">
      {/* Background decorative elements - boosted opacity for more vibrancy */}
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_theme(colors.slate.700/0.03)_1px,_transparent_1px)] bg-[length:60px_60px] opacity-50" />
      <div className="absolute top-0 left-0 w-96 h-96 bg-blue-500/20 rounded-full -translate-x-1/2 -translate-y-1/2 blur-3xl" />
      <div className="absolute bottom-0 right-0 w-96 h-96 bg-purple-500/20 rounded-full translate-x-1/2 translate-y-1/2 blur-3xl" />

      <div className="relative z-10 container mx-auto px-4 py-6 lg:py-8">
        <header className="mb-6 lg:mb-8 text-center">
          <div className="inline-flex items-center gap-3 mb-4">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center shadow-lg">
              <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
            </div>
            <h1 className="text-3xl lg:text-4xl font-bold text-white tracking-tight">
              Tech News Aggregator
            </h1>
          </div>

          <p className="text-slate-400 text-lg mb-4 max-w-2xl mx-auto">
            Stay updated with the latest tech news - AI, Cloud, DevOps, and more
          </p>

          <div className="flex items-center justify-center gap-4">
            <div className={`inline-flex items-center px-4 py-2 rounded-full text-sm font-medium transition-all duration-300 ${
              status === 'ready'
                ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                : status === 'loading'
                ? 'bg-blue-500/20 text-blue-300 border border-blue-500/30'
                : 'bg-amber-500/20 text-amber-300 border border-amber-500/30'
            }`}>
              <div className={`w-2 h-2 rounded-full mr-2 animate-pulse ${
                status === 'ready'
                  ? 'bg-emerald-400'
                  : status === 'loading'
                  ? 'bg-blue-400'
                  : 'bg-amber-400'
              }`}></div>
              {status === 'ready' ? 'Ready to chat' : status === 'loading' ? 'Processing...' : 'Initializing...'}
            </div>

            {messages.length > 0 && (
              <div className="text-sm text-slate-500">
                {messages.length} message{messages.length !== 1 ? 's' : ''}
              </div>
            )}
          </div>
        </header>

        <main className="relative grid lg:grid-cols-2 gap-6">
          <div className="order-2 lg:order-1">
            <ChatInterface selectedTopic={selectedTopic} />
          </div>
          <div className="order-1 lg:order-2">
            <NewsFeed selectedTopic={selectedTopic} />
          </div>
        </main>
      </div>
    </div>
  )
}

export default App
