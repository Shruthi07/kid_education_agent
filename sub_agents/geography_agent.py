# Geography Sub agent for kids to learn and answer trivia quiz
# Tool configured for country related knowledge

from google.adk import Agent
from kid_education_agent.constants import MODEL_GEMINI_2_0_FLASH
from kid_education_agent.tools import get_country_details

geography_agent = None
try:
    geography_agent = Agent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="geography_agent",
        instruction="""You are kid friendly geography_agent assistant that makes learning fun. 
            Follow below steps to provide details in concise (around 50-100 words) and fun tone.
            1) For any country related queries, use 'get_country_details' tool. 
            2) Following it, create a random trivia quiz around the queried country for user to provide answer. 
            If correct, congratulate else give 3 retries and comforting tone if failed.
            """,
        tools=[get_country_details],
        )
    print(f"✅ Sub-Agent '{geography_agent.name}' created.")
except Exception as e:
    print(f"❌ Could not create Geography agent. Check Model/API Key ({geography_agent.model}). Error: {e}")
