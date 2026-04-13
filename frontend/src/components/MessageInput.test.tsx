import { describe, it, expect, vi } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import MessageInput from './MessageInput'

describe('MessageInput', () => {
  it('should render input and button', () => {
    render(
      <MessageInput
        value=""
        onChange={() => {}}
        onSend={() => {}}
        disabled={false}
      />
    )

    expect(screen.getByPlaceholderText(/type your message/i)).toBeInTheDocument()
    expect(screen.getByRole('button')).toBeInTheDocument()
  })

  it('should call onChange when typing', async () => {
    const user = userEvent.setup()
    const handleChange = vi.fn()

    render(
      <MessageInput
        value=""
        onChange={handleChange}
        onSend={() => {}}
        disabled={false}
      />
    )

    const input = screen.getByPlaceholderText(/type your message/i)
    await user.type(input, 'Hello')

    // onChange is called for each character typed
    expect(handleChange).toHaveBeenCalled()
  })

  it('should call onSend when button is clicked', () => {
    const handleSend = vi.fn()

    render(
      <MessageInput
        value="Test message"
        onChange={() => {}}
        onSend={handleSend}
        disabled={false}
      />
    )

    const button = screen.getByRole('button')
    fireEvent.click(button)

    expect(handleSend).toHaveBeenCalledTimes(1)
  })

  it('should call onSend when Enter key is pressed', () => {
    const handleSend = vi.fn()

    render(
      <MessageInput
        value="Test message"
        onChange={() => {}}
        onSend={handleSend}
        disabled={false}
      />
    )

    const input = screen.getByPlaceholderText(/type your message/i)
    fireEvent.keyPress(input, { key: 'Enter', code: 'Enter', charCode: 13 })

    expect(handleSend).toHaveBeenCalledTimes(1)
  })

  it('should not call onSend on Shift+Enter', () => {
    const handleSend = vi.fn()

    render(
      <MessageInput
        value="Test message"
        onChange={() => {}}
        onSend={handleSend}
        disabled={false}
      />
    )

    const input = screen.getByPlaceholderText(/type your message/i)
    fireEvent.keyPress(input, { key: 'Enter', code: 'Enter', charCode: 13, shiftKey: true })

    expect(handleSend).not.toHaveBeenCalled()
  })

  it('should disable input and button when disabled prop is true', () => {
    render(
      <MessageInput
        value=""
        onChange={() => {}}
        onSend={() => {}}
        disabled={true}
      />
    )

    const input = screen.getByPlaceholderText(/type your message/i)
    const button = screen.getByRole('button')

    expect(input).toBeDisabled()
    expect(button).toBeDisabled()
  })

  it('should display the value prop', () => {
    render(
      <MessageInput
        value="Current message"
        onChange={() => {}}
        onSend={() => {}}
        disabled={false}
      />
    )

    const input = screen.getByPlaceholderText(/type your message/i) as HTMLInputElement
    expect(input.value).toBe('Current message')
  })
})
