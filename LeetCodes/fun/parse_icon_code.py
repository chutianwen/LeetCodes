from bs4 import BeautifulSoup
import json
import argparse

# python parse_icon_code.py --input byton-icons-v3.svg  --output map.json
parser = argparse.ArgumentParser()
parser.add_argument('--input', dest='input', help='input containing mapping', required=True)
parser.add_argument('--output', dest='output', help='output json file', required=True)

args = parser.parse_args()

with open(args.input, 'r', encoding='utf8') as f:
	data = f.read()
	soup = BeautifulSoup(data, 'xml')
	test = soup.findAll("glyph")[0]
	name_to_code = {item['glyph-name']: item['unicode'] for item in soup.findAll("glyph")}
	with open(args.output, 'w', encoding='utf8') as outfile:
		json.dump(name_to_code, outfile)
