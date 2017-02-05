import os
from shutil import copyfile
from resource_type import ResourceType
import argparse

ORIG_DIR = os.getcwd()

NODPI = ResourceType('drawable', '')
LDPI = ResourceType('drawable-ldpi', '.75x')
MDPI = ResourceType('drawable-mdpi', '1x')
HDPI = ResourceType('drawable-hdpi', '1.5x')
XHDPI = ResourceType('drawable-xhdpi', '2x')
XXHDPI = ResourceType('drawable-xxhdpi', '3x')
XXXHDPI = ResourceType('drawable-xxxhdpi', '4x')


def main():

    # parse command line arguments
    input_dir, output_dir, prefix = parseArgs()

    processFiles(input_dir, output_dir, prefix)


def processFiles(input_dir, output_dir, prefix):

    # register resource types
    resources = []
    resources.append(LDPI)
    resources.append(MDPI)
    resources.append(HDPI)
    resources.append(XHDPI)
    resources.append(XXHDPI)
    resources.append(XXXHDPI)
    resources.append(NODPI)

    # wor in the input directory
    os.chdir(input_dir)
    input_dir = os.getcwd()

    # get all files
    onlyfiles = [f for f in os.listdir('.')
                 if os.path.isfile(os.path.join('.', f))]

    # map files into appropriate resources
    for fname in onlyfiles:
        for resourceType in resources:
            if (resourceType.scaleFactor in fname):
                resourceType.addFile(os.path.abspath(fname))
                break

    # move to output directory
    createOutputDir(output_dir)
    os.chdir(output_dir)

    # copy files into new density drawable directories
    for resourceType in resources:
        if (resourceType.files != []):
            createDirectory(resourceType.dirName)
            for fname in resourceType.files:
                copyfile(fname, createAndroidName(resourceType, fname, prefix))


def createDirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def parseArgs(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        help='Path to the input directory. If not '
                        'specified it assumes current directory',
                        default='.')
    parser.add_argument('--output',
                        help='Path to the output directory. If not specified '
                        'it will create create new resource directories '
                        'within the current directory',
                        default='.')
    parser.add_argument('--prefix',
                        help='Prefix to the asset file names',
                        default='')
    args = parser.parse_args(args) if args is not None else parser.parse_args()
    return args.input, args.output, args.prefix


def createOutputDir(out_path):
    # create output directory
    os.chdir(ORIG_DIR)
    if not os.path.exists(out_path):
        os.makedirs(out_path)


def createAndroidName(resource, path, prefix):
    fname = os.path.basename(path).replace('@' + resource.scaleFactor, '')
    fname = fname.replace('-', '_')
    return resource.dirName + "/" + prefix + fname


if __name__ == "__main__":
    main()
