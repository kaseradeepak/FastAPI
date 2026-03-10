from openai import OpenAI
import base64

client = OpenAI() 

response = client.responses.create(
    model="gpt-5.4",
    input="Generate an image of indian cricket team, holding all the ICCC trohies they have won.",
    tools=[{"type": "image_generation"}],
)

# Save the image to a file
image_data = []
for output in response.output:
    if output.type == "image_generation_call":
        image_data.append(output.result)

# if image_data:
#     image_base64 = image_data[0]
#     with open("cat_and_otter.png", "wb") as f:
#         f.write(base64.b64decode(image_base64))

if image_data:
    image_base64 = image_data[0]
    with open("ict.png", "wb") as f:
        f.write(base64.b64decode(image_base64))