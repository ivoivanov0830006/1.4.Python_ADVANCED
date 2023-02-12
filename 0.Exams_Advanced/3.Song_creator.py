def add_songs(*args):
    songs = {}
    for song in args:
        song_name = song[0]
        song_text = song[1]

        if song_name not in songs.keys():
            songs[song_name] = []
        songs[song_name] += song_text

    result = ""

    for name, text in songs.items():
        result += f"- {name}\n"
        if text:
            for text_line in text:
                result += f"{text_line}\n"

    return result


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
