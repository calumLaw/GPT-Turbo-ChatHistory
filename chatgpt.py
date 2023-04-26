import os
import openai
import json

api_key = "API_KEY_HERE"

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to load conversation history from a JSON file
def load_conversation_history(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    else:
        return []

# Function to save conversation history to a JSON file
def save_conversation_history(file_path, conversation_history):
    with open(file_path, "w") as f:
        json.dump(conversation_history, f, indent=2)

# Function to send a message to GPT-3.5 Turbo and receive a response
def chat_gpt(message, conversation_history=None):
    model_engine = "gpt-3.5-turbo"

    if conversation_history is None:
        conversation_history = []

    conversation_history.append({"role": "system", "content": "You are a helpful assistant."})
    conversation_history.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=conversation_history,
        temperature=0.5,
        max_tokens=100
    )

    chat_response = response.choices[0].message['content'].strip()
    return chat_response

# Main loop for cmd line interaction
def main():
    print("Welcome to ChatGPT CLI: Type 'exit' to quit")
    conversation_history_file = "conversation_history.json"
    conversation_history = load_conversation_history(conversation_history_file)

    while True:
        # Get user input
        user_message = input("You: ")

        # Check if the user wants to quit
        if user_message.lower() == 'exit':
            break

        # Call the chat_gpt function and print the response
        response = chat_gpt(user_message, conversation_history)
        conversation_history.append({"role": "assistant", "content": response})
        save_conversation_history(conversation_history_file, conversation_history)
        print(f"ChatGPT: {response}")

if __name__ == '__main__':
    main()
