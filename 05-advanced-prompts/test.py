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

text=f"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, name!'

if __name__ == '__main__':
    app.run()
"""
prompt=f"""

帮我改进这段代码，让他更加高效，要求回答仅提供一种改进方案,代码：{text}
"""
response = get_completion(prompt)
print(response)