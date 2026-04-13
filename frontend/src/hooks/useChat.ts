/**
 * Custom hook for chat functionality
 */
import { useState } from 'react';
import { useChatStore } from '../store/chatStore';
import { streamChatMessage } from '../services/chat';
import type { Message } from '../types/chat';

export function useChat() {
  const {
    messages,
    isStreaming,
    error,
    conversationId,
    addMessage,
    appendToLastMessage,
    setStreaming,
    setError,
    setConversationId,
    clearMessages,
  } = useChatStore();

  const [inputValue, setInputValue] = useState('');

  const sendMessage = async (content: string) => {
    if (!content.trim() || isStreaming) {
      return;
    }

    // Clear any previous errors
    setError(null);

    // Add user message
    const userMessage: Message = {
      id: `user-${Date.now()}`,
      content: content.trim(),
      role: 'user',
      timestamp: new Date(),
    };
    addMessage(userMessage);

    // Create assistant message placeholder
    const assistantMessage: Message = {
      id: `assistant-${Date.now()}`,
      content: '',
      role: 'assistant',
      timestamp: new Date(),
    };
    addMessage(assistantMessage);

    // Start streaming
    setStreaming(true);
    setInputValue('');

    try {
      const stream = streamChatMessage({
        message: content.trim(),
        conversation_id: conversationId || undefined,
      });

      for await (const chunk of stream) {
        if (chunk.type === 'chunk') {
          appendToLastMessage(chunk.content);
        } else if (chunk.type === 'done') {
          if (chunk.conversation_id) {
            setConversationId(chunk.conversation_id);
          }
          break;
        }
      }
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'An error occurred';
      setError(errorMessage);
      appendToLastMessage(`\n\n[Error: ${errorMessage}]`);
    } finally {
      setStreaming(false);
    }
  };

  return {
    messages,
    isStreaming,
    error,
    inputValue,
    setInputValue,
    sendMessage,
    clearMessages,
  };
}
