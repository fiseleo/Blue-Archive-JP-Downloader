import os
import extractor
from download_assets import ROOT, RAW, EXT


def removeEmptyDirectories(rootDirectory: str):
    for parentDirectoryPath, subDirectoryName, file in os.walk(rootDirectory, topdown=False):
        for subFolder in subDirectoryName:
            dirPath = os.path.join(parentDirectoryPath, subFolder)
            if not os.listdir(dirPath):
                # if folder is empty, remove it
                os.rmdir(dirPath)
                print(f"remove empty folder: {dirPath}")


def extractBundles(sourceDirectory: str, outDirectory: str):
    for root, dirs, files in os.walk(sourceDirectory):
        for f in files:
            if not f.endswith(".bundle"):
                continue
            fp = os.path.join(root, f)
            extractor.extract_assets(fp, outDirectory)


if __name__ == '__main__':
    extractBundles(RAW, EXT)
    removeEmptyDirectories(EXT)
