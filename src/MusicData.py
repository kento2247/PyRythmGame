import csv
import os

from dotenv import load_dotenv

load_dotenv()
folder_path = os.getenv("folder_path")


class MusicData:
    def __init__(self):
        self.music_list = [
            ["gomakasi", "ごまかし"],
            ["maware", "回レ雪月花"],
            ["watashinotensi", "ワタシノテンシ"],
            ["AngelicAngel", "Angelic Angel"],
            ["nopoi", "ノーポイ！"],
            ["sukida", "好きだ"],
            ["tentaikansoku", "天体観測"],
            ["Catch the Moment", "Catch the Moment"],
        ]

    def get_notes_array(self, music_title):
        try:
            for i in self.music_list:
                if music_title in i[0]:
                    return self.list_convert(music_title)
            else:
                raise Exception("music_title is not in music_list")
        except Exception as e:
            print(e)
            return False

    def list_convert(self, filename):
        return_list = []
        try:
            with open(folder_path + "/csv/" + filename + ".csv") as file_name:
                file_read = csv.reader(file_name)
                for i in file_read:
                    return_list.append(int(i[0]))
                return return_list
        except Exception as e:
            print(e)
            raise Exception("file not found")
