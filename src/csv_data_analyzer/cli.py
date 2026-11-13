
import json
from pathlib import Path

import typer

from csv_data_analyzer.analyzer import analyze_csv

app = typer.Typer(
    help="Analyze CSV datasets and generate statistical reports."
)


@app.command()
def analyze(
    file: Path = typer.Argument(
        ...,
        help="Path to the CSV file to analyze.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Save the report to a JSON file.",
    ),
):
    """Analyze a CSV file and display its statistics."""
    try:
        report = analyze_csv(str(file))
    except (FileNotFoundError, ValueError) as error:
        typer.echo(f"Error: {error}", err=True)
        raise typer.Exit(code=1) from error

    result = json.dumps(report, indent=2)

    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(result + "\n", encoding="utf-8")
        typer.echo(f"Report saved to {output}")
    else:
        typer.echo(result)


def main():
    app()


if __name__ == "__main__":
    main()
