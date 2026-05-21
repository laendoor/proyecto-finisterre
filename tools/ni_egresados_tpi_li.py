"""
Genera un CSV con Nuevos Inscriptos y Egresados de TPI y LI por año.

Schema de salida:
    Año | NI TPI | NI LI | NI TPI+LI | Egresados TPI | Egresados LI | Egresados TPI+LI

Uso:
    python ni_egresados_tpi_li.py
    python ni_egresados_tpi_li.py --desde 2010
    python ni_egresados_tpi_li.py --input ../investigacion/datos/Estudiantes-Datos-abiertos-a-082025.csv
"""

import argparse
from pathlib import Path

import pandas as pd

DEFAULT_INPUT = Path(__file__).parent / "../investigacion/datos/Estudiantes-Datos-abiertos-a-082025.csv"
DEFAULT_OUTPUT = Path(__file__).parent / "../investigacion/datos/ni_egresados_tpi_li.csv"

CAREERS = {
    "Tecnicatura Universitaria en Programación Informática": "TPI",
    "Licenciatura en Informática": "LI",
}

START_YEAR = 2007  # año de inicio de TPI


def parse_european_number(series: pd.Series) -> pd.Series:
    return (
        series.astype(str)
        .str.strip()
        .replace("nan", pd.NA)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .pipe(pd.to_numeric, errors="coerce")
        .round()
        .astype("Int64")
    )


def load(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, sep=";", encoding="utf-8-sig")
    df.columns = df.columns.str.strip()
    df["Nuevos Inscriptos"] = parse_european_number(df["Nuevos Inscriptos"])
    df["Egresados"] = parse_european_number(df["Egresados"])
    df["Año"] = pd.to_numeric(df["Año"], errors="coerce").astype("Int64")
    return df


def build(df: pd.DataFrame, desde: int) -> pd.DataFrame:
    df = df[df["Propuesta Formativa"].isin(CAREERS)].copy()
    df["Carrera"] = df["Propuesta Formativa"].map(CAREERS)
    df = df[df["Año"] >= desde]

    agg = (
        df.groupby(["Año", "Carrera"])[["Nuevos Inscriptos", "Egresados"]]
        .sum()
        .unstack("Carrera")  # columnas: (NI, TPI), (NI, LI), (Eg, TPI), (Eg, LI)
    )

    # Aplanar MultiIndex de columnas
    agg.columns = [f"{met} {car}" for met, car in agg.columns]
    agg = agg.reset_index()

    # Columnas de totales
    agg["NI TPI+LI"] = agg["Nuevos Inscriptos TPI"].add(agg["Nuevos Inscriptos LI"], fill_value=0).astype("Int64")
    agg["Egresados TPI+LI"] = agg["Egresados TPI"].add(agg["Egresados LI"], fill_value=0).astype("Int64")

    # Orden y nombres finales
    agg = agg.rename(columns={
        "Nuevos Inscriptos TPI": "NI TPI",
        "Nuevos Inscriptos LI":  "NI LI",
        "Egresados TPI":         "Egresados TPI",
        "Egresados LI":          "Egresados LI",
    })

    return agg[["Año", "NI TPI", "NI LI", "NI TPI+LI", "Egresados TPI", "Egresados LI", "Egresados TPI+LI"]]


def main():
    parser = argparse.ArgumentParser(description="NI y Egresados TPI/LI por año")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--desde", type=int, default=START_YEAR)
    args = parser.parse_args()

    df = load(args.input)
    result = build(df, args.desde)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(args.output, index=False, encoding="utf-8-sig", sep=";")

    print(f"✓ {len(result)} años ({result['Año'].min()}–{result['Año'].max()})")
    print(f"  Output: {args.output.resolve()}")
    print()
    print(result.to_string(index=False))


if __name__ == "__main__":
    main()
