import cv2
import numpy as np
import mediapipe as mp

class VideoCamera_S(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()

        self.knee_bend_threshold = 100
        self.squat_count = 0
        self.is_squatting = False

    def __del__(self):
        self.video.release()

    def get_remaining_squats(self, count):
        remaining_squats = max(0, count - self.squat_count)
        return remaining_squats

    def calculate_angle(self, a, b, c):
        a = np.array([a.x, a.y])
        b = np.array([b.x, b.y])
        c = np.array([c.x, c.y])

        ab = b - a
        bc = b - c

        theta = np.arccos(np.dot(ab, bc) / (np.linalg.norm(ab) * np.linalg.norm(bc)))
        angle = np.degrees(theta)
        return angle

    def get_frame_squats(self, count):
        remaining_squats = self.get_remaining_squats(count)
        ret, frame = self.video.read()

        # Convert the frame to RGB for Mediapipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with Mediapipe Pose
        results = self.pose.process(rgb_frame)

        # Draw landmarks on the frame
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            left_hip = landmarks[self.mp_pose.PoseLandmark.LEFT_HIP]
            left_knee = landmarks[self.mp_pose.PoseLandmark.LEFT_KNEE]
            left_ankle = landmarks[self.mp_pose.PoseLandmark.LEFT_ANKLE]

            # Calculate angle
            left_angle = self.calculate_angle(left_hip, left_knee, left_ankle)

            # Check for squat reps
            if left_angle < self.knee_bend_threshold and not self.is_squatting:
                self.is_squatting = True
            elif left_angle > (180 - self.knee_bend_threshold) and self.is_squatting:
                self.is_squatting = False
                self.squat_count += 1

            # Draw squat count on the frame
            cv2.putText(frame, f'Remaining Squats: {remaining_squats}', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            mp.solutions.drawing_utils.draw_landmarks(
                frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

        # Encode the frame to JPEG for streaming
        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes(), remaining_squats
