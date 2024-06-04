import threading
import os

def unli_sana(txt_file): # text filedagi matnda nechta unli qatnashganini sanovchi funksiya
    with open(txt_file, 'r') as f:
        text = f.read()
        result = 0
        unlilar = 'auioe'

        for i in text:
            if i.lower() in unlilar:
                result += 1

        return result


def file_counter(): # funksiya joylashgan papkadagi barcha txt filelarni list typeda qaytaruvchi funksiya
    path = os.getcwd()
    files = os.listdir(path)
    txt_files = []
    for file in files:
        if file.endswith(".txt"):
            txt_files.append(file)
    return txt_files

def create_threads(): # file_counter funksiyasidan qaytgan filelar sonichalik threads funksiyalar yaratuvchi funksiya
    files = file_counter()
    threads_list = []
    for file in files:
        def my_thread():
            result = f"{file} faylida {unli_sana(file)} dona unli harf bor"
            return result
        thread = threading.Thread(target=my_thread)
        thread.start()
        threads_list.append(my_thread())

    return threads_list

print(create_threads())