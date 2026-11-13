
import pytest

from csv_data_analyzer.analyzer import analyze_csv


def test_csv_statistics():
    report = analyze_csv("examples/sample.csv")

    assert report["rows"] == 5
    assert report["columns"] == 4
    assert report["missing_values"]["age"] == 1
    assert report["missing_values"]["score"] == 1
    assert report["numeric_statistics"]["age"]["mean"] == 23.5
    assert report["numeric_statistics"]["score"]["mean"] == 86.25


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        analyze_csv("examples/nonexistent.csv")


def test_invalid_file_extension(tmp_path):
    file_path = tmp_path / "data.txt"
    file_path.write_text("name,score\nAlice,90\n", encoding="utf-8")

    with pytest.raises(ValueError):
        analyze_csv(str(file_path))


def test_all_missing_numeric_values(tmp_path):
    file_path = tmp_path / "missing.csv"
    file_path.write_text(
        "name,score\nAlice,10\nBob,\n",
        encoding="utf-8",
    )

    report = analyze_csv(str(file_path))

    assert report["missing_values"]["score"] == 1
    assert report["numeric_statistics"]["score"]["mean"] == 10.0
