from os import listdir
from os.path import isfile, join
import pprint
import urllib.robotparser as urobot
import csv

files = [f for f in listdir("robots") if isfile(join("robots", f))]
ai_robots = open("ai-robots.txt").read().splitlines()

pprint.pp(ai_robots)

results = []

for file in files:
    site_blocks_ai = False
    site_allows_ai = False
    site_blocks_all = False

    pprint.pp(f"reading {file} robots.txt...")

    fd = open(f"robots/{file}")
    rfp = urobot.RobotFileParser()
    rfp.parse(fd.readlines())
    entries = [rfp.default_entry, *
               rfp.entries] if rfp.default_entry else rfp.entries
    for entry in entries:
        for ruleline in entry.rulelines:
            if ("*" in entry.useragents and not ruleline.allowance):
                site_blocks_all = True
            if (set(ai_robots) & set(entry.useragents)):
                if (ruleline.allowance):
                    site_allows_ai = True
                else:
                    site_blocks_ai = True

                # print(entry.useragents, ruleline.path, ruleline.allowance)

    results.append({
        "site": file[:-4],
        "site_allows_ai": site_allows_ai,
        "site_blocks_ai": site_blocks_ai,
        "site_blocks_all": site_blocks_all,
    })

pprint.pp(results)

keys = results[0].keys()

with open('results.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(results)
