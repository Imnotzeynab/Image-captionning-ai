BLIP Image Captioning

A simple AI image captioning project using Salesforce's pretrained BLIP vision-language model. The application takes an image, analyzes its visual content, and automatically generates a natural-language caption.

Demo

The program takes an image such as:
cat.jpg

and generates a caption such as: a cat sitting on a couch


The image and generated caption are also displayed together using Matplotlib.


Tech Stack

* Python 3.12
* PyTorch
* Hugging Face Transformers
* Salesforce BLIP
* Pillow
* Matplotlib
Getting Started
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
2. Install dependencies
pip install transformers torch pillow matplotlib
3. Add an image

Place an image named: cat.jpg

in the project directory.

4. Run the project

On Windows:

py -3.12 main.py

The model will load, generate a caption, display the image, and print the caption in the terminal.


GPU / GPU Support

The program automatically detects whether CUDA is available:
device = "cuda" if torch.cuda.is_available() else "cpu"

If a compatible GPU is available, the model runs on CUDA. Otherwise, it runs on the CPU.

 Future Improvements

* [ ] Allow users to select any image
* [ ] Add a graphical user interface
* [ ] Support multiple images
* [ ] Save generated captions
* [ ] Build a web interface
* [ ] Compare different image-captioning models
* [ ] Add visual question answering


 Model

This project uses **BLIP (Bootstrapping Language-Image Pre-training)** developed by Salesforce Research.

Model: `Salesforce/blip-image-captioning-base`


Computer Science | Machine Learning | Artificial Intelligence
