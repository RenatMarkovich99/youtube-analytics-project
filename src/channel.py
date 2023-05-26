import os
import json

from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения

api_key = os.environ.get("YT_API_KEY")
# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    # api_key = os.environ("YT_API_KEY")
    # youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str, ):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)

        channel_data = self.youtube.channels().list(id=self._channel_id, part='snippet, statistics').execute()['items'][
            0]

        self.title = channel_data['snippet']['title']
        self.description = channel_data['snippet']['description']
        self.url = channel_data['snippet']['customUrl']
        self.subscribers_count = channel_data['statistics']['subscriberCount']
        self.video_count = channel_data['statistics']['videoCount']
        self.views_count = channel_data['statistics']['viewCount']

    @property
    def channel(self):
        """Возвращает название канала."""
        return self.youtube.channels()

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel_response = self.youtube.channels().list(id=self._channel_id, part='snippet, statistics').execute()['items'][0]

        print(channel_response)

    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с YouTube API
        """
        service = build('youtube', 'v3', developerKey=api_key)
        return service

    def to_json(self, file_path):
        """
        Сохраняем значения атрибутов экземпляра Channel в json файле
        """
        with open(file_path, 'w') as f:
            json.dumps({
                'id': self._channel_id,
                'title': self.title,
                'url': self.url,
                'description': self.description,
                'subscribersCount': self.subscribers_count,
                'videoCount': self.video_count,
                'viewsCount': self.views_count
            }, f, indent=4)
