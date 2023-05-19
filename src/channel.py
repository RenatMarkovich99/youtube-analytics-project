import os

from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key='AIzaSyAD1nP_uEubiZKJa9-fmcYiKKIXZ7Ud8Fk'

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id

    @property
    def channel(self):
        """Возвращает название канала."""
        return youtube.channels()

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel = self.channel.list(id=self._channel_id, part='snippet,statistics').execute()
        for a, b in channel:
            print(a, b)
        #print(key"+")

