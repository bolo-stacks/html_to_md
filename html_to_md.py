# # Problem Description

# Looking for a simple python script that I can point at a URL and it will return well formatted markdown of all sub pages
# Acceptance Criteria

# Hierarchy of pages found is important. Also want to get all text organized together. Should be a quick project.
# ChatGPT

# To achieve this task, you can use the requests library to fetch the HTML content of the pages and BeautifulSoup to parse and extract information from the HTML. Here's a simple Python script that you can use as a starting point:

# python

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_links_and_text(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract text content
    text_content = soup.get_text(separator='\n', strip=True)
    
    # Extract links
    links = []
    for link in soup.find_all('a', href=True):
        absolute_url = urljoin(base_url, link['href'])
        links.append(absolute_url)
    
    return links, text_content

def crawl_site(start_url):
    visited_urls = set()
    queue = [(start_url, '')]

    while queue:
        current_url, parent_text = queue.pop(0)

        if current_url in visited_urls:
            continue

        print(f"Processing: {current_url}")

        html_content = get_page_content(current_url)

        if html_content:
            links, text_content = extract_links_and_text(html_content, current_url)

            # Print hierarchical structure
            print(f"{'  ' * (parent_text.count('\n') + 1)}- {current_url}")

            # Print text content
            print(text_content)

            # Add links to the queue
            for link in links:
                queue.append((link, text_content))

            visited_urls.add(current_url)

if __name__ == "__main__":
    start_url = input("Enter the starting URL: ")
    crawl_site(start_url)

'''
This script defines three functions:

    get_page_content(url): Fetches the HTML content of a given URL.
    extract_links_and_text(html_content, base_url): Extracts links and text content from the HTML.
    crawl_site(start_url): Crawls the website starting from the given URL, printing the hierarchical structure and text content.
'''

# Make sure to install the required libraries before running the script:

# bash

# pip install requests beautifulsoup4

# Copy and paste this script into a Python file, run it, and enter the starting URL when prompted. 
# The script will crawl the website, print the hierarchical structure, and organize the text content.
