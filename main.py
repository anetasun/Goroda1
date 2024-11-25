from auto_py_to_exe.config import language_hint
from opencage.geocoder import OpenCageGeocode
from tkinter import *

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language="ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            return f"Широта: {lat}, Долгота: {lng}"
        else:
            return "Город не найден"
    except Exception as e:
            return f"ВОЗНИКЛА ошибка: {e}"


def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}:\n {coordinates}")


# Пример использования
key = '8d66793abf364248baa40309ef5fc6b0'


# Интерфейс
window = Tk()
window.title("Координаты городов")
window.geometry("320x100")

# Элементы интерфейса
entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)

button = Button(text="Поиск координат", command=show_coordinates)
button.pack()

label = Label(text="Введите город и нажмите на кнопку")
label.pack()

window.mainloop()


