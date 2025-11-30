# Greeting Sub agent to greet kids
from google.adk import Agent
from kid_education_agent.constants import MODEL_GEMINI_2_0_FLASH

greeting_agent = None
try:
    # Use a defined model constant
    greeting_agent = Agent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="greeting_agent",
        instruction="You are the Greeting Agent.",
        description="Addresses kids in fun and simple greetings ",
    )
    print(f"✅ Sub-Agent '{greeting_agent.name}' created.")
except Exception as e:
    print(f"❌ Could not create Greeting agent. Check Model/API Key ({greeting_agent.model}). Error: {e}")
