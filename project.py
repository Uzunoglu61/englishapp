import json
import random

def main():
    words = load_data()
    while True:
        print("\nEnglish Dictionary App")
        print("1. Search Word")
        print("2. Synonym Quiz")
        print("3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            word = input("Enter word: ").lower()
            result = search_word(words, word)
            print(result["definition"] if result else "Word not found!")

        elif choice == "2":
            score = quiz(words)
            print(f"Your score: {score}/5")

        elif choice == "3":
            break

def load_data():
    try:
        with open("data.json") as f:
            return json.load(f)["words"]
    except FileNotFoundError:
        return []

def search_word(words, target):
    return next((w for w in words if w["word"] == target), None)

def get_synonyms(word_entry):
    return word_entry.get("synonyms", [])

def quiz(words):
    score = 0
    sample = random.sample(words, min(5, len(words)))

    for word in sample:
        synonyms = get_synonyms(word)
        if not synonyms:
            continue

        answer = random.choice(synonyms)
        print(f"\nWhat's a synonym for {word['word']}?")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer in synonyms:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answers: {', '.join(synonyms)}")

    return score

if __name__ == "__main__":
    main()