from setuptools import *

kwargs = {
	"author" : "Frankie Primerano",
	"author_email" : "frankieprimerano@gmail.com",
	"description" : "A lightweight filesystem container for creating isolated development environments.",
	"entry_points" : {"console_scripts" : ["coffer=coffer.coffer:checkArgs"]},
	"name" : "Coffer",
	"packages" : ["coffer", "coffer.utils"],
	"version" : "1.1.0",
}

setup(**kwargs)
