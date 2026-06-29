# Safarip
Rip media files from Safari cache effortlessly.  
Targetting macOS 26.5.

## Usages
Creative work with Grok? You don't want to save every file manually? With Safarip you can just scroll through!

## Overview
Safarip monitors cache directory of Safarip and saves newly added files.  

## Installation
Create a virtual environment and install dependencies.

```
python -m venv .venv
source ./.venv/bin/activate
python pip install -r requirements.txt
python main.py
```

## Usage
You can run it through venv or with `run.zsh`.  
Syntax: `python main.py [directory]`. 
If specified, added files will be copied to `directory`. Output directory must exist before running the script.  
`extender` will associate every file with appropriate extension for easier processing (media only). 
If `directory` is not specified, only file detection messaege will appear.

1. Run script
2. Prepare environment / website
3. Press Enter to start

It's very important to close unused tabs, since they *may* cache their files in the background.

## Caveats

#### Permissions
You may need to grant Terminal (or your running environment) full filesystem access permission. Otherwise watching/copying will fail.  

#### Grok Imagine
Depending on Grok Imagine UI (they change once in a while), you might need to scroll through every generated picture for it to be saved.  
Video files will be saved only when downloaded (which is redundant, in a sense).

## TODO
* Handle extension renaming internally
* Human-readable filenames
