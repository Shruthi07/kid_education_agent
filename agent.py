from google.adk.agents import Agent
import logging
from kid_education_agent.constants import MODEL_GEMINI_2_0_FLASH
from kid_education_agent.sub_agents import (greeting_agent, science_agent,
                                            finance_agent, geography_agent,
                                            farewell_agent)

# Main agent -> Kid learning assistant. Delegates to sub agents per query content
# Sub Agents Used -> Greeting, Science, Finance, Geography and Farewell
root_agent = Agent(
        name="kid_education_main_agent",
        model=MODEL_GEMINI_2_0_FLASH,
        description="Main agent: A helpful assistant for kids that handles queries  related to finance, science and geography.",
        instruction="""You are the main friendly kids education assistant Agent. 
                    Delegate greeting to 'greeting_agent', science related queries to 'science_agent', 
                    finance related queries to 'finance_agent', geography related queries to 'geography_agent' 
                    and farewell to 'farewell_agent'.
                    """,
        sub_agents=[greeting_agent, science_agent, finance_agent, geography_agent, farewell_agent],
)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)