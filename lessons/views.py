from django.shortcuts import render

def home(request):
    lesson = {
        "letter": "ب",
        "name": "بَاء",

        "harakat": [
            {"arabic": "بَ", "english": "Ba"},
            {"arabic": "بُ", "english": "Bu"},
            {"arabic": "بِ", "english": "Bi"},
            {"arabic": "بْ", "english": "Silent"},
            {"arabic": "بَّ", "english": "Bba"},
        ],

        "madd": [
            {"arabic": "بَا", "english": "Baa"},
            {"arabic": "بُو", "english": "Boo"},
            {"arabic": "بِي", "english": "Bee"},
        ],

        "words": [
            {"arabic": "أَبٌ", "english": "Father"},
            {"arabic": "بَابٌ", "english": "Door"},
        ]
    }

    return render(request, 'home.html', {'lesson': lesson})