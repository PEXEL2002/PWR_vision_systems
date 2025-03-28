# Laboratorium3 – Progowanie obrazu

Ten projekt zawiera skrypt Pythona realizujący różne metody progowania na obrazie z kamery termowizyjnej, przedstawiającym prostokątną płytkę grzewczą.

## 📌 Cel zadania

Celem jest analiza obrazu termowizyjnego poprzez wyodrębnienie pola temperatury oraz porównanie wyników trzech metod progowania.

## 🧠 Funkcjonalność

Skrypt:

1. Wczytuje obraz podany jako argument (lub z pliku).
2. Pozwala wybrać fragment obrazu zawierający wyłącznie pole temperatury.
3. Wykonuje progowanie trzema metodami:
   - **Proste progowanie** (globalne),
   - **Progowanie adaptacyjne**,
   - **Progowanie metodą Otsu**.
4. Wyświetla i zapisuje wyniki każdej z metod progowania.
5. Eksportuje rezultaty do plików graficznych.