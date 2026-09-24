import ollama
print("i am ai chatbot with q&a")
print("type exit to terminate\n")
while True:
    question = input("you: ")
    if question.lower() == "exit":
        print("bot: goodbye")
        break
    response = ollama.chat(
        model = "llama3.2",
        messages = [
            {
            "role" : "user",
            "content" : question
            }
        ]
    )
    print("bot:",response["message"]["content"])