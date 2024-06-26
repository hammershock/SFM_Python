# -*- coding: utf-8 -*-
"""
Incremental MultiView Structure From Motion
         ---- A simple Practice in Python

Requirements:
opencv-python
numpy
matplotlib
joblib
tqdm
networkx
scipy(for Bundle Adjustment)

@author: Hanmo Zhang
@email: zhanghanmo@bupt.edu.cn
"""
import argparse
from sfm_lite import load_calibration_data, SFM
from sfm_lite.visualize import visualize_points3d


def main(image_dir, calibration_file, min_matches, use_ba, ba_tol, verbose):
    K = load_calibration_data(calibration_file)
    sfm = SFM(image_dir, K)
    sfm.construct(min_matches=min_matches, use_ba=use_ba, ba_tol=ba_tol, verbose=verbose)
    visualize_points3d(sfm.graph.X3d, sfm.graph.colors, s=5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run SFM reconstruction on a set of images.")
    parser.add_argument('--image_dir', type=str, default="./ImageDataset_SceauxCastle/images", help='Directory containing images for reconstruction.')
    parser.add_argument('--calibration_file', type=str, default="./ImageDataset_SceauxCastle/images/K.txt", help='File containing camera calibration data.')
    parser.add_argument('--min_matches', type=int, default=80, help='Minimum pairs of matches. Default is 80.')
    parser.add_argument('--use_ba', action='store_true', help='Whether to use bundle adjustment. Default is False.')
    parser.add_argument('--ba_tol', type=float, default=1e-10, help='Tolerance for bundle adjustment. Default is 1e-10.')
    parser.add_argument('--verbose', type=int, default=0, help='Verbose of output. Default is 0.')

    args = parser.parse_args()
    main(args.image_dir, args.calibration_file, args.min_matches, args.use_ba, args.ba_tol, args.verbose)
