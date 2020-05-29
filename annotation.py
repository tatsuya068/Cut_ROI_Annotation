

import cv2
import glob
import os
import yaml
import argparse
import json
import shutil
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir',default=None, help='読み込むフォルダ名')
    parser.add_argument('--output_dir', default=None,help='出力フォルダ名')
    args = parser.parse_args()
    return args

def main():

    CONFIG = parse_args()
    input_dir = CONFIG.input_dir
    output_dir = CONFIG.output_dir

    show_font = cv2.FONT_HERSHEY_SIMPLEX

    SAVE_DIR = Path(output_dir)
    SAVE_DIR.mkdir(exist_ok=True)
    print(f'\n\n===>>>> save dir : {SAVE_DIR}\n\n')

    # Read the data and sort
    files = glob.glob(os.path.join(input_dir, '*'))
    files = sorted(files)

    max_len = len(files)


        # Read the file
    img_path_ = files[0]
        # Read the image
    org_img_ = cv2.imread(img_path_)
    # Get height and width
    height, width = org_img_.shape[:2]


    index = 0
    left_top_x = 100
    left_top_y = 0
    right_bottom_x = width -100
    right_bottom_y = height 

    tmp = []
    while True:

        # Read the file
        img_path = files[index]
        # Read the image
        org_img = cv2.imread(img_path)
        # Get height and width
        height, width = org_img.shape[:2]

        color = (255, 255, 255)
        show_img = org_img.copy()
        show_img_2 = cv2.rectangle(show_img, (left_top_x,left_top_y), (right_bottom_x, right_bottom_y), color, thickness= 9)
        cv2.putText(show_img_2, img_path.split('/')[-1], (left_top_x + 10, left_top_y + 120), cv2.FONT_HERSHEY_SIMPLEX, 4.0, (255, 255, 255), thickness=9)
        cv2.putText(show_img_2, f'[{index+1}/{max_len}]', (left_top_x + 10, left_top_y + 320), cv2.FONT_HERSHEY_SIMPLEX, 4.0, (255, 255, 255), thickness=9)
        # window sizeの調整
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        # 画像の表示
        cv2.imshow('image', show_img_2)

        key = cv2.waitKey(0)

        if key == ord('1'):
            left_top_x = left_top_x - 10 if left_top_x > 0 else left_top_x
        if key == ord('3'):
            left_top_y = left_top_y - 10 if left_top_y > 0 else left_top_y
        if key == ord('5'):
            right_bottom_x = right_bottom_x - 10 if right_bottom_x > 0 else right_bottom_x
        if key == ord('7'):
            right_bottom_y = right_bottom_y - 10 if right_bottom_y > 0 else right_bottom_y
        if key == ord('2'):
            left_top_x = left_top_x + 10 if left_top_x < width else left_top_x
        if key == ord('4'):
            left_top_y = left_top_y + 10 if left_top_y < height else left_top_y
        if key == ord('6'):
            right_bottom_x = right_bottom_x + 10 if right_bottom_x < width else right_bottom_x
        if key == ord('8'):
            right_bottom_y = right_bottom_y + 10 if right_bottom_y < height else right_bottom_y


        if key == ord('k'):
            index = index - 1 if index > 0 else index

        if key == ord('j'):

            #画像の書き出しと次の画像へ
            img_cut = org_img[left_top_y : right_bottom_y, left_top_x : right_bottom_x,:]
            tmp_img_path = Path(img_path).stem 
            tmp_img_path = tmp_img_path + '_cut.jpg'
            print(tmp_img_path)
            print(f'==(annotated)==>>> {SAVE_DIR / tmp_img_path}')
            print('\n\n')
            cv2.imwrite(str(SAVE_DIR / tmp_img_path), img_cut )
            index = index + 1 if index < len(files) -1 else index

        # 【q】で終了
        if key == ord("q"):
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    main()

