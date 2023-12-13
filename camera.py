import cv2
import numpy as np
import mediapipe as mp

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()

        self.left_elbow_up = False
        self.right_elbow_up = False
        self.rep_count = 0
        self.prev_curl_side = None

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

    def get_remaining_curls(self, count):
        remaining_curls = max(0, count - self.rep_count)
        return remaining_curls

    def get_frame(self, count):
        remaining_curls = self.get_remaining_curls(count)
        ret, frame = self.video.read()

        # Convert the frame to RGB for Mediapipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with Mediapipe Pose
        results = self.pose.process(rgb_frame)

        # Draw landmarks on the frame
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            left_shoulder = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER]
            left_elbow = landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW]
            left_wrist = landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST]

            right_shoulder = landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER]
            right_elbow = landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW]
            right_wrist = landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST]

            # Calculate angles
            left_angle = self.calculate_angle(left_shoulder, left_elbow, left_wrist)
            right_angle = self.calculate_angle(right_shoulder, right_elbow, right_wrist)

            # Check for bicep reps
            if left_angle > 160 and not self.left_elbow_up:
                self.left_elbow_up = True
                self.prev_curl_side = 'left'
            elif left_angle < 50 and self.left_elbow_up:
                self.left_elbow_up = False

            if right_angle > 160 and not self.right_elbow_up:
                self.right_elbow_up = True
                self.prev_curl_side = 'right'
            elif right_angle < 50 and self.right_elbow_up:
                self.right_elbow_up = False

                # Count a rep only if the current curl is of the opposite side
                if self.prev_curl_side == 'left':
                    self.rep_count += 1

            # Draw rep count on the frame
            cv2.putText(frame, f'Remaining Curls: {remaining_curls}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            mp.solutions.drawing_utils.draw_landmarks(
                frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

        # Encode the frame to JPEG for streaming
        ret, jpeg = cv2.imencode('.jpg', frame)

        
        return jpeg.tobytes(), remaining_curls