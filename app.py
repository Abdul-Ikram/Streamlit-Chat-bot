from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain import LLMChain
from langchain.prompts.prompt import PromptTemplate
from langchain.memory import ConversationBufferMemory

app = FastAPI()
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

class Prompt(BaseModel):
    user_prompt: str

@app.get("/")
async def read_root():
    return {"RESPONSE": "API IS RUNNING SUCCESSFULLY!"}

@app.post("/prompt")
def read_prompt(prompt: Prompt):
    try:
        userprompt = prompt.user_prompt

        template = """
        You are a chatbot that is an idiot
        {chat_history}
        Human: {human_input}
        Chatbot:
        """
        
        prompt_template = PromptTemplate(
            input_variables=['chat_history', 'human_input'],
            template=template
        )

        memory = ConversationBufferMemory(memory_key='chat_history')
        llm_chain = LLMChain(
            llm = OpenAI(openai_api_key=openai_api_key, model_name='gpt-3.5-turbo-instruct'),
            prompt=prompt_template,
            verbose=True,
            memory=memory
        )

        response = llm_chain.predict(human_input=userprompt)
        print("Response: ", response)

        return {'response' : response}


    except Exception as error:
        return {"error": error}
    
