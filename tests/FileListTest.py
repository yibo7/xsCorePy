from unittest import TestCase

from XsCore.XsFso.FileList import XsFileList


class FileListTest(TestCase):

    # def testSubList(self):
    #
    #     # xsFl = XsFileList("D:\work\管理\CoinBig", ['.txt'])
    #     xsFl = XsFileList("D:\work\管理\CoinBig")
    #     lsRz = xsFl.getSubFiles()
    #     for sP in lsRz:
    #         print(sP)
    #     self.assertTrue(len(lsRz) > 10)

    def testSubListAsync(self):
        xsFl = XsFileList("D:\work\管理\CoinBig")
        xsFl.getSubFilesAsync(self.callBackFile)

    def callBackFile(self, src):
        print(src)