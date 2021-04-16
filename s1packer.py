import os
import sys
import subprocess
from distutils.dir_util import copy_tree
import click


@click.command()
@click.option("--directory", prompt="Song folder path",  help="Full path to song folder.")
@click.option("--unpack", default=False, help="Use --unpack=True in order to convert mp3 back to wav.")
def hello(directory, unpack):
    """Converts all wav files to mp3 in folder, and vice versa."""
    print("Input folder: " + directory)

    newDirEnding = ".unpacked" if unpack else ".packed"
    newDir = directory+newDirEnding
    print("Copying directory to: " + newDir)
    copy_tree(directory, newDir)
    directory = newDir
    # encodedFormat = '.flac'
    encodedFormat = '.mp3'
    rawFormat = '.wav'

    if (unpack):
        inExt = encodedFormat
        outExt = rawFormat
    else:
        inExt = rawFormat
        outExt = encodedFormat

    print(f'Looking for "{inExt}" files...')
    count = 0
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(inExt):
                count = count+1
                filePath = os.path.join(subdir, filename)
                newFilePath = filePath.replace(inExt, outExt)
                if (unpack):
                    cmd = f'ffmpeg -y -i "{filePath}" "{newFilePath}"'
                else:
                    cmd = f'ffmpeg -y -i "{filePath}" -vn -ar 44100 -ac 2 -q:a 2 "{newFilePath}"'

                # cmd = f'ffmpeg -y -i "{filePath}" -c:a flac "{newFilePath}"'

                print("Running command: " + cmd)
                subprocess.call(cmd)
                print(f'Deleting file: {filePath}')
                os.remove(filePath)
    print(f'Done converting {count} files. Please see output directory: {directory}')


if __name__ == '__main__':
    hello()
