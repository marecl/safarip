#!/bin/zsh

for f in "$@"; do
    mime=$(file --mime-type -b "$f")
    ext=""

    case "$mime" in
        image/jpeg)          ext="jpg" ;;
        image/png)           ext="png" ;;
        image/gif)           ext="gif" ;;
        image/webp)          ext="webp" ;;
        image/heic)          ext="heic" ;;
        application/pdf)     ext="pdf" ;;
        video/mp4)           ext="mp4" ;;
        video/quicktime)     ext="mov" ;;
        audio/mpeg)          ext="mp3" ;;
        audio/x-wav)         ext="wav" ;;
        application/zip)     ext="zip" ;;
        text/plain)          ext="txt" ;;
        *)                   echo "Unknown type: $mime -> $f"; continue ;;
    esac

    current_ext="${f##*.}"
    if [[ "$current_ext" != "$ext" ]]; then
        newname="$f.$ext"
        if [[ -e "$newname" ]]; then
            echo "File exists: $newname"
        else 
            mv -v "$f" "$newname"
        fi  
    fi
done
