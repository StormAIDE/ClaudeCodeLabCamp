# Frontend - ClaudeCode Lab Agent

React 19 TypeScript frontend with Vite, TanStack Query, and Tailwind CSS for AI-powered chat interface.

## Setup

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Configure environment (optional):**
   - Copy `.env.example` to `.env` if you need custom API URLs

3. **Run the dev server:**
   ```bash
   npm run dev
   ```

   The app will be available at http://localhost:5173

4. **Build for production:**
   ```bash
   npm run build
   ```

## Available Scripts

- `npm run dev` - Start dev server (hot reload enabled)
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint
- `npm test` - Run Vitest unit tests
- `npm run test:ui` - Run tests with interactive UI
- `npm run test:coverage` - Generate coverage report

## Features

- Real-time chat interface with agent responses
- Agent status indicator (connected/error states)
- Auto-scroll message list
- Input validation (prevents empty messages)
- Type-safe with TypeScript
- Modern UI with Tailwind CSS
- Responsive design
- Comprehensive test coverage (30 tests)

## Tech Stack

- **React 19** - Latest React with improved hooks
- **TypeScript** - Full type safety
- **Vite** - Fast build tool with HMR
- **TanStack Query** - Server state management and caching
- **Zustand** - Client state management
- **Axios** - HTTP client for API calls
- **Tailwind CSS** - Utility-first styling
- **Vitest** - Fast unit testing framework
- **Testing Library** - Component testing utilities

## Project Structure

```
frontend/
├── src/
│   ├── components/         # React components
│   │   ├── ChatInterface.tsx     # Main chat UI
│   │   ├── MessageList.tsx       # Message display
│   │   ├── MessageInput.tsx      # Input field
│   │   └── StatusBadge.tsx       # Agent status
│   ├── api/
│   │   └── agent.ts        # API client (Axios)
│   ├── store/
│   │   └── agentStore.ts   # Zustand state management
│   ├── types/              # TypeScript type definitions
│   ├── hooks/              # Custom React hooks
│   ├── App.tsx            # Main app component
│   └── main.tsx           # Entry point with QueryClientProvider
├── public/                 # Static assets
├── tests/                  # Test files
└── vite.config.ts         # Vite configuration
```

## API Integration

The frontend communicates with the backend at `http://localhost:8000` via proxy configuration in `vite.config.ts`.

### Endpoints Used

- `GET /api/v1/agent/status` - Get agent status
- `POST /api/v1/agent/chat` - Send message to agent (supports streaming)

### Example API Call

```typescript
import { chatWithAgent } from './api/agent';

const response = await chatWithAgent({
  message: "Hello, agent!",
  stream: false
});

console.log(response.data.response);
```

## State Management

### Zustand Store (`store/agentStore.ts`)

Manages client-side state:
- Messages array
- Agent status (ready, thinking, error)
- Add/clear message actions

```typescript
const { messages, status, addMessage, setStatus } = useAgentStore();
```

### TanStack Query

Handles server state:
- Automatic caching
- Request deduplication
- Background refetching
- Mutation handling

## Testing

### Run Tests

```bash
npm test                 # Run all tests
npm test -- --watch      # Watch mode
npm run test:ui          # Interactive UI
npm run test:coverage    # With coverage report
```

### Test Coverage

- **30 tests** covering:
  - API client (`agent.test.ts`)
  - Zustand store (`agentStore.test.ts`)
  - Components (`MessageInput.test.tsx`, `MessageList.test.tsx`)
  - Dependencies (`dependencies.test.ts`)

### Writing Tests

Tests use Vitest and React Testing Library:

```typescript
import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';

describe('MyComponent', () => {
  it('renders correctly', () => {
    render(<MyComponent />);
    expect(screen.getByText('Hello')).toBeInTheDocument();
  });
});
```

## Development

### Hot Module Replacement (HMR)

Vite provides instant HMR - changes appear immediately without full page reload.

### Type Checking

TypeScript is configured in `tsconfig.json`:
- Strict mode enabled
- React 19 JSX runtime
- Path aliases configured

### Linting

ESLint configured with:
- TypeScript support
- React hooks rules
- Recommended best practices

Run linter:
```bash
npm run lint
```

## Building for Production

```bash
npm run build
```

Output will be in `dist/` directory:
- Optimized bundles
- Minified code
- Tree-shaking applied
- Assets with cache-busting hashes

Preview production build:
```bash
npm run preview
```

## Styling

Tailwind CSS utility classes are used throughout:
- `bg-*` - Background colors
- `text-*` - Text colors and sizes
- `p-*`, `m-*` - Padding and margins
- `flex`, `grid` - Layout
- `rounded-*` - Border radius
- `shadow-*` - Shadows

Custom configuration in `tailwind.config.js`.

## Environment Variables

Optional `.env` file:
```
VITE_API_URL=http://localhost:8000
```

Access in code:
```typescript
const apiUrl = import.meta.env.VITE_API_URL;
```

## Important Notes

- **Port 5173**: Default Vite dev server port (configurable in `vite.config.ts`)
- **API Proxy**: `/api` requests proxied to backend (see `vite.config.ts`)
- **React 19**: Uses latest React features and JSX runtime
- **Type Safety**: All components and functions are fully typed

## Next Steps

- Implement streaming support for real-time responses
- Add message history persistence (localStorage or database)
- Implement markdown rendering for agent responses
- Add dark mode toggle
- Add loading skeleton for better perceived performance
- Implement message retry functionality
