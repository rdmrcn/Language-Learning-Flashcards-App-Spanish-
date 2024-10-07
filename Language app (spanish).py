import random

common_words_spanish = [
    {"spanish": "el", "english": "the"},
    {"spanish": "de", "english": "of"},
    {"spanish": "que", "english": "that"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to"},
    {"spanish": "en", "english": "in"},
    {"spanish": "un", "english": "a"},
    {"spanish": "ser", "english": "to be"},
    {"spanish": "se", "english": "self"},
    {"spanish": "no", "english": "no"},
    {"spanish": "haber", "english": "to have"},
    {"spanish": "por", "english": "by"},
    {"spanish": "con", "english": "with"},
    {"spanish": "su", "english": "his/her/its"},
    {"spanish": "para", "english": "for"},
    {"spanish": "como", "english": "like/as"},
    {"spanish": "estar", "english": "to be"},
    {"spanish": "tener", "english": "to have"},
    {"spanish": "le", "english": "to him/her"},
    {"spanish": "lo", "english": "the/it"},
    {"spanish": "todo", "english": "all"},
    {"spanish": "pero", "english": "but"},
    {"spanish": "más", "english": "more"},
    {"spanish": "hacer", "english": "to do"},
    {"spanish": "o", "english": "or"},
    {"spanish": "poder", "english": "to be able to"},
    {"spanish": "decir", "english": "to say"},
    {"spanish": "este", "english": "this"},
    {"spanish": "ir", "english": "to go"},
    {"spanish": "otro", "english": "other"},
    {"spanish": "ese", "english": "that"},
    {"spanish": "la", "english": "the"},
    {"spanish": "si", "english": "if"},
    {"spanish": "me", "english": "me"},
    {"spanish": "ya", "english": "already"},
    {"spanish": "ver", "english": "to see"},
    {"spanish": "porque", "english": "because"},
    {"spanish": "dar", "english": "to give"},
    {"spanish": "cuando", "english": "when"},
    {"spanish": "él", "english": "he"},
    {"spanish": "muy", "english": "very"},
    {"spanish": "sin", "english": "without"},
    {"spanish": "vez", "english": "time"},
    {"spanish": "mucho", "english": "much"},
    {"spanish": "saber", "english": "to know"},
    {"spanish": "qué", "english": "what"},
    {"spanish": "sobre", "english": "about"},
    {"spanish": "mi", "english": "my"},
    {"spanish": "alguno", "english": "some"},
    {"spanish": "mismo", "english": "same"},
    {"spanish": "yo", "english": "I"},
    {"spanish": "también", "english": "also"},
    {"spanish": "hasta", "english": "until"},
    {"spanish": "año", "english": "year"},
    {"spanish": "dos", "english": "two"},
    {"spanish": "querer", "english": "to want"},
    {"spanish": "entre", "english": "between"},
    {"spanish": "así", "english": "so"},
    {"spanish": "primero", "english": "first"},
    {"spanish": "desde", "english": "since"},
    {"spanish": "grande", "english": "big"},
    {"spanish": "eso", "english": "that"},
    {"spanish": "ni", "english": "nor"},
    {"spanish": "nos", "english": "us"},
    {"spanish": "llegar", "english": "to arrive"},
    {"spanish": "pasar", "english": "to pass"},
    {"spanish": "tiempo", "english": "time"},
    {"spanish": "ella", "english": "she"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "día", "english": "day"},
    {"spanish": "uno", "english": "one"},
    {"spanish": "bien", "english": "well"},
    {"spanish": "poco", "english": "little"},
    {"spanish": "deber", "english": "to owe"},
    {"spanish": "entonces", "english": "then"},
    {"spanish": "poner", "english": "to put"},
    {"spanish": "cosa", "english": "thing"},
    {"spanish": "tanto", "english": "so much"},
    {"spanish": "hombre", "english": "man"},
    {"spanish": "parecer", "english": "to seem"},
    {"spanish": "nuestro", "english": "our"},
    {"spanish": "tan", "english": "so"},
    {"spanish": "donde", "english": "where"},
    {"spanish": "ahora", "english": "now"},
    {"spanish": "parte", "english": "part"},
    {"spanish": "después", "english": "after"},
    {"spanish": "vida", "english": "life"},
    {"spanish": "quedar", "english": "to stay"},
    {"spanish": "siempre", "english": "always"},
    {"spanish": "creer", "english": "to believe"},
    {"spanish": "hablar", "english": "to talk"},
    {"spanish": "llevar", "english": "to carry"},
    {"spanish": "dejar", "english": "to leave"},
    {"spanish": "nada", "english": "nothing"},
    {"spanish": "cada", "english": "each"},
    {"spanish": "parejo", "english": "even"},
    {"spanish": "seguir", "english": "to follow"},
    {"spanish": "menos", "english": "less"},
    {"spanish": "nuevo", "english": "new"},
    {"spanish": "encontrar", "english": "to find"}
]

def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['spanish']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct answer!\n")
            score += 1
        else:
            print(f"Wrong answer, the correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(common_words_spanish)

if __name__ == "__main__":
    main()
