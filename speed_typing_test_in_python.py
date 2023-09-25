import random
import time

def generate_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a versatile programming language.",
        "Coding is fun and challenging.",
        "Practice makes perfect.",
        "Keep calm and code on."
    ]
    return random.choice(sentences)

def calculate_accuracy(reference, typed):
    reference_words = reference.split()
    typed_words = typed.split()
    
    correct_words = [w1 for w1, w2 in zip(reference_words, typed_words) if w1 == w2]
    accuracy = len(correct_words) / len(reference_words) * 100
    return accuracy

def main():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")
    
    sentence = generate_random_sentence()
    print("Type the following sentence:")
    print(sentence)
    
    start_time = time.time()
    user_input = input("Your typing: ")
    end_time = time.time()
    
    typing_time = end_time - start_time
    accuracy = calculate_accuracy(sentence, user_input)
    words_per_minute = len(sentence.split()) / (typing_time / 60)
    
    print("\nTyping speed: {:.2f} words per minute".format(words_per_minute))
    print("Accuracy: {:.2f}%".format(accuracy))

if __name__ == "__main__":
    main()
