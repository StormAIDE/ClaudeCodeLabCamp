import { useQuery } from '@tanstack/react-query';
import { fetchRoboticsArticles } from '../api/robotics';
import type { Article, RoboticsSubtopic } from '../types/api';

const REFRESH_INTERVAL_MS = 60 * 1000;

export interface UseRoboticsNewsResult {
  articles: Article[];
  isLoading: boolean;
  isFetching: boolean;
  isError: boolean;
  error: Error | null;
  refetch: () => void;
}

export function useRoboticsNews(subtopic: RoboticsSubtopic): UseRoboticsNewsResult {
  const { data, isLoading, isFetching, isError, error, refetch } = useQuery({
    queryKey: ['robotics', subtopic],
    queryFn: () => fetchRoboticsArticles(subtopic),
    refetchInterval: REFRESH_INTERVAL_MS,
    staleTime: REFRESH_INTERVAL_MS,
  });

  return {
    articles: data ?? [],
    isLoading,
    isFetching,
    isError,
    error: isError ? (error as Error) : null,
    refetch,
  };
}
