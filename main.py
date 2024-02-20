import numpy as np
import pandas as pd
from typing import List
from keras.models import Sequential
from keras.layers import Dense, Input


def uniqueElems(l: list) -> list:
    result: list = []
    for item in l:
        if result:
            if item not in result:
                result.append(item)
        else:
            result.append(item)
    return result


def timeToSec(time: str) -> int:
    result: int = 0
    time_splited = time.split(':')
    result += int(time_splited[0]) * 3600
    result += int(time_splited[1]) * 60
    result += int(time_splited[2])
    return result


df = pd.read_csv('pizza_sales.csv')
sizes = np.array(df['pizza_size'].tolist()).reshape(len(df['pizza_size'].tolist()), 1)
size_kinds = uniqueElems(df['pizza_size'].tolist())
prices: List[float] = df['unit_price'].tolist()
times = np.array(timeToSec(df['order_time'].tolist())).reshape(len(df['order_time'].tolist()), 1)
x_train = np.hstack([times, sizes])
y_train = np.array(prices, dtype='float64').reshape(len(prices), 1) / max(prices)
sizes_encoding = {
    el: ind for ind, el in enumerate(size_kinds)
}

model = Sequential()
model.add(Input(2))
model.add(Dense(20, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
print(sizes_encoding)
print(model.summary())

model.compile(loss='mse', metrics=['mse'])
model.fit(x_train, y_train, epochs=150)
model.evaluate(x_train)

user_size = input(f'Введите размер пиццы: {", ".join(size_kinds)}\n')
user_time = input(f'Введите время приготовления пиццы: h:m:s\n')
user_size_preprocessed = encoding_size[user_size] / max(sizes)
user_time_preprocessed = timeToSec(user_time) / time_max[0]
user_tenor = np.array([user_size_preprocessed, user_time_preprocessed]).reshape(1, 2)
print(user_tenor.shape)
result_tensor = model.predict(user_tenor)
result = result_tensor * max(prices)
print(f'Ваша пицца стоит {result[0, 0]}$\nЗаплатите в течении 1 часа на сбербанк '
      f'+7 (913) 024-61-55, в противном случае мы продадим ваши долги в '
      f'коллекторскую компанию')
