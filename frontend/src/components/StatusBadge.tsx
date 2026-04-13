import { type ReactNode } from 'react'

interface StatusBadgeProps {
  status: 'success' | 'warning' | 'error' | 'info'
  children: ReactNode
  size?: 'sm' | 'md' | 'lg'
  className?: string
}

export default function StatusBadge({
  status,
  children,
  size = 'md',
  className = ''
}: StatusBadgeProps) {
  const statusClasses = {
    success: 'bg-green-900 text-green-200',
    warning: 'bg-yellow-900 text-yellow-200',
    error: 'bg-red-900 text-red-200',
    info: 'bg-blue-900 text-blue-200',
  }

  const sizeClasses = {
    sm: 'px-2 py-1 text-xs',
    md: 'px-3 py-1 text-sm',
    lg: 'px-4 py-2 text-base',
  }

  const dotClasses = {
    success: 'bg-green-400',
    warning: 'bg-yellow-400',
    error: 'bg-red-400',
    info: 'bg-blue-400',
  }

  const dotSizeClasses = {
    sm: 'w-1.5 h-1.5',
    md: 'w-2 h-2',
    lg: 'w-2.5 h-2.5',
  }

  return (
    <span
      className={`inline-flex items-center rounded-full font-medium ${statusClasses[status]} ${sizeClasses[size]} ${className}`}
    >
      <span className={`${dotClasses[status]} ${dotSizeClasses[size]} rounded-full mr-2`}></span>
      {children}
    </span>
  )
}
