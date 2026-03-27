import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import numpy as np
import torch
from tabulate import tabulate


def print_gpu_details(print_details):
    """Prints all available GPUs in a formatted table with key details"""
    
    gpu_details = []
    
    if torch.cuda.is_available():
        num_gpus = torch.cuda.device_count()
        
        for gid in range(num_gpus):
            props = torch.cuda.get_device_properties(gid)
            
            details = {
                'Device ID': str(gid),
                'Name': props.name,
                'Memory (GB)': f"{props.total_memory / (1024**3):.2f}",
                'PCI Bus ID': "Unknown",
                'GFX Version': os.environ.get('HSA_OVERRIDE_GFX_VERSION', 'Native')
            }
            gpu_details.append(details)
    
    # Print table if GPUs found
    if gpu_details:
        if print_details:
            print("\n" + "="*85)
            print("ACTIVE GPU CONFIGURATION".center(85))
            print("="*85)
            print(tabulate(gpu_details, headers="keys", tablefmt="grid"))
            print("="*85 + "\n")
    else:
        print("No GPU devices found!")


def configure_gpu():
    """Configure GPU settings (VRAM control removed)"""
    
    if not torch.cuda.is_available():
        raise RuntimeError("No GPU found")
    
    num_gpus = torch.cuda.device_count()
    
    for gid in range(num_gpus):
        props = torch.cuda.get_device_properties(gid)
        print(f"Configured GPU {gid}: {props}")
        
        device = torch.device(f'cuda:{gid}')
        
        # Force GPU usage
        x = torch.ones((1, 1), device=device)
        y = x + 1
        _ = y.cpu()  # Force execution


def activate_gpu(print_details=True):
    
    print_gpu_details(print_details)
    configure_gpu()