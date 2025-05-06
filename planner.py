import json
from openai import AsyncOpenAI

client = AsyncOpenAI()

async def make_plan(prompt: str) -> dict:
    system_prompt = (
        "You are an AI planner. "
        "Given a user request, respond *only* with valid JSON of the form:\n"
        "{ \"steps\": [\"step1 description\", \"step2 description\", …] }"
    )
    resp = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": prompt}
        ]
    )
    text = resp.choices[0].message.content.strip()
    return json.loads(text)
