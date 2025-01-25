#!/bin/bash
directory_path = "./*"

for file in "$directory_path"; do
    mv "$file" "${file%/*}/.${file##*/}";
done