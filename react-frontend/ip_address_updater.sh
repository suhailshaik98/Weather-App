#!/bin/bash

# Check if the script is provided with at least one argument
if [ $# -lt 1 ]; then
  echo "Usage: $0 <file_path> [localhost_flag]"
  exit 1
fi

file_path="$1"
localhost_flag="$2"

# Check if the second argument is provided and equals "localhost"
if [ "$localhost_flag" = "localhost" ]; then
  new_url="localhost"
else
  # Use curl to get the IP address from api.ipify.org
  new_url=$(curl -s https://api.ipify.org)

  # Check if the curl command encountered any errors
  if [ $? -ne 0 ]; then
    echo "Error fetching IP address from api.ipify.org"
    exit 1
  fi
fi

# Use sed to replace the line with the new URL
sed -i "s/const url=\"placeholder\"/const url=\"$new_url\"/" "$file_path"

# Check if sed encountered any errors
if [ $? -eq 0 ]; then
  echo "Line in $file_path updated to: const url=\"$new_url\""
else
  echo "Error updating the line in $file_path"
fi
