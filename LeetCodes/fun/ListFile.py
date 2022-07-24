import glob
import os
import csv
import argparse


def directory_content_to_csv(dir_path, output_csv):
	item_paths = glob.glob(dir_path + "/**/*", recursive=True)
	with open(output_csv, mode='w') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['Name', 'Suffix', 'Abs path'])
		for item_path in item_paths:
			if os.path.isfile(item_path):
				name = item_path.split("/")[-1].split(".")[0]
				suffix = item_path.split(".")[-1]
				abs_path = os.path.abspath(item_path)
				writer.writerow([name, suffix, abs_path])


parser = argparse.ArgumentParser()
parser.add_argument('--dir_path', dest='dir_path', help='path of directory you want to list contents', default='.', required=False)
parser.add_argument('--output_path', dest='output_path', help='path of csv file holing the content list', default='content_list.csv', required=False)

args = parser.parse_args()

directory_content_to_csv(args.dir_path, args.output_path)