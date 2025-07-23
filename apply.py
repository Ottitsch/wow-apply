import pyautogui
import time
import keyboard
import random
import math
from datetime import datetime

stop_flag = False

def human_like_move(x, y, duration_range, jitter):
    """Use a single pyautogui.moveTo with easing to simulate human-like motion"""
    end_x = x + random.randint(-jitter, jitter)
    end_y = y + random.randint(-jitter, jitter)
    duration = random.uniform(*duration_range)
    pyautogui.moveTo(end_x, end_y, duration=duration, tween=pyautogui.easeInOutQuad)

def stop():
    global stop_flag
    stop_flag = True
    print("\n[!] Quit signal received. Exiting immediately...")

def safe_click(x, y, jitter=5):
    """Click with slight randomness in position"""
    if stop_flag:
        return
    human_like_move(x,y,duration_range=(0.05, 0.1),jitter=jitter)
    pyautogui.click(x,y)

def refresh():
    if stop_flag:
        return
    print("Refreshing dungeon")
    safe_click(550, 155)
    time.sleep(random.uniform(0.3, 0.6))

def cancel():
    safe_click(530, 220)
    safe_click(530, 250)
    safe_click(530, 290)
    safe_click(530, 330)
    safe_click(530, 365)

def apply(x, y):
    if stop_flag:
        return
    print(f"Applying to group at ({x},{y})")
    safe_click(x, y, 15)
    time.sleep(random.uniform(0.3, 0.6))
    safe_click(500, 530)
    time.sleep(random.uniform(0.2, 0.4))
    safe_click(900, 310)
    time.sleep(random.uniform(0.5, 1.0))

def main():
    start = datetime.now()
    global stop_flag
    print("Starting auto-apply script. Press 'q' to quit immediately.")
    keyboard.add_hotkey('q', stop)

    while not stop_flag:
        cancel()
        refresh()
        apply(500, 220)
        apply(500, 250)
        apply(500, 290)
        apply(500, 330)
        apply(500, 365)
        safe_click(900, 310)
        # Random delay between cycles (e.g. 4 to 7 seconds)
        wait_time = random.uniform(4.0, 7.0)
        for _ in range(int(wait_time / 0.5)):
            if stop_flag:
                break
            time.sleep(0.5)

    end = datetime.now()
    print("Total time spent in queue: ", end-start)
    print("Script stopped.")

if __name__ == "__main__":
    print("Switch to WoW window in 5 seconds...")
    time.sleep(5)
    main()

