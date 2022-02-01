import os
import codecs
import collections

out = ""

out += "<UL>\n"
dirnames = [dirs for root, dirs, files in os.walk('.')][0]
dirnames.remove('.git')
dirnames.sort()

filepaths = collections.OrderedDict({dirname: [os.path.join(root, name)
             for root, dirs, files in os.walk(dirname)
             for name in files if name.endswith(".html")] for dirname in dirnames})


for directory in filepaths.keys():
    out+= "  <LI>" + directory + "</LI>\n"
    out+= "  <UL>"
    for file in filepaths[directory]:
        name = file.split(os.path.sep)[-1].replace('.html', '')
        out+= "    <LI><a href=" + file + ">" + "</a></LI>"
    out+= "  </UL>"
out+= "</UL>"

with codecs.open('index.html', 'w', encoding="utf-8") as f:
    f.write(out)

[(root, dirs, files) for root, dirs, files in os.walk('.')]