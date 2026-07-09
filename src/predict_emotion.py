import cv2
import numpy as np
from tensorflow.keras.models import load_model
import time

# ===========================
# Load Trained Model
# ===========================
model = load_model("trained_model/best_emotion_model.keras")

# Emotion Labels
emotion_labels = [
    "Angry",
    "Disgust",
    "Fear",
    "Happy",
    "Neutral",
    "Sad",
    "Surprise"
]

# Emojis
emoji = {
    "Angry": "😠",
    "Disgust": "🤢",
    "Fear": "😨",
    "Happy": "😊",
    "Neutral": "😐",
    "Sad": "😢",
    "Surprise": "😲"
}

# Face Detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

prev_time = time.time()

print("Emotion Detection Started...")
print("Press Q to Quit")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(60,60)
    )

    for (x,y,w,h) in faces:

        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face,(48,48))
        face = face.astype("float32")/255.0
        face = np.expand_dims(face,-1)
        face = np.expand_dims(face,0)

        prediction = model.predict(face,verbose=0)

        emotion_id = np.argmax(prediction)
        emotion = emotion_labels[emotion_id]
        confidence = np.max(prediction)*100

        color=(0,255,0)

        cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)

        cv2.putText(
            frame,
            f"{emotion} {confidence:.1f}%",
            (x,y-15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

    # FPS
    current=time.time()
    fps=1/(current-prev_time)
    prev_time=current

    cv2.putText(
        frame,
        f"FPS : {int(fps)}",
        (10,30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,0,0),
        2
    )

    cv2.imshow("Professional Emotion Detector",frame)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()