#!/bin/bash

RTVE2018_path=$1

echo "Downloading landmarks.zip ..."
gdown https://drive.google.com/uc?id=13oIvMv-xHp9t24RCCNOeIA6YvsAoZw9K

echo "Unzipping data"
unzip ./src/transcriptions.zip -d ./data/transcriptions/
unzip ./src/landmarks.zip -d ./data/landmarks/

echo "Obtaining LIP-RTVE samples from source data alignments"
python3 src/scripts/get_samples.py --alignments ./src/alignments.csv --source-dir $RTVE2018_path --output-dir ./data/LIP-RTVE/

echo "Extracting LIP-RTVE's Regions of Interest"
python3 src/scripts/get_ROIs.py --samples-dir ./data/LIP-RTVE/mp4/ --landmarks-dir ./data/landmarks/ --roi-types fitMouths wideMouths faces SOTA --output-dir ./data/ROIs/

echo "\nLIP-RTVE completed!"
