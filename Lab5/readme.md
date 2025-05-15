# Laboratorium 5 – Wyrównanie kartki względem obrazu

Projekt zawiera skrypt Pythona, którego celem jest wykrycie i wyrównanie kartki znajdującej się na obrazie względem jego krawędzi, przy użyciu progowania i transformaty Hougha.

## 📌 Cel zadania

Celem zadania jest:

- oddzielenie kartki od tła,
- wykrycie linii krawędzi kartki za pomocą transformaty Hougha,
- obliczenie kąta odchylenia i przekształcenie obrazu tak, aby kartka była wyrównana względem krawędzi obrazu,
- wizualizacja wszystkich etapów przetwarzania.

## 🧠 Funkcjonalność

Skrypt:

1. Wczytuje obraz zawierający kartkę.
2. Przeprowadza silne rozmycie obrazu (np. za pomocą filtra Gaussa), aby zredukować szumy przed progowaniem.
3. Wykonuje progowanie binarne, aby oddzielić kartkę od tła.
4. Stosuje transformację Hougha (`cv2.HoughLines` lub `cv2.HoughLinesP`) do wykrycia linii prostych odpowiadających krawędziom kartki.
5. Oblicza kąty wykrytych linii i wybiera dominujący kierunek.
6. Obraca obraz w taki sposób, aby kartka była zgodna z poziomą/pionową osią obrazu.
7. Wyświetla i zapisuje kolejne etapy przetwarzania, w tym:
   - Obraz po rozmyciu,
   - Obraz po progowaniu,
   - Obraz z nałożonymi wykrytymi liniami,
   - Obraz po wyrównaniu.

## 🖼️ Wynik

Efektem działania skryptu jest obraz z wyrównaną kartką względem krawędzi kadru. Dodatkowo generowane są obrazy pośrednie dokumentujące każdy etap przetwarzania. Wszystkie wyniki zapisywane są w formacie graficznym do dalszej analizy lub sprawozdania.
