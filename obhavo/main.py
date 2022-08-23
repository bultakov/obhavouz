from aiohttp import ClientSession
from bs4 import BeautifulSoup

__author__ = 'bultakov'


class ObHavo:
    def __init__(self, city: str = None):
        self.city: str = city
        self.BASE_URL: str = 'https://obhavo.uz/'
        self.urls: dict = {
            'toshkent': 'https://obhavo.uz/',
            'andijon': 'https://obhavo.uz/andijan',
            'buxoro': 'https://obhavo.uz/bukhara',
            'jizzax': 'https://obhavo.uz/jizzakh',
            'qarshi': 'https://obhavo.uz/karshi',
            'navoyi': 'https://obhavo.uz/navoi',
            'namangan': 'https://obhavo.uz/namangan',
            'nukus': 'https://obhavo.uz/nukus',
            'samarqand': 'https://obhavo.uz/samarkand',
            'termiz': 'https://obhavo.uz/termez',
            'urganch': 'https://obhavo.uz/urgench',
            'fargona': 'https://obhavo.uz/ferghana',
            'xiva': 'https://obhavo.uz/khiva'
        }

    async def get_soup(self) -> BeautifulSoup:
        async with ClientSession() as session:
            async with session.get(url=self.BASE_URL) as response:
                content: str = await response.text()
        return BeautifulSoup(markup=content, features='html.parser')

    async def obhavo(self) -> dict:
        self.BASE_URL: str = self.urls.get(self.city.lower(), None)
        if self.city is None or self.BASE_URL is None:
            return {
                'message': 'Bunday Shahar topilmadi!!!',
                'data': {}
            }
        soup: BeautifulSoup = await self.get_soup()
        day: soup = soup.find('div', 'current-day')
        degree: soup = soup.find('div', 'current-forecast')
        weather_info: soup = soup.find('div', 'current-forecast-desc')
        city: soup = soup.find('h2')
        description: soup = soup.find('div', 'current-forecast-details')
        data: dict = {
            "city": str(city.text),
            "day": str(day.text),
            "info": str(weather_info.text),
            "description": str(description.text),
            "degree": str(degree.text).replace('\n', '')
        }
        return {
            'message': 'ok',
            'data': data
        }

    async def all(self) -> list:
        data: list = list()
        for key, value in self.urls.items():
            self.BASE_URL = value
            soup: BeautifulSoup = await self.get_soup()
            day: soup = soup.find('div', 'current-day')
            degree: soup = soup.find('div', 'current-forecast')
            weather_info: soup = soup.find('div', 'current-forecast-desc')
            city: soup = soup.find('h2')
            description: soup = soup.find('div', 'current-forecast-details')
            data.append(
                {
                    "city": str(city.text),
                    "day": str(day.text),
                    "info": str(weather_info.text),
                    "description": str(description.text),
                    "degree": str(degree.text).replace('\n', '')
                }
            )
        return data
