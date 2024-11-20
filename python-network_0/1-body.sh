#!/bin/bash
 
# Function to send a GET request to a URL and display the body of the response.
# This function uses curl to send the request.
 
# @param $1: The URL to send the GET request to.
sendGetRequest() {
    local url="$1"  # Capture the URL passed as a parameter.
 
    # Send the GET request using curl and store the response in a variable.
    local response
    response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
 
    # Check if the response status code is 200 (OK).
    if [ "$response" -eq 200 ]; then
        # If the response status code is 200, display the body of the response.
        curl -s "$url"
    else
        # If the response status code is not 200, display an error message.
        echo "Error: Unexpected response status code $response"
    fi
}
