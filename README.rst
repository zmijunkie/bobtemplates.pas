
How we plan to create a PAS Plugin:



./bin/mrbob  bobtemplates.pas:plugin -O example.foo_pas 

./bin/mrbob --list-questions bobtemplates.pas:plugin


Does nearly nothing (yet) - this software is still a 
prototype. 

requirements.txt could be wrong - needs more testing -
look at my output from invoking 'pip freeze':

3to2==1.0
Babel==2.3.4
Beaker==1.8.1
BeautifulSoup==3.2.1
Cython==0.23.3
DateTime==4.0.1
Fabric==1.10.1
Glances==1.6.1
Jinja2==2.8
Mako==1.0.7
Markdown==2.4.1
MarkupSafe==0.23
Numeric==24.2
PyXB==1.2.4
PyYAML==3.11
Pygments==2.1.3
Sphinx==1.4.9
Unidecode==0.4.17
alabaster==0.7.9
archgenxml==2.7.dev0
astroid==1.3.6
backports==1.0
bpython==0.13.1
configparser==3.5.0
decorator==3.4.0
docutils==0.12
ecdsa==0.13
enum34==1.1.6
ephem==3.7.6.0
etk.docking==0.2
eulexistdb==0.19.1
eulxml==0.21.2
feedparser==5.2.1
flake8==3.3.0
gaphas==0.7.2
gaphor==0.17.2
gdbm==2.7.14
gntp==1.0.3
guess-language-spirit==0.5a5
hgreview==0.4
html2text==2014.9.25
httplib2==0.9.1
i18ndude==3.4.0
imagesize==0.7.1
ipaddr==trunk
libxml2-python==2.9.2
logilab-common==0.63.2
lxml==3.4.4
mccabe==0.6.1
mercurial==2.9.1
nose==1.3.1
numpy==1.9.2
ordereddict==1.1
paramiko==1.15.2
pbr==0.10.8
pdoc==0.3.2
plone.i18n==3.0.1
ply==3.6
psutil==0.6.1
py==1.4.26
pycairo==1.10.0
pycodestyle==2.0.0
pycrypto==2.6.1
pydns==2.3.6
pyflakes==1.5.0
pygobject==3.26.1
pylint==1.4.3
pync==1.6.1
pyparsing==2.0.3
pyspf==2.0.11
pytest==2.6.4
python-Levenshtein==0.11.2
python-dateutil==2.6.0
python-jenkins==0.4.5
python-ldap==2.3.10
pytidylib==0.2.4
pytz==2016.7
requests==2.13.0
review==1510
robotframework==2.8.5
robotframework-ride==1.3
robotframework-selenium2library==1.6.0
roman==2.0.0
selenium==3.0.2
simplegeneric==0.8.1
simplejson==3.8.2
six==1.10.0
snowballstemmer==1.2.1
-e git://github.com/michaeljones/sphinx-to-github.git@0a46518fe01e0c489a82ce95d16f20a0a2c3fc1b#egg=sphinxtogithub-master
stripogram==1.5
typing==3.5.2.2
ua-parser==0.6.1
unicodecsv==0.14.1
urwid==1.2.1
user-agents==1.0.1
virtualenv==12.1.1
wsgiref==0.1.2
wxPython==2.8.12.1
wxPython-common==2.8.12.1
xmiparser==1.5
zope.browser==2.1.0
zope.component==4.2.1
zope.configuration==4.0.3
zope.contenttype==4.1.0
zope.documenttemplate==3.4.3
zope.event==4.0.3
zope.exceptions==4.0.7
zope.i18n==4.0.0
zope.i18nmessageid==4.0.3
zope.interface==4.1.2
zope.location==4.0.3
zope.proxy==4.1.4
zope.publisher==4.1.0
zope.schema==4.4.2
zope.security==4.0.1
zope.structuredtext==4.1.0
zope.tal==4.1.0


