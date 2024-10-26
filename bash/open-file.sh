#!/bin/bash
# Author: @codedsprit <roshan0x01@gmail.com>

# small script to open files. doesn't need to specify file type.

# Check if the file exists
if [ ! -e "$1" ]; then
  echo "Error: file does not exist."
  exit 1
fi

# Determine the file type and open the file with the appropriate command
file_type=$(file --mime-type --brief "$1")

case $file_type in
  text/*|application/octet-stream) nvim "$1";;
  image/jpeg|image/png) sxiv "$1";;
  application/pdf) zathura "$1";;
  inode/directory) cd "$1" || exit ;;
  *) echo "Error: unable to open file."; exit 1;;
esac

exit 0
