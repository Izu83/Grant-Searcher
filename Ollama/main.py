import ollama

def chat_with_mistral(prompt, temperature=0.5):
    try:
        response = ollama.chat(
            model='mistral',
            messages=[{'role': 'user', 'content': prompt}],
            options={'temperature': temperature})

        return response.get('message', {}).get('content', 'No valid response')
    
    except Exception as e:
        print("Exception:", e)
        return "An error occurred"

if __name__ == "__main__":
    user_input = ''
    while True:    
        user_input = input("Enter your prompt('exit' to leave):\n>> ")
        if user_input == 'exit':
            break
        reply = chat_with_mistral(user_input, 0.5)
        print("Mistral AI:\n<< ", reply)