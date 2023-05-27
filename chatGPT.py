import openai

openai.api_key = "OPENAI-SECRET-KEY"


def askChatGPT(question):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=question,
    temperature=0.3,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0.6,
  )
  data = response.choices[0].text
  return "response: " + data.strip()


while True:
  data = input("Ask me:")
  print(askChatGPT(data))
