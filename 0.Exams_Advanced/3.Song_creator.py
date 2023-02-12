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
