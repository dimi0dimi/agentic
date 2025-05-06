from openai import AsyncOpenAI

client = AsyncOpenAI()

async def run_step(step: str) -> str:
    """
    Execute one step by asking the model to perform it.
    """
    system_prompt = "You are an AI assistant that carries out a single task described in the user input."
    resp = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": step}
        ]
    )
    return resp.choices[0].message.content.strip()
