There are two python scripts in this repository: 

(1) 1_Fruit_Crate_Labels_JSON.py - This python script scrapes the Produce Crate Labels from the Digital Commonweath: Massachusetts Collection Online. This is the first script in the program; it needs to be ran first. The json it produces will with used by the second script. 

(2) 2_Fruit_Crate_Labels_Image_Download.py - This python script downloads images from the Digital Commonweath: Massachusetts Collection Online's Produce Crate Labels Collection. This is the second script in the program; it needs to be ran second. It uses the JSON produced by script 1. An empty folder titled Images need to be created in your directory before running; this is where the images will be downloaded to. The label titles are used as the file names for each image, a tool such as NameChanger (https://mrrsoftware.com/namechanger/) could be used to rename the image files as necessary.
