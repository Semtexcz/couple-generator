# Couple Generator

CLI nástroj pro generování náhodných dvojic ze seznamu jmen uložených v CSV souboru.  
Pokud je počet osob lichý, jeden člověk zůstane sám.

## Instalace

Doporučený způsob instalace je pomocí [pipx](https://pypa.github.io/pipx/):

```bash
pipx install .
````

Tím se zpřístupní příkaz `couple-generator` v systému.

Pokud nechceš používat pipx, můžeš nainstalovat také klasicky:

```bash
pip install .
```

## Použití

Základní použití:

```bash
couple-generator jmena.csv
```

### Vstupní CSV

Nástroj rozpozná, zda CSV obsahuje:

* **1 sloupec** – jedno jméno na řádek
* **2 sloupce** – jméno a příjmení (budou spojeny mezerou)

#### Příklad (1 sloupec):

```csv
Anna
Petr
Jan
Eva
Lucie
```

#### Příklad (2 sloupce):

```csv
Anna,Nováková
Petr,Dvořák
Jan,Svoboda
Eva,Malá
Lucie,Horáková
```

### Výstup

```
Dvojice:
- Jan Svoboda & Lucie Horáková
- Petr Dvořák & Eva Malá
Zůstal sám: Anna Nováková
```

## Vývoj

Po úpravách kódu lze příkaz spustit lokálně přímo přes `poetry run`:

```bash
poetry run couple-generator jmena.csv
```

## Autor

* [Daniel Kopecký](mailto:kopecky.d@gmail.com)


