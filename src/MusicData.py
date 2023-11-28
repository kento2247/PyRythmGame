import csv
import os

from dotenv import load_dotenv


class MusicData:
    def __init__(self):
        load_dotenv()
        self.folder_path = os.getenv("folder_path")
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

    def get_music_list(self):
        return self.music_list

    def get_notes_array(self, music_title):
        try:
            for i in self.music_list:
                if music_title in i[0]:
                    file_path = f"{self.folder_path}/csv/{music_title}.csv"
                    return self._csv_to_list(file_path)
            else:
                raise Exception("music_title is not in music_list")
        except Exception as e:
            print(e)
            return False

    def _csv_to_list(self, file_path):
        return_list = []
        try:
            with open(file_path) as file_name:
                file_read = csv.reader(file_name)
                for i in file_read:
                    return_list.append(int(i[0]))
                return return_list
        except Exception as e:
            print(e)
            raise Exception("file not found")
