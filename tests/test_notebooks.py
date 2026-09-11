import json
from pathlib import Path


ROOT = Path(__file__).parents[1]
NOTEBOOKS = ROOT / "notebooks"


def load_notebook(name: str) -> dict:
    with (NOTEBOOKS / name).open(encoding="utf-8") as file:
        return json.load(file)


def test_notebooks_are_valid_v4_documents() -> None:
    for path in NOTEBOOKS.glob("*.ipynb"):
        notebook = load_notebook(path.name)
        assert notebook["nbformat"] == 4
        assert notebook["cells"]
        assert all("cell_type" in cell and "source" in cell for cell in notebook["cells"])


def test_two_sum_notebook_executes_without_errors() -> None:
    namespace: dict = {}
    notebook = load_notebook("two_sum.ipynb")

    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            source = "".join(cell["source"])
            exec(compile(source, "two_sum.ipynb", "exec"), namespace)
