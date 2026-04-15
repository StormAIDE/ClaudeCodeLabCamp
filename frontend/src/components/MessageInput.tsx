import { type KeyboardEvent, useRef, useEffect } from 'react'

interface MessageInputProps {
  value: string
  onChange: (value: string) => void
  onSend: () => void
  disabled: boolean
}

export default function MessageInput({ value, onChange, onSend, disabled }: MessageInputProps) {
  const textareaRef = useRef<HTMLTextAreaElement>(null)

  const handleKeyPress = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      onSend()
    }
  }

  // Auto-resize textarea based on content
  useEffect(() => {
    const textarea = textareaRef.current
    if (textarea) {
      textarea.style.height = 'auto'
      textarea.style.height = `${Math.min(textarea.scrollHeight, 120)}px`
    }
  }, [value])

  const canSend = !disabled && value.trim().length > 0

  return (
    <div className="border-t border-white/[0.08] bg-slate-800/30 backdrop-blur-sm">
      <div className="p-4 lg:p-6">
        <div className="flex items-end gap-3">
          {/* Input area with modern styling */}
          <div className="flex-1 relative">
            <textarea
              ref={textareaRef}
              id="message-input"
              name="message"
              value={value}
              onChange={(e) => onChange(e.target.value)}
              onKeyDown={handleKeyPress}
              placeholder="Type your message... (Shift+Enter for new line)"
              disabled={disabled}
              aria-label="Message input"
              className="w-full bg-white/[0.05] border border-white/[0.08] text-white placeholder-slate-400 rounded-2xl px-4 py-3 pr-12 focus:outline-none focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500/50 disabled:opacity-50 resize-none transition-all duration-200 backdrop-blur-sm min-h-[3rem] max-h-[7.5rem]"
              rows={1}
            />

            {/* Character count indicator */}
            {value.length > 0 && (
              <div className="absolute bottom-2 right-12 text-xs text-slate-500">
                {value.length}
              </div>
            )}

            {/* Input actions */}
            <div className="absolute right-2 bottom-2 flex items-center gap-1">
              {/* Clear button */}
              {value.length > 0 && !disabled && (
                <button
                  onClick={() => onChange('')}
                  className="w-6 h-6 rounded-full hover:bg-white/[0.1] text-slate-400 hover:text-slate-300 transition-colors flex items-center justify-center"
                  title="Clear message"
                >
                  <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              )}
            </div>
          </div>

          {/* Send button with improved design */}
          <button
            onClick={onSend}
            disabled={!canSend}
            className={`relative overflow-hidden rounded-2xl px-6 py-3 font-medium transition-all duration-200 flex items-center gap-2 min-w-[5rem] ${
              canSend
                ? 'bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white shadow-lg shadow-blue-500/25 hover:shadow-blue-500/40 transform hover:scale-[1.02]'
                : 'bg-white/[0.05] border border-white/[0.08] text-slate-500 cursor-not-allowed'
            }`}
          >
            {disabled ? (
              <>
                <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
                <span className="hidden sm:inline">Sending</span>
              </>
            ) : (
              <>
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                </svg>
                <span className="hidden sm:inline">Send</span>
              </>
            )}

            {/* Ripple effect on click */}
            {canSend && (
              <div className="absolute inset-0 -z-10">
                <div className="absolute inset-0 bg-white/20 rounded-2xl opacity-0 hover:opacity-100 transition-opacity duration-200"></div>
              </div>
            )}
          </button>
        </div>

        {/* Input hints */}
        <div className="flex items-center justify-between mt-3 text-xs text-slate-500">
          <div className="flex items-center gap-4">
            <span>Press Enter to send, Shift+Enter for new line</span>
          </div>

          {disabled && (
            <div className="flex items-center gap-1 text-blue-400">
              <div className="w-2 h-2 bg-blue-400 rounded-full animate-pulse"></div>
              <span>AI is typing...</span>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
