# Rule-Based Python Chatbot

A simple, lightweight, and interactive rule-based chatbot implemented in pure Python. The chatbot runs entirely in the console, handles common greetings, and includes fallback mechanisms for unrecognized inputs.

## Features
- **Continuous Conversation Loop:** Remains active until the user explicitly types `bye`.
- **Predefined Rules:** Responds to queries like `hello` and `how are you`.
- **Case and Spacing Insensitivity:** Cleans user input to reliably match keywords regardless of trailing spaces or uppercase letters.
- **Fallback Response:** Returns a friendly default reply for any unrecognized inputs.
- **Pure Python:** No external dependencies required.

## Requirements
- Python 3.x

## How to Run
1. Clone or download this repository.
2. Open your terminal or command prompt in the repository's root directory.
3. Run the following command:
   ```bash
   python chatbot.py
   ```
   *(or `py chatbot.py` on Windows)*

## Example Interaction
```text
Chatbot: Hello! I am a simple rule-based chatbot. Type 'bye' to exit.
You: hello
Chatbot: Hi!
You: how are you
Chatbot: I'm fine, thanks!
You: what is the weather today?
Chatbot: I don't understand that.
You: bye
Chatbot: Goodbye!
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

