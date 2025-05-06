def summarize_results(results: list[str]) -> str:
  """
  Combine individual step outputs into a final cohesive summary.
  """
  header = "✅ All steps completed. Here are the results:\n"
  body = "\n\n".join(f"• {r}" for r in results)
  return header + body
