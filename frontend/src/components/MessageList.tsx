import { type Message } from '../store/agentStore'

interface MessageListProps {
  messages: Message[]
  containerRef?: React.RefObject<HTMLDivElement | null>
  isLoading?: boolean
}

// Avatar component for consistent user/assistant avatars
const MessageAvatar = ({ role }: { role: 'user' | 'assistant' }) => {
  if (role === 'user') {
    return (
      <div className="w-8 h-8 rounded-full bg-gradient-to-br from-blue-500 to-blue-600 flex items-center justify-center flex-shrink-0 shadow-sm shadow-blue-500/30">
        <svg className="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
        </svg>
      </div>
    )
  }

  return (
    <div className="w-8 h-8 rounded-full bg-gradient-to-br from-purple-500 to-purple-600 flex items-center justify-center flex-shrink-0 shadow-sm shadow-purple-500/30">
      <svg className="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
      </svg>
    </div>
  )
}

// Typing indicator component
const TypingIndicator = () => (
  <div className="flex items-center gap-3 mb-4 animate-fade-in">
    <MessageAvatar role="assistant" />
    <div className="bg-purple-500/10 border border-purple-500/20 rounded-2xl rounded-bl-sm px-4 py-3 max-w-[70%] backdrop-blur-sm">
      <div className="flex items-center gap-1">
        <div className="w-2 h-2 bg-purple-300 rounded-full animate-bounce"></div>
        <div className="w-2 h-2 bg-purple-300 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
        <div className="w-2 h-2 bg-purple-300 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
      </div>
    </div>
  </div>
)

export default function MessageList({ messages, containerRef, isLoading = false }: MessageListProps) {

  if (messages.length === 0) {
    return (
      <div className="h-[24rem] flex items-center justify-center">
        <div className="text-center px-6 py-8">
          <div className="w-14 h-14 mx-auto mb-5 rounded-2xl bg-gradient-to-br from-blue-500 to-purple-600 border border-blue-500/30 flex items-center justify-center animate-float shadow-lg shadow-blue-500/30">
            <svg className="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
            </svg>
          </div>

          <h3 className="text-xl font-semibold text-white mb-2">
            Welcome to Tech News Aggregator
          </h3>
          <p className="text-slate-300 mb-5 max-w-md mx-auto leading-relaxed">
            Ask me about the latest tech news and I'll search real sources for you!
          </p>

          <div className="flex flex-wrap justify-center gap-2">
            <div className="px-3 py-1.5 bg-blue-500/20 border border-blue-500/30 rounded-full text-xs text-blue-200 hover:bg-blue-500/30 hover:border-blue-500/40 transition-all duration-200 cursor-default shadow-sm shadow-blue-500/10">
              Latest AI news
            </div>
            <div className="px-3 py-1.5 bg-purple-500/20 border border-purple-500/30 rounded-full text-xs text-purple-200 hover:bg-purple-500/30 hover:border-purple-500/40 transition-all duration-200 cursor-default shadow-sm shadow-purple-500/10">
              Cloud trends
            </div>
            <div className="px-3 py-1.5 bg-emerald-500/20 border border-emerald-500/30 rounded-full text-xs text-emerald-200 hover:bg-emerald-500/30 hover:border-emerald-500/40 transition-all duration-200 cursor-default shadow-sm shadow-emerald-500/10">
              Security updates
            </div>
            <div className="px-3 py-1.5 bg-white/[0.08] border border-white/[0.15] rounded-full text-xs text-slate-300 hover:bg-white/[0.12] hover:border-white/[0.2] transition-all duration-200 cursor-default">
              Trending topics
            </div>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div ref={containerRef} className="h-[32rem] overflow-y-auto overscroll-behavior-contain px-6 py-4 space-y-6 scroll-smooth">
      {messages.map((message, index) => {
        const isUser = message.role === 'user'
        const isFirstInGroup = index === 0 || messages[index - 1]?.role !== message.role
        const isLastInGroup = index === messages.length - 1 || messages[index + 1]?.role !== message.role

        return (
          <div
            key={message.id}
            className={`flex items-start gap-3 animate-fade-in ${isUser ? 'flex-row-reverse' : 'flex-row'}`}
            style={{ animationDelay: `${index * 0.1}s` }}
          >
            {/* Avatar - only show for first message in group */}
            <div className="w-8 h-8 flex-shrink-0">
              {isFirstInGroup && <MessageAvatar role={message.role} />}
            </div>

            {/* Message bubble */}
            <div
              className={`group relative max-w-[75%] lg:max-w-[70%] ${
                isUser ? 'text-right' : 'text-left'
              }`}
            >
              {/* Message content */}
              <div
                className={`relative px-4 py-3 text-sm leading-relaxed transition-all duration-200 ${
                  isUser
                    ? 'bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-2xl rounded-br-sm shadow-lg shadow-blue-500/25'
                    : 'bg-purple-500/10 text-slate-50 border border-purple-500/20 rounded-2xl rounded-bl-sm backdrop-blur-sm'
                }`}
              >
                <div className="whitespace-pre-wrap break-words">
                  {message.content}
                </div>

                {/* Message timestamp - appears on hover */}
                <div
                  className={`absolute top-full mt-1 text-xs text-slate-500 opacity-0 group-hover:opacity-100 transition-opacity duration-200 ${
                    isUser ? 'right-0' : 'left-0'
                  }`}
                >
                  {message.timestamp.toLocaleTimeString([], {
                    hour: '2-digit',
                    minute: '2-digit'
                  })}
                </div>
              </div>

              {/* Message status indicator for user messages */}
              {isUser && isLastInGroup && (
                <div className="flex justify-end mt-1">
                  <div className="w-4 h-4 text-slate-500">
                    <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                </div>
              )}
            </div>
          </div>
        )
      })}

      {/* Typing indicator */}
      {isLoading && <TypingIndicator />}
    </div>
  )
}
