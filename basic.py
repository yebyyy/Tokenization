from base import Tokenizer, get_stats, merge

class BasicTokenizer(Tokenizer):
    def __init__(self):
        super().__init__()

    def train(self, text, vocab_size, verbose=False):
        assert vocab_size >= 256
        num_merges = vocab_size - 256
        tokens = list(text.encode("utf-8"))
        merges = {}
        vocab = {char: bytes([char]) for char in range(256)}
        for i in range(num_merges):
            stat = get_stats(tokens)
            pair = max(stat, key=stat.get)
            char = 256 + i
            tokens = merge(tokens, pair, char)
            merges[pair] = char
            vocab[char] = vocab[pair[0]] + vocab[pair[1]]
            if verbose:
                print(f"merge {i + 1}/{num_merges}: {pair} -> {char} ({vocab[char]}) had {tokens[pair]} occurrences")
        self.merges = merges
        self.vocab = vocab

    def encode(self, text):
        text_bytes = text.encode("utf-8")
        tokens = list(text_bytes)
        while len(tokens) >= 2:
            stats = get_stats(tokens)
            pair = min(stats, key=lambda p: self.merges.get(p, float("inf")))
            if pair not in self.merges:
                break
            char = self.merges[pair]
            tokens = merge(tokens, pair, char)
        return tokens


    def decode(self, tokens):
        token = b"".join([self.vocab[i] for i in tokens])
        text = token.decode("utf-8", errors="replace")
        return text