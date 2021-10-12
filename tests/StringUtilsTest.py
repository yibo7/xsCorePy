from unittest import TestCase

from XsCore import XsHttpUtils, XsStringUtils


class StringUtilsTest(TestCase):

    def testGetHtmlUrls(self):
        htmlc = XsHttpUtils.getHtml('http://www.beimai.com/baike/243a107743b0c.html')
        urls = XsStringUtils.getHtmlUrls(htmlc)
        for url in urls:
            print(url)

    def testGetChinese(self):
        cns = XsStringUtils.getChinese("fsfs我是，opopl中国人")
        for cn in cns:
            print(cn)

    def testSplitLines(self):
        rzs = XsStringUtils.splitLines("ab c\n\nde fg\rkl\r\n")
        print(rzs)

    def testSplit(self):
        rzs = XsStringUtils.split("ab cnkde fgnkl","nk")
        print(rzs)

    def testCutStartEnd(self):
        testTxt = 'Cats are aaa smarter than bbb dogs'
        rz = XsStringUtils.cutStartEnd(testTxt, "aaa", "bbb")
        print(rz)