#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# notez qu'on import la lib
# donc assurez-vous que l'importe n'a pas d'effet de bord
import ai42

# Ceci n'est qu'un appel de fonction. Mais il est trèèèèèèèèèèès long
# et il comporte beaucoup de paramètres
setup(

	# le nom de votre bibliothèque, tel qu'il apparaitre sur pypi
	name='ai42',

	# la version du code
	version=ai42.__version__,

	# Liste les packages à insérer dans la distribution
	# plutôt que de le faire à la main, on utilise la foncton
	# find_packages() de setuptools qui va cherche tous les packages
	# python recursivement dans le dossier courant.
	# C'est pour cette raison que l'on a tout mis dans un seul dossier:
	# on peut ainsi utiliser cette fonction facilement
	packages=find_packages(),

	# votre pti nom
	author="judumay",

	# Votre email, sachant qu'il sera publique visible, avec tous les risques
	# que ça implique.
	author_email="judumay@student.42.fr",

	# Une description courte
	description="Wallah",

	include_package_data=True,

	# Il n'y a pas vraiment de règle pour le contenu. Chacun fait un peu
	# comme il le sent. Il y en a qui ne mettent rien.
	classifiers=[],

	license="WTFPL",

)