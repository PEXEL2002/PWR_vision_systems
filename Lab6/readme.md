# Laboratorium 6 – Analiza stabilności punktów charakterystycznych

Projekt zawiera skrypt Pythona, który umożliwia detekcję charakterystycznych punktów obrazu (rogów), a następnie analizę ich zachowania po obrocie obrazu.

## 📌 Cel zadania

Celem zadania jest:

- wykrycie punktów charakterystycznych (rogów) na obrazie,
- wykonanie obrotu obrazu o wybrany kąt (30–60°),
- ponowna detekcja punktów po transformacji,
- porównanie wyników w celu oceny stabilności wykrytych punktów względem transformacji geometrycznych.

## 🧠 Funkcjonalność

Skrypt:

1. Wczytuje dostarczony obraz.
2. Wykrywa rogi obrazu przy użyciu funkcji `cv2.goodFeaturesToTrack`.
3. Obraca obraz o wybrany kąt (np. 45°), przyjmując pionową linię kamienicy z lewej jako linię referencyjną.
4. Wykonuje ponowną detekcję rogów na obróconym obrazie.
5. Porównuje położenia wykrytych punktów przed i po transformacji.
6. Wyświetla obrazy z zaznaczonymi punktami przed i po obrocie.
7. Zapisuje wygenerowane obrazy do plików graficznych.
8. Generuje sprawozdanie prezentujące wyniki oraz interpretację zachowania punktów.

## 🖼️ Wynik

Efektem działania skryptu są:

- dwa obrazy z naniesionymi wykrytymi punktami charakterystycznymi – przed i po obrocie,
- porównanie rozmieszczenia punktów na obu obrazach,
- ocena ich trwałości względem transformacji geometrycznej (obrotu).

Wszystkie wyniki zapisywane są w formacie graficznym oraz tekstowym (raport), gotowe do dołączenia do sprawozdania.
