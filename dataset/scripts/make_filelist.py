import os
import sys
import glob


class filelist:
    def __init__(self, fname="index.txt"):
        self.outfilename = fname

    def grep_fname(self, dirPath):
        # return all image path into the dirs
        _dirPath = os.path.abspath(dirPath)
        imagelist = glob.glob(os.path.join(_dirPath, "*.jpg"))
        return imagelist

    def writetxtfile(self, imglist):
        cnt = 0
        with open(self.outfilename, 'w') as f:
            for fpath in imglist:
                f.write(fpath + '\n')
                cnt += 1

        return cnt


if __name__ == '__main__':
    Filegrep = filelist()
    dirs = []
    underfile = glob.glob("../Images/*")
#    underdir = list(filter(lambda files
    print(underfile)
    for fn in underfile:
        if os.path.isdir(os.path.abspath(fn)):
            dirs.append(os.path.abspath(fn))

    picnums = 0

    for d in dirs:
        imagelist = Filegrep.grep_fname(d)
        picnums += Filegrep.writetxtfile(imagelist)

    print("Sum of picture : {}".format(picnums))
