# MatBench Experiments

This repository explores building machine learning predictors for different materials properties using [Matbench datasets](https://matbench.materialsproject.org/). The aim is to investigate how choices of material representation, model, and hyperparameters affect predictive performance, and to compare the results with leading methodologies reported on the [Matbench leaderboard](https://matbench.materialsproject.org/).

## Starting point: experimental bandgap prediction

The project began with the `matbench_expt_gap` dataset, predicting experimental bandgaps from chemical composition. The initial experiments use Magpie composition features, random forests, and XGBoost, including Bayesian hyperparameter optimisation.

[matbench-bandgap-predictor.ipynb](matbench-bandgap-predictor.ipynb) records this initial work and its results. Future experiments will explore additional materials properties and prediction approaches.

The current notebook uses its own train/test split. Comparisons with published methods provide context; direct benchmark comparisons require matching the official Matbench evaluation protocol.

## Inspiration and acknowledgements

This work was inspired by completing Prof Aron Walsh’s **Machine Learning for Materials** lecture course at Imperial College London. It began with my work in Lecture9 of the [course repository](https://github.com/aronwalsh/MLforMaterials), then developed into this independent project.

The course was developed by Aron Walsh with assistance from Anthony Onwuli and Zhenzhu Li. The original teaching material is credited to its authors.

## Matbench reference

Matbench provides datasets and an evaluation framework for materials property prediction. Dataset information and published results are available on the [Matbench website](https://matbench.materialsproject.org/), with code in the [Matbench repository](https://github.com/materialsproject/matbench).

Dunn, A., Wang, Q., Ganose, A., Dopp, D. & Jain, A. **Benchmarking materials property prediction methods: the Matbench test set and Automatminer reference algorithm.** *npj Computational Materials* **6**, 138 (2020). [doi:10.1038/s41524-020-00406-3](https://doi.org/10.1038/s41524-020-00406-3).

## Run locally

Install [uv](https://docs.astral.sh/uv/), then run from this directory:

```sh
uv sync --locked
uv run jupyter lab
```

Select the Python environment belonging to this project. The notebook downloads its dataset through matminer and requires internet access for the first download. Hyperparameter optimisation can take substantial time.

The Python 3.12 environment definitions and full course dependency set are retained in `pyproject.toml`, `uv.lock`, and `.python-version`. The small `src/mlformaterials` scaffold supports the existing package configuration. Installed virtual environments are recreated locally and are not committed.

## License notice

[LICENSE](LICENSE) is copied unchanged from the course repository and contains CC0 1.0 Universal. The upstream README displays a CC-BY 4.0 badge instead. This discrepancy is recorded here without resolving it or asserting a different license for the course material. Dataset and third-party library terms remain separate.
