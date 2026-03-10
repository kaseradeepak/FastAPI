from openai import OpenAI

client = OpenAI()

respone = client.responses.create(
    model="gpt-5.4",
    input="Create a plan to learn FastAPI for beginner students.",
    text={
        "format": {
            "type": "json_schema",
            "name": "fastapi_study_plan",
            "schema": {
                "type": "object",
                "properties": {
                    "topic": {"type": "string"},
                    "difficulty": {
                        "type": "string",
                        "enum": ["beginner", "intermediate", "advanced"]
                    },
                    "estimated_hours": {"type": "integer"},
                    "prerequisites": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": ["topic", "difficulty", "estimated_hours", "prerequisites"],
                "additionalProperties": False
            }
        }
    }
)

print(respone.output[0].content[0].text)