import genanki
import pandas as pd
clues = pd.read_pickle("../clues.p")


my_model = genanki.Model(
    1240052566,
    'Crossword Model',
    fields=[
        {'name': 'Clue'},
        {'name': 'Word'},
        {'name': 'Explanation'},
        {'name': 'Length'}
    ],
    templates=[
        {
            'name': "Card",
            'qfmt': """
                    {{Clue}}
                    <br>
                    <br>
                    {{Length}} characters
                    """,
            'afmt': """
                    {{FrontSide}}
                    <hr id="answer">
                    {{Word}}
                    <br>
                    <br>
                    Explanation: {{Explanation}}
                    """
        }
    ],
    css="""
    .card {
        font-family: arial;
        font-size: 20px;
        text-align: center;
        color: black;
        background-color: lavender;
    }
    """
)

my_deck = genanki.Deck(
    1547334673,
    'NYT Crossword Clues'
)


filtered_clues = clues.loc[clues.Total >= 12]
randomized = filtered_clues.groupby("Word").sample(10, random_state=0)
clues = randomized
clues = clues.sample(len(clues))

for i in range(len(clues)):
    entry = clues.iloc[i]
    length = len(str(entry.Word))

    my_note = genanki.Note(
        model=my_model,
        fields=[str(entry.Clue), str(entry.Word),
                str(entry.Explanation), str(length)]
    )

    my_deck.add_note(my_note)

genanki.Package(my_deck).write_to_file('./output.apkg')
