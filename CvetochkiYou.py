from tensorflow import keras
from keras.layers import Input, Dense, Conv2D, Flatten
from keras.models import Sequential


def getModel():
    model = Sequential()
    model.add(Input((28, 28, 1)))
    model.add(Conv2D(filters=32, kernel_size=(4, 4), activation="relu"))
    model.add(Flatten())
    model.add(Dense(units=10, activation="softmax"))
    model.compile(loss="categorical_crossentropy", metrics=["accuracy", "mse"])
    return model


def prepareData():
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    x_train = x_train / 255
    x_test = x_test / 255
    y_train = keras.utils.to_categorical(y_train)
    y_test = keras.utils.to_categorical(y_test)
    return x_train, y_train, x_test, y_test


if __name__ == "__main__":
    model = getModel()
    x, y, xt, yt = prepareData()
    model.fit(x, y, epochs=138, batch_size=32)
    model.save("mama-savely")
    model.evaluate(xt, yt)
