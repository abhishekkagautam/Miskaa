from bs4 import BeautifulSoup
import requests
import json
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
urls = [
    "https://www.instructables.com/Building-a-Self-Driving-Boat-ArduPilot-Rover/",
    "https://www.instructables.com/Hydraulic-Craft-Stick-Box/",
    "https://www.instructables.com/How-to-Make-a-Self-Watering-Plant-Stand/"
    ]
i=1
li=['scraped_url', 'header_title', 'youtube_url',' image_url']
for url in urls:
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    x_a=soup.find_all('a')
    x_head=soup.find_all('head')
    x_image=soup.find_all('img')
    key="url"+str(i)+".xml"
    f = open(key,"w+")
    
    f.write("head ::\n")
    for j in x_head:
        f.write("\n"+str(j))
    f.write("\n\n\n\nImage tags ::\n")
    
    for j in x_image:
        f.write("\n"+str(j))
    f.write("\n\n\n\nAnchor tag ::\n ")
    for j in x_a:
        f.write("\n"+str(j))    
    f.close()
    i=i+1