# PVB (PYTHON VOCABULARY BUILDER)
#### Video Demo:  <URL HERE>
#### Description:

### Project overview

This is my final project for the CS50's Introduction to programming with Python (CS50P). My project is called *PVB*, which a abbreviation for *Python Vocabulary Builder*. Hence the name, it is simply a programme which helps you enhance your *English* vocabulary by allowing you to make and edit your own vocabulary list and generate short vocab quizes for you to test your knowledge.
My program, when run will consists of 6 files:

    1. project.py: code for the program itself
    2. test_project.py: a pytest file for 4 functions in "project.py"
    3. vocab.csv: the vocab sheet as a csv file generated in "project.py"
    4. main_status.csv: a csv file generated in "project.py"
    5. requirements.txt: a txt file containing all the extra libraries imported in "project.py"
    6. README.md: a markdown file containing detailed information about this project and how it came to be

### Background story

The idea of writting this program first occur to me when I was learning the the SAT. Currently, I am learning for the upcoming SAT in October, and as we all know, learning the vocabulary is cruicial for acing the SAT, escpecially for international students like me. Fair to say, for me, as an English-as-second-language student, learning the vocabulary is an excruciating proccess. As suggested by almost every of my English teacher, I began collecting new words and try to learn them using flashcards. Because it will probably take a very long time to create the flashcards by hand, I searched for webs and applications online where they allow you to create your own flashcards. After a while, it occured to me: since I have a CS50P final project to do and I am trying to find an application to learn vocabulary, how about I create my own flashcard builder, a program where I am allowed to create and save my own vocabulary list and flashcards? The idea excited me and I went straight to work.

### About the "project.py" - the code for PVB itself

The actions that PVB allow you to do are:

    1. Add new vocabs to vocabulary sheet after initally creating the sheet as a csv in the first place
    2. Edit your vocabulary sheet: either edit a word by or delete a word
    3. View your vocabulary sheet: print out you vocab sheet in a form of a table
    4. Take a vocabulary quiz to test your knowledge: PVB will generate 10 questions based on your vocabulary sheet for you to answer

To actually implemented those actions, I had to write these functions below:

    1. main()
    2. make_word_list()
    3. make_type_list()
    4. make_definition_list()
    5. in_sheet()
    6. sort_csv()
    7. add_vocab()
    8. edit_vocab()
    9. view_vocab()
    10.take quiz()

**_1. The "main()" function_**

This function is called via the code at the end of the file:

    if __name__ == "__main__":
        main()

First of all, the "main()" function prints out this:

    Welcome to the PVB (Python Vocab Builder)!
    1. Add new word to my vocab list
    2. Edit my vocab list
    3. View my vocab list
    4. Take a vocab quiz
    what do you want to do today? Enter 1, 2, 3, or 4:

And expect the user to enter their input.

Then, the "main()" function must deal with the fact that there are no vocab list yet created in the folder, there for the user really cannot do anything else except create and add at least one word to the "vocab.csv" file before they can do anything else. Using the "os" library to check whether "vocab.csv" is truely empty, therefore assigning the "empty_flag" as "True", the program makes sure that the user must input "1" and rejects any different input via this message:

    Warning: Your vocab sheet is empty! Please select 1 and add new words to it!

And keep printing that warning until the input is ultimately "1". After the user have input 1 and add at least 1 word into their vocab list, the "empty_flag" value become "False". Now, the user can proceed to do anything they want by inputing "1", "2", "3", or "4" when prompted later on when they run the program.

There is another problem that I ran to when running the program - writting the header for the "vocab.csv". Ultimately, this problem was overcome using the file "main_status.csv" and the "header_flag". More precisely, the "main_status.csv" keep track of the times when "main()" is called (simply by appending the number "1" on each line when "main()" is called). Using that technique, I can code the program so that it only add the header for "vocab.csv" the _first_ time "main()" is called - when the "header_flag" value is "True". After that, by observing if there are more than one "1" in "main_status.csv", the "header_flag" will remain "False" and the program will not add another header for the "vocab.csv" file everytime "main()" is called.

**_The 2. "make_word_list()", 3. "make_type_list()", 4. "make_definition_list()" functions_**

These function role in this program is simply to create a list containing all of the words in the user's vocab sheet - "vocab.csv", another containg their types (noun, verb, etc) and another containing their definition. First, I use "os" to make sure that these function will only run when the "vocab.csv" file is not empty. Then, using "csv.reader" to access the data in the csv file, I can loop through it and create the lists.

**_5. The "in_sheet(word)" function_**

This function have a parameter called "word" and hence it name, it will return if "True", the word is already in the vocab sheet or "False" if the word is not. To implement this, I used the "make_word_list" above to create a list of all of the words and loop through it to determine whether the return value will be "True" or "False"

**_6. The "sort_csv()" function_**

This function role is to sort the file "vocab.csv" alphabetically. First, using the "make_word_list" function, I create a word list. Then, after removing the header "word" (because we will not sort the header as it will remain in the first row of the csv file), I sorted that list using the built-in function "sorted(list)". I call this sorted list of words "sorter". Next, using the "csv.reader", I was able to obtain a nested list contain every words along with their type and definition. I called this list "reader". Consequently, I loop the words in "sorter" through the list "reader" to match the sorted words with their type and definition and add them, already sorted alphabetically, to a list called "sorted_list". Finally, by using "csv.DictWriter" and looping through the "sorted_list", I _re-write_ the all of the rows in the "vocab.csv" file; all except the header, which remains in its position at the top of the file.

**_7. The "add_vocab()" function_**
This function is allow the user to add new words to their vocabulary list.

First, the user is prompted for the word, its type and definition. Then, the word is added to the "vocab.csv" file and, via the "sort_csv" function, the file is sorted again every time a new word is added.

Especially, if the word that the user input when prompted is already in the sheet, examined by the function "in_sheet(word)", the program will notify the user via this outputting this format string:

    f"'{word}' is already in your vocab sheet!"

and prompt the user again for another word.

The process above is repeated again using a "While True" loop and will be exterminated if the input is "done".

**_8. The "edit_vocab()" function_**

This function allows user to edit or delete a word in their vocab sheet.

First, the function will prompt the user for the word that they want to edit. If the word is _not_ in the "vocab.csv" file, checked by the function "in_sheet(word), the user will be notified:

    This word is not in your vocab sheet! Please type another word or type 'done' to exit and input '1' to add new words to your vocabulary sheet:

and prompt the user again for another the word.

If the word inputed is already in the vocab sheet, then that word is deleted using the "drop" function in the "pandas" (imported as pd) library. I "borrowed" the technique from W3School link: https://www.tutorialspoint.com/how-to-delete-only-one-row-in-csv-with-python . After the word is deleted, if the user only want to delete the word, they simply type in "done" to exit using "sys.exit()" and the "break_flag", or if they want to edit the word, they can type in the word and repeat the process of inputing its type and definition the as they did in the "add_vocab" function.

**_9. The "view_vocab" function_**

This function, using the "tabulate" function from the "tabulate" library, print out the file "vocab.csv" in the form of a table with 3 rows for each of the 3 header: "word", "type" and "definition".

**_10. The "take_quiz()" function_**

This function can generate a 10-question vocabulary quiz.

First, it print out the instructions:

    Welcome to the vocab quiz!
    INSTRUCTIONS:
    This quiz will contain 10 questions
    You will be presented a definition, and your job is to input the correct word
    You have 3 tries. If after that you still get the question wrong, the correct answer will be shown and the program will move on to the next question

Then using the 2, 3, and 4 function above, lists of words, their type and their definition is generated. Next using "randint" from the built-in "random" library, the program is able to pick randomly an word in the word list. The word is saved as the variable "correct_ans". By matching the word with its type and definition in the type list and definition list, a question is printed:

    f"Question {question_no}: What word have this definition: '{definition_list[question_index].upper()}'? Given that this word is a {type_list[question_index].upper()}: "

And prompt the user for the answer as input. If the answer is the same as "correct_ans", thus the answer is correct, the promgram will print out:

    Correct!

and the score increases by 1 point.
However, if the answer is wrong, the program will print out:

    Incorrect! Please try again:

Everytime the user get the question wrong, the variable "tries" will increase by 1. If "tries" is equall to 3, as stated above in the instructions, the program will automatically print out the correct answer:

    f"The correct word is {correct_ans.upper()}"

and move on the the next questions.

After the user have completed the quiz, their score is printed, along with the list of words that they got wrong, implemented by these lines of code below:

        print("You have completed the quiz!")
        print("")
        print(f"Your score is {score}/10")
        print("")
        print("The words you got wrong are:")
        set_wrong_words = set(wrong_words)
        for word in set_wrong_words:
            print(word.upper())

### About the pytest file "test_project.py
As required by CS50P, _at least_ 3 of the functions in "project.py" must be accompanied by a "test_...()" function. Therefore, in this file, I have written 4 test functions for 4 of the functions below:

    1. make_word_list()
    2. make_type_list()
    3. make_definition_list()
    4. in_sheet(word)

### Conclusion

This program, **PVB**, is the fruit of more than a week of coding and fairly speaking, I am proud of how it came out. The design and coding process took about 2 days, and the rest is dedicated for debugging and fixing problems, which poped up almost non-stop for about 4 days before I was able to take care of them thoroughly.
This project helped me greatly to re-think and practice what I have learned throughout this course and in addition to that, really show me how thrilling, (and somewhat painfully beacuse of the bugs) it is when a computer program is implemented and developed from the initial idea. All in all, **PVB** is a great conclusion for a challlenging yet unbelievably fun 2-month journey of CS50P.

### THIS WAS CS50 !
