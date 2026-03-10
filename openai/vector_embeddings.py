from openai import OpenAI

client = OpenAI()

response = client.embeddings.create(
    model="text-embedding-3-large",
    input="masai"
)

# embeddings = []
# for item in response.data:
#     embeddings.append(item.embedding)

print(len(response.data[0].embedding))