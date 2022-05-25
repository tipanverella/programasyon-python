"""
Module sa baw zouti pouw lire dokiman tip text,
csv, tabulaire, etc...
"""

import csv
import pandas as pd


def li_text(file_path: str):
    """
    Fonksyon sa kapab lire yon dokiman tip text.
    """
    with open(file_path, "r", encoding="cp1252", sep=" ") as file:
        lire = file.read()
    return lire


def li_csv(file_path: str, sep: str = ","):
    """
    Fonction sa a lire dokiman csv.
    """
    with open(file_path, "r", encoding="utf-8") as csv_file:
        ask = input(
            "Ekri (tablo) siw vle lil en tablo, (csv) siw vle lil en mode original la. "
        )
        if ask == "tablo":
            lire = pd.read_table(csv_file, sep)
        else:
            lire = csv.DictReader(csv_file, sep)
            for row in lire:
                print(row)
    return lire


def li_tab(file_path: str, sep: str = "|"):
    """
    Fonction sa lire menm lire tableau.
    """
    with open(file_path, "r", encoding="utf-8") as tab:
        lire = pd.read_table(tab, sep)
        for row in lire:
            print(row)
        return lire


def error():
    """
    Fonction error
    """
    while True:
        try:
            int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops! That was no valid number. Try again...")
        finally:
            print("Goodbye!!!")


