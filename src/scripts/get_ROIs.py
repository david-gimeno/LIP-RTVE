"""
Authors: David Gimeno-Gomez & Carlos-D. Martinez Hinarejos

Algorithm in charge of extracting the SOTA Regions of Interest was mainly based on the work carried out in:

https://github.com/mpc001/Visual_Speech_Recognition_for_Multiple_Languages/tree/master/dataloader

"""
import os
import argparse
import numpy as np
from tqdm import tqdm
from utils import *

def crop_patch(roi_type, video_pathname, landmarks, window_margin=12):
    """crop_patch.
        :param video_pathname: str, the filename for the processed video.
        :param landmarks: List, the interpolated landmarks.
    """

    frame_idx = 0
    frame_gen = load_video(video_pathname)
    sequence = []
    while True:
        try:
            frame = frame_gen.__next__() ## -- BGR
        except StopIteration:
            break

        window_margin = min(window_margin // 2, frame_idx, len(landmarks) - 1 - frame_idx)
        smoothed_landmarks = np.mean([landmarks[x] for x in range(frame_idx - window_margin, frame_idx + window_margin + 1)], axis=0)
        smoothed_landmarks += landmarks[frame_idx].mean(axis=0) - smoothed_landmarks.mean(axis=0)

        if roi_type == "SOTA":
            transformed_frame, transformed_landmarks = affine_transform(
                frame,
                smoothed_landmarks,
                np.load(os.path.join( os.path.dirname(__file__), "./src/scripts/resources/20words_mean_face.npy")),
                grayscale=False,
                )

            start_idx = 48; stop_idx = 68
            crop_height = 96; crop_width = 96

            sequence.append( cut_patch( transformed_frame,
                                    transformed_landmarks[start_idx:stop_idx],
                                    crop_height//2,
                                    crop_width//2,))

        else:
            align_landmarks = np.concatenate((smoothed_landmarks[48:], smoothed_landmarks[4:13], smoothed_landmarks[31:36]))
            aligned_frame = rotate_frame(align_landmarks, frame)

            if roi_type == "fitMouths":
                margin = 3
                roi_landmarks = smoothed_landmarks[48:]
            elif roi_type == "wideMouths":
                margin = 0
                roi_landmarks = np.concatenate((smoothed_landmarks[48:], smoothed_landmarks[4:13], smoothed_landmarks[31:36]))
            elif roi_type == "faces":
                margin = 0
                roi_landmarks = smoothed_landmarks

            x, y, w, h = cv2.boundingRect(np.array(roi_landmarks))
            roi = aligned_frame[(y - margin):(y + h + margin), (x - margin):(x + w + margin)]
            sequence.append(roi)

        frame_idx += 1

    return sequence

def extract_rois(samples_dir, landmarks_dir, roi_types, output_dir):
    """extract_rois.
        :param landmarks_dir: str, directory where landmarks are stored
        :param rois_type: list, list that indicates the types of ROIs must be extracted
        :param output_dir: str, directory where ROIs will be stored
    """
    for roi_type in roi_types:
        spkrs = sorted(os.listdir(landmarks_dir))
        for spkr in tqdm(spkrs, desc=roi_type + ": %Speakers", bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'):
            samples = sorted(os.listdir(os.path.join(landmarks_dir, spkr)))
            for sample in tqdm(samples, desc=roi_type + ": %Samples", leave=False, bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'):
                sampleID = sample.split('.')[0]

                sample_path = os.path.join(samples_dir, spkr, sampleID + ".mp4")
                dst_dir = os.path.join(output_dir, roi_type, spkr, sampleID)
                os.makedirs(dst_dir, exist_ok=True)

                landmarks = read_pkl(os.path.join(landmarks_dir, spkr, sample))

                if landmarks != None:
                    sequence = crop_patch(roi_type, sample_path, landmarks)
                    for i, frame in enumerate(sequence):
                        dst_file = os.path.join(dst_dir, sampleID + '_' + str(i).zfill(4) + '.png')
                        cv2.imwrite(dst_file, frame)
                else:
                    print('Error in:', sampleID, '!!')

if __name__ == "__main__":
    ## DEFINING SCRIPT PARAMETERS ##
    parser = argparse.ArgumentParser(description='Region of Interest Extraction from the 68 facial landmarks previously computed',
                                     epilog="Usage: python get_ROIs.py --samples-dir ./data/LIP-RTVE/mp4/ --landmarks-dir ./data/landmarks/ --roi-types fitMouths faces SOTA --output-dir ./ROIs/")

    parser.add_argument("--samples-dir", default="../data/LIP-RTVE/mp4/", type=str, help="Directory where MP4 samples are stored.")
    parser.add_argument("--landmarks-dir", default="../src/landmarks/", type=str, help="Directory where landmarks are stored.")
    parser.add_argument("--roi-types", nargs='+', default=["fitMouth", "wideMouth", "faces", "SOTA"], type=str, help="List that indicates the types of ROIs must be extracted. You can choose whether extract the so-called 'fitMouths', 'wideMouths', 'faces' and/or 'SOTA'.")
    parser.add_argument("--output-dir", default="../data/ROIs/", type=str, help="Directory where ROIs will be stored.")

    args = parser.parse_args()

    ## EXTRACTING ROIs ##
    extract_rois(args.samples_dir, args.landmarks_dir, args.roi_types, args.output_dir)
