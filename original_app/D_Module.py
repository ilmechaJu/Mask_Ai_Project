import cv2
import mediapipe as mp
from dynamikontrol import Module
import tensorflow as tf
import numpy as np
import time


class MaskPipeline:
    def __init__(self) -> None:
        # Define the input size of the model
        self.input_size = (224, 224)
        self.model = tf.keras.models.load_model("saved_model.h5")

        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_face_detection = mp.solutions.face_detection

        self.face_detection = self.mp_face_detection.FaceDetection(
            min_detection_confidence=0.7
        )

    def get_processing(self, img_ori_path: str):
        start_time = time.time()
        frame = cv2.imread(img_ori_path)
        if not frame:
            return

        model_frame = cv2.resize(frame, self.input_size, frame)
        # Expand Dimension (224, 224, 3) -> (1, 224, 224, 3) and Normalize the data
        model_frame = np.expand_dims(model_frame, axis=0) / 255.0

        # Predict
        is_mask_prob = self.model.predict(model_frame)[0]
        is_mask = np.argmax(is_mask_prob)

        # Compute the model inference time
        inference_time = time.time() - start_time
        fps = 1 / inference_time
        fps_msg = "Time: {:05.1f}ms {:.1f} FPS".format(inference_time * 1000, fps)

        if is_mask == 0:
            msg_mask = "Mask Off"
        else:
            msg_mask = "Mask On"

        msg_mask += " ({:.1f})%".format(is_mask_prob[is_mask] * 100)

        frame = cv2.flip(frame, 1)  # mirror image

        results = self.face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if results.detections:
            for detection in results.detections:
                self.mp_drawing.draw_detection(frame, detection)

                cv2.putText(
                    frame,
                    fps_msg,
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 0),
                    thickness=1,
                )
                cv2.putText(
                    frame,
                    msg_mask,
                    (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    thickness=2,
                )
                break

        img_name, img_ext = img_ori_path.split(".")
        ret_image_path = img_name + "_ret." + img_ext
        cv2.imwrite(ret_image_path, frame)
        return ret_image_path

        # Show the frame passed to the model
        # cv2.imshow("debug", model_frame[0])

    # face_detection.close()
    # module.disconnect()


mask_pipeline = MaskPipeline()
