"Build a simple LLM application"
import os
import groq
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
#create a client
groq_client=groq.Groq(api_key=GROQ_API_KEY)
sys_prompt="""You are a helpful virtual assistant.\
      your goal is to provide useful and relevant responses to my query"""

models=["llama-3.1-405b-reasoning",
        "llama-3.1-70b-versatile",
        "llama-3.1-8b-instant",
        "mixtral-8x7b-32768"]

def generate(model,query,temperature=0):
    
    response=groq_client.chat.completions.create(
        model=model,
        messages=[
            {"role":"system","content":sys_prompt},
            {"role":"user","content":query},
        ],
        response_format={"type":"text"},
        temperature=temperature
    )
    answer = response.choices[0].message.content
    return answer

if __name__=="__main__":
      model=models[1]
      query="what country is leading in the olypmics and what makes them spectacular"
      response=generate(model,query,temperature=0)
      print(response)

