text = """The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is."""


def get_top_three_word_occurences(text):
    if not isinstance(text, str):
        raise TypeError("Argument must be of type str.")

    words = [word.casefold().rstrip(".") for word in text.split()]
    word_occurences = {}
    for word in words:
        if word not in word_occurences:
            word_occurences[word] = 0
        word_occurences[word] += 1

    top_three = sorted(word_occurences.items(), key=lambda x: x[1], reverse=True)[:3]

    return f"'{top_three[0][0]}' -> {top_three[0][1]}, '{top_three[1][0]}' -> {top_three[1][1]}, '{top_three[2][0]}' -> {top_three[2][1]}"


def get_shortest_sentence(text):
    if not isinstance(text, str):
        raise TypeError("Argument must be of type str.")

    sentences = [sentence.strip() for sentence in text.split(".") if sentence]
    shortest = sentences[0]
    for sentence in sentences:
        if len(sentence) < len(shortest):
            shortest = sentence

    number_of_words = len(shortest.split(" "))
    return f"'{shortest}' -> {number_of_words}"


def capitalize_every_other_letter(text):
    if not isinstance(text, str):
        raise TypeError("Argument must be of type str.")

    words = [word.capitalize() for word in text.split()]
    capitalized = []
    for word in words:
        chars = list(word)

        for i in range(0, len(chars), 2):
            chars[i] = chars[i].capitalize()
            word = "".join(chars)

        capitalized.append(word)

    return " ".join(capitalized)


def reverse_word_order(text):
    if not isinstance(text, str):
        raise TypeError("Argument must be of type str.")
    words = [word for word in text.split()]
    return " ".join(words[::-1])


if __name__ == "__main__":
    print("1. Top three most used words:", get_top_three_word_occurences(text))
    print("2. Shortest sentence and its word count:", get_shortest_sentence(text))
    print(
        "3. First and every other letter capitalized:\n\t",
        capitalize_every_other_letter(text),
    )
    print("4. Reversed word order:\n\t", reverse_word_order(text))
