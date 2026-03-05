from openai import OpenAI

#API KEY
client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="Explain indexing in Databases.",
    max_output_tokens=500,
    stream=True
)

    # temperature=0.2,
    # top_p=0.1

for event in response:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)

# print(response)

# Tokenization : Explain indexing in Databases.
# response -> output -> message -> content -> text

# Temperature : 0-2
# Temperature is a parameter which controls the creativity or randomness.
# Temperature = 0 : Highly deterministic 
# Temperature = 2 : Highly creative

# Normal response - Wait until the respone gets completed.
# Streaming - Start giving the output as soon as we have it. Like Gpt types the output.