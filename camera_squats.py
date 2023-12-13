import cv2
import numpy as np
import mediapipe as mp

class VideoCamera_S(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()

        self.left_knee_up = False
        self.right_knee_up = False
        self.squat_count = 0
        self.prev_squat_side = None

    def __del__(self):
        self.video.release()

    def calculate_angle(self, a, b, c):
        a = np.array([a.x, a.y])
        b = np.array([b.x, b.y])
        c = np.array([c.x, c.y])

        ab = b - a
        bc = b - c

        theta = np.arccos(np.dot(ab, bc) / (np.linalg.norm(ab) * np.linalg.norm(bc)))
        angle = np.degrees(theta)
        return angle

    def get_remaining_squats(self, count):
        remaining_squats = max(0, count - self.squat_count)
        return remaining_squats

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

            right_hip = landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP]
            right_knee = landmarks[self.mp_pose.PoseLandmark.RIGHT_KNEE]
            right_ankle = landmarks[self.mp_pose.PoseLandmark.RIGHT_ANKLE]

            # Calculate angles
            left_angle = self.calculate_angle(left_hip, left_knee, left_ankle)
            right_angle = self.calculate_angle(right_hip, right_knee, right_ankle)

            # Check for squat reps
            if left_angle < 100 and not self.left_knee_up:
                self.left_knee_up = True
                self.prev_squat_side = 'left'
            elif left_angle > 160 and self.left_knee_up:
                self.left_knee_up = False

            if right_angle < 100 and not self.right_knee_up:
                self.right_knee_up = True
                self.prev_squat_side = 'right'
            elif right_angle > 160 and self.right_knee_up:
                self.right_knee_up = False

                # Count a squat only if the current knee lift is of the opposite side
                if self.prev_squat_side == 'left':
                    self.squat_count += 1

            # Draw squat count on the frame
            cv2.putText(frame, f'Remaining Squats: {remaining_squats}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            mp.solutions.drawing_utils.draw_landmarks(
                frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

        # Encode the frame to JPEG for streaming
        ret, jpeg = cv2.imencode('.jpg', frame)
        
        return jpeg.tobytes(), remaining_squats
