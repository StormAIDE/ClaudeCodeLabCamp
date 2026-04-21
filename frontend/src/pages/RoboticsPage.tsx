import React, { useState } from 'react';
import { ArticleCard } from '../components/ArticleCard';
import { useRoboticsNews } from '../hooks/useRoboticsNews';
import { ROBOTICS_SUBTOPIC_LABELS, type RoboticsSubtopic } from '../types/api';

// ── Skeleton ──────────────────────────────────────────────────────────────────
function ArticleCardSkeleton() {
  return (
    <div className="bg-white/[0.05] backdrop-blur-xl border border-white/[0.12] rounded-lg p-4 animate-pulse">
      <div className="flex justify-between items-start mb-2">
        <div className="h-5 bg-white/[0.1] rounded w-3/4" />
        <div className="h-5 bg-blue-500/20 rounded-full w-16 ml-2" />
      </div>
      <div className="space-y-2 mb-3">
        <div className="h-3 bg-white/[0.07] rounded w-full" />
        <div className="h-3 bg-white/[0.07] rounded w-5/6" />
        <div className="h-3 bg-white/[0.07] rounded w-4/6" />
      </div>
      <div className="bg-white/[0.03] border border-white/[0.08] rounded-md p-2 mb-3">
        <div className="h-3 bg-white/[0.07] rounded w-1/3" />
      </div>
      <div className="flex justify-between">
        <div className="h-3 bg-white/[0.05] rounded w-24" />
        <div className="h-3 bg-white/[0.05] rounded w-24" />
      </div>
    </div>
  );
}

// ── Filter Chips ──────────────────────────────────────────────────────────────
interface FilterChipsProps {
  active: RoboticsSubtopic;
  onChange: (slug: RoboticsSubtopic) => void;
}

function RoboticsFilterChips({ active, onChange }: FilterChipsProps) {
  return (
    <div className="sticky top-0 z-20 bg-slate-900/80 backdrop-blur-xl border-b border-white/[0.08] py-3 px-4 -mx-4">
      <div className="flex gap-2 overflow-x-auto pb-1 [scrollbar-width:none] [-webkit-overflow-scrolling:touch]">
        {ROBOTICS_SUBTOPIC_LABELS.map(({ slug, label }) => (
          <button
            key={slug}
            onClick={() => onChange(slug)}
            aria-pressed={active === slug}
            className={`
              flex-shrink-0 px-4 py-1.5 rounded-full text-sm font-medium border
              transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500/50
              ${active === slug
                ? 'bg-blue-500/30 text-blue-200 border-blue-500/50 shadow-[0_0_12px_rgba(59,130,246,0.2)]'
                : 'bg-white/[0.05] text-slate-400 border-white/[0.12] hover:bg-white/[0.08] hover:text-white'
              }
            `}
          >
            {label}
          </button>
        ))}
      </div>
    </div>
  );
}

// ── Empty State ───────────────────────────────────────────────────────────────
function EmptyState() {
  return (
    <div className="text-center py-16 bg-white/[0.03] rounded-xl border-2 border-dashed border-white/[0.12]">
      <div className="w-16 h-16 mx-auto mb-4 rounded-full bg-gradient-to-br from-blue-500/20 to-purple-600/20 flex items-center justify-center border border-white/[0.1]">
        <svg className="w-8 h-8 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5}
            d="M9 3H5a2 2 0 00-2 2v4m6-6h10a2 2 0 012 2v4M9 3v18m0 0h10a2 2 0 002-2V9M9 21H5a2 2 0 01-2-2V9m0 0h18" />
        </svg>
      </div>
      <p className="text-slate-300 font-medium mb-2">No articles found</p>
      <p className="text-slate-500 text-sm">
        Try a different filter or check back after the next refresh.
      </p>
    </div>
  );
}

// ── Error State ───────────────────────────────────────────────────────────────
interface ErrorStateProps {
  message: string;
  onRetry: () => void;
}

function ErrorState({ message, onRetry }: ErrorStateProps) {
  return (
    <div className="text-center py-16 bg-red-500/[0.05] rounded-xl border border-red-500/20">
      <p className="text-red-300 font-medium mb-4">{message}</p>
      <button
        onClick={onRetry}
        className="px-4 py-2 bg-red-500/20 hover:bg-red-500/30 text-red-300 rounded-lg border border-red-500/30 transition-colors text-sm"
      >
        Try again
      </button>
    </div>
  );
}

// ── Main Page ─────────────────────────────────────────────────────────────────
const SKELETON_COUNT = 6;

export function RoboticsPage() {
  const [activeSubtopic, setActiveSubtopic] = useState<RoboticsSubtopic>('all');
  const { articles, isLoading, isFetching, isError, error, refetch } = useRoboticsNews(activeSubtopic);

  return (
    <div className="relative z-10">
      <header className="mb-6 text-center">
        <div className="inline-flex items-center gap-3 mb-4">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center shadow-lg shadow-blue-500/30">
            <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2}
                d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
          </div>
          <h1 className="text-3xl lg:text-4xl font-bold text-white tracking-tight">
            Robotics News
          </h1>
        </div>
        <p className="text-slate-400 text-lg max-w-2xl mx-auto">
          Latest developments in robotics — humanoids, drones, ROS, and more
        </p>
        {isFetching && !isLoading && (
          <span className="inline-flex items-center gap-1.5 mt-3 px-3 py-1 rounded-full text-xs bg-blue-500/10 text-blue-400 border border-blue-500/20">
            <div className="w-1.5 h-1.5 rounded-full bg-blue-400 animate-pulse" />
            Refreshing…
          </span>
        )}
      </header>

      <RoboticsFilterChips active={activeSubtopic} onChange={setActiveSubtopic} />

      <main className="mt-6">
        {isError && (
          <ErrorState
            message={error?.message ?? 'Failed to load robotics news.'}
            onRetry={refetch}
          />
        )}

        {isLoading && (
          <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
            {Array.from({ length: SKELETON_COUNT }).map((_, i) => (
              <ArticleCardSkeleton key={i} />
            ))}
          </div>
        )}

        {!isLoading && !isError && articles.length === 0 && <EmptyState />}

        {!isLoading && !isError && articles.length > 0 && (
          <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
            {articles.map((article) => (
              <ArticleCard
                key={article.id}
                article={{
                  ...article,
                  published_date: article.published_date ?? '',
                  fetched_at: article.fetched_at ?? '',
                }}
              />
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
