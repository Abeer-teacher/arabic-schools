def lesson(request, letter):

    # 🧠 كل الحروف (مع الهمزة)
    letters = ['أ', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز',
               'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ',
               'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']

    # 🔤 تحويل الرابط إلى حرف
    mapping = {
        'alif': 'أ',
        'ba': 'ب',
        'ta': 'ت',
        'tha': 'ث',
        'jeem': 'ج',
        'ha': 'ح',
        'kha': 'خ',
        'dal': 'د',
        'thal': 'ذ',
        'ra': 'ر',
        'zay': 'ز',
        'seen': 'س',
        'sheen': 'ش',
        'sad': 'ص',
        'dad': 'ض',
        'taa': 'ط',
        'zaa': 'ظ',
        'ain': 'ع',
        'ghain': 'غ',
        'fa': 'ف',
        'qaf': 'ق',
        'kaf': 'ك',
        'lam': 'ل',
        'meem': 'م',
        'noon': 'ن',
        'ha2': 'ه',
        'waw': 'و',
        'ya': 'ي'
    }

    if letter not in mapping:
        return render(request, 'home.html', {'error': 'Lesson not found'})

    current_letter = mapping[letter]

    # 🧠 الحروف المسموحة (تدريجي)
    index = letters.index(current_letter)
    allowed_letters = letters[:index + 1]

    # 🎯 الحركات
    harakat = ['َ', 'ُ', 'ِ']
    sounds = [current_letter + h for h in harakat]

    # 🎯 المد
    madd = [
        current_letter + 'َا',
        current_letter + 'ُو',
        current_letter + 'ِي'
    ]

    # 🎯 مقاطع
    syllables = []
    for l1 in allowed_letters:
        for l2 in allowed_letters:
            syllables.append(l1 + 'َ' + l2 + 'َ')

    # 🎯 كلمات تدريب
    words = []
    for l1 in allowed_letters:
        for l2 in allowed_letters:
            for l3 in allowed_letters:
                words.append(l1 + 'َ' + l2 + 'َ' + l3 + 'َ')

    # 🔁 التنقل
    keys = list(mapping.keys())
    key_index = keys.index(letter)

    prev_letter = keys[key_index - 1] if key_index > 0 else keys[0]
    next_letter = keys[key_index + 1] if key_index < len(keys)-1 else keys[-1]

    return render(request, 'home.html', {
        'letter': current_letter,
        'sounds': sounds,
        'madd': madd,
        'syllables': syllables[:8],
        'words': words[:8],
        'prev_letter': prev_letter,
        'next_letter': next_letter
    })