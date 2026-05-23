from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def lesson(request, letter):

    lessons = {

        "alef": {
            "letter": "أ",
            "harakat": [
                {"form": "أَ", "sound": "A"},
                {"form": "أُ", "sound": "U"},
                {"form": "إِ", "sound": "I"},
                {"form": "أْ", "sound": ""},
                {"form": "أّ", "sound": ""},
                {"form": "أٌ", "sound": ""}
            ],
            "madd": [
                "أَا",
                "أُو",
                "إِي"
            ],
            "words": [
                {"word": "أَبْ", "sound": "Ab"},
                {"word": "أَبا", "sound": "Aba"},
            ]
        },

        "ba": {
            "letter": "ب",
            "harakat": [
                {"form": "بَ", "sound": "Ba"},
                {"form": "بُ", "sound": "Bu"},
                {"form": "بِ", "sound": "Bi"},
                {"form": "بْ", "sound": ""},
                {"form": "بّ", "sound": ""},
                {"form": "بٌ", "sound": ""}
            ],
            "madd": [
                "بَا",
                "بُو",
                "بِي"
            ],
            "words": [
                {"word": "بَ", "sound": "Ba"},
                {"word": "بَا", "sound": "Baa"},
                {"word": "أَبْ", "sound": "Ab"},
            ]
        },

        "ta": {
            "letter": "ت",
            "harakat": [
                {"form": "تَ", "sound": "Ta"},
                {"form": "تُ", "sound": "Tu"},
                {"form": "تِ", "sound": "Ti"},
                {"form": "تْ", "sound": ""},
                {"form": "تّ", "sound": ""},
                {"form": "تٌ", "sound": ""}
            ],
            "madd": [
                "تَا",
                "تُو",
                "تِي"
            ],
            "words": [
                {"word": "تَ", "sound": "Ta"},
                {"word": "تَا", "sound": "Taa"},
                {"word": "بَتْ", "sound": "Bat"},
                {"word": "أَتْ", "sound": "At"},
            ]
        },

    }

    lesson_data = lessons.get(letter)

    if not lesson_data:
        return render(request, "home.html")

    return render(request, "home.html", {
        "lesson": lesson_data
    })