from rich.console import Console
from rich.text import Text
from basic import BasicTokenizer
from regex import RegexTokenizer

# Function to print tokens with colors
def print_colored_tokens(tokens):
    console = Console()
    colored_text = Text()

    # Define a set of colors to cycle through
    colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "white", "bright_red", "bright_green", "bright_blue", "bright_yellow", "bright_magenta", "bright_cyan"]

    for i, token in enumerate(tokens):
        color = colors[i % len(colors)]
        colored_text.append(str(token) + " ", style=color)

    console.print(colored_text)

# Function to print decoded text with colored tokens
def print_colored_decoded_text(tokens, vocab):
    console = Console()
    colored_text = Text()

    # Define a set of colors to cycle through
    colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]

    for i, token in enumerate(tokens):
        color = colors[i % len(colors)]
        token_text = vocab[token].decode("utf-8", errors="replace")
        colored_text.append(token_text, style=color)

    console.print(colored_text)

if __name__ == "__main__":
    # Read input text from file
    with open('taylorswift.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Train the tokenizer on the input text
    basic_tokenizer = BasicTokenizer()
    regex_tokenizer = RegexTokenizer()

    basic_tokenizer.train(text, vocab_size=10000, verbose=False)

    txt = input("\nInput: ")
    # Encode the text
    tokens = basic_tokenizer.encode(txt)

    # Print encoded tokens with colors
    print("\nEncoded Tokens:")
    print_colored_tokens(tokens)

    # Print decoded text with colored tokens
    print("\nDecoded Text with Colors:")
    print_colored_decoded_text(tokens, tokenizer.vocab)