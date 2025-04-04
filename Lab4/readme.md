# Laboratorium4 – Konturowanie i operacje morfologiczne

Projekt zawiera skrypt Pythona realizujący analizę obrazu z wykorzystaniem konturowania, progowania oraz operacji morfologicznych w celu oczyszczenia obrazu i usunięcia drobnych artefaktów.

## 📌 Cel zadania

Celem zadania jest przetworzenie obrazu poprzez:

- wyodrębnienie konturów,
- zastosowanie progowania,
- usunięcie zakłóceń i szumów za pomocą operacji morfologicznych (`open` i `close`).

## 🧠 Funkcjonalność

Skrypt:

1. Wczytuje obraz z folderu roboczego.
2. Przeprowadza konturowanie obrazu (z użyciem wcześniej przygotowanych masek lub gotowej funkcji).
3. Stosuje progowanie do binarnej segmentacji obrazu.
4. Wykonuje operacje morfologiczne:
   - **Otwarcie (open)** – w celu usunięcia drobnych zakłóceń,
   - **Zamknięcie (close)** – w celu wypełnienia niewielkich dziur w obiektach.
5. Wyświetla i zapisuje kolejne etapy przetwarzania obrazu.

## 🖼️ Wynik

Efektem działania skryptu jest obraz z wyraźnie wyodrębnionymi strukturami, oczyszczony z drobnych artefaktów oraz gotowy do dalszej analizy.

Wyniki zapisywane są w postaci plików graficznych przedstawiających poszczególne etapy przetwarzania.
