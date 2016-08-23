from setuptools import *

kwargs = {
	"author" : "Frankie Primerano",
	"author_email" : "frankieprimerano@gmail.com",
	"description" : "A lightweight platform for creating isolated and portable development environments",
	"entry_points" : {"console_scripts" : ["coffer=coffer.coffer:checkArgs"]},
	"name" : "Coffer",
	"packages" : ["coffer", "coffer.utils"],
	"version" : "1.3.1",
}

setup(**kwargs)
