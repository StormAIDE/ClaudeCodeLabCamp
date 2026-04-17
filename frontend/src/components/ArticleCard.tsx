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
  // Extract domain from URL for display
  const getDomain = (url: string) => {
    try {
      const urlObj = new URL(url);
      return urlObj.hostname.replace('www.', '');
    } catch {
      return 'Unknown source';
    }
  };

  return (
    <div className="bg-white/[0.05] backdrop-blur-xl border border-white/[0.12] rounded-lg p-4 hover:shadow-lg hover:bg-white/[0.08] transition-all duration-300">
      <div className="flex justify-between items-start mb-2">
        <h3 className="text-lg font-semibold text-white flex-1">
          <a
            href={article.url}
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-blue-400 transition-colors"
          >
            {article.title}
          </a>
        </h3>
        <span className="ml-2 px-2 py-1 bg-blue-500/20 text-blue-300 text-xs rounded-full whitespace-nowrap border border-blue-500/30">
          {article.topic}
        </span>
      </div>

      <p className="text-slate-300 text-sm mb-3">
        {article.summary}
      </p>

      {/* Source information section */}
      <div className="bg-white/[0.03] border border-white/[0.08] rounded-md p-2 mb-3">
        <div className="flex items-center gap-2 mb-1">
          <svg className="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" />
          </svg>
          <span className="text-xs font-medium text-slate-400">Source:</span>
        </div>
        <a
          href={article.url}
          target="_blank"
          rel="noopener noreferrer"
          className="text-xs text-blue-400 hover:text-blue-300 hover:underline break-all block"
        >
          {getDomain(article.url)}
        </a>
        <div className="text-[10px] text-slate-500 mt-1 truncate" title={article.url}>
          {article.url}
        </div>
      </div>

      <div className="flex justify-between items-center text-xs text-slate-500">
        <span>Published: {new Date(article.published_date).toLocaleDateString()}</span>
        <span>Fetched: {new Date(article.fetched_at).toLocaleDateString()}</span>
      </div>
    </div>
  );
};
