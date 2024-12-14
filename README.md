# [CVPR 2024] MeaCap: Memory-Augmented Zero-shot Image Captioning

**Authors**:
Ronit Bhansali
<br/>
Replicating the implementation of MeaCap.

# MeaCapReplication: Memory-Augmented Zero-shot Image Captioning

This repository contains a replication of the MeaCap model, designed for zero-shot image captioning by leveraging a memory-augmented approach. This project enables generating captions for images without the need for task-specific training data.

---

## Repository Structure

- **assets/**: Contains auxiliary files and resources used by the project.
- **data/**: Directory for storing datasets and related data files.
- **dataset/**: Includes scripts and tools for dataset preparation and management.
- **image_example/**: Provides example images for testing and demonstration purposes.
- **language_models/**: Houses pre-trained language models utilized in the project.
- **models/**: Directory for storing trained model checkpoints and configurations.
- **src/**: Contains the source code for the project, including implementation of the MeaCap model.
- **utils/**: Utility scripts and functions to support various tasks within the project.
- **viecap/**: Specific components or modules related to the VieCap extension of the project.
- **MeaCapReplication.ipynb**: Jupyter notebook demonstrating the model setup, execution, and results. This is the recommended starting point for replication.
- **Meacap.pdf**: PDF document detailing the MeaCap model architecture and methodology.
- **args.py**: Handles command-line arguments for various scripts.
- **compute_clip_score.py**: Computes CLIP scores for evaluating the alignment of images and captions.
- **environment_setup.sh**: Shell script for setting up the environment and dependencies.
- **inference.py**: Script to perform inference with the trained MeaCap model.
- **microsoftevaluation.py**: Implements evaluation metrics/tools, potentially using Microsoft's evaluation framework.
- **prepare_embedding.py**: Prepares embeddings necessary for the model’s memory-augmented operations.
- **requirements.txt**: Lists all Python dependencies required for the project.
- **viecap_inference.py**: Performs inference using the VieCap-specific module.

---

## Installation

To install and set up the MeaCapReplication project, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/Ronit26x/MeaCapReplication.git
cd MeaCapReplication
```
### 2. Set up the virtual environment (optional)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```



