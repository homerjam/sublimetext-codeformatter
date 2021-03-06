# @author 		Avtandil Kikabidze
# @copyright 		Copyright (c) 2008-2013, Avtandil Kikabidze (akalongman@gmail.com)
# @link 			http://long.ge
# @license 		GNU General Public License version 2 or later;

import os
import sys
import re
import sublime
import subprocess

try:
 	# Python 3
	from .lib import cssbeautifier
except (ValueError):
 	# Python 2
	from lib import cssbeautifier


class CssFormatter:
	def __init__(self, formatter):
		self.formatter = formatter


	def format(self, text):
		text = text.decode("utf-8")
		opts = self.formatter.settings.get('codeformatter_css_options')


		stderr = ""
		stdout = ""
		options = cssbeautifier.default_options()

		if (opts["indent_size"]):
			options.indent_size = opts["indent_size"]
		else:
			options.indent_size = 4

		if (opts["indent_char"]):
			options.indent_char = opts["indent_char"]
		else:
			options.indent_char = ' '

		if (opts["indent_with_tabs"]):
			options.indent_with_tabs = True
		else:
			options.indent_with_tabs = False


		if (opts["selector_separator_newline"]):
			options.selector_separator_newline = True
		else:
			options.selector_separator_newline = False

		if (opts["end_with_newline"]):
			options.end_with_newline = True
		else:
			options.end_with_newline = False




		try:
 		 	stdout = cssbeautifier.beautify(text, options)
		except Exception as e:
		 	stderr = str(e)

		if (not stderr and not stdout):
			stderr = "Formatting error!"

		return stdout, stderr



