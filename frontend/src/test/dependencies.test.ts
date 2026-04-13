import { describe, it, expect } from 'vitest'

/**
 * Tests to verify all required dependencies are installed and importable
 */

describe('frontend dependencies', () => {
  it('should import react', async () => {
    const React = await import('react')
    expect(React).toBeDefined()
    expect(React.useState).toBeDefined()
    expect(React.useEffect).toBeDefined()
  })

  it('should import react-dom', async () => {
    const ReactDOM = await import('react-dom')
    expect(ReactDOM).toBeDefined()
  })

  it('should import axios', async () => {
    const axios = await import('axios')
    expect(axios.default).toBeDefined()
    expect(axios.default.create).toBeDefined()
  })

  it('should import zustand', async () => {
    const { create } = await import('zustand')
    expect(create).toBeDefined()
  })

  it('should import @tanstack/react-query', async () => {
    const TanstackQuery = await import('@tanstack/react-query')
    expect(TanstackQuery.QueryClient).toBeDefined()
    expect(TanstackQuery.QueryClientProvider).toBeDefined()
    expect(TanstackQuery.useMutation).toBeDefined()
  })

  it('should import @testing-library/react', async () => {
    const TestingLibrary = await import('@testing-library/react')
    expect(TestingLibrary.render).toBeDefined()
    expect(TestingLibrary.screen).toBeDefined()
    expect(TestingLibrary.fireEvent).toBeDefined()
  })

  it('should import @testing-library/user-event', async () => {
    const userEvent = await import('@testing-library/user-event')
    expect(userEvent.default).toBeDefined()
  })

  it('should import @testing-library/jest-dom', async () => {
    const jestDom = await import('@testing-library/jest-dom/matchers')
    expect(jestDom).toBeDefined()
  })

  it('should import vitest', async () => {
    const { describe, it, expect, vi } = await import('vitest')
    expect(describe).toBeDefined()
    expect(it).toBeDefined()
    expect(expect).toBeDefined()
    expect(vi).toBeDefined()
  })
})
