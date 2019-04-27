# Shakkipelit

Ohjelmalla voi selata shakkipelejä mitä ohjelmaan on syötetty. Ohjelmassa on näkymä, jossa listataan kaikki pelit. Listasta pääsee kyseisen pelin tietoihin, josta näkyy tarkemmat tiedot esim. kaikki siirrot. Näkystä pääsee myös muuttamaan pelin tietoja.

Sovelluksen pääsivulta pääsee myös näkymään, jossa pelin voi lisätä.

Toiminnot:
- uuden pelin syöttäminen
- pelien selailu
- pelien hakeminen sijainnin, pelaajien, aloituksen mukaan
- pelien muokkaus
- pelien haku käyttäjän, aloituksen, sijainnin tai päivämäärän mukaan

Sovellus sijaitsee herokussa osoitteessa: https://shakkipelit.herokuapp.com/games

### Testitunnukset

Nimi:hello
Salasana:world

## Käyttötapaukset

[Tarkempi kuvaus käyttötapauksista](https://github.com/AlecSiikaluoma/Shakkipelit/blob/master/documentation/kayttotapaukset.md)

## Tietokannan rakenne

Tietokannassa säilytetään pelit "game" -taulussa. On myös "opening" taulu, jossa säilytetään tunnetut aloitukset. Nämä kaksi taulua voidaan liitää keskenään.

[Tietokantakaavio](https://github.com/AlecSiikaluoma/Shakkipelit/blob/master/documentation/tietokantakaavio.jpg)

## Jatkokehitys

Sovellusta voisi laajentaa lukemaan .pgn muotoisia pelitiedostaja ja peli näkymään voisi lisätä jonkin yksinkertaisen JavaScript shakkilaudan, jossa peli voitaisiin visualisoida.

## Ohjeet

[Käyttöohje](https://github.com/AlecSiikaluoma/Shakkipelit/blob/master/documentation/kayttoohje.md)
[Asennusohje](https://github.com/AlecSiikaluoma/Shakkipelit/blob/master/documentation/asennusohje.md)
