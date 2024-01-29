# The OpenAI SDK was updated on Nov 8, 2023 with new guidance for migration
# See: https://github.com/openai/openai-python/discussions/742

## Updated
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
  api_key=os.environ['AZURE_OPENAI_KEY'],  # this is also the default, it can be omitted
  api_version = "2023-05-15"
  )

deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']

## Updated
def get_completion(prompt):
    messages = [{"role": "user", "content": prompt}]       
    response = client.chat.completions.create(   
        model=deployment,                                         
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
        max_tokens=1024
    )
    return response.choices[0].message.content

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