import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Start capturing from the webcam
cap = cv2.VideoCapture(0)

def get_finger_count(hand_landmarks):
    """
    Returns the number of fingers raised (0 to 5)
    """
    finger_tips = [8, 12, 16, 20]
    finger_count = 0

    # Check if each finger (except thumb) is raised
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            finger_count += 1

    # Thumb check (based on x position)
    if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
        finger_count += 1

    return finger_count

def get_command(finger_count):
    """
    Maps finger count to command
    """
    commands = {
        0: "STOP",
        1: "MOVE FORWARD",
        2: "MOVE BACKWARD",
        3: "TURN LEFT",
        4: "TURN RIGHT",
        5: "READY"
    }
    return commands.get(finger_count, "UNKNOWN")

while True:
    success, img = cap.read()
    if not success:
        break

    # Convert image to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    # If hand is detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            count = get_finger_count(hand_landmarks)
            command = get_command(count)

            # Display command on screen
            cv2.putText(img, f"Command: {command}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

            print("Gesture Detected:", command)

    # Show the webcam image
    cv2.imshow("Hand Gesture Recognition", img)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
