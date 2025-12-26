import random

name = input("как вас зовут?(имена всех игроков,пожалуйста(через запятую))")

names = name.split(",")

words = []


letter_scores = {
    "А": 1,
    "Б": 1,
    "В": 1,
    "Г": 1,
    "Д": 1,
    "Е": 1,
    "Ё": 6,
    "Ж": 1,
    "З": 1,
    "И": 1,
    "Й": 7,
    "К": 1,
    "Л": 1,
    "М": 2,
    "Н": 1,
    "О": 1,
    "П": 1,
    "Р": 2,
    "С": 2,
    "Т": 5,
    "У": 4,
    "Ф": 3,
    "Х": 2,
    "Ц": 5,
    "Ч": 5,
    "Ш": 5,
    "Щ": 5,
    "Ъ": 10,
    "Ь": 10,
    "Ы": 3,
    "Э": 3,
    "Я": 1
    }

converted_dictionary = letter_scores.keys()


def get_random_letter(keys):
    list_letters = list(keys)
    random_letter = random.choice(list_letters)
    
    return random_letter


def get_word_with_letter(letter):
    print(f"начальная буква:{letter}")
    for name in names:
        print(f"Игрок {name} ходит")
        while True :
                
            word = input(f"Введите слово на букву {letter}: ")
            if letter == word[0].upper():
                words.append(word)
                break
            else:
                print("неправильно,попробуйте заного")
                continue
all_scores = []


def calculate_scores(words):
    
    for word in words:
        scores = 0
        for i in word:
            scores += letter_scores.get(i.upper())
        all_scores.append(scores)


def main():
    get_word_with_letter(get_random_letter(converted_dictionary))
    calculate_scores(words)
    winner = 0
    for i in range(len(names)):
        if all_scores[winner] < all_scores[i]:
            winner = i
        print(f"{names[i]} набрал {all_scores[i]} очков")
    print(f"{names[winner]} победил,ура")

if __name__ == "__main__":
    main()
