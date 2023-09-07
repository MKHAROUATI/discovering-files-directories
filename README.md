# discovering-files-directories
 
markdown
Copy code
# Web Page Checker

This Python script allows you to check the HTTP status codes and reasons for a list of URLs obtained from a text file. It helps you quickly identify the status of web pages.

## Prerequisites

Before using this script, make sure you have the following installed:

- Python 3.x
- The `requests` library (you can install it using `pip install requests`)

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

   ```bash
   
   python3 script.py arg1 arg2
arg1: The base URL to which the URLs from the text file will be appended.
arg2: The path to the text file containing the list of URLs, one URL per line.
The script will process each URL in the text file and display the HTTP status code and reason for each URL that does not return a 404 error.
Example
Suppose you have a text file named urls.txt with the following contents:

page1
page2
page3
You can use the script like this:

python3 script.py http://example.com urls.txt
The script will check http://example.com/page1, http://example.com/page2, and http://example.com/page3, displaying the status code and reason for each URL that does not return a 404 error.

Note
Make sure to provide arg1 in the format http:// or https:// followed by the domain.
Ensure that arg2 contains a valid path to the text file with one URL per line.
License
This project is licensed under the MIT License - see the LICENSE file for details.

You can place this README.md file in the same directory as your script and update