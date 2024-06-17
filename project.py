import csv
import pandas as pd
import os
from tabulate import tabulate
from random import randint
import sys


def main():
    header_flag = False
    with open("main_status.csv", "a", newline="") as main_status:
        writer_main_status = csv.writer(main_status)
        writer_main_status.writerow("1")
    with open("main_status.csv") as main_status2:
        reader_main_status_2 = csv.reader(main_status2)
        reader_main_status_2_list = []
        for row in reader_main_status_2:
            reader_main_status_2_list.append(row)
        if len(reader_main_status_2_list) == 1:
            header_flag = True
        else:
            header_flag = False
    with open("vocab.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["word", "type", "definition"])
        if header_flag == True:
            writer.writeheader()
    with open("vocab.csv") as file2:
        reader2 = csv.reader(file2)
        reader2 = list(reader2)
    if len(reader2) == 1:
        empty_flag = True
    else:
        empty_flag = False
    print("Welcome to the PVB (Python Vocab Builder)!")
    print("1. Add new word to my vocab list")
    print("2. Edit my vocab list")
    print("3. View my vocab list")
    print("4. Take a vocab quiz")
    prompt = input("what do you want to do today? Enter 1, 2, 3, or 4: ")
    while True:
        if empty_flag == True and prompt != "1":
            prompt = input(
                "Warning: Your vocab sheet is empty! Please select 1 and add new words to it! "
            )
        if prompt == "1":
            add_vocab()
            empty_flag == False
            break
        if empty_flag == False:
            if prompt == "2":
                edit_vocab()
                break
            elif prompt == "3":
                view_vocab()
                break
            elif prompt == "4":
                take_quiz()
                break
            else:
                prompt = input("Please enter 1, 2, 3, or 4! ")


def make_word_list():
    word_list = []
    if os.stat("vocab.csv").st_size != 0:
        with open("vocab.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                word_list.append(row[0])
        return word_list
    else:
        empty_flag = True


def make_type_list():
    type_list = []
    if os.stat("vocab.csv").st_size != 0:
        with open("vocab.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                type_list.append(row[1])
        return type_list
    else:
        empty_flag = True


def make_definition_list():
    definition_list = []
    if os.stat("vocab.csv").st_size != 0:
        with open("vocab.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                definition_list.append(row[2])
        return definition_list
    else:
        empty_flag = True


def in_sheet(word):
    if os.stat("vocab.csv").st_size != 0:
        word_list = make_word_list()
        if word in word_list:
            return True
        else:
            return False


def sort_csv():
    if os.stat("vocab.csv").st_size != 0:
        with open("vocab.csv") as file:
            reader = csv.reader(file)
            reader = list(reader)
            sorters = []
            for _ in reader:
                sorters.append(_[0])
            sorters = sorted(sorters)
            header_index = sorters.index("word")
            sorters2 = sorters[:]
            sorters[0] = sorters[header_index]
            sorters[header_index] = sorters2[0]
            header = sorters[0]
            words = sorted(sorters[1:])
            sorters = []
            sorters.append(header)
            for word in words:
                sorters.append(word)
            sorted_list = []
            for sorter in sorters:
                for l in reader:
                    if sorter in l:
                        appendee = []
                        for _ in l:
                            appendee.append(_)
                        sorted_list.append(appendee)
        with open("vocab.csv", "w", newline="") as file2:
            writer = csv.DictWriter(file2, fieldnames=["word", "type", "definition"])
            for _ in sorted_list:
                writer.writerow({"word": _[0], "type": _[1], "definition": _[2]})


def add_vocab():
    print("Enter 'done' if you have finished adding the new words")
    while True:
        word = input("Please enter the word: ").strip().lower()
        if word == "done":
            break
        if in_sheet(word) == True and os.stat("vocab.csv").st_size != 0:
            word_list = make_word_list()
            while word in word_list:
                print(f"'{word}' is already in your vocab sheet!")
                word = input("Please enter another word or type 'done' to exit: ")
        if word == "done":
            break
        word_type = (
            input("What is the type of the word? Please do not use abbreviation! ")
            .strip()
            .lower()
        )
        if word_type == "done":
            break
        definition = input("Please enter the word's definition: ").strip().lower()
        if definition == "done":
            break
        with open("vocab.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["word", "type", "definition"])
            writer.writerow({"word": word, "type": word_type, "definition": definition})
        print("'" + word + "'" + " is added to your vocab list!")
        if os.stat("vocab.csv").st_size != 0:
            sort_csv()


def edit_vocab():
    #refrerence for how to delete a row in csv file: "https://www.tutorialspoint.com/how-to-delete-only-one-row-in-csv-with-python"
    if os.stat("vocab.csv").st_size != 0:
        break_flag = False
        word = input(
            "What is the word that you wish to change or delete? Type 'done' if you wish to exit: "
        )
        if word == "done":
            break_flag = True
        if break_flag == False:
            if in_sheet(word) == False:
                while True:
                    word = input(
                        "This word is not in your vocab sheet! Please type another word or type 'done' to exit and input '1' to add new words to your vocabulary sheet: "
                    )
                    if in_sheet(word) == True:
                        break
                    if word == "done":
                        break
            if word == "done":
                break_flag = True
            if break_flag == False:
                df = pd.read_csv("vocab.csv", index_col="word")
                df = df.drop(word)
                df.to_csv("vocab.csv", index=True)
                print(
                    f"'{word}' is deleted! Please enter another word and its definition as replacement or type 'done' if you want only want to delete that word!"
                )
                word = input("Please enter the word: ").strip().lower()
                if word == "done":
                    sys.exit()
                if in_sheet(word) == True and os.stat("vocab.csv").st_size != 0:
                    word_list = make_word_list()
                    while word in word_list:
                        print(f"'{word}' is already in your vocab sheet!")
                        word = input(
                            "Please enter another word or type 'done' to exit: "
                        )
                if word == "done":
                    sys.exit()
                word_type = (
                    input(
                        "What is the type of the word? Please do not use abbreviation! "
                    )
                    .strip()
                    .lower()
                )
                if word_type == "done":
                    sys.exit()
                definition = (
                    input("Please enter the word's definition: ").strip().lower()
                )
                if definition == "done":
                    sys.exit()
                with open("vocab.csv", "a", newline="") as file:
                    writer = csv.DictWriter(
                        file, fieldnames=["word", "type", "definition"]
                    )
                    writer.writerow(
                        {"word": word, "type": word_type, "definition": definition}
                    )
                print("'" + word + "'" + " is added to your vocab list!")
                if os.stat("vocab.csv").st_size != 0:
                    sort_csv()


def view_vocab():
    if os.stat("vocab.csv").st_size != 0:
        vocab_list = []
        with open("vocab.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                i = []
                for _ in range(3):
                    i.append(row[_])
                vocab_list.append(i)
            vocab_list.pop(0)
        print(
            tabulate(
                vocab_list,
                headers=["WORD", "TYPE", "DEFINITION"],
                tablefmt="fancy_grid",
            )
        )


def take_quiz():
    if os.stat("vocab.csv").st_size != 0:
        print("Welcome to the vocab quiz!")
        print("INSTRUCTIONS:")
        print("This quiz will contain 10 questions")
        print(
            "You will be presented a definition, and your job is to input the correct word"
        )
        print(
            "You have 3 tries. If after that you still get the question wrong, the correct answer will be shown and the program will move on to the next question"
        )
        print("Good luck!")
        print("")
        word_list = make_word_list()
        word_list.pop(0)
        type_list = make_type_list()
        type_list.pop(0)
        definition_list = make_definition_list()
        definition_list.pop(0)
        score = 0
        wrong_words = []
        question_no = 1
        while question_no <= 10:
            tries = 0
            question_index = randint(0, len(definition_list) - 1)
            question = f"Question {question_no}: What word have this definition: '{definition_list[question_index].upper()}'? Given that this word is a {type_list[question_index].upper()}: "
            correct_ans = word_list[question_index]
            answer = input(question).strip().lower()
            while True:
                if answer != correct_ans:
                    wrong_words.append(word_list[question_index])
                    answer = input("incorrect! Please try again: ").strip().lower()
                    tries += 1
                if tries == 3:
                    print(f"The correct word is {correct_ans.upper()}")
                    break
                if answer == correct_ans:
                    print("Correct!")
                    if tries == 0:
                        score += 1
                    break
            question_no += 1
        print("You have completed the quiz!")
        print("")
        print(f"Your score is {score}/10")
        print("")
        print("The words you got wrong are:")
        set_wrong_words = set(wrong_words)
        for word in set_wrong_words:
            print(word.upper())


if __name__ == "__main__":
    main()
