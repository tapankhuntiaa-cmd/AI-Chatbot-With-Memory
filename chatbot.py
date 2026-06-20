from google import genai

# Paste your Gemini API Key here
API_KEY = "your API key"

# Create Gemini client
client = genai.Client(api_key=API_KEY)

# Memory storage
conversation_history = []

# Chat history file
chat_file = open("chat_history.txt", "a", encoding="utf-8")

print("=" * 50)
print("🤖 AI Chatbot with Memory Started!")
print("Type 'exit' to quit.")
print("=" * 50)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\nChatbot ended.")
        chat_file.close()
        break

    # Save user message
    conversation_history.append(f"User: {user_input}")
    chat_file.write(f"User: {user_input}\n")

    # Create prompt with conversation history
    prompt = "\n".join(conversation_history)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        bot_reply = response.text

        print("\nBot:", bot_reply)

        # Save bot response
        conversation_history.append(f"Bot: {bot_reply}")
        chat_file.write(f"Bot: {bot_reply}\n\n")

    except Exception as e:
        print("\nError:", e)
        print("Please try again later.\n")

chat_file.close()