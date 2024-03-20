import ollama

stream = ollama.chat(
    model='mario',
    messages=[
        {'role': 'user', 'content': 'Who is Bowser? Show me only 2-3 lines'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
