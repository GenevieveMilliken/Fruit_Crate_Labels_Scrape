""" code written by G. Milliken, reusable under MIT license""" 

#This python script scrapes the Produce Crate Labels from the Digital Commonweath: Massachusetts Collection Online
#This is the first script in the program; it needs to be ran first. The json it produces will with used by script titled 2_Fruit_Crate_Labels_Image_Download.py

#import modules needed for this script
from bs4 import BeautifulSoup
import requests
import json

#create an empty list to hold data
all_my_data = []

#create for loop that will paginate through multiple pages
#parse html into soup item
for pages in range(0,3):
	url = f"https://www.digitalcommonwealth.org/search?f%5Bcollection_name_ssim%5D%5B%5D=Produce+Crate+Labels&f%5Binstitution_name_ssim%5D%5B%5D=Boston+Public+Library&per_page={pages*50}"
	results_page = requests.get(url)
	page_html = results_page.text
	soup = BeautifulSoup(page_html, "html.parser")

	#find div that hold the metadata needed
	all_labels = soup.find_all("div", attrs = {'class': 'document'})

	#create a forloop and data dictionary 
	for items in all_labels:

		my_data = {
		"item url": None,
		"caption": None,
		"image url": None,
		}

		#get absolute url for each fruit label and assign it to "item url" in data dictionary
		item_link = items.find('a') 
		abs_url = "https://www.digitalcommonwealth.org" + item_link["href"]
		my_data["item url"] = abs_url
		# print(abs_url)

		#parse "item url" for each item and create a soup object
		item_request = requests.get(abs_url)
		item_html = item_request.text
		item_soup = BeautifulSoup(item_html, "html.parser")

		#locate where the metadata is within the larger div structure
		all_item_info = item_soup.find_all("div", attrs={'id': 'item_metadata_base'})

		#locate caption, strip white space, and assign to "caption" in data dictionary
		for caption in all_item_info:
			caption = caption.find('dd')
			caption = caption.text
			caption = caption.strip()
			my_data["caption"] = caption
		# print(caption)
		# print(my_data)

		#locate image urls
		all_photo_urls = item_soup.find_all("div", attrs={'id': 'img_show_canvas'})
	
		#locate image urls and assign to "image url" in data dictionary	
		for photo_url in all_photo_urls:
			link_list = photo_url.find_all("img")
		for link in link_list:
			# print(link['src'])
			my_data["image url"] = link['src']

		#append data so it is all together
		all_my_data.append(my_data)

# print(all_my_data)

#write to JSON
with open('fruit_crate_labels.json', 'w') as file_object:
	json.dump(all_my_data, file_object, indent=2)
	print('Thy Fruit JSON is Ready')

