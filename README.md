# Numbers-to-text-converter
Aplikacja 'liczby pisane slownie' oparta jest na Django.
Składa się z formularza, w którym przekazana jest liczba całkowita oraz widoku, który zwraca zapis słowny danej liczby.

### Przykład działania:
- input: 10, output: “dziesięć”
- input: 67, output: “sześćdziesiąt siedem”
- input: 11234981, output: “jedenaście milionów dwieście trzydzieści cztery tysiące dziewięćset osiemdziesiąt jeden”



### Podsumowanie:
- [x] Serwer Django otwiera stronę poprawnie
- [x] Działa tylko dla zakresu liczb 1-999
- [x] Działa w Javascript
- [ ] Nie działa w Pythonie (problem z uruchomieniem zdarzeń klawiatury - standardowy moduł Pythona 'keyboard' nie działa w Windowsie)
- [ ] Nie wyświetla poprawnie nazw dla liczb powyżej tysiąca (np. 25805)
