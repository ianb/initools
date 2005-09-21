from setuptools import setup, find_packages

version = '0.2'

setup(name='INITools',
      version=version,
      description="Tools for parsing and using INI-style files",
      long_description="""\
A set of tools for parsing and using ``.ini``-style files, including
an abstract parser and several tools built on that parser.


Repository available at `http://svn.colorstudy.com/INITools/trunk
<http://svn.colorstudy.com/INITools/trunk#egg=INITools>`_
""",
      classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
        ],
      url="http://pythonpaste.org/initools/",
      keywords="config parser ini",
      author="Ian Bicking",
      author_email="ianb@colorstudy.com",
      license="MIT",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      zip_safe=True,
      )
      
