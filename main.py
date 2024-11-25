from auto_py_to_exe.config import language_hint
from opencage.geocoder import OpenCageGeocode

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language="ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            return lat, lng
        else:
            return "Город не найден"
    except Exception as e:
            return f"вОЗНИКЛА ошибка: {e}"


# Пример использования
key = '8d66793abf364248baa40309ef5fc6b0'
city = 'Химки'
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")
