import os
import sys

script_path = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(script_path)

import torch

from torchvision import transforms
from fast_scnn import get_fast_scnn
from fast_scnn import resize_image_matrix
from visualize import get_color_pallete
from PIL import Image




def demo(
    input_pic="/mnt/Personal/Projects/Autofocus/Code/Object_Extraction/fscnn/input_pic/frank.png",
    model_loc="/mnt/Personal/Projects/Autofocus/Code/Object_Extraction/fscnn/fast_scnn_citys.pth",
    outdir="/mnt/Personal/Projects/Autofocus/Code/Object_Extraction/fscnn/output_pic",
    dataset="citys",
    use_cpu=False
):
    """
    Run Fast-SCNN inference on a single image.

    Parameters
    ----------
    input_pic : str
        Path to the input image.
    model_loc : str
        Path to pretrained Fast-SCNN model.
    outdir : str
        Directory to save result.
    dataset : str
        Dataset name used for color palette.
    use_cpu : bool
        Force CPU even if CUDA is available.
    """

    # -------------------------
    # Device selection
    # -------------------------
    if use_cpu:
        device = torch.device("cpu")
    else:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # -------------------------
    # Output directory
    # -------------------------
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    # -------------------------
    # Image preprocessing
    # -------------------------
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(
            [0.485, 0.456, 0.406],
            [0.229, 0.224, 0.225]
        ),
    ])

    image = Image.open(input_pic).convert("RGB")
    print(image.size)
    image,org_dim = resize_image_matrix(image,2**8,2**8)
    image_tensor = transform(image).unsqueeze(0).to(device) # type: ignore

    # -------------------------
    # Load pretrained model
    # -------------------------
    model = get_fast_scnn(model_loc, map_cpu=use_cpu).to(device)
    print("Finished loading model!")
    model.eval()

    # -------------------------
    # Inference
    # -------------------------
    with torch.no_grad():
        outputs = model(image_tensor)

    pred = torch.argmax(outputs[0], 1).squeeze(0).cpu().numpy()

    # -------------------------
    # Color mask and save
    # -------------------------
    mask = get_color_pallete(pred, dataset)

    outname = os.path.splitext(
        os.path.split(input_pic)[-1]
    )[0] + ".png"

    save_path = os.path.join(outdir, outname)
    
    mask.save(save_path)

    
    # mask_normal,_ = resize_image_matrix(mask,org_dim[0],org_dim[1])
    # mask_normal.save(save_path)
    
    # print(type(mask))

    print(f"Saved result to: {save_path}")


demo(input_pic="/mnt/Personal/Projects/Autofocus/test_folder/cactus.jpg")
