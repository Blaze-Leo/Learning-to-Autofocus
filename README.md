# Learning-to-Autofocus

Arxiv Paper - 2004.12260v3

Attempt at implementing the code. Very low GPU memory of 4GB is available to me. Can't run the training at 128x128 size patches and thus running at 32x32 size patches.

Since there are very patches corresponding to label 0 and 41-48, I have removed those from the output and thus my model only outputs logits for labels 1-40.

Training dataset size = 396870
Testing dataset size = 55949

Final model has MAE = 1.9641 on Test dataset and ~0.8 on Training and Validation dataset.

Heavily edited [Dataset](https://huggingface.co/datasets/blaze-leo/Learning-to-Autofocus)
