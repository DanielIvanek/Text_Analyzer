def word_length_histogram(text):
    word_lengths = {}

    # Rozdělí text na jednotlivá slova
    words = text.split()

    # Spočítá délku každého slova a zvýší početnost pro danou délku
    for word in words:
        length = len(word)
        if length in word_lengths:
            word_lengths[length] += 1
        else:
            word_lengths[length] = 1

    # Získá maximální délku slova
    max_length = max(word_lengths.keys())

    # Pro každou délku slova vytvoří řádek grafu
    for length in range(1, max_length + 1):
        # Získá početnost pro danou délku slova, pokud existuje, jinak je početnost 0
        count = word_lengths.get(length, 0)

        # Vytvoří řádek grafu
        line = f"{length:2d}| {'*' * count}"
        print(line)

# Příklad použití
text = "Toto je jednoduchý příklad textu pro sloupcový graf"
word_length_histogram(text)