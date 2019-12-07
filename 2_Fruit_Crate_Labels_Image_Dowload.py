#This python script downloads images from the Digital Commonweath: Massachusetts Collection Online's Produce Crate Labels Collection
#This is the second script in the program; it needs to be ran second. It uses the JSON produced by the script titled 1_Fruit_Crate_Labels_JSON.py
#An empty folder titled Images need to be created in your directory before running; this is where the images will be downloaded to

import json
import urllib.request

def download_image(url, file_path, caption):
	full_path = file_path + caption + '.jpg'
	try:
		urllib.request.urlretrieve(url, full_path)
	except FileNotFoundError:
		pass

# open json file, extract information, write images to file
with open('fruit_crate_labels.json') as f_object:
	text = json.load(f_object)
	for data_dict in text:
		caption = data_dict['caption']
		url = data_dict['image url']
		download_image(url, "Images/", caption)
