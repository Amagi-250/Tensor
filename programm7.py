import os

print(f"Имя Операционной системы: {os.name}")
print(f"Имя пользователя вошедшего в терминал: {os.getlogin()}")
print(f"Список файлов и директорий в папке: {os.listdir()}")
