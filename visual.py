import sys
from basic import BasicTokenizer

def visualize():
    tokenizer = BasicTokenizer()
    print("Basic Tokenizer Console")
    print("Type 'exit' to quit.")
    
    while True:
        text = input("Enter text to tokenize: ")
        if text.lower() == 'exit':
            print("Exiting...")
            break
        
        # Assuming the tokenizer has a method to tokenize text directly
        # This might require modifying the BasicTokenizer to include such a method
        # For demonstration, let's assume it's called `tokenize`
        # You would need to implement training before tokenizing in a real scenario
        # Here, we're skipping training for simplicity
        tokens = tokenizer.tokenize(text)
        print("Tokens:", tokens)

visualize()