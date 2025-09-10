import csv
import random
import click

def nacti_jmena(soubor):
    jmena = []
    with open(soubor, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row:
                continue
            # Pokud je jen jeden sloupec
            if len(row) == 1:
                jmena.append(row[0].strip())
            # Pokud jsou dva sloupce, spojíme
            elif len(row) >= 2:
                jmena.append(f"{row[0].strip()} {row[1].strip()}")
    return jmena

def vytvor_dvojice(seznam):
    random.shuffle(seznam)
    dvojice = [(seznam[i], seznam[i+1]) for i in range(0, len(seznam) - 1, 2)]
    posledni = seznam[-1] if len(seznam) % 2 == 1 else None
    return dvojice, posledni

@click.command()
@click.argument("csv_soubor", type=click.Path(exists=True))
def main(csv_soubor):
    """Vytvoří náhodné dvojice ze seznamu jmen v CSV souboru."""
    jmena = nacti_jmena(csv_soubor)
    if not jmena:
        click.echo("Soubor je prázdný nebo neobsahuje platná jména.")
        return

    dvojice, posledni = vytvor_dvojice(jmena)

    click.echo("Dvojice:")
    for d in dvojice:
        click.echo(f"- {d[0]} & {d[1]}")

    if posledni:
        click.echo(f"Zůstal sám: {posledni}")

if __name__ == "__main__":
    main()
