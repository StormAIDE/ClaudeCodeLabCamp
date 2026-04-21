import axios from 'axios';
import type { Article, RoboticsSubtopic } from '../types/api';

const api = axios.create({
  baseURL: '/api/v1',
  headers: { 'Content-Type': 'application/json' },
});

export async function fetchRoboticsArticles(
  subtopic: RoboticsSubtopic,
  limit = 20,
): Promise<Article[]> {
  const params: Record<string, string | number> =
    subtopic === 'all' ? { limit } : { subtopic, limit };
  const response = await api.get<Article[]>('/robotics', { params });
  return response.data;
}

export async function fetchRoboticsSubtopics(): Promise<string[]> {
  const response = await api.get<string[]>('/robotics/subtopics');
  return response.data;
}
