import numpy as np

def random_predict(number:int=np.random.randint(1, 100)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # число попыток
    mn = 1 # границы для предполагаемого числа
    mx = 101   
    predict_number = np.random.randint(mn, mx) # предполагаемое число
        
    while True:
        count += 1

        if number == predict_number:
            break
        
        elif predict_number > number:
            mx = predict_number - 1
            predict_number = round((mn + mx) // 2)
            
        elif predict_number < number:
            mn = predict_number + 1
            predict_number = round((mn + mx) // 2)
            
    return count

print(f'Количество попыток {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    counts_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 100, size=(1000)) # загадали список чисел
    
    for number in random_array:
        counts_ls.append(random_predict(number))
        
    score = int(np.mean(counts_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    
    return score

score_game(random_predict)