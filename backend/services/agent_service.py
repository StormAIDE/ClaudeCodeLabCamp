"""
Agent service for managing AI agent interactions using Strands SDK.
"""
from strands import Agent, tool
import logging
import ast
import operator
from backend.config import settings

logger = logging.getLogger(__name__)


@tool
def get_weather(location: str) -> str:
    """
    Get the current weather for a location.

    Args:
        location: The city or location to get weather for

    Returns:
        Weather information as a string
    """
    # Mock implementation - replace with actual weather API
    return f"The weather in {location} is sunny and 72°F"


@tool
def calculate(expression: str) -> str:
    """
    Evaluate a mathematical expression safely using AST.

    Args:
        expression: The mathematical expression to evaluate

    Returns:
        The result of the calculation
    """
    # Define allowed operators
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    def eval_node(node):
        if isinstance(node, ast.Constant):  # Python 3.8+
            return node.value
        elif isinstance(node, ast.BinOp):
            left = eval_node(node.left)
            right = eval_node(node.right)
            op = allowed_operators.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
            return op(left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = eval_node(node.operand)
            op = allowed_operators.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
            return op(operand)
        else:
            raise ValueError(f"Unsupported expression: {type(node).__name__}")

    try:
        tree = ast.parse(expression, mode='eval')
        result = eval_node(tree.body)
        return f"The result is: {result}"
    except Exception as e:
        return f"Error calculating: {str(e)}"


class AgentService:
    """Service for managing AI agent interactions."""

    def __init__(self):
        """Initialize the agent with Strands SDK."""
        self.agent = Agent(
            name="lab-assistant",
            model=settings.CLAUDE_MODEL_ID,
            system_prompt="""You are a helpful AI assistant for the ClaudeCode Labcamp project.
            You can help with weather information, calculations, and general questions.
            Be concise and friendly in your responses.""",
            tools=[get_weather, calculate]
        )
        logger.info(f"Initialized agent with model: {settings.CLAUDE_MODEL_ID}")

    async def chat(self, message: str) -> str:
        """
        Send a message to the agent and get a response.

        Args:
            message: User message

        Returns:
            Agent response text
        """
        try:
            logger.info(f"Processing message: {message}")
            response = await self.agent.invoke_async(message)
            # Get the response dict and extract text from message
            result_dict = response.to_dict()

            # Extract text from the assistant's message content
            if 'message' in result_dict and 'content' in result_dict['message']:
                content = result_dict['message']['content']
                if isinstance(content, list):
                    text_parts = [block.get('text', '') for block in content if 'text' in block]
                    return ' '.join(text_parts)
                return content

            # Fallback: return the entire dict as JSON string
            return str(result_dict)
        except Exception as e:
            logger.error(f"Error in agent chat: {str(e)}")
            raise

    async def stream_chat(self, message: str):
        """
        Stream agent response chunks.

        Args:
            message: User message

        Yields:
            Response chunks as they're generated
        """
        try:
            logger.info(f"Streaming message: {message}")
            async for chunk in self.agent.stream_async(message):
                if hasattr(chunk, 'content') and chunk.content:
                    yield f"data: {chunk.content}\n\n"
        except Exception as e:
            logger.error(f"Error in agent streaming: {str(e)}")
            yield f"data: Error: {str(e)}\n\n"
