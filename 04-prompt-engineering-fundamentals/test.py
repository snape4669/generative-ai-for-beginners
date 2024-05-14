# The OpenAI SDK was updated on Nov 8, 2023 with new guidance for migration
# See: https://github.com/openai/openai-python/discussions/742

#Note: The openai-python library support for Azure OpenAI is in preview.
#Note: This code sample requires OpenAI Python library version 1.0.0 or higher.
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
  api_key=os.getenv("AZURE_OPENAI_KEY"),
  api_version="2024-02-15-preview"
)
## Updated
def get_completion(prompt):
    messages_text = [{"role": "user", "content": prompt}]       
    completion = client.chat.completions.create(
      model="test", # model = "deployment_name"
      messages = messages_text,
      temperature=0.7,
      max_tokens=800,
      top_p=0.95,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None
    )

## ---------- Call the helper method

### 1. Set primary content or prompt text
text = f"""
who are you
"""

### 2. Use that in the prompt template below
prompt = f"""
```{text}```
"""

## 3. Run the prompt
response = get_completion(prompt)
print(response)
