#!/bin/bash

rtve2018_path=$1
## Unzipping data ##
unzip ./src/transcriptions.zip -d ./data/transcriptions/
unzip ./src/landmarks.zip -d ./data/landmarks/

## Obtaining LIP-RTVE samples from source data alignmets ##
python3 src/scripts/get_samples.py --alignments ./src/alignments.csv --source-dir $rtve2018_path --output-dir ./data/LIP-RTVE/

## Extracting LIP-RTVE's Regions of Interest ##
python3 src/scripts/get_ROIs.py --samples-dir ./data/LIP-RTVE/ --landmarks-dir ./data/landmarks/ --roi-types fitMouths wideMouths faces SOTA --output-dir ./data/ROIs/

echo "\nLIP-RTVE completed!"
