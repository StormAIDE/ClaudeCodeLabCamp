/**
 * API-related TypeScript types
 */

export interface ChatRequest {
  message: string;
  conversation_id?: string;
}

export interface ChatResponse {
  response: string;
  conversation_id: string;
}

export interface AgentInfo {
  id: string;
  name: string;
  description: string;
  capabilities?: string[];
  status?: string;
}

export interface ApiError {
  detail: string;
  error?: string;
}
