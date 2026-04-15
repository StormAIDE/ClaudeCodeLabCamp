---
name: component
description: Generate a React TypeScript component with Tailwind CSS
usage: /component ComponentName [description]
examples:
  - /component Button A reusable button component
  - /component UserCard Displays user information
---

# Generate React TypeScript Component

You are generating a new React TypeScript component for the ClaudeCode Lab project.

## Input Parameters

Extract the following from the user's input:
1. **ComponentName** (required): PascalCase component name (e.g., Button, UserCard, ChatMessage)
2. **description** (optional): Brief description of the component's purpose

## Component Generation Rules

### File Location
- Create file at: `/Users/ka.akhtar/ClaudeCodeTest/frontend/src/components/{ComponentName}.tsx`
- Use exact PascalCase naming for both component and filename

### Component Structure

Generate a component with the following structure:

```typescript
import { type ReactNode } from 'react'

interface {ComponentName}Props {
  // Add props based on component purpose
  // Example: children?: ReactNode
  // Example: className?: string
  // Example: onClick?: () => void
}

export default function {ComponentName}({ /* destructure props */ }: {ComponentName}Props) {
  return (
    <div className="/* Tailwind CSS classes */">
      {/* Component JSX */}
    </div>
  )
}
```

### Styling Guidelines
- **Always use Tailwind CSS** - no inline styles or CSS modules
- Use project's color scheme:
  - Background: `bg-gray-800`, `bg-gray-700`, `bg-gray-900`
  - Text: `text-white`, `text-gray-100`, `text-gray-400`
  - Primary: `bg-blue-600`, `hover:bg-blue-700`, `text-blue-200`
  - Borders: `border-gray-700`, `border-gray-600`
- Include responsive classes where appropriate
- Add hover/focus states for interactive elements

### TypeScript Best Practices
- Use `type` imports: `import { type ReactNode } from 'react'`
- Define props interface with `{ComponentName}Props` naming
- Make props optional with `?` when appropriate
- Export component as default: `export default function`

### Common Props Patterns

**For container components:**
```typescript
interface Props {
  children: ReactNode
  className?: string
}
```

**For interactive components:**
```typescript
interface Props {
  onClick?: () => void
  disabled?: boolean
  label: string
}
```

**For data display components:**
```typescript
interface Props {
  data: DataType
  onAction?: (id: string) => void
}
```

### After Generation

1. Create the component file
2. Show the user the generated code
3. Suggest where/how to import and use it
4. Offer to create a test file if requested

## Example Output

For input: `/component LoadingSpinner Shows a loading indicator`

Create: `/Users/ka.akhtar/ClaudeCodeTest/frontend/src/components/LoadingSpinner.tsx`

```typescript
interface LoadingSpinnerProps {
  size?: 'sm' | 'md' | 'lg'
  className?: string
}

export default function LoadingSpinner({ 
  size = 'md', 
  className = '' 
}: LoadingSpinnerProps) {
  const sizeClasses = {
    sm: 'w-4 h-4',
    md: 'w-8 h-8',
    lg: 'w-12 h-12',
  }

  return (
    <div className={`flex items-center justify-center ${className}`}>
      <div
        className={`${sizeClasses[size]} border-4 border-blue-600 border-t-transparent rounded-full animate-spin`}
        role="status"
        aria-label="Loading"
      />
    </div>
  )
}
```

## Important Notes

- **Do not** create test files unless explicitly requested
- **Do not** modify existing components
- **Do not** add to git or commit automatically
- **Follow** the project's existing component patterns (see MessageInput.tsx, MessageList.tsx)
- **Use** functional components only (no class components)
- **Ensure** all TypeScript types are properly defined

Now generate the component based on the user's input!
