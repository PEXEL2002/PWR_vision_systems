# Laboratorium 7 – Wykrywanie i śledzenie wskaźnika laserowego

Projekt zawiera skrypt Pythona, którego celem jest wczytanie sekwencji obrazów przedstawiających poruszający się wskaźnik laserowy na ścianie, wizualizacja tej sekwencji jako animacja poklatkowa oraz detekcja położenia lasera wraz z obliczeniem przesunięcia.

## 📌 Cel zadania

Celem zadania jest:

- wczytanie sekwencji obrazów w odpowiedniej kolejności,
- wyświetlenie animacji z określoną prędkością (symulacja filmu poklatkowego),
- wykrycie położenia wskaźnika laserowego na każdym z obrazów,
- obliczenie i zapisanie przesunięcia ΔX, ΔY pomiędzy pierwszą a ostatnią klatką,
- wygenerowanie animacji w formacie `.gif`,
- przygotowanie sprawozdania z uzyskanymi wynikami.

## 🧠 Funkcjonalność

Skrypt:

1. Wczytuje obrazy z archiwum `.zip` lub folderu (upewniając się, że są posortowane po nazwie).
2. Tworzy animację z obrazów z określoną częstotliwością klatek.
3. Wykrywa wskaźnik laserowy na każdej klatce (np. poprzez analizę jasności lub koloru).
4. Zapisuje współrzędne położenia punktu laserowego dla każdej klatki.
5. Oblicza przesunięcie ΔX, ΔY względem pozycji początkowej.
6. Generuje animację w formacie `.gif` przedstawiającą ruch wskaźnika.
7. Zapisuje wyniki oraz obrazy do folderu projektu.

## 🖼️ Wynik

Efektem działania skryptu są:

- 🎞️ Animacja `.gif` przedstawiająca ruch wskaźnika laserowego na ścianie,
- 📍 Plik tekstowy lub konsolowy z informacją o przesunięciu punktu laserowego między klatkami: `ΔX` i `ΔY`