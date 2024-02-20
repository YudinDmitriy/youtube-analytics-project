import requests
from googleapiclient.discovery import build
import os
import json

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.id = self.__channel_id['items'][0]['id']
        self.title = self.__channel_id['items'][0]['snippet']['title']
        self.description = self.__channel_id['items'][0]['snippet']['description']
        self.url = f'https://youtube.com/{self.__channel_id['items'][0]['snippet']['customUrl']}'
        self.subscriber_count = self.__channel_id['items'][0]['statistics']['subscriberCount']
        self.video_count = self.__channel_id['items'][0]['statistics']['videoCount']
        self.view_count = self.__channel_id['items'][0]['statistics']['viewCount']


    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.__channel_id, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, file):
        with open(file, 'a') as f:
            json.dump(self.__channel_id, f, indent=2, ensure_ascii=False)
            f.write('\n')