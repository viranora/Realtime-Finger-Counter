import time
from dataclasses import dataclass

import cv2
import mediapipe as mp


@dataclass
class HandResult:
    landmarks: any
    handedness: str


class FingerCounter:
    """Parmakların açık/kapalı durumuna göre toplamı hesaplar."""

    FINGER_TIPS = [4, 8, 12, 16, 20]
    FINGER_PIPS = [2, 6, 10, 14, 18]

    def count(self, hand_result: HandResult) -> int:
        lm = hand_result.landmarks.landmark
        fingers = []

        thumb_tip = lm[self.FINGER_TIPS[0]]
        thumb_ip = lm[3]
        if hand_result.handedness == "Right":
            fingers.append(thumb_tip.x < thumb_ip.x)
        else:
            fingers.append(thumb_tip.x > thumb_ip.x)

        for tip_idx, pip_idx in zip(self.FINGER_TIPS[1:], self.FINGER_PIPS[1:]):
            fingers.append(lm[tip_idx].y < lm[pip_idx].y)

        return int(sum(fingers))


def main() -> None:
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        model_complexity=1,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.5,
    )
    mp_drawing = mp.solutions.drawing_utils
    mp_styles = mp.solutions.drawing_styles

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Kamera açılamadı. Lütfen bağlı olduğundan emin olun.")

    finger_counter = FingerCounter()
    prev_time = time.time()

    try:
        while True:
            success, frame = cap.read()
            if not success:
                print("Kare okunamadı, kamera bağlantısını kontrol edin.")
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb_frame.flags.writeable = False
            results = hands.process(rgb_frame)
            rgb_frame.flags.writeable = True

            finger_count = 0
            label_text = "El algılanmadı"

            if results.multi_hand_landmarks and results.multi_handedness:
                hand_landmarks = results.multi_hand_landmarks[0]
                handed_label = results.multi_handedness[0].classification[0].label
                hand_result = HandResult(hand_landmarks, handed_label)
                finger_count = finger_counter.count(hand_result)
                label_text = f"{handed_label} el - {finger_count} parmak"

                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_styles.get_default_hand_landmarks_style(),
                    mp_styles.get_default_hand_connections_style(),
                )

            current_time = time.time()
            fps = 1.0 / (current_time - prev_time) if current_time != prev_time else 0.0
            prev_time = current_time

            cv2.putText(
                frame,
                label_text,
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
                cv2.LINE_AA,
            )
            cv2.putText(
                frame,
                f"FPS: {fps:.1f}",
                (10, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )

            cv2.imshow("Parmak Sayma", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        hands.close()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
