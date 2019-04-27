# Asennusohje

- Vaatimukset: Python3, venv, SQLITE, Postgres (tuotannossa)
1. Lataa lähdekoodi
2. Luo virtualevnrionment: "virtualenv venv"
3. Käynnistä virtualenv: "source venv/bin/activate"
4. Lataa lisäosat: "pip install -r requirements.txt"
5. Käynnistä sovellus: "python run.py"
6. Avaa kansiossa /app oleva .db tiedosta komennolla: "sqlite3 games.db"
7. Suorita komento "INSERT INTO account (name, username, password) VALUES ('hello world', 'hello', 'world');" 
8. Nyt pääset kirjautumaan sekä testaamaan sovellusta käyttänimellä "hello" ja salasanalla "world