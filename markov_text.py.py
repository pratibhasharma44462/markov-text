import random

# -------------------------------
#  Sample Training Text
# -------------------------------
text = """
Artificial intelligence is transforming the world.
Technology is evolving rapidly and changing industries.
Machine learning helps computers learn from data.
AI is used in healthcare, education, and business.
The future of technology is very exciting and powerful.
"""

def build_markov_chain(text):
    words = text.split()
    chain = {}

    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]

        if current_word not in chain:
            chain[current_word] = []

        chain[current_word].append(next_word)

    return chain


def generate_text(chain, start_word, length=20):
    word = start_word
    result = [word]

    for _ in range(length):
        if word in chain:
            word = random.choice(chain[word])
            result.append(word)
        else:
            break

    return " ".join(result)


chain = build_markov_chain(text)

generated = generate_text(chain, "Artificial", 20)

print("Generated Text:\n")
print(generated)

