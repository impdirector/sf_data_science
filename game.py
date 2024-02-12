def random_predict(number:int=1) -> int:
    """_summary_

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    # количество попыток
    count = 0
    
    # Режим работы игры
    mode = int(input("Режим игры 1 - человек, 2 - компьютер:"))

    while True:
        count += 1
        if mode == 1:
            predict_number = int(input("Угадай число от 1 до 100:"))
        else:
            predict_number = np.random.randint(1, 101)
        
        if predict_number > number:
            print("Число должно быть меньше")
        elif predict_number < number:
            print("Число должно быть больше")
        else:
            return count


import numpy as np

number = np.random.randint(1, 101) # загадываем число

# количество попыток
count = 0

count = random_predict(number) 
print(f"Количество попыток {count}!")   
            
            

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(random_predict)

    