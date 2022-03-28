"""
Authors: David Gimeno-Gomez & Carlos-D. Martinez Hinarejos

"""

import os
import argparse
import subprocess
import pandas as pd
from tqdm import tqdm
from utils import get_source_rtve2018_path

def extract_samples(alignments_path, source_dir, output_dir):
    """extract_rois.
        :param landmarks_dir: str, CSV file where alignments are stored
        :param source_dir: str, directory where MP4 source data is placed
        :param output_dir: str, directory where LIP-RTVE samples will be stored
    """
    alignments = list(pd.read_csv(alignments_path).itertuples(index=False, name=None))
    for i, sampleID, sourceID, startTime, duration in tqdm(alignments, desc="%Samples", bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'):
        spkrID = sampleID.split("_")[0]

        output_mp4_spkr_dir = os.path.join(output_dir, "mp4", spkrID)
        os.makedirs(output_mp4_spkr_dir, exist_ok=True)
        output_mp4_path = os.path.join(output_mp4_spkr_dir, sampleID + ".mp4")

        source_path = get_source_rtve2018_path(source_dir, sourceID)

        output_wav_spkr_dir = os.path.join(output_dir, "wav", spkrID)
        os.makedirs(output_wav_spkr_dir, exist_ok=True)
        output_wav_path = os.path.join(output_wav_spkr_dir, sampleID + ".wav")

        ## EXTRACTING THE LIP-RTVE SAMPLE FROM ITS CORRESPONDING SOURCE-DATA  ##
        subprocess.call([
            "ffmpeg",
            "-y",
            "-ss", startTime,
            "-t", str(duration),
            "-i", source_path,
            output_mp4_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        ## OBTAINING THE WAV FROM THE PREVIOUS LIP-RTVE MP4 SAMPLE ##
        subprocess.call([
            "ffmpeg",
             "-y",
            "-i", output_mp4_path,
            "-ar", "16000",
            "-ac", "1",
            "-acodec", "pcm_s16le",
            output_wav_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    ## DEFINING SCRIPT PARAMETERS ##
    parser = argparse.ArgumentParser(description='Region of Interest Extraction from the 68 facial landmarks previously computed',
                                     epilog="Usage: python get_samples.py --alignments ../alignments.csv --source-dir ../data/RTVE2018-20H --output-dir ../data/LIP-RTVE/")

    parser.add_argument("--alignments", default="../alignments.csv", type=str, help="CSV file where alignments are stored.")
    parser.add_argument("--source-dir", default="../data/RTVE2018-20H/", type=str, help="Directory where MP4 source data is placed.")
    parser.add_argument("--output-dir", default="../data/LIP-RTVE/", type=str, help="Directory where MP4 samples will be stored.")

    args = parser.parse_args()

    ## EXTRACTING LIP-RTVE SAMPLES ##
    extract_samples(args.alignments, args.source_dir, args.output_dir)
