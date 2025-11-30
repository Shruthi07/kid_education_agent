# Farewell Sub agent
from google.adk import Agent
from kid_education_agent.constants import MODEL_GEMINI_2_0_FLASH

farewell_agent = None
try:
    farewell_agent = Agent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="farewell_agent",
        instruction="You are the Farewell Agent.",
        description="Addresses kids with fun and simple farewell notes",
    )
    print(f"✅ Sub-Agent '{farewell_agent.name}' created.")
except Exception as e:
    print(f"❌ Could not create Farewell agent. Check Model/API Key ({farewell_agent.model}). Error: {e}")
