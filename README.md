# MatBench Experiments

Experiments predicting experimental material bandgaps from composition using the `matbench_expt_gap` dataset, Magpie features, random forests, and XGBoost with Bayesian hyperparameter optimisation.

Open [matbench-bandgap-predictor.ipynb](matbench-bandgap-predictor.ipynb) to view the work and saved results. This is a work in progress: the initial notebook preserves my Lecture9 work unchanged. One code cell contains the prose “Predicting experimental bandgap” and must be changed to Markdown before running all cells.

## Run locally

Install [uv](https://docs.astral.sh/uv/), then run from this directory:

```sh
uv sync --locked
uv run jupyter lab
```

Select the Python environment belonging to this project. The notebook downloads its dataset through matminer and requires internet access for the first download. Hyperparameter optimisation can take substantial time.

The Python 3.12 environment definitions and full course dependency set are retained in `pyproject.toml`, `uv.lock`, and `.python-version`. The small `src/mlformaterials` scaffold supports the existing package configuration. Installed virtual environments are recreated locally and are not committed.

## Acknowledgements and provenance

Adapted from Lecture9 of [Machine Learning for Materials](https://github.com/aronwalsh/MLforMaterials), a public course by Prof Aron Walsh at Imperial College London, developed with Anthony Onwuli and Zhenzhu Li. The initial copy comes from my locally modified course checkout, whose upstream HEAD was `3b4f745`.

My model development and experiments build on the course notebook; the original teaching material is credited to its authors. This repository is an independent learning project.

The dataset is `matbench_expt_gap`, distributed through [matminer](https://hackingmaterials.lbl.gov/matminer/) and described by [Matbench](https://matbench.materialsproject.org/). The notebook uses its own train/test split; results should not be treated as official Matbench benchmark scores.

## License notice

[LICENSE](LICENSE) is copied unchanged from the course repository and contains CC0 1.0 Universal. The upstream README displays a CC-BY 4.0 badge instead. This discrepancy is recorded here without resolving it or asserting a different license for the course material. Dataset and third-party library terms remain separate.
