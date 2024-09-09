# Deploy Python Backend to your local machine

## Requirement:
 - Sufficient RAM/VRAM: at least 16GB in total 
   - x86 Processor, or you having a well-performing architectural translation layer (Apple Rosetta 2)
 - Python2.7 and Python3.12 installed
 - Required packages installed

## Steps to deploy
1. install Python
   - Python 3.12
   - Python 2.7
   - **Python Dependencies**:
     - use **pip2** to install requirements.txt under /src/py2/requirements.txt
     - use **pip3** to install requirements.txt under /src/py3/requirements.txt
        
     **Please note not all packages are listed in requirements.txt, you may need to install some packages manually**
2. install Git
   - (Optional) Git LFS
3. Git clone
   - The backend file(Compulsory)
   - LLM Model(Git clone or OneDrive download)
4. Download LLM Models
   - Download link: TODO: Upload compressed file to OneDrive
   - **Or**, you can obtain gemma 2 with 2b params in **[Hugging Face](https://huggingface.co/google/gemma-2-2b-it_)** and clone the repo using **Git LFS**
5. (Optional) turn firewall off
6. run API (you can use **[postman](https://www.postman.com)** to debug)

