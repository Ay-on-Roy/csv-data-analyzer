# CSV Data Analyzer

CSV Data Analyzer is a Python command-line application that reads CSV files and produces statistical reports. It calculates dataset size, identifies missing values, summarizes numeric columns, and exports results as JSON.

The project uses **Poetry 2.5.1** for dependency management, version management, and packaging.

## Requirements

- Python 3.14

- Poetry 2.5.1

## Installation

Clone the repository and open the project directory:

```bash

git clone git@github.com:Ay-on-Roy/csv-data-analyzer.git

cd csv-data-analyzer

```

Install all project and development dependencies:

```bash

poetry install

```

Poetry uses `pyproject.toml` and `poetry.lock` to resolve and install dependencies.

## Run the application

Analyze the sample CSV file:

```bash

poetry run csv-analyzer examples/sample.csv

```

Generate a JSON report:

```bash

poetry run csv-analyzer examples/sample.csv --output reports/sample-report.json

```

Display command-line help:

```bash

poetry run csv-analyzer --help

```

## Run automated tests

The project uses pytest to test CSV statistics, missing-file handling, invalid file extensions, and missing numerical values.

```bash

poetry run pytest -v

```

The current test suite contains four tests.

## Build the project

Validate the project configuration:

```bash

poetry check

poetry check --lock

```

Compile the Python source files into bytecode:

```bash

poetry run python -m compileall -q src

```

Generate distribution packages:

```bash

poetry build

```

The resulting files are created in `dist/`:

```text

csv_data_analyzer-0.1.1-py3-none-any.whl

csv_data_analyzer-0.1.1.tar.gz

```

The Wheel is an installable Python package. The `.tar.gz` file contains the source distribution. Python bytecode compilation is separate from Poetry's package-building process.

## Dependency management

Runtime dependencies:

- `pandas`: Reads CSV data and calculates statistics.

- `typer`: Provides the command-line interface.

Development dependency:

- `pytest`: Runs automated tests.

Add a new runtime dependency:

```bash

poetry add package-name

```

Add a development dependency:

```bash

poetry add --group dev package-name

```

Display the dependency tree:

```bash

poetry show --tree

```

The dependency declarations are stored in `pyproject.toml`, while the exact resolved dependency versions are recorded in `poetry.lock`.

## Project version management

The project initially used version `0.1.0`.

Poetry was used to increase it to `0.1.1`:

```bash

poetry version patch

```

Check the current version:

```bash

poetry version

```

## Reproducible builds

To reproduce the development environment and build:

```bash

poetry check --lock

poetry install

poetry run pytest -v

poetry build

```

The committed `poetry.lock` file records the resolved versions of all dependencies.

## Build configuration

The `pyproject.toml` file defines the package name, version, description, Python requirements, dependencies, CLI entry point, and build backend.

The `\[project.scripts]` section registers the `csv-analyzer` command.

The `\[build-system]` section identifies the Poetry build backend used to create Python distributions.

## Project structure

```text

csv-data-analyzer/

├── pyproject.toml

├── poetry.lock

├── README.md

├── src/

│   └── csv_data_analyzer/

│       ├── __init__.py

│       ├── analyzer.py

│       └── cli.py

├── examples/

│   └── sample.csv

└── tests/

    └── test_analyzer.py

```

## Author

Ayon Roy

Master's student, Cyber-Physical and Social Systems, Université Jean Monnet, France.

