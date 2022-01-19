import random
from datetime import datetime
import pandas as pd

# from pandas import read_excel
# clues = read_excel("./NYT Crossword_2009_2016.xlsx")
# reading as pickle is faster
clues = pd.read_pickle("clues.p")

length = len(clues)
size = 3000
start = 1

rand_seq = list(range(start, start+size+1))
random.shuffle(rand_seq)
idx = 0
while True:
    # rand = random.randint(start, start+size)
    if idx >= len(rand_seq):
        print("done training!")
        quit()
    rand = rand_seq[idx]
    idx += 1
    print(f"random integer: {rand}")
    entry = clues.iloc[rand]

    question = entry.Clue
    answer = entry.Word
    # day = entry.Weekday

    print(f"{question}")
    # print(f"{day} clue")
    print(f"{len(answer)} letters")
    response = input()

    was_correct = response.lower() == answer.lower()
    if was_correct:
        print(f"Answer was {answer}. CORRECT")
    else:
        print(f"Answer was {answer}. You said {response}")
    was_correct = str(was_correct)

    input()
    print(entry.Explanation)
    input()

    csv_row = [datetime.now().strftime(
        '%Y:%m:%d'), datetime.now().strftime(
        '%H:%M:%S'), question, response, answer, was_correct, str(rand)]
    csv_row = ",".join(csv_row) + "\n"
    with open('data/train.csv', 'a') as fd:
        fd.write(csv_row)
