import random

def get_name():
    name_input = input("как вас зовут?(имена всех игроков,пожалуйста(через запятую))")
    names = [name.strip() for name in name_input.split(",") if name.strip()]
    if not names:
        print("игра закончилась,нету имен")
        return []
    return names


def get_random_letter(letter_scores):
    return random.choice(list(letter_scores.keys()))


def is_valid_letter(letter):
    zapret_letters = ["Ы","Ъ","Ь"]
    return letter not in zapret_letters


def get_valid_letter(letter_scores):
    while True:
        letter = get_random_letter(letter_scores)
        if is_valid_letter(letter):
            return letter


def get_word_with_letter(player_name,letter):
    while True :
                
        word = input(f"игрок {player_name},введите слово на букву {letter}: ").strip()
        if not word:
            print("слова нету")
            continue
        
        if letter == word[0].upper():
            return word
        else:
            print(f"неправильно,Слово должно начинаться на букву {letter},попробуйте заного")
            continue


def calculate_scores(word,letter_scores):
    score = 0
    for char in word:
        score += letter_scores[char.upper()]
    return score

def round(names,letter_scores):
    letter = get_valid_letter(letter_scores)
    print(f"начальная буква: {letter}")
    words = []
    scores = []
    for name in names:
        word = get_word_with_letter(name,letter)
        words.append(word)
        score = calculate_scores(word,letter_scores)
        scores.append(score)
        print(f"{name} назвал слово {word} и получил {score} очков ")
    return words,scores


def winner(names,scores):
    max_score = max(scores)
    winners = [names[i] for i,score in enumerate(scores) if score == max_score]    
    if len(winners) == 1:
        return winners[0],max_score
    else:
        return "ничья между: " + ",".join(winners),max_score
    
        
def main():
    letter_scores = {
    "А": 1,"Б": 1,"В": 1,"Г": 1,"Д": 1,"Е": 1,"Ё": 6,"Ж": 1,"З": 1,"И": 1,"Й": 7,"К": 1,
    "Л": 1,"М": 2,"Н": 1,"О": 1,"П": 1,"Р": 2,"С": 2,"Т": 5,"У": 4,"Ф": 3,"Х": 2,"Ц": 5,
    "Ч": 5,"Ш": 5,"Щ": 5,"Ъ": 10,"Ь": 10,"Ы": 5,"Э": 3,"Я": 1,"Ю": 2
    }
    print("добро пожаловать в игру скрабл")
    names = get_name()
    if not names: return
    words,scores = round(names,letter_scores)
    print("\nрезультаты раунда:")
    for i,name in enumerate(names):
        print(f"игрок {name} набрал {scores[i]} очков введя слово {words[i]}")
    final_winner,final_score = winner(names,scores)
    print(f"\nпобедитель:{final_winner} с {final_score} очками,вы ура!!!!!!!!!!!!!!")
    
    
if __name__ == "__main__":
    main()    
