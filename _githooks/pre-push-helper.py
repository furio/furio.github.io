import sys
from os import listdir
from os.path import isfile, join

if len(sys.argv) < 3:
    print("Not enough args")
    exit(1)

tag_dir = sys.argv[1]
tag_files = [f.replace(".html", "") for f in listdir(tag_dir) if isfile(join(tag_dir, f)) and f.endswith(".html")]

md_files = []
for md_dir in sys.argv[2:]:
    md_files += [join(md_dir, f) for f in listdir(md_dir) if isfile(join(md_dir, f)) and f.endswith(".md")]

tags = []
for md in md_files:
    md_file = open(md, "r")
    md_lines = md_file.readlines()
    for line in md_lines:
        if line.startswith("tags: "):
            splitted = line.split(":", 1)
            tags += splitted[1].strip().replace("[","").replace("]","").split(",")
            break
    md_file.close()

tags = map(lambda x: x.strip(), tags)

missing_tags = list(set(tags) - set(tag_files))
if len(missing_tags) > 0:
    print(missing_tags)
    exit(1)

exit(0)
