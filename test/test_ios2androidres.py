import unittest
import os
import argparse
import shutil
import ios2android as converter
import filecmp
from resource_type import ResourceType


class TestiOS2AndroidRes(unittest.TestCase):

    def setUp(self):
        # save cwd so we can revert back to it when we're done with a test
        self.cwd = os.getcwd()

    def test_processFiles(self):
        converter.processFiles('./test/img/', 'output/', 'ic_')
        os.chdir(self.cwd)
        self.assertTrue(filecmp.cmp(
            './test/img/android-body@1.5x.png',
            'output/drawable-hdpi/ic_android_body.png'))
        self.assertTrue(filecmp.cmp(
            './test/img/android-body@2x.png',
            'output/drawable-xhdpi/ic_android_body.png'))
        self.assertTrue(filecmp.cmp(
            './test/img/android-body@3x.png',
            'output/drawable-xxhdpi/ic_android_body.png'))
        self.assertTrue(filecmp.cmp(
            './test/img/android-body@4x.png',
            'output/drawable-xxxhdpi/ic_android_body.png'))
        self.assertTrue(filecmp.cmp(
            './test/img/android-boat.png',
            'output/drawable/ic_android_boat.png'))

        shutil.rmtree('output')

    def test_createAndroidName(self):
        self.assertEquals(
            'drawable-hdpi/ic_ios_name_convention.png',
            converter.createAndroidName(
                converter.HDPI,
                '/Path/To/File/ios-name-convention@1.5x.png',
                'ic_'))

    def tearDown(self):
        os.chdir(self.cwd)

if __name__ == '__main__':
    unittest.main()
