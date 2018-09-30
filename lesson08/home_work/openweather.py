__author__ = "Андрей Петров"
import os
import json
import urllib.request as request
import gzip
import shutil
import sqlite3

""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
"""
APIURL = 'http://api.openweathermap.org/data/2.5/'
URL_CITY_NAMES = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
CITY_FILE_NAME = 'city.list.json'    

def get_appid():
    with open('app.id', encoding='UTF-8') as f:
        return f.readline()

def get_city_list(file, url):
    if not os.path.isfile(file):
        download_city_list(file, url)
        
    with open(file, encoding='UTF-8') as f:
        cities_list = json.load(f)
    return cities_list

def download_city_list(url, file):
    request.urlretrieve(url, file + '.gz')
    with gzip.open(file + '.gz', 'rb') as f_in:
        with open(file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


            


"""
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    
"""



def get_city_by_name():
    name = input('Название города на английском: ')
    searches = []
    for city in cities_list:
        if city['name'].find(name) >= 0:
            searches.append(city)
            
    if len(searches) > 1:
        print('Таких городов несколько: ')
        for i, city in enumerate(searches):
            print('#{}. Страна: {} Город: ({})'.format(i, city['country'], city['name']))
        inp = input('Укажите порядковый номер или "all" для всех: ')
        if inp == 'all':
            return searches
        else:
            return searches[int(inp)]
    elif len(searches) == 1:
        return searches[0]
    else:
        return 'Город не найден.'

def get_city_data(cities, appid, metric='y'):
    url = APIURL
    if isinstance(cities, list):
        clist =  ','.join(format(n['id']) for n in cities)
        url += 'group?id={}&appid={}'.format(clist, appid)
    else:
        url += 'weather?id={}&appid={}'.format(cities['id'], appid)
    if(metric == 'y'):
        url += '&units=metric'
    return json.load(request.urlopen(url))

"""
== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
def save_data(data):
    weather = [(data["id"], data["name"], data["dt"], data["main"]["temp"], data["weather"][0]["id"])]
    connect = sqlite3.connect("cities.db")
    c = connect.cursor()
    query = "CREATE TABLE IF NOT EXISTS '{}' (\
        city_id INTEGER PRIMARY KEY, \
        city_name VARCHAR(255), \
        date DATE, \
        temperatire INTEGER, \
        weather_id INTEGER)".format(data["name"])
    print(query)
    c.execute(query)
    query_2 = "INSERT OR REPLACE INTO '{}' VALUES (?, ?, ?, ?, ?)".format(data["name"])
    c.executemany(query_2, weather)
    connect.commit()
    c.close()
    connect.close()

def print_from_db(data):
    connect = sqlite3.connect("cities3.db")
    c = connect.cursor()
    c.execute("select * from '{}';".format(data['name']))
    print(cursor.fetchone())
    
if __name__ == "__main__":  
    apid = get_appid()
    cities_list = get_city_list(CITY_FILE_NAME, URL_CITY_NAMES) 
    city = get_city_by_name()
    data = get_city_data(city, apid)
    save_data(data)
    print_from_db(data)
