import cv2
import mediapipe as mp
from dynamikontrol import Module
import tensorflow as tf
import numpy as np
import time


# Define the input size of the model
input_size = (224, 224)
model = tf.keras.models.load_model("saved_model.h5")
ANGLE_STEP = 1

module = Module()

mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection

face_detection = mp_face_detection.FaceDetection(
    min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)
angle = 0 # motor current angle
cap.set(cv2.CAP_PROP_BUFFERSIZE, 5)

while cap.isOpened():
    start_time = time.time()
    ret, frame = cap.read()
    if not ret:
        break

    model_frame = cv2.resize(frame, input_size, frame)
    # Expand Dimension (224, 224, 3) -> (1, 224, 224, 3) and Normalize the data
    model_frame = np.expand_dims(model_frame, axis=0) / 255.0

    # Predict
    is_mask_prob = model.predict(model_frame)[0]
    is_mask = np.argmax(is_mask_prob)

    # Compute the model inference time
    inference_time = time.time() - start_time
    fps = 1 / inference_time
    fps_msg = "Time: {:05.1f}ms {:.1f} FPS".format(inference_time * 1000, fps)

    if is_mask == 0:
        msg_mask = "Mask Off"
    else:
        msg_mask = "Mask On"

    msg_mask += " ({:.1f})%".format(is_mask_prob[is_mask]*100)


    frame = cv2.flip(frame, 1) # mirror image

    results = face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(frame, detection)

            x1 = detection.location_data.relative_bounding_box.xmin # left side of face bounding box
            x2 = x1 + detection.location_data.relative_bounding_box.width # right side of face bounding box

            cx = (x1 + x2) / 2 # center of the face

            if cx < 0.4: # left -> clockwise
                angle += ANGLE_STEP
                module.motor.angle(angle)
            elif cx > 0.6: # right -> counter clockwise
                angle -= ANGLE_STEP
                module.motor.angle(angle)

            cv2.putText(frame, fps_msg, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness=1)
            cv2.putText(frame, msg_mask, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), thickness=2)
            # cv2.putText(frame, '%d deg' % (angle), org=(10, 110), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
            #             color=255, thickness=2)
            break
    # Show the result and frame
    cv2.imshow('Face Cam', frame)

    # Show the frame passed to the model
    cv2.imshow('debug', model_frame[0])


    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
face_detection.close()
module.disconnect()