from django.shortcuts import render

# قائمة الحروف
letters = ["ا", "ب", "ت", "ث"]

def lesson(request, letter):
    if letter not in letters:
        return render(request, 'home.html')

    index = letters.index(letter)

    prev_letter = letters[index - 1] if index > 0 else None
    next_letter = letters[index + 1] if index < len(letters) - 1 else None

    lesson = {
        "letter": letter,
        "examples": [
            {"arabic": "بَ", "english": "Ba"},
            {"arabic": "بُ", "english": "Bu"},
            {"arabic": "بِ", "english": "Bi"},
        ],
        "words": [
            {"arabic": "باب", "english": "Door"},
            {"arabic": "بيت", "english": "House"},
        ]
    }

    return render(request, 'home.html', {
        'lesson': lesson,
        'prev_letter': prev_letter,
        'next_letter': next_letter
    })