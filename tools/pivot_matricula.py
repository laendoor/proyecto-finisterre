"""
Genera un CSV pivotado con datos históricos de matrícula por carrera.

Fuente: Portal de Transparencia UNQ
Formato fuente: filas = (carrera, año), valores con separador europeo (1.234,00)

Uso:
    python pivot_matricula.py
    python pivot_matricula.py --input ../investigacion/datos/Estudiantes-Datos-abiertos-a-082025.csv
    python pivot_matricula.py --metric NI        # solo nuevos inscriptos
    python pivot_matricula.py --metric egresados
"""

import argparse
from pathlib import Path

import pandas as pd

DEFAULT_INPUT = Path(__file__).parent / "../investigacion/datos/Estudiantes-Datos-abiertos-a-082025.csv"
DEFAULT_OUTPUT = Path(__file__).parent / "../investigacion/datos/matricula_pivot.csv"

METRIC_COLS = {
    "ni_ri":      "Alumnos (NI+RI)",
    "ni":         "Nuevos Inscriptos",
    "egresados":  "Egresados",
}


def parse_european_number(series: pd.Series) -> pd.Series:
    """Convierte '1.234,00' → 1234 (entero). Vacíos → NaN."""
    return (
        series.astype(str)
        .str.strip()
        .replace("nan", pd.NA)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .pipe(pd.to_numeric, errors="coerce")
        .round()
        .astype("Int64")  # nullable integer (acepta NaN)
    )


def load(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, sep=";", encoding="utf-8-sig")
    df.columns = df.columns.str.strip()

    # "Departamento de Ciencia y Tecnología (presencial)" → Departamento + Modalidad
    extracted = df["Responsable Académica"].str.extract(r"^(.+?)\s+\((presencial|virtual)\)$")
    df["Departamento"] = extracted[0]
    df["Modalidad"] = extracted[1]

    df = df.rename(columns={
        "Tipo Propuesta Formativa": "Nivel",
        "Propuesta Formativa": "Carrera",
    })

    for col in METRIC_COLS.values():
        df[col] = parse_european_number(df[col])

    df["Año"] = pd.to_numeric(df["Año"], errors="coerce").astype("Int64")
    return df


def pivot(df: pd.DataFrame, metric: str) -> pd.DataFrame:
    col = METRIC_COLS[metric]

    pivoted = df.pivot_table(
        index=["Departamento", "Modalidad", "Nivel", "Carrera"],
        columns="Año",
        values=col,
        aggfunc="sum",
    )

    # Flatten column names (años como int, no MultiIndex)
    pivoted.columns = [int(c) for c in pivoted.columns]
    pivoted = pivoted.sort_index()
    pivoted = pivoted.reset_index()
    pivoted.columns.name = None

    return pivoted


def main():
    parser = argparse.ArgumentParser(description="Pivotea matrícula UNQ por carrera × año")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--metric",
        choices=list(METRIC_COLS.keys()),
        default="ni_ri",
        help="Qué columna pivotar (default: ni_ri = NI+RI)",
    )
    args = parser.parse_args()

    df = load(args.input)
    result = pivot(df, args.metric)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(args.output, index=False, encoding="utf-8-sig")

    year_cols = [c for c in result.columns if isinstance(c, int)]
    print(f"✓ {len(result)} carreras × {len(year_cols)} años ({min(year_cols)}–{max(year_cols)})")
    print(f"  Métrica: {args.metric} ({METRIC_COLS[args.metric]})")
    print(f"  Output:  {args.output.resolve()}")


if __name__ == "__main__":
    main()
