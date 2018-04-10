import sys
import os
import glob


args = sys.argv
imagePath = os.path.abspath(args[1])
labelPath = os.path.abspath(args[2])

imageDirsList = os.listdir(imagePath)
labelDirsList = os.listdir(labelPath)

imageList = []
labelList = []


class rmUnsetedImages:
    def __init__(self, imgext="*.jpg", txtext="*.txt"):
        self.imgext = imgext
        self.txtext = txtext

    def getImagesList(self):
        for dir in imageDirsList:
            imgDir = os.path.join(imagePath, dir)
            _imageList = glob.glob(os.path.join(imgDir, self.imgext))
            _imageList.insert(0, dir)
            imageList.append(_imageList)

#        print(imageList)

    def getLabelsList(self):
        for dir in labelDirsList:
            lblDir = os.path.join(labelPath, dir)
            _labelList = glob.glob(os.path.join(lblDir, self.txtext))
            labelList.extend(_labelList)
        self.labelsNameOnly = self.grepNameOnly(labelList)

    def rmUnseted(self):
        for image in imageList:
            dir = image[0]
            image.pop(0)
            rmImageDir = os.path.join(imagePath, dir)
            for imgName in image:
                # 画像ファイル名はユニークなので、ラベル名もユニークになるのでこの実装にした
                basename = os.path.basename(imgName)
                name, ext = os.path.splitext(basename)

                if name not in self.labelsNameOnly:
                    print(name)
                    name = name + ext
                    os.remove(os.path.join(rmImageDir, name))

    def grepNameOnly(self, labelList):
        flist = []
        for files in labelList:
            base = os.path.basename(files)
            name, ext = os.path.splitext(base)
            flist.append(name)
        return flist


if __name__ == '__main__':
    Unbound = rmUnsetedImages()
    Unbound.getImagesList()
    Unbound.getLabelsList()
    Unbound.rmUnseted()
