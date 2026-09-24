import ollama
print("i am ai chatbot with q&a")
print("type exit to terminate\n")
messages = []
while True:
    user_input = input("you: ")
    #stop chatbot
    if user_input.lower() == "exit":
        print("bot: goodbye")
        break
    messages.append(
        {
        "role" : "user",
        "content" : user_input 
        }
    )
    response = ollama.chat(
        model = "llama3.2",
        messages = messages
    )
    #get ai response
    ai_message = response["message"]["content"]
    print("ai: ",ai_message)
    messages.append(
        {
        "role" : "assisstant",
        "content" : ai_message
        }
    )
    #print conversation history for loop
    print("\n---chat history---")
    for message in messages:
        if message["role"] == "user":
            print("you: ", message["content"])

        else:
            print("ai:", message["content"])
    print("---------\n")
    