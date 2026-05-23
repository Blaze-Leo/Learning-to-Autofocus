# Learning-to-Autofocus

**Reference Paper:** [Learning to Autofocus](https://learntoautofocus-google.github.io/)

This project is an implementation attempt of the Learning-to-Autofocus framework under limited hardware constraints.

---

## Setup Constraints

* Available GPU memory: **16 GB**
* Due to memory limitations:

  * Training performed on **32×32 patches** instead of 128×128
* Output space adjusted:

  * Labels **0 and 41–48 removed** (insufficient samples)
  * Model predicts focus levels in range **1–40** (40 focii)

---

## Dataset

* Training samples ~ **400,000**
* Testing samples ~ **60,000**

Dataset used (modified version):
[Learning-to-Autofocus Dataset](https://huggingface.co/datasets/blaze-leo/Learning-to-Autofocus)

---

## Results

* **Train / Validation MAE:** ~1
* **Test MAE:** ~2
* The maximum error possible is 40

---

## Notes

* Significant preprocessing and filtering applied to the dataset
* Reduced label space improves training stability but disregards some labels
* Smaller patch size trades spatial context for feasibility on constrained hardware
---
