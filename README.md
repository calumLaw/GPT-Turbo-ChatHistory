# GPT-Turbo-ChatHistory
ChatGPT CLI // Calum Lawrence

This is a command-line interface (CLI) for using the OpenAI GPT-3.5 Turbo model. It allows you to have a conversation with the GPT-3.5 Turbo model using natural language.

Getting Started

Prerequisites

Python 3.9 or later


Installing

Clone the repository: git clone https://github.com/calumLaw/chatgpt_cli.git
Navigate to the cloned directory: cd chatgpt_cli
Install the required packages: pip install -r requirements.txt


Usage

Navigate to the cloned directory: cd chatgpt_cli
Run the script: python chatgpt.py
Type your message and hit Enter to get a response from the GPT-3.5 Turbo model.
Type 'exit' and hit Enter to quit the script.


Conversational Context Management

This script includes Conversational Context Management which allows the chatbot to remember past conversations even if the application is restarted. The conversation history is stored in a JSON file named conversation_history.json.

Examples

To get a response to a general message, type: Hello, can you help me with something?
To get a poem, type: Write me a 10 word poem.
To get a joke, type: Tell me a joke.
To get a speech from Donald Trump as a basketball coach, type: Write a line of speech as if donald trump were a basketball coach on the sidelines of watching his team play, and they were just about to score a basket.


License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

This project was built with the OpenAI API.
