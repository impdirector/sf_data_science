"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def fast_random_predict(number: int = 1) -> int:
    """Рандомно угадываем число, с коррекцией

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    left_border = 1
    right_border = 101

    while True:
        count += 1
        predict_number = np.random.randint(left_border, right_border)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number < predict_number:
            right_border = predict_number
        else:
            left_border = predict_number
    return count

def fast_random_predict_v2(number: int = 1) -> int:
    """Угадываем число методом разделяй и влавствуй. 

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # число попыток
    left_border = 1 # левая граница диапазона поиска
    right_border = 101 # правая граница диапазона поиска
     
    while True:
        count += 1
        
        # Берем число по середине диапазона 
        predict_number = (right_border + left_border)//2  # предполагаемое число
        
        # Выбираем левую или правую часть диапазона в зависимости от того в какой диапазон попадает число
        # Если число угадали, возвращаем число попыток    
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number < predict_number:
            right_border = predict_number
        else:
            left_border = predict_number
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    print('Run benchmarking for fast_random_predict: ', end='')
    score_game(fast_random_predict)
    print('Run benchmarking for fast_random_predict_ v2: ', end='')
    score_game(fast_random_predict_v2)
