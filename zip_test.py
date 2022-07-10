import os
import zipfile
from pprint import pprint
import pyfiglet as pyfiglet


# функция записи каталога в zip-фрхив
def add_zip(path):
    file_dir = os.listdir(path)
    zip_name = input('Выберите название архива ==>')
    with zipfile.ZipFile(f'{zip_name}.zip', mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(path, file)
            zf.write(add_file)

    os.system('file test.zip')


# функция сравнения архивов
def merge_zip(path1, path2):
    zip1_set = set()
    zip2_set = set()
    result = {}
    with zipfile.ZipFile(path1, mode='r') as zf_first:
        for file in zf_first.namelist():
            zip1_set.add(file)

    with zipfile.ZipFile(path2, mode='r') as zf_first:
        for file in zf_first.namelist():
            zip2_set.add(file)

    result['Idetical'] = zip1_set & zip2_set
    result['Unique_in_zip1'] = zip1_set.difference(zip2_set)
    result['Unique_in_zip2'] = zip2_set.difference(zip1_set)

    pprint(result)


if __name__ == '__main__':
    while True:
        preview = pyfiglet.figlet_format('EAGLE-TEST', font="slant")
        print(preview)
        anserw = input('\nЕсли вы хотите зархивировать каталог нажмите 1\n'
                       'Если сравнить два архива архива нажмите 2\n==>')

        if anserw == '1':
            path = input('Введите путь к файлу для его архивации: \n==>')
            add_zip(path)

        if anserw == '2':
            path1 = input('Введите путь к  первому файлу : \n==>')
            path2 = input('Введите путь к  второму файлу : \n==>')
            merge_zip(path1, path2)
