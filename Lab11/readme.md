
# Laboratorium 11 – Korekcja temperatury barwowej (White Balance)

Projekt zawiera skrypt Pythona służący do przeprowadzenia korekcji temperatury barwowej obrazu, w celu uzyskania możliwie neutralnej bieli na podstawie wybranej próbki z obrazu.

## 📌 Cel zadania

Celem zadania jest:

- wczytanie obrazu z nieprawidłowym balansem bieli,
- wskazanie fragmentu obrazu, który powinien być biały,
- obliczenie średnich wartości kanałów kolorów (BGR) dla tego obszaru,
- przeskalowanie całego obrazu tak, aby ten fragment miał zrównoważone składowe kolorów,
- uzyskanie obrazu z naturalnym odwzorowaniem barw.

## 🧠 Funkcjonalność

Skrypt:

1. Wczytuje obraz `krasnal.jpg`.
2. Wybiera ręcznie zdefiniowaną próbkę obszaru obrazu (np. biały element sceny).
3. Oblicza średnią wartość kanałów B, G, R z tej próbki.
4. Oblicza współczynniki korekcji, aby wyrównać te kanały do wspólnej wartości średniej.
5. Przeskalowuje obraz zgodnie z wyliczonymi współczynnikami.
6. Wyświetla i zapisuje obraz wynikowy jako `white_balanced.jpg`.

## 🖼️ Wynik

Efektem działania skryptu jest obraz o poprawionej kolorystyce, w którym zdefiniowany fragment (biały) został rzeczywiście zrównoważony względem barwy – dzięki czemu całe zdjęcie wygląda bardziej naturalnie.

---

**Przykład użycia:**  
Użytkownik może zmienić współrzędne fragmentu `img[220:240, 100:120]`, jeśli biały obszar znajduje się w innym miejscu na obrazie.

