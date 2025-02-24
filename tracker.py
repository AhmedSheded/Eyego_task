import cv2

def main():
    cap = cv2.VideoCapture(0)


    # frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # fps = 30
    #
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter('output.avi', fourcc, fps, (frame_width, frame_height))
    #
    _, frame = cap.read()

    print("Select an object to track and press SPACE or ENTER.")
    bbox = cv2.selectROI("Tracker", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Tracker")

    tracker = cv2.TrackerCSRT_create()
    tracker.init(frame, bbox)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        success, bbox = tracker.update(frame)
        if success:
            x, y, w, h = map(int, bbox)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Tracking Lost", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # out.write(frame)

        cv2.imshow("Object Tracker", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("[INFO] Exiting...")
            break

    cap.release()
    # out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()