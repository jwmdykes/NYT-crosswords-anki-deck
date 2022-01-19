from random import randint
from PyDictionary import PyDictionary
from datetime import datetime
import pandas as pd

dictionary = PyDictionary()

# from pandas import read_excel
# clues = read_excel("./NYT Crossword_2009_2016.xlsx")

clues = pd.read_pickle("clues.p")

length = len(clues)
while True:
    rand = randint(0, length)
    entry = clues.iloc[rand]
    word = entry.Word
    answer = word.replace(" ", "").replace(
        "-", "").replace("'", "").replace("!", "")

    len_answer = len(answer)
    letter = randint(0, len_answer-1)

    answer_list = list(answer)
    removed = answer_list[letter]  # keep track of removed letter
    answer_list[letter] = '?'
    question = "".join(answer_list)

    responses = []
    print(f"word: {question}")
    responses.append(input())
    print(f"clue: {entry.Clue}")
    responses.append(input())
    print(f"answer: {entry.Word}. your response: {responses[0]}")
    responses.append(input())
    print(f"{entry.Explanation}")
    responses.append(input())

    # if "d" in responses:
    #     # look up the word in the dictionary
    #     print(f"Showing definitions for {word}")
    #     print(dictionary.printMeanings(word))

    response = responses[0]  # first response is response to question
    was_correct = str((response.lower() == answer.lower())
                      or (response.lower() == removed.lower()))

    print(f"letter removed: {removed}")
    print(f"Your response was {was_correct}")

    csv_row = [datetime.now().strftime(
        '%Y:%m:%d'), datetime.now().strftime(
        '%H:%M:%S'), question, response, answer, removed, was_correct, str(rand)]
    csv_row = ",".join(csv_row) + "\n"
    with open('data/letter-train.csv', 'a') as fd:
        fd.write(csv_row)
