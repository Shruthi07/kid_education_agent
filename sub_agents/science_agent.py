# Science Sub Agent for kids to learn and answer quiz
# Configured tool for chemical element related content and

from google.adk import Agent
from kid_education_agent.constants import MODEL_GEMINI_2_0_FLASH
from kid_education_agent.tools import get_element_info_by_name

science_agent = None
try:
    science_agent = Agent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="science_agent",
        instruction="""You are kid friendly science assistant that makes learning fun. 
            Follow below steps to provide details in concise (around 50-100 words) and fun tone.
            1) For any chemical element related queries, use 'get_element_info_by_name' tool. 
            2) Following it, create a quiz around the queried topic for user to provide answer. 
            If correct, congratulate else give 3 retries and comforting tone if failed.
            """,
        tools=[get_element_info_by_name],
        )
    print(f"✅ Sub-Agent '{science_agent.name}' created.")
except Exception as e:
    print(f"❌ Could not create Science sub agent. Check Model/API Key ({science_agent.model}). Error: {e}")
