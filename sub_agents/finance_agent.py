# Finance LLM Sub agent to provide friendly fun answers to kids (with safety parameters) for financial terms
from google.adk.agents import LlmAgent
from google.genai import types
from kid_education_agent.constants import MODEL_GEMINI_2_0_FLASH

finance_agent = None
try:
    finance_agent = LlmAgent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="finance_agent",
        instruction="""You are kid friendly finance assistant that makes learning fun. 
            Provide details in concise manner and fun tone.
            """,
        generate_content_config=types.GenerateContentConfig(
            temperature=0.5,  # More deterministic output
            max_output_tokens=150,
            safety_settings=[
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                    threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
                )
            ]
        )
    )

    print(f"✅ Sub-Agent '{finance_agent.name}' created.")
except Exception as e:
    print(f"❌ Could not create Finance agent. Check Model/API Key ({finance_agent.model}). Error: {e}")