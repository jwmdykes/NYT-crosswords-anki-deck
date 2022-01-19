import genanki
import pandas as pd
clues = pd.read_pickle("clues.p")


my_model = genanki.Model(
    1240052566,
    'Crossword Model',
    fields=[
        {'name': 'Clue'},
        {'name': 'Word'},
        {'name': 'Explanation'},
        {'name': 'Name'}
    ],
    templates=[
        {
            'name': "{{Name}}",
            'qfmt': """
                    {{Clue}}
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
    ]
)

my_deck = genanki.Deck(
    1547334673,
    'NYT Crossword Clues'
)


# for i in range(len(clues)):
for i in range(300):
    entry = clues.iloc[i]
    name = f"Card {i}"

    my_note = genanki.Note(
        model=my_model,
        fields=[entry.Clue, entry.Word, entry.Explanation, name]
    )

    my_deck.add_note(my_note)

genanki.Package(my_deck).write_to_file('./anki/output.apkg')
