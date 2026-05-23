def lesson(request, letter):

    letters = ['ba', 'ta', 'tha']

    index = letters.index(letter)

    prev_letter = letters[index - 1] if index > 0 else letters[0]
    next_letter = letters[index + 1] if index < len(letters)-1 else letters[-1]

    lesson = {
        "letter": letter,
        "examples": [
            {"arabic": "بَ", "english": "Ba"},
            {"arabic": "بُ", "english": "Boo"},
            {"arabic": "بِ", "english": "Bee"},
        ],
        "words": [
            {"arabic": "أَب", "english": "Father"},
            {"arabic": "بَاب", "english": "Door"},
        ]
    }

    return render(request, 'home.html', {
        'lesson': lesson,
        'prev_letter': prev_letter,
        'next_letter': next_letter
    })