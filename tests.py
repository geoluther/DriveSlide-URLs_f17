#!/usr/bin/python
import csv
import sys
from datetime import date

import html_partials


def build_links(file):
	with open(file) as csvfile:
		html = ""
		reader = csv.reader(csvfile)
		for line in reader:
			html += "<li><a href='{}' target='_blank'>{}</a></li>".format(line[1], line[0])
		return html


def build_menu(files):
	# today = datetime.today()
	# print today

	menu = "<p class='menu'>"
	for file in files:
		handle = get_handle(file)

		menu += """
   		<button class="btn btn-primary" type="button" data-toggle="collapse" data-target="#{0}"
   		aria-expanded="false" aria-controls="collapse{0}">
        {0}
        </button>
        """.format(handle)

        menu += "</p>"
        return menu


def get_handle(filename):
	handle = filename.split('.')[0]
	handle = handle.split(' ')[-1]
	return handle


def build_list(file):
	html = ""
	handle = get_handle(file)
	collapse = "collapse"
	d = date.today()
	dayofweek = d.strftime("%A")
	if handle == dayofweek:
		collapse = "collapse show"
	html += '<div class="{}" id="{}">'.format(collapse, handle)
	html += '<h4>{}</h4>'.format(handle)
	html += '<ul class="list-unstyled">'
	html += build_links(file)
	html += '</ul></div>'
	return html


def main(files):
	print html_partials.header
	menu = build_menu(files)
	body = ""
	print menu

	for file in files:
		html = build_list(file)
		body += html

	print body
	print html_partials.footer


if __name__ == "__main__":
	files = [ name for name in sys.argv[1:] ]
	# print files
	main(files)
