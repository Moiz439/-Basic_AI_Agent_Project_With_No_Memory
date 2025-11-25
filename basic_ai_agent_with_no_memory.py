## Besic AI Agent With No Memmory.
from langchain_ollama import OllamaLLM

# AI Model from Ollama
llm= OllamaLLM(model="mistral")

print("\n Welcom to your AI Agent! Ask me anything.")
while True:
    question = input("Your Question (or type 'exit' to stop ) :")
    if question.lower() == 'exit' :
        print("Goodbye!")
        break
    response = llm.invoke(question)
    print("\n Ai Resoponse: ", response)











