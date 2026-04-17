import React from 'react';

interface TopicFilterProps {
  selectedTopic: string;
  onTopicChange: (topic: string) => void;
}

const TOPICS = [
  'All',
  'AI/ML',
  'Cloud/DevOps',
  'Web Development',
  'Mobile',
  'Security',
  'Data Science'
];

export const TopicFilter: React.FC<TopicFilterProps> = ({ selectedTopic, onTopicChange }) => {
  return (
    <div className="flex flex-wrap gap-2 mb-4">
      {TOPICS.map((topic) => (
        <button
          key={topic}
          onClick={() => onTopicChange(topic)}
          className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
            selectedTopic === topic
              ? 'bg-blue-600 text-white'
              : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
          }`}
        >
          {topic}
        </button>
      ))}
    </div>
  );
};
