# setup.py
import setuptools

setuptools.setup(name="medinetparsepy",
                 version="0.1",
                 description="Parses Data from the Medinet Scheduling System.",
                 url="https://github.com/JonasEngstrom/medinetparsepy",
                 author="Jonas Engström",
                 author_email="JonasEngstrom@users.noreply.github.com",
                 license="MIT",
                 install_requires=[
                     'bs4',
                     'pandas',
                     'matplotlib',
                     'numpy'
                 ],
                 package_dir={"": "src"},
                 packages=setuptools.find_packages(where="src")
                 )
