import cv2
import mediapipe as mp
import numpy as np
import pickle
import pygame
import time
from gtts import gTTS
from mutagen.mp3 import MP3


def Play(text1):
    """Convert text to speech and play it"""
    print(f"\nPredicted: {text1}")
    myobj = gTTS(text=text1, lang='en', tld='com', slow=False)
    myobj.save("voice.mp3")

    print('\n------------Playing--------------\n')
    song = MP3("voice.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load('voice.mp3')
    pygame.mixer.music.play()
    time.sleep(song.info.length)
    pygame.quit()


# Load trained model
with open('number.pkl', 'rb') as f1:
    svm1 = pickle.load(f1)

# Mediapipe setup
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Open camera
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Resize for consistency
        image = cv2.resize(image, (500, 500))

        # Convert the BGR image to RGB before processing
        image.flags.writeable = False
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        # Draw hand landmarks
        image.flags.writeable = True
        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            n = len(results.multi_hand_landmarks)
            print("Hands detected:", n)

            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

            without_garbage, clean = [], []
            for i in range(n):
                data = results.multi_hand_landmarks[i]
                data = str(data).strip().split('\n')

                garbage = ['landmark {', '  visibility: 0.0', '  presence: 0.0', '}']
                for j in data:
                    if j not in garbage:
                        without_garbage.append(j)

                for j in without_garbage:
                    j = j.strip()
                    clean.append(j[2:])

                for k in range(len(clean)):
                    clean[k] = float(clean[k])

            # Predict gesture if one hand is detected
            if n == 1:
                Class = svm1.predict(np.array(clean).reshape(-1, 63))
                Class = str(Class[0])  # convert numeric result to string
                Play(Class)
                cv2.putText(image, Class, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 2)
            else:
                print("Multiple hands detected, skipping classification.")

        # Show video feed
        cv2.imshow('MediaPipe Hands', image)

        # Exit on 'q'
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
