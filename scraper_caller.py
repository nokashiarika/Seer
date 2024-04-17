import sys
import webbrowser
import requests
from scraper import call_open_ai
from parser.locator import find_location
from fetcher.fetch_home_html import fetch_home_html
from fetcher.fetch_home_html import homes

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <prompt>")
        sys.exit(1)
    
    prompt = sys.argv[1]
    print(f"You entered the prompt: {prompt}")
    if find_location(prompt,[]):
        data = "some data needing location processing"
        city = find_location(prompt, [])
        print(city)
        url = f"https://www.zillow.com/homes/{city.replace(' ', '-')}_rb/"
        print(f"Opening Zillow page for {city}: {url}")
        fetch_home_html("url")
        #if html_content:
            #print(html_content)
    # print(call_open_ai(str(homes[0])))

if __name__ == "__main__":
    main()
