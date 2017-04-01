import util.phantomjs
from os import listdir
from util.phantomjs import netsniff
import time
from multiprocessing import Pool

#Loop throuh seed
seeds_path  = "../seeds/"
output_path = "../output/json/"
seed_filename = "hospital_websites_urls_seed_3_v1.0.txt"
seed_filename = "hospital_websites_test.txt"

"""
   Read seename file and loop through all urls in it.
   call netsniff to get json and save into output folder
"""

start_time = time.time()

def call_netsniff_saveto_file(url):
    json = netsniff(url)
    # create file name based on url
    file_name = url.replace(".com/", ".com ").replace(".org/", ".org ").replace("https://", "").replace("http://","").replace("/","").replace("?", "").replace("=", "").replace("&", "").strip()
    # write to file
    file = open(output_path + file_name + '.json', 'w')
    file.write(json)
    file.close()


pool = Pool()
urls = []
with open(seeds_path+seed_filename) as input_file:
    for url in input_file:
        urls.append(url)

#Call URLs in parallel
pool.map(call_netsniff_saveto_file, urls)

elapsed_seconds = time.time() - start_time
elapsed_minutes = elapsed_seconds/60
elapsed_hours   = elapsed_minutes/60
print("--- %s seconds ---" % elapsed_seconds)
print("--- %s minutes ---" % elapsed_minutes)
print("--- %s hours   ---" % elapsed_hours)