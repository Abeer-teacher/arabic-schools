from django.shortcuts import render

# الصفحة الرئيسية
def index(request):
    return render(request, 'index.html')


# نظام الدروس (ديناميك)
def lesson(request, letter):

    lessons = {

        "ba": {
            "letter": "ب",
            "harakat": [
                "بَ (Ba)",
                "بُ (Bu)",
                "بِ (Bi)",
                "بْ (B)",
                "بّ (Bb)",
                "بٌ (Bun)"
            ],
            "madd": [
                "بَا (Baa)",
                "بُو (Boo)",
                "بِي (Bee)"
            ],
            "words": [
                "بَ (Ba)",
                "بَا (Baa)",
                "بُو (Boo)",
                "بِي (Bee)"
            ]
        },

        "ta": {
            "letter": "ت",
            "harakat": [
                "تَ (Ta)",
                "تُ (Tu)",
                "تِ (Ti)",
                "تْ (T)",
                "تّ (Tt)",
                "تٌ (Tun)"
            ],
            "madd": [
                "تَا (Taa)",
                "تُو (Too)",
                "تِي (Tee)"
            ],
            "words": [
                "تَ (Ta)",
                "تَا (Taa)",
                "تُو (Too)",
                "تِي (Tee)"
            ]
        }

    }

    lesson_data = lessons.get(letter)

    if not lesson_data:
        return render(request, 'home.html', {"error": "Lesson not found"})

    return render(request, 'home.html', {"lesson": lesson_data})