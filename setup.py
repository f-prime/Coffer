from setuptools import *

kwargs = {
	"author" : "Frankie Primerano",
	"author_email" : "frankieprimerano@gmail.com",
	"description" : "A lightweight platform for creating isolated and portable development environments",
	"entry_points" : {"console_scripts" : ["coffer=coffer.coffer:checkArgs"]},
	"name" : "coffer-container",
	"packages" : ["coffer", "coffer.utils"],
	"version" : "1.3.2",
        "url":"https://github.com/Max00355/Coffer",
        "keywords":"container coffer docker vm virtualenv",
        "license":"MIT",
        "long_description":open("README.md").read(),
    }

        

setup(**kwargs)
