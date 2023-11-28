import csv
import os

from dotenv import load_dotenv

load_dotenv()
folder_path = os.getenv("folder_path")


def get_notes_array(music_title):
    for i in music_list:
        if music_title in i[0]:
            return list_convart(music_title)
    else:
        return [0]


music_list = [
    ["gomakasi", "ごまかし"],
    ["maware", "回レ雪月花"],
    ["watashinotensi", "ワタシノテンシ"],
    ["AngelicAngel", "Angelic Angel"],
    ["nopoi", "ノーポイ！"],
    ["sukida", "好きだ"],
    ["tentaikansoku", "天体観測"],
    ["Catch the Moment", "Catch the Moment"],
]


def list_convart(filename):
    return_list = []
    with open(folder_path + "/csv/" + filename + ".csv") as file_name:
        file_read = csv.reader(file_name)
        for i in file_read:
            return_list.append(int(i[0]))
    # print(return_list)
    return return_list
