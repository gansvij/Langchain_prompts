from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="qwen/qwen3-32b")
model1= ChatOpenAI()

chat_history = [
    SystemMessage(content="You are a helpfull AI assistant")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model1.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI : ", result.content)
    
print(chat_history)