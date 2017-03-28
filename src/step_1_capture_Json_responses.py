import util.phantomjs
from os import listdir
from util.phantomjs import netsniff

#Loop throuh seed
seeds_path  = "../seeds/"
output_path = "../output/json/"
seed_filename = "hospital_websites_urls_seed_3_v1.0.txt"

"""
   Read seename file and loop through all urls in it.
   call netsniff to get json and save into output folder
"""

with open(seeds_path+seed_filename) as input_file:
    for url in input_file:
        print(url)
        json = netsniff(url)
        #create file name based on url
        file_name = url.replace(".com/", ".com ").replace(".org/", ".org ").replace("https://", "").replace("http://","").replace("/", "").replace("?", "").replace("=", "").replace("&", "")
        #write to file
        file = open(output_path + file_name + '.json', 'w')
        file.write(json)
        file.close()