import React from 'react';

interface Article {
  id: number;
  title: string;
  url: string;
  summary: string;
  topic: string;
  published_date: string;
  fetched_at: string;
}

interface ArticleCardProps {
  article: Article;
}

export const ArticleCard: React.FC<ArticleCardProps> = ({ article }) => {
  return (
    <div className="bg-white border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
      <div className="flex justify-between items-start mb-2">
        <h3 className="text-lg font-semibold text-gray-900 flex-1">
          <a
            href={article.url}
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-blue-600 transition-colors"
          >
            {article.title}
          </a>
        </h3>
        <span className="ml-2 px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full whitespace-nowrap">
          {article.topic}
        </span>
      </div>

      <p className="text-gray-600 text-sm mb-3">
        {article.summary}
      </p>

      <div className="flex justify-between items-center text-xs text-gray-500">
        <span>Published: {new Date(article.published_date).toLocaleDateString()}</span>
        <span>Fetched: {new Date(article.fetched_at).toLocaleDateString()}</span>
      </div>
    </div>
  );
};
