def run_chatbot():
    """
    Main loop for the rule-based chatbot.
    Greets the user, processes inputs, and responds based on predefined rules.
    """
    print("Chatbot: Hello! I am a simple rule-based chatbot. Type 'bye' to exit.")
    
    while True:
        # Get input from the user, strip leading/trailing whitespace, and convert to lowercase for matching
        user_input = input("You: ").strip().lower()
        
        # Match input to predefined responses using if-elif-else
        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break  # Exit the loop
        else:
            print("Chatbot: I don't understand that.")

def main():
    run_chatbot()

if __name__ == "__main__":
    main()
