#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <day_number>"
    exit 1
fi

day=$1

# Format day with leading zero for directory/file name
padded_day=$(printf "%02d" $day)

# Create directory if it doesn't exist
mkdir -p "$padded_day"

# Check for session cookie
if [ -z "$AOC_SESSION" ]; then
    if [ -f ".session" ]; then
        AOC_SESSION=$(cat .session)
    else
        echo "Error: AOC_SESSION environment variable not set and .session file not found"
        echo "Please set AOC_SESSION or create a .session file with your cookie"
        exit 1
    fi
fi

# Download the input file
curl -o "$padded_day/input.txt" \
     --cookie "session=$AOC_SESSION" \
     "https://adventofcode.com/2025/day/$day/input"

# Create empty test.txt file
touch "$padded_day/test.txt"
touch "$padded_day/aoc_${padded_day}a.py"
touch "$padded_day/aoc_${padded_day}b.py"



echo "Downloaded input for day $day to $padded_day/input.txt"
