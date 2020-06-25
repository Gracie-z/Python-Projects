import requests
from lxml import etree

# Get the web page
url = "https://www.rosygracie.com/"
web = requests.get(url).text
web_page = etree.HTML(web)

# Get the image
image = web_page.xpath('//*[@id="comp-k6g461lv3imgimage"]/@src')[0]
real_image = requests.get(image)
with open("rosiegracie.jpg",'wb') as f:
    f.write(real_image.content)