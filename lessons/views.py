from django.shortcuts import render

def lesson(request, letter):
    letters = [chr(i) for i in range(0x0627, 0x064A + 1)]

    if letter not in letters:
        letter = 'ا'

    index = letters.index(letter)

    prev_letter = letters[index - 1] if index > 0 else None
    next_letter = letters[index + 1] if index < len(letters) - 1 else None

    lesson = {
        "letter": letter,
        "examples": [
            {"arabic": letter + "َ", "english": "a"},
            {"arabic": letter + "ُ", "english": "u"},
            {"arabic": letter + "ِ", "english": "i"},
        ],
        "words": [
            {"arabic": letter + "ب", "english": "word"},
            {"arabic": letter + "ت", "english": "word"},
        ]
    }

    return render(request, 'home.html', {
        'lesson': lesson,
        'prev_letter': prev_letter,
        'next_letter': next_letter,
    })