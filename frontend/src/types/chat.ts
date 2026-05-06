/**
 * Chat-related TypeScript types
 */

export interface Message {
  id: string;
  content: string;
  role: 'user' | 'assistant';
  timestamp: Date;
}

export interface ChatState {
  messages: Message[];
  isStreaming: boolean;
  error: string | null;
}

export interface StreamChunk {
  type: 'chunk' | 'done';
  content: string;
  done: boolean;
  conversation_id?: string;
}
