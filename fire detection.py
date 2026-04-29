import cv2
import numpy as np
import threading
import time
import pygame
# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load("alarm.mp3")

# Globals for alarm control
alarm_playing = False
alarm_lock = threading.Lock()

def start_alarm():
    global alarm_playing
    with alarm_lock:
        if not alarm_playing:
            print("🔔 Alarm started.")
            pygame.mixer.music.play(-1)  # loop alarm
            alarm_playing = True
            threading.Thread(target=stop_alarm_after_delay, daemon=True).start()

def stop_alarm_after_delay():
    global alarm_playing
    time.sleep(60)  # run alarm for 60 seconds
    with alarm_lock:
        pygame.mixer.music.stop()
        alarm_playing = False
        print("🔕 Alarm stopped after 1 minute.")

def detect_fire(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Fire-like color range in HSV
    lower_fire = np.array([10, 100, 200])  # stricter range to avoid false positives
    upper_fire = np.array([35, 255, 255])

    mask = cv2.inRange(hsv, lower_fire, upper_fire)

    # Optional: Morphology to reduce noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    fire_detected = False
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 2000:  # area threshold to ignore small objects
            # Optional: Brightness check — mean V channel inside contour
            mask_contour = np.zeros(mask.shape, dtype=np.uint8)
            cv2.drawContours(mask_contour, [cnt], -1, 255, -1)
            mean_val = cv2.mean(hsv[:, :, 2], mask=mask_contour)[0]  # mean brightness (V)

            if mean_val > 200:  # high brightness typical of fire
                fire_detected = True
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(frame, "🔥 Fire Detected!", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

    return frame, fire_detected

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame, fire = detect_fire(frame)
        cv2.imshow("Fire Detection", processed_frame)

        if fire:
            print("🔥 Fire detected!")
            start_alarm()  # start alarm (if not already playing)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    pygame.mixer.music.stop()

if __name__ == "__main__":
    main()