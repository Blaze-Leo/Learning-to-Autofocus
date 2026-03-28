
---

# Learning-to-Autofocus

**Reference Paper:** [Learning to Autofocus](https://learntoautofocus-google.github.io/)

This project is an implementation attempt of the Learning-to-Autofocus framework under limited hardware constraints.

---

## Setup Constraints

* Available GPU memory: **4 GB**
* Due to memory limitations:

  * Training performed on **32×32 patches** instead of 128×128
* Output space adjusted:

  * Labels **0 and 41–48 removed** (insufficient samples)
  * Model predicts focus levels in range **1–40**

---

## Dataset

* Training samples: **396,870**
* Testing samples: **55,949**

Dataset used (modified version):
[Learning-to-Autofocus Dataset](https://huggingface.co/datasets/blaze-leo/Learning-to-Autofocus)

---

## Results

* **Test MAE:** 1.9641
* **Train / Validation MAE:** ~0.8

---

## Reproducibility

* Framework: PyTorch
* GPU: 4GB VRAM
* Input size: 32×32 patches
* Output classes: 40 focus levels

---

## Notes

* Significant preprocessing and filtering applied to the dataset
* Reduced label space improves training stability but disregards some labels
* Smaller patch size trades spatial context for feasibility on constrained hardware

---
