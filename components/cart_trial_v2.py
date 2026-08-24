import pandas as pd


def show(df: pd.DataFrame, max_rows: int = 20, float_fmt: str = "{:,.2f}") -> None:

    n = len(df)
    view = df.head(max_rows)

    with pd.option_context(
        "display.max_rows", max_rows,
        "display.max_columns", None,
        "display.width", 120,
        "display.float_format", float_fmt.format,
    ):
        print(view.to_string())

    if n > max_rows:
        print(f"\n... {n - max_rows} more rows")
    print(f"[{n} rows x {len(df.columns)} columns]")


def _coerce(value: str):
    """Turn a typed string into int/float/None when possible, else leave as str."""
    value = value.strip()
    if value == "" or value.lower() in ("na", "nan", "none"):
        return None
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value


def build_dataframe() -> pd.DataFrame:
    print("Let's collect some people.\n")
    print("Enter a name to add a person. Leave the name blank to finish.\n")

    columns = ["name", "favourite food", "age"]
    rows = []

    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        food = input("Favourite food: ").strip()
        age = input("Age: ").strip()
        rows.append({
            "name": name,
            "favourite food": food if food else None,
            "age": _coerce(age),
        })
        print()

    return pd.DataFrame(rows, columns=columns)


if __name__ == "__main__":
    df = build_dataframe()
    print()
    show(df)