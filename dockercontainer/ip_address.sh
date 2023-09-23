#!/bin/bash

# Define the URL of the IP address API
IP_API_URL="https://api.ipify.org?format=json"

# Define the file path where you want to save the IP address
# IP_FILE="ip_address.txt"

# Use curl to fetch the IP address from the API and save it to the file
# curl -s "$IP_API_URL" > "$IP_FILE"
export ip_address=$(curl -s "$IP_API_URL" | jq -r '.ip')
# echo $ip_address
# Set the IP address as an environment variable
export ip_address_url="$ip_address"
