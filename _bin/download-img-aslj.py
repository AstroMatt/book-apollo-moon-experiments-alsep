import re
import requests


URL = [
    'https://www.hq.nasa.gov/alsj/a11/images11.html',
    'https://www.hq.nasa.gov/alsj/a12/images12.html',
    'https://www.hq.nasa.gov/alsj/a13/images13.html',
    'https://www.hq.nasa.gov/alsj/a14/images14.html',
    'https://www.hq.nasa.gov/alsj/a15/images15.html',
    'https://www.hq.nasa.gov/alsj/a16/images16.html',
    'https://www.hq.nasa.gov/alsj/a17/images17.html',
]

FILENAMES = re.compile(r'href="(.*?)"')
EXTENSIONS = {'GIF', 'png', 'gif', 'mov', 'JPG', 'jpg', 'wmv', 'tif'}
TO_DOWNLOAD = []


for url in URL:
    resp = requests.get(url)
    base_url = re.sub(r'images[0-9]{2}.html', '', url)

    for filename in FILENAMES.findall(resp.text):
        extension = filename.split('.')[-1]

        if extension in EXTENSIONS:
            TO_DOWNLOAD.append(f'{base_url}{filename}')

for url in TO_DOWNLOAD:
    if 'HR' in url:
        lowresolution_filename = url.replace('HR', '')

        if lowresolution_filename in TO_DOWNLOAD:
            TO_DOWNLOAD.remove(lowresolution_filename)


with open('/tmp/download.txt', mode='w') as file:
    for line in TO_DOWNLOAD:
        file.write(line+'\n')
