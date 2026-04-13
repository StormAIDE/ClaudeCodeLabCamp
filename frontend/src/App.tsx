import ChatInterface from './components/ChatInterface'
import { useAgentStore } from './store/agentStore'

function App() {
  const { status } = useAgentStore()

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900">
      <div className="container mx-auto px-4 py-8">
        <header className="mb-8 text-center">
          <h1 className="text-4xl font-bold text-white mb-2">
            ClaudeCode Lab Agent
          </h1>
          <p className="text-gray-400">
            AI Assistant powered by Claude 4 via Strands SDK
          </p>
          <div className="mt-4">
            <span className={`inline-flex items-center px-3 py-1 rounded-full text-sm font-medium ${
              status === 'ready' ? 'bg-green-900 text-green-200' : 'bg-yellow-900 text-yellow-200'
            }`}>
              <span className={`w-2 h-2 rounded-full mr-2 ${
                status === 'ready' ? 'bg-green-400' : 'bg-yellow-400'
              }`}></span>
              {status === 'ready' ? 'Ready' : 'Initializing...'}
            </span>
          </div>
        </header>

        <main>
          <ChatInterface />
        </main>
      </div>
    </div>
  )
}

export default App
