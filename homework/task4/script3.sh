#!/bin/bash

printf "%s\n" "Enter a word"
read word
printf "%s\n" "Enter a file name"
read file
wordcount=$(grep -c $word $file)
printf "%s%s\n" "Word count is: " "$wordcount"
exit 0 
