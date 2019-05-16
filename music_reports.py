def read_file(file_to_read = 'text_albums_data.txt'):
    """
    Read the txt file
    """
    with open(file_to_read) as f:
        music_data = f.readlines()
    for index, item in enumerate(music_data):
        music_data[index] = item.strip()
    for index, item in enumerate(music_data):
        music_data[index] = item.split('\n')
    return music_data

def convert_txt_to_data():
    """
    Put it into a decque/list/tuple/dictionary/whatever
    in the given order: artist,album, year,genre,length.
    """
    pass

def sort_music_data(sort_by = None):
    """
    Take the music_data file from convert_txt_to_data and sort it by user choice
    Put it into a decque/list/tuple/dictionary/whatever
    in the given order: artist,album, year,genre,length.
    """
    for lists in read_file():
        print(lists)
    pass

def sort_by_user_arg(user_argument = 'sort by ex. artist'):
    """
    Sort what the user wants to see by argument with a loop
    """
    pass

def data_music_parcelled():
    """
    Segregate the data into small chunks for easy access by display.py
    """
    pass

sort_music_data()