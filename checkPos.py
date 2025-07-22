import pyautogui
import time
import keyboard  # For global hotkeys

def main():
    screen_width, screen_height = pyautogui.size()
    print(f"Virtual screen size (includes all monitors): {screen_width} x {screen_height}")
    print("Move the mouse around. Press 'q' to stop.\n")

    while True:
        if keyboard.is_pressed('q'):  # Stop if 'q' is pressed
            print("\nStopped by user.")
            break

        x, y = pyautogui.position()
        print(f"Mouse position: X={x:6}  Y={y:6}", end='\r')
        time.sleep(0.1)

if __name__ == "__main__":
    main()

