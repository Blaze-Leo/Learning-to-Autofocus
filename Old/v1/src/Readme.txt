Learning to Autofocus - Readme File

Test Dataset and Train Dataset Location - https://learntoautofocus-google.github.io/

Tested

OS - Windows 23H2 and Ubuntu 24.04
GPU - Nvidia RTX 3050 and AMD Radeon 6600

Folder Structure Needed to run Code

Super_Path
└── Autofocus
    ├── Test
    │   └── Cache
    │   └── ...archive...
    ├── Train
    │   └── ...train<number>...
    ├── Cache
    ├── Exp1
    │   └── Test
    ├── Exp2
    │   └── Test
    └── Exp3
        └── Test


Folder Structure After Running all Code

Super_Path
└── Autofocus
    ├── Test
    │   └── Cache
    │       ├── dataset.dat
    │       ├── labels.dat
    │       ├── length.dat
    │       └── patch.dat
    │   └── ...archive...
    ├── Train
    │   └── ...train<number>...
    ├── Cache
    │   ├── dataset.dat
    │   ├── labels.dat
    │   ├── length.dat
    │   └── patch.dat
    ├── Exp1
    │   ├── Test
    │   │   ├── dataset.dat
    │   │   ├── labels.dat
    │   │   ├── length.dat
    │   │   └── patch.dat
    │   ├── dataset.dat
    │   ├── labels.dat
    │   ├── length.dat
    │   ├── patch.dat
    │   └── Experiment_1_model.keras
    ├── Exp2
    │   ├── Test
    │   │   ├── dataset.dat
    │   │   ├── labels.dat
    │   │   ├── length.dat
    │   │   └── patch.dat
    │   ├── dataset.dat
    │   ├── labels.dat
    │   ├── length.dat
    │   ├── patch.dat
    │   └── Experiment_2_model.keras
    └── Exp3
        ├── Test
        │   ├── dataset.dat
        │   ├── labels.dat
        │   ├── length.dat
        │   └── patch.dat
        ├── dataset.dat
        ├── labels.dat
        ├── length.dat
        ├── patch.dat
        └── Experiment_3_model.keras

Modules needed for Code to Run

- os
- pprint
- numpy
- random
- cv2
- OpenEXR
- Imath
- tqdm
- copy
- time
- shutil
- tensorflow
- tensorflow.keras
- MobileNetV2
- Model
- Input
- Dense
- GlobalAveragePooling2D
- Adam

Command Line - pip install numpy opencv-python OpenEXR tqdm tensorflow

[For AMD users look into ROCm. You need to make a virtual environment and set tensorflow-rocm in there to make it work, or look into plaidML]

File Details

Every file has a variable at the beginning called "autofocus_path". This variable is the only data one has to edit to make this code work. This data is used all over the code assuming the file structure provided. The value of this variable should be "Super_Path/Autofocus/". And remember to give the slash ('\') at the last. No other variable change is necessary.

Train_Dataset.ipynb - This file creates the train dataset with 15 patches per image. The threshold can of course be changed to any other variable. Since making the data takes a lot of RAM the code has been desgnied to directly write the dataset to the disk, so not much RAM is needed. This code should be run first as the other codes depend on it.

Test_Dataset.ipynb - This file creates the test dataset with 15 patches per image. The threshold can of course be changed to any other variable. Since making the data takes a lot of RAM the code has been desgnied to directly write the dataset to the disk, so not much RAM is needed. This code should be run first as the testing of the model depends on it.

Experiment_1.ipynb - This contains the first experiment where 128x18x98 tensors are given to the model for training consisting of 49 left dual pixel data and 49 right dual pixel data per image. There are also functions to reduce the dataset size for users with limited power. All the details regarding the model is inside the file. For anyone to to run this file Train_Dataset.ipynb and Test_Dataset.ipynb are perquisites.

Experiment_2.ipynb - This contains the second experiment where 128x18x49 tensors are given to the model for training consisting of 49 left dual pixel data and 49 right dual pixel data merged together by taking their mean per image. There are also functions to reduce the dataset size for users with limited power. All the details regarding the model is inside the file. For anyone to to run this file Train_Dataset.ipynb and Test_Dataset.ipynb are perquisites.

Experiment_3.ipynb - This contains the first experiment where 128x18x98 tensors are given to the model for training consisting of 49 left dual pixel data and 49 right dual pixel data per image. Since the ground truth labels are going to be different this file also makes its own ground truth labels for both train and test data. There are also functions to reduce the dataset size for users with limited power. All the details regarding the model is inside the file. For anyone to to run this file Train_Dataset.ipynb and Test_Dataset.ipynb are perquisites.

Additional Details

If the code gets stuck at training, no need to regenerate the dataset in the Experiment_<number>.ipynb files. There is a code block with its markdown saying "Initializing the Test and Train Dataset". Run from there and the variables will be restored from the disk. 

Since the dataset is quite big. One can delete the 'raw_left_pd' and 'raw_right_pd' folders as they are of no use. 'scaled_images' can also be deleted but those contain the RGB images so it is advised to keep them for visualization of the output in the future.

It is also advised to keep the generated datasets under Exp<number> folders in some other backup place as mis-clicks in the ipynb file can wipe out the dataset.
