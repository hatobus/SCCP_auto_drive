import cv2
import os

class Matching_traf_mark:
    def __init__(self):
        pass

    def load_pic(self, label_file, target_file):
        try:
            LABEL_FILE = "../img/test_label" + label_file
            TARGET_FILE = "../img/test_capcha" + target_file

        except IOError:
            print("{0} or {1} can't be opened.".format(label_file, target_file))
        
        return [LABEL_FILE, TARGET_FILE]

    def resize_to_gray(self, label, target, IMG_SIZE=(200, 200), filename="stopimg"):
        pictures = [label, target]
        pic_list = []

        for pic in pictures:
            read_pic = cv2.imread(pic, cv2.IMREAD_GRAYSCALE)
            read_pic = cv2.resize(pic, IMG_SIZE)
            pic_list.append(read_pic)
        
        return pic_list

    def Matching_AKAZE(self, label_pic, target_pic):
        akaze = cv2.AKAZE_create()

       	# 特徴量の検出と特徴量ベクトルを計算
       	kp1, des1 = akaze.detectAndCompute(target_pic, None)
       	kp2, des2 = akaze.detectAndCompute(label_pic, None)

       # Brute-Force Matcher生成
       	bf = cv2.BFMatcher()

       # 特徴量ベクトル同士をBrute-Force＆KNNでマッチング
       	matches = bf.knnMatch(des1, des2, k=2)

       # データを間引きする
       	ratio = 0.2
       	good = []
       	for m, n in matches:
            if m.distance < ratio * n.distance:
                good.append([m])

        img3 = cv2.drawMatchesKnn(target_pic, kp1, label_pic, kp2, good[:30], None, flags=2)

        cv2.imwrite("../img/outputimg" + filename + "out" + ".png", img3)


if __name__ == "__main__":
    Mark = Matching_traf_mark()
    Stop_label, Stop_capche = Mark.resize_to_gray("stop.png", "stop_capcha.png")
    Resized = Mark.resize_to_gray(Stop_label, Stop_capche)
    Mark.Matching_AKAZE(Resized[0], Resized[1])
