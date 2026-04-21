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

export interface Article {
  id: number;
  title: string;
  url: string;
  summary: string;
  topic: string;
  subtopic: string;
  published_date: string | null;
  fetched_at: string | null;
}

export const ROBOTICS_SUBTOPICS = [
  'all',
  'general',
  'humanoids',
  'drones',
  'ros',
  'research',
  'industrial',
] as const;

export type RoboticsSubtopic = typeof ROBOTICS_SUBTOPICS[number];

export interface RoboticsSubtopicLabel {
  slug: RoboticsSubtopic;
  label: string;
}

export const ROBOTICS_SUBTOPIC_LABELS: RoboticsSubtopicLabel[] = [
  { slug: 'all',        label: 'All' },
  { slug: 'general',   label: 'General' },
  { slug: 'humanoids', label: 'Humanoids' },
  { slug: 'drones',    label: 'Drones' },
  { slug: 'ros',       label: 'ROS / Software' },
  { slug: 'research',  label: 'Research' },
  { slug: 'industrial',label: 'Industrial' },
];
