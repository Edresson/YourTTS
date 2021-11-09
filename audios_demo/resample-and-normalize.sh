#!/bin/bash

SOURCE_DIR="./"
TARGET_DIR="./"
OUT_EXTENSION=".wav"
SEARCH_EXTENSION=".wav" 
export SOURCE_DIR
export TARGET_DIR
export OUT_EXTENSION
export SEARCH_EXTENSION
doone() {
    flacFile="$1"
    if [[ "$(basename "${flacFile}")" != ._* ]] ; then # Skip files starting with "._"
        tmpVar="${flacFile}"
        mp3File="${tmpVar/$SOURCE_DIR/$TARGET_DIR}"
        mp3File="${mp3File/$SEARCH_EXTENSION/$OUT_EXTENSION}"
        mp3FilePath=$(dirname "${mp3File}")
        mkdir -p "${mp3FilePath}"
        # if [ ! -f "$mp3File" ]; then # If the mp3 file doesn't exist already
        echo "Input: $flacFile"
        echo "Output: $mp3File"
        #ffmpeg-normalize "$flacFile" -o "$mp3File" -f -ar 16000 -f
        ffmpeg-normalize "$flacFile" -nt rms -t=-27  -o "$mp3File" -f -ar 16000 -f
        #fi
    fi
}

dofiles() {
    flacFile="$1"
    if [[ "$(basename "${flacFile}")" != ._* ]] ; then # Skip files starting with "._"
        tmpVar="${flacFile}"
        mp3File="${tmpVar/$SOURCE_DIR/$TARGET_DIR}"
        mp3FilePath=$(dirname "${mp3File}")
        mkdir -p "${mp3FilePath}"
        if [ ! -f "$mp3File" ]; then # If the mp3 file doesn't exist already
            echo "Input: $flacFile"
            echo "Output: $mp3File"
            cp "$flacFile" "$mp3File"
        fi
    fi
}



export -f doone
# export -f dofiles



# texts
# find "${SOURCE_DIR}" -type f \( -iname "*.txt" \) -print0 |
#    parallel -0 dofiles
# Find all flac/wav files in the given SOURCE_DIR and iterate over them:
find "${SOURCE_DIR}" -type f \( -iname "*${SEARCH_EXTENSION}" \) -print0 |
  parallel -0 doone
  
