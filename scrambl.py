import random


def get_player_names():
    name_input = input("Как вас зовут? (имена всех игроков через запятую): ")
    names = [name.strip() for name in name_input.split(",") if name.strip()]
    if not names:
        print("Игра закончилась — нет имён.")
        return []
    return names


def get_random_letter(letter_scores):
    return random.choice(list(letter_scores.keys()))


def is_valid_letter(letter):
    problematic_letters = {"Ы", "Ъ", "Ь"}
    return letter not in problematic_letters


def get_valid_letter(letter_scores):
    while True:
        letter = get_random_letter(letter_scores)
        if is_valid_letter(letter):
            return letter


def get_word_with_letter(player_name, letter):
    while True:
        word = input(f"Игрок {player_name}, введите слово на букву {letter}: ").strip()
        if not word:
            print("Слово не может быть пустым. Попробуйте снова.")
            continue

        if letter == word[0].upper():
            return word
        else:
            print(f"Неправильно. Слово должно начинаться на букву {letter}. Попробуйте снова.")


def calculate_scores(word, letter_scores):
    score = 0
    for char in word:
        if char.upper() in letter_scores:
            score += letter_scores[char.upper()]
    return score


def play_round(names, letter_scores):
    letter = get_valid_letter(letter_scores)
    print(f"\nНачальная буква: {letter}")

    words = []
    scores = []

    for name in names:
        word = get_word_with_letter(name, letter)
        words.append(word)
        score = calculate_scores(word, letter_scores)
        scores.append(score)
        print(f"{name} назвал слово {word} и получил {score} очков.")

    return words, scores


def determine_winner(names, scores):
    max_score = max(scores)
    winners = [names[i] for i, score in enumerate(scores) if score == max_score]

    if len(winners) == 1:
        return winners[0], max_score
    else:
        return "Ничья между: " + ", ".join(winners), max_score


def main():
    letter_scores = {
        "А": 1, "Б": 1, "В": 1, "Г": 1, "Д": 1, "Е": 1, "Ё": 6,
        "Ж": 1, "З": 1, "И": 1, "Й": 7, "К": 1, "Л": 1, "М": 2,
        "Н": 1, "О": 1, "П": 1, "Р": 2, "С": 2, "Т": 5, "У": 4,
        "Ф": 3, "Х": 2, "Ц": 5, "Ч": 5, "Ш": 5, "Щ": 5, "Ъ": 10,
        "Ь": 10, "Ы": 5, "Э": 3, "Я": 1, "Ю": 2
    }

    print("Добро пожаловать в игру «Скрабл»!")
    names = get_player_names()
    if not names:
        return

    words, scores = play_round(names, letter_scores)

    print("\nРезультаты раунда:")
    for i, name in enumerate(names):
        print(f"Игрок {name} набрал {scores[i]} очков, введя слово «{words[i]}».")

    final_winner, final_score = determine_winner(names, scores)
    print(f"\nПобедитель: {final_winner} с {final_score} очками! Ура!")


if __name__ == "__main__":
    main()
