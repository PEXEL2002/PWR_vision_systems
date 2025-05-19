import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# === PARAMETRY ===
FOLDER = "Photo"
OUTPUT_GIF = "output/animation.gif"
DELTA_FILE = "output/delta.txt"
FPS = 10

# === PRZYGOTOWANIE FOLDERU WYJŚCIOWEGO ===
os.makedirs("output", exist_ok=True)

# === WCZYTYWANIE I SORTOWANIE OBRAZÓW ===
image_files = sorted([
    os.path.join(FOLDER, f)
    for f in os.listdir(FOLDER)
    if f.lower().endswith((".jpg", ".png"))
])

frames = []
laser_coords = []
delta_steps = []

# === DETEKCJA I OBLICZANIE PRZESUNIĘĆ KROK PO KROKU ===
prev_coord = None

for file in image_files:
    img = cv2.imread(file)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    frames.append(img_rgb)

    # Detekcja najjaśniejszego punktu
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, _, _, max_loc = cv2.minMaxLoc(gray)
    laser_coords.append(max_loc)

    # Oblicz przesunięcie względem poprzedniego punktu
    if prev_coord is None:
        delta_steps.append((0, 0))  # brak ruchu w 1. klatce
    else:
        dx = max_loc[0] - prev_coord[0]
        dy = -(max_loc[1] - prev_coord[1])
        delta_steps.append((dx, dy))

    prev_coord = max_loc

# === CAŁKOWITE PRZESUNIĘCIE OD POCZĄTKU DO KOŃCA ===
start_x, start_y = laser_coords[0]
end_x, end_y = laser_coords[-1]
total_dx = end_x - start_x
total_dy = end_y - start_y

# === ZAPIS WSZYSTKICH PRZESUNIĘĆ DO PLIKU ===
with open(DELTA_FILE, "w", encoding="utf-8") as f:
    f.write(f"ΔX całkowite = {total_dx}, ΔY całkowite = {total_dy}\n")
    f.write(f"Start: ({start_x}, {start_y})\n")
    f.write(f"End:   ({end_x}, {end_y})\n\n")
    f.write("🧭 Przesunięcia między klatkami:\n")
    for i, (dx, dy) in enumerate(delta_steps):
        f.write(f"Klatka {i + 1}: ΔX = {dx}, ΔY = {dy}\n")

# === GENEROWANIE GIF ===
fig, ax = plt.subplots()
im = ax.imshow(frames[0])
plt.axis('off')

def update(frame):
    im.set_data(frames[frame])
    return [im]

ani = FuncAnimation(fig, update, frames=len(frames), interval=1000 / FPS, blit=True)
ani.save(OUTPUT_GIF, writer=PillowWriter(fps=FPS))

print("Gotowe:")
print(f"  - GIF zapisany jako: {OUTPUT_GIF}")
print(f"  - ΔX, ΔY dla każdej klatki zapisane w: {DELTA_FILE}")
