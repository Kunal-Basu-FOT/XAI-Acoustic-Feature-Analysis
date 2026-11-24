# Acoustic features and explainable speaker classification

An exploratory study of speaker classification from short voice recordings
using acoustic features and local explanations. The analysis compares k-nearest
neighbors, random forest, multilayer perceptron, support vector machine, and
XGBoost classifiers. The work was accepted for presentation at the 2025
*Innovations in Science and Technology: A Perspective of Viksit Bharat@2047*
conference.

## Data and evaluation

The dataset contains student voice recordings collected at the Faculty of
Technology, University of Delhi, including some identical-twin speakers. The
recordings are not distributed here. The notebook selects 101 class folders,
then splits up to 10 recordings per folder into seven training and three test
recordings with random seed 42. Its saved outputs report 707 training and 303
test recordings. Speakers therefore occur in **both** partitions: this is
within-speaker recording recognition, not generalization to unseen speakers.

Audio is resampled to 44.1 kHz, filtered, and summarized with 40 mean MFCCs
and one pitch feature. Min-max scaling is fitted on training recordings and
applied to test recordings. Hyperparameters are selected with stratified
seven-fold cross-validation on the training set; the table below uses the
separate test recordings. The notebook also shows example LIME explanations.

## Saved results

| Model | Training CV accuracy | Test accuracy (303 recordings) |
|---|---:|---:|
| k-nearest neighbors | 0.9590 | 0.9505 |
| Random forest | 0.9703 | 0.9571 |
| Multilayer perceptron | 0.9646 | 0.9868 |
| Support vector machine (linear kernel) | 0.9745 | 0.9835 |
| XGBoost | 0.8557 | 0.8746 |

The numbers come from saved notebook outputs and can be re-extracted with
`python scripts/extract_results.py`. They have not been recomputed from the
private audio for this repository update. The notebook does not report a
separate twin-only test metric. Its LIME examples describe individual
predictions; they do not establish population-level feature rankings.

## Repository contents

- `ICIST-70_30(MM).ipynb`: original analysis record,
  including saved plots and model outputs.
- [`results/metrics.csv`](results/metrics.csv): compact model comparison.
- [`scripts/extract_results.py`](scripts/extract_results.py): extracts the
  accuracy values from the notebook outputs.
- [`DATA.md`](DATA.md): input layout and data-access limitations.

The notebook retains its original Windows paths as a record of the analysis.
To rerun it, obtain authorized access to the recordings, install the packages
in `requirements.txt`, and replace the `E:\PythonJupyter\70_30 Split` root with
your local working directory. Python 3.12 is recommended for the notebook's
f-string syntax. The original preprocessing fits the imputer before the inner
cross-validation, so the CV column should be treated as a model-selection
diagnostic rather than an unbiased performance estimate. A new study should
also use speaker-disjoint evaluation if unseen-speaker performance is the goal.

The voice recordings and extracted per-recording features are not included
because they concern human participants. Only aggregate model results and the
analysis code are shared.
