#!/bin/bash

RTVE2018_path=$1

mkdir ./data/
mkdir ./data/transcriptions/
mkdir ./data/landmarks/

echo -e "#############################"
echo -e "Downloading landmarks.zip ..."
echo -e "#############################"
gdown -O ./src/ https://drive.google.com/uc?id=13oIvMv-xHp9t24RCCNOeIA6YvsAoZw9K

echo -e "##############"
echo -e "Unzipping data"
echo -e "##############"

unzip ./src/transcriptions.zip -d ./data/transcriptions/
unzip ./src/landmarks.zip -d ./data/landmarks/

echo -e "######################################################"
echo -e "Obtaining LIP-RTVE samples from source data alignments"
echo -e "######################################################"
python3 src/scripts/get_samples.py --alignments ./src/alignments.csv --source-dir $RTVE2018_path --output-dir ./data/LIP-RTVE/

echo -e "#########################################"
echo -e "Extracting LIP-RTVE's Regions of Interest"
echo -e "#########################################"
python3 src/scripts/get_ROIs.py --samples-dir ./data/LIP-RTVE/mp4/ --landmarks-dir ./data/landmarks/ --roi-types fitMouths wideMouths faces SOTA --output-dir ./data/ROIs/

echo -e "###################"
echo -e "LIP-RTVE completed!"
echo -e "###################"
