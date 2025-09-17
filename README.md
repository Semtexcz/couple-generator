# Couple Generator

CLI nástroj pro generování náhodných dvojic nebo asymetrického přiřazení ze seznamu jmen uložených v CSV souboru.
Pokud je počet osob lichý, jeden člověk u symetrických dvojic zůstane sám.
V asymetrickém režimu každý dostane někoho jiného na opravu – tedy **nikdo nemá sám sebe a páry nejsou vzájemné**.

## Instalace

Doporučený způsob instalace je pomocí [pipx](https://pypa.github.io/pipx/):

```bash
pipx install .
```

Tím se zpřístupní příkaz `couple-generator` v systému.

Pokud nechceš používat pipx, můžeš nainstalovat také klasicky:

```bash
pip install .
```

## Použití

Základní použití (symetrické dvojice):

```bash
couple-generator jmena.csv
```

Asymetrické přiřazení (každý opravuje jiného):

```bash
couple-generator jmena.csv --asym
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

#### Symetrické dvojice:

```
Dvojice:
- Jan Svoboda & Lucie Horáková
- Petr Dvořák & Eva Malá
Zůstal sám: Anna Nováková
```

#### Asymetrické přiřazení:

```
Asymetrické přiřazení:
- Jan Svoboda opravuje Lucii Horákovou
- Lucie Horáková opravuje Evu Malou
- Eva Malá opravuje Petra Dvořáka
- Petr Dvořák opravuje Annu Novákovou
- Anna Nováková opravuje Jana Svobodu
```

## Vývoj

Po úpravách kódu lze příkaz spustit lokálně přímo přes `poetry run`:

```bash
poetry run couple-generator jmena.csv
```

Pro asymetrické přiřazení:

```bash
poetry run couple-generator jmena.csv --asym
```

## Autor

* [Daniel Kopecký](mailto:kopecky.d@gmail.com)
* 
