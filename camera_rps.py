import cv2
from keras.models import load_model
import numpy as np
import time
import random

time_limit = 5
start_time = time.time()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    start_time = time.time()
    time_limit = 3
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image
        prediction = model.predict(data)
        if (time.time() - start_time) > time_limit:
            break

        cv2.imshow('frame', frame)

        if prediction[0][0] > 0.5:
            user_choice = "rock"
        elif prediction[0][1] > 0.5:
            user_choice = "paper"
        elif prediction[0][2] > 0.5:
            user_choice = "scissors"
        else:
            user_choice = "nothing"
    return user_choice

    cap.release()
    cv2.destroyAllWindows()

def get_winner():
    computer_wins = 0
    user_wins = 0
    game_msg = ""

    while True:
        user_choice = get_user_choice()
        print("User choice:", user_choice)
        computer_choice = get_computer_choice()
        print("Computer choice:", computer_choice)

        if (computer_choice == user_choice):
            game_msg = ("draw")
        elif (user_choice == "rock") and (computer_choice == "paper"):
            game_msg = ("you have lost")
            computer_wins += 1
        elif (user_choice == "rock") and (computer_choice == "scissors"):
            game_msg = ("you have won")
            user_wins += 1
        elif (user_choice == "paper") and (computer_choice == "rock"):
            game_msg = ("you have won")
            user_wins += 1
        elif (user_choice == "paper") and (computer_choice == "scissors"):
            game_msg = ("you have lost")
            computer_wins += 1
        elif (user_choice == "scissors") and (computer_choice == "rock"):
            game_msg = ("you have lost")
            computer_wins += 1
        elif (user_choice == "scissors") and (computer_choice == "paper"):
            game_msg = ("you have won")
            user_wins += 1

        if user_wins == 3 or computer_wins == 3:
            break

    print(game_msg)
    print("User Wins: ", user_wins)
    print("Computer Wins: ", computer_wins)

get_winner()