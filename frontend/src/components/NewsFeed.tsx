import React from 'react';
import { ArticleCard } from './ArticleCard';
import { useAgentStore } from '../store/agentStore';

interface Article {
  id?: number;
  title: string;
  url: string;
  summary: string;
  topic?: string;
  published_date: string;
  fetched_at?: string;
}

interface NewsFeedProps {
  selectedTopic: string;
}

export const NewsFeed: React.FC<NewsFeedProps> = ({ selectedTopic }) => {
  const { sources } = useAgentStore();

  return (
    <div className="w-full max-w-4xl mx-auto p-4">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">
          {sources.length > 0 ? 'Sources Used' : 'Sources'}
        </h2>
        <p className="text-sm text-gray-600">
          {sources.length > 0
            ? `${sources.length} source${sources.length > 1 ? 's' : ''} used for your query`
            : 'Ask a question to see sources'}
        </p>
      </div>

      {sources.length === 0 && (
        <div className="text-center py-12 bg-gray-50 rounded-lg border-2 border-dashed border-gray-300">
          <svg className="w-16 h-16 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <p className="text-gray-600 font-medium mb-2">No sources yet</p>
          <p className="text-gray-500 text-sm">
            Ask about tech news in the chat and<br />
            sources will appear here
          </p>
        </div>
      )}

      <div className="space-y-4">
        {sources.map((article: Article, index: number) => (
          <ArticleCard
            key={article.id || index}
            article={{
              ...article,
              id: article.id || index,
              topic: article.topic || 'General',
              fetched_at: article.fetched_at || new Date().toISOString()
            }}
          />
        ))}
      </div>
    </div>
  );
};
