# Laboratorium 9 – Wyrównanie histogramu obrazu

Projekt zawiera skrypt Pythona, którego celem jest poprawa kontrastu obrazu poprzez przekształcenie go do odcieni szarości, analizę histogramu oraz wykonanie wyrównania histogramu.

## 📌 Cel zadania

Celem zadania jest:

- przekształcenie obrazu do odcieni szarości,
- wyznaczenie i zapisanie histogramu intensywności przed przetwarzaniem,
- wykonanie wyrównania histogramu (ang. histogram equalization),
- zapisanie przetworzonego obrazu oraz nowego histogramu.

## 🧠 Funkcjonalność

Skrypt:

1. Wczytuje obraz z pliku.
2. Konwertuje obraz na odcienie szarości (`cv2.cvtColor(..., cv2.COLOR_BGR2GRAY)`).
3. Wyznacza histogram obrazu przed wyrównaniem i zapisuje go w postaci wykresu.
4. Przeprowadza wyrównanie histogramu (`cv2.equalizeHist(...)`) w celu poprawy kontrastu.
5. Zapisuje:
   - obraz w odcieniach szarości,
   - obraz po wyrównaniu histogramu,
   - histogramy przed i po wyrównaniu.
6. Wyświetla obrazy i histogramy (opcjonalnie).

## 🖼️ Wynik

Efektem działania skryptu są:

- Obraz w odcieniach szarości (`gray_output.jpg`),
- Histogram obrazu przed wyrównaniem (`histogram_before.png`),
- Obraz po wyrównaniu histogramu (`equalized_output.jpg`),
- Histogram po wyrównaniu (`histogram_after.png`).

Wszystkie wyniki są zapisywane w formie graficznej i mogą być użyte w sprawozdaniu.
