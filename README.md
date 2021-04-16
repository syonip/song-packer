# A script to convert all wav files in folder (recursively) to mp3 and vice versa


You can use this to "pack" a Studio One song folder to about 1/10 the size.
I use this to save backups of song demos, where the recordings are scratch recordings anyway and I don't care about a lossy conversion.

## Warnings
- Use at your own risk!
- Always back up your songs before messing around with scripts you find on the internet!
- Don't use this on good recordings where you care about the quality! The mp3 conversion causes loss of quality that cannot be recovered.
- Tested on Windows 10

## Requirements
- python
- ffmpeg
- click (pip install -U click)

## Usage

### Pack a song
`python .\s1packer.py --directory "C:\Users\Johnny\Documents\Studio One\Songs\riff idea 099000"`

This will create a "packed" folder named "riff idea 099000.packed", which has mp3 instead of wav media files. This folder cannot be opened in Studio One until it is "unpacked"

### Unpack a song
`python .\s1packer.py --directory "C:\Users\Johnny\Documents\Studio One\Songs\riff idea 099000.packed" --unpack=True`

This will create an "unpacked" folder with all media converted back to wav (NOT original quality!)
Now the ".song" file in this folder should open in Studio One. 