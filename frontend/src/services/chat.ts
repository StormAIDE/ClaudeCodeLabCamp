/**
 * Chat API service with SSE streaming support
 */
import { apiClient } from './api';
import type { ChatRequest, ChatResponse, AgentInfo } from '../types/api';
import type { StreamChunk } from '../types/chat';

/**
 * Send a chat message and get complete response (non-streaming)
 */
export async function sendMessage(request: ChatRequest): Promise<ChatResponse> {
  const response = await apiClient.post<ChatResponse>('/api/v1/chat/message', request);
  return response.data;
}

/**
 * Stream chat responses using Server-Sent Events
 */
export async function* streamChatMessage(
  request: ChatRequest
): AsyncGenerator<StreamChunk, void, unknown> {
  const response = await fetch('/api/v1/chat/stream', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(request),
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  const reader = response.body?.getReader();
  const decoder = new TextDecoder();

  if (!reader) {
    throw new Error('Response body is not readable');
  }

  let buffer = '';

  try {
    while (true) {
      const { done, value } = await reader.read();

      if (done) {
        break;
      }

      buffer += decoder.decode(value, { stream: true });

      // Split by double newline (SSE event separator)
      const events = buffer.split('\n\n');
      buffer = events.pop() || '';

      for (const event of events) {
        if (!event.trim()) continue;

        // Parse SSE format: "event: message\ndata: {...}"
        const lines = event.split('\n');
        let data = '';

        for (const line of lines) {
          if (line.startsWith('data:')) {
            data = line.substring(5).trim();
          }
        }

        if (data) {
          try {
            const chunk: StreamChunk = JSON.parse(data);
            yield chunk;

            if (chunk.done) {
              return;
            }
          } catch (e) {
            console.error('Failed to parse SSE data:', e);
          }
        }
      }
    }
  } finally {
    reader.releaseLock();
  }
}

/**
 * Get list of available agents
 */
export async function getAgents(): Promise<AgentInfo[]> {
  const response = await apiClient.get<{ agents: AgentInfo[] }>('/api/v1/agents');
  return response.data.agents;
}
