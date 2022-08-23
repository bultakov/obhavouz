![alt text](https://i.imgur.com/thARTOK.png)

````
pip install ObHavoUz
````

````
from asyncio import get_event_loop

from obhavo import ObHavo


async def main():
    data = await ObHavo(city='samarqand').obhavo()
    print(data)

if __name__ == '__main__':
    get_event_loop().run_until_complete(main())
````
````
{'city': 'Samarqand', 'day': 'Bugun, 22 avgust', 'info': 'Ochiq havo', 'description': "\n\nNamlik: 13%\nShamol: G'arbiy-shimoli-g'arbiy, 4.4 m/s\nBosim: 757 mm sim. ust.\n\n\nOy: Eski oy\nQuyosh chiqishi: 05:50\nQuyosh botishi: 19:19\n\n\n", 'degree': '+31°+15°'}
````
````
print(data.get('city'))
>>> Samarqand
````

````
from asyncio import get_event_loop

from obhavo import ObHavo


async def main():
    data = await ObHavo().all()
    print(data)

if __name__ == '__main__':
    get_event_loop().run_until_complete(main())
````
# Shaharlar ro'yhati
**Toshkent**
**Samarqand**
**Andijon**
**Buxoro**
**Jizzax**
**Qarshi**
**Navoyi**
**Namangan**
**Nukus**
**Termiz**
**Urganch**
**Fargona**
**Xiva**
