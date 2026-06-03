from django.shortcuts import render

def lesson(request, letter):
    # كل الحروف العربية
    letters = [
        'ا','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز',
        'س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ك',
        'ل','م','ن','ه','و','ي'
    ]

    # لو الحرف مش موجود
    if letter not in letters:
        letter = 'ا'

    index = letters.index(letter)

    prev_letter = letters[index - 1] if index > 0 else None
    next_letter = letters[index + 1] if index < len(letters) - 1 else None

    lesson = {
        "letter": letter,
        "examples": [],
        "words": []
    }

    return render(request, 'home.html', {
        'lesson': lesson,
        'prev_letter': prev_letter,
        'next_letter': next_letter
    })