# Laboratorium 8 – Progowanie w przestrzeni HSV

Projekt zawiera skrypt Pythona, którego celem jest izolacja kwiatu z kolorowego obrazu przy użyciu przestrzeni barw HSV oraz operacji progowania.

## 📌 Cel zadania

Celem zadania jest:

- konwersja obrazu RGB do przestrzeni HSV,
- wykonanie progowania na warstwie H (Hue), aby wyodrębnić obiekt (kwiat),
- zastosowanie uzyskanej maski binarnej do oryginalnego obrazu w celu izolacji kwiatu z tła,
- wygenerowanie i zapisanie wyników oraz obrazów pośrednich.

## 🧠 Funkcjonalność

Skrypt:

1. Wczytuje obraz przedstawiający czerwony kwiat.
2. Konwertuje obraz z przestrzeni BGR do HSV za pomocą `cv2.cvtColor`.
3. Dla kanału H wykonuje progowanie – ustalany jest zakres odpowiadający barwie kwiatu.
4. Tworzy maskę binarną, która wyodrębnia piksele odpowiadające kwiatowi.
5. Stosuje tę maskę na oryginalnym obrazie, aby usunąć tło.
6. Wyświetla i zapisuje:
   - obraz HSV,
   - binarną maskę,
   - końcowy obraz z wyizolowanym kwiatem.

## 🖼️ Wynik

Efektem działania skryptu są:

- 🌸 Obraz z wyodrębnionym kwiatem,
- 🖤 Maska binarna pokazująca obszary odpowiadające wybranemu kolorowi,
- 🎨 Obraz HSV oraz poszczególne jego kanały (opcjonalnie),
- Pliki graficzne gotowe do zamieszczenia w sprawozdaniu.
