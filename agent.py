import asyncio
import json
from planner import make_plan
from executor import run_step
from aggregator import summarize_results

async def run_agent(user_query: str) -> str:
    # 1️⃣ PLAN
    plan = await make_plan(user_query)           # returns a dict with {"steps": [...]}

    results = []
    # 2️⃣ EXECUTE
    for i, step in enumerate(plan["steps"], 1):
        print(f"Executing step {i}: {step}")
        result = await run_step(step)
        results.append(result)

    # 3️⃣ AGGREGATE
    summary = summarize_results(results)
    return summary

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()  # ensure OPENAI_API_KEY is in env
    query = input("🎓 What would you like your agent to do? ")
    final_output = asyncio.run(run_agent(query))
    print("\n🤖 Agent’s final output:\n")
    print(final_output)
