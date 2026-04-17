import React, { useState, useEffect } from 'react';
import { ArticleCard } from './ArticleCard';
import { TopicFilter } from './TopicFilter';
import axios from 'axios';

interface Article {
  id: number;
  title: string;
  url: string;
  summary: string;
  topic: string;
  published_date: string;
  fetched_at: string;
}

export const NewsFeed: React.FC = () => {
  const [articles, setArticles] = useState<Article[]>([]);
  const [selectedTopic, setSelectedTopic] = useState<string>('All');
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const fetchArticles = async (topic: string) => {
    setLoading(true);
    setError(null);

    try {
      const params = topic !== 'All' ? { topic, days: 7 } : { days: 7 };
      const response = await axios.get('/api/v1/news', { params });
      setArticles(response.data);
    } catch (err) {
      setError('Failed to fetch articles. Please try again.');
      console.error('Error fetching articles:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchArticles(selectedTopic);
  }, [selectedTopic]);

  return (
    <div className="w-full max-w-4xl mx-auto p-4">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Tech News Feed</h2>
        <TopicFilter selectedTopic={selectedTopic} onTopicChange={setSelectedTopic} />
      </div>

      {loading && (
        <div className="text-center py-8">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="text-gray-600 mt-4">Loading articles...</p>
        </div>
      )}

      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-4">
          <p className="text-red-800">{error}</p>
        </div>
      )}

      {!loading && !error && articles.length === 0 && (
        <div className="text-center py-8">
          <p className="text-gray-600">No articles found for this topic.</p>
        </div>
      )}

      <div className="space-y-4">
        {articles.map((article) => (
          <ArticleCard key={article.id} article={article} />
        ))}
      </div>
    </div>
  );
};
