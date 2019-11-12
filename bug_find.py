import pelican
from pelican.settings import read_settings
settings = read_settings('pelicanconf.py')
pelican = pelican.Pelican(settings)
pelican.run()
