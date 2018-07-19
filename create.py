import random
import csv
import os.path

manifest = """{
	"name": "Taboola New Tab",
	"version": "1.0",
	"description": "Taboola New Tab",
	"manifest_version": 2,
	"short_name": "New Tab",
	"chrome_url_overrides": {
	 	"newtab": "newtab.html"
	},
	"icons": { 
		"16": "img/icon16.png",
        "48": "img/icon48.png",
        "128": "img/icon128.png" 
	},
	"browser_action": {
    	"default_icon": "img/icon32.png"
  	}
}
"""

css = """div.wall {
  max-width: 1500px;
  font-size: 14px;
}
.card {
  padding-top: 20px;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  background: white;
  transition: 0.3s;
  width: 20%;
  border-radius: 5px;
  height: 90%;
  display: inline-block;
  margin: 20px;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
  background-color: #d3f3ff
}

.cardimg { 
  border-radius: 5px 5px 0 0;
  max-width: 50%;
  height: 100%;
  max-height: 100px;
  padding-bottom: 5px;
}

.cardletter {
  height: 90px; 
  border-radius: 5px 5px 5px 5px; 
  padding-bottom: 5px; 
  width: 40%; 
  font-size: 75px; 
  color: white;
}

.container {
  padding-top: 5px;
  padding-bottom: 5px;
  background: #eeeeee;
  height: 100%;
}

.chip {
  font-size: 12px;
  display: inline-block;
  padding: 0 25px;
  height: 45px;
  line-height: 50px;
  border-radius: 25px;
  background-color: #f1f1f1;
  display: inline-block;
  margin: 20px;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
}

.chip:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
  background-color: #d3f3ff
}

.chip img {
  float: left;
  margin: 0 10px 0 -25px;
  height: 45px;
  width: 45px;
  border-radius: 50%;
  background-color: white;
}

.tag {
  position: absolute;
  padding-top: 5px;
  padding-bottom: 5px;
  background: #eeeeee;
  height: 100%;
}

body {
  margin: 0;
}

table { 
  table-layout: fixed; 
}

td { 
  width: 25%; 
}

a:link, a:visited { 
    color: black;
    text-decoration: none;
}

input[type=text] {
    width: 80%;
    box-sizing: border-box;
    border: 2px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
    background-color: white;
    background-image: url('img/g.png');
    background-position: 10px 10px; 
    background-size: 20px auto;
    background-repeat: no-repeat;
    padding: 12px 20px 12px 40px;
}
"""

html_start = """<!DOCTYPE html>
<html><head><title>New Tab</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
</head>
<body><center>
  <div style="padding-top:20px; padding-bottom:5px; background:#229dcc" align="center">
    <img src="img/header.png">
  </div>
  <div style="background:linear-gradient(to bottom, #229dcc , white); height:20px"></div>
  <div style="background-color: white; height:10px"></div>
  <div class="wall">"""

html_end = """ <div style="background-color: white; height:50px"></div>
  </div>
</center>
</body></html> 
"""


def random_color():
    r = lambda: random.randint(0, 240)
    return '#%02X%02X%02X' % (r(), r(), r())


def get_image_name(name,alt_image):
    if alt_image is None or not alt_image:
        img_name = "img/" + name.replace(' ','').lower() + '.png'
    else:
        img_name = "img/" + alt_image
    if os.path.isfile(img_name):
        return img_name
    else:
        return None


def html_chip(chip_name,url,image_name):
    if image_name is None or not image_name:
        img = ''
    else:
        img =  """<img src="{image_name}">""".format(image_name=image_name)
    return """<div class="chip"><a href="{url}">{img}{chip_name}</a></div>""".format(chip_name=chip_name,url=url,img=img)


def html_card(card_name,url,image_name):
    if image_name is None:
        img_html = """<div class="cardletter" style="background-color: {color}; ">{letter}</div><div style="height: 10px"></div>""".format(letter=card_name[0].upper(),color=random_color())
    else:
        img_html = """<img src="{image_name}" class="cardimg">""".format(image_name=image_name)
    return """<a href="{url}">
    <div class="card">
      {img_html}
      <div class="container" align="center">
        {card_name} 
      </div>
    </div></a>""".format(card_name=card_name,image_name=image_name,img_html=img_html,url=url)


def add_objects_to_file(file,csv_name,row_length,html_func):
    try:
        with open(csv_name, newline='') as csvf:
            reader = csv.reader(csvf)
            i = 0
            for row in reader:
                i = i + 1
                if len(row) < 2:
                    raise RuntimeError('CSV file must contain at lease two columns!')
                elif len(row) == 2:
                    alt_img = None
                else:
                    alt_img = row[2]
                name = row[0]
                image_name = get_image_name(name, alt_img)
                file.write(html_func(name, row[1], image_name))
                if i % row_length == 0 and i > 0:
                    file.write('<br>')
            if csv_name == 'cards.csv' and i % row_length != 0:
                while i % row_length != 0:
                    i = i + 1
                    file.write(html_func('&nbsp;','','img/blank.png'))
                file.write('<br>')
            if not (i - 1) % row_length == 0:
                file.write('<br>')
    except FileNotFoundError:
        print("CSV file {file} was not found".format(file=csv_name))

if __name__ == '__main__':
    with open('manifest.json','w') as f:
        f.write(manifest)
    with open('style.css','w') as f:
        f.write(css)
    with open('newtab.html','w') as f:
        f.write(html_start)
        add_objects_to_file(f,'chips.csv',8,html_chip)
        add_objects_to_file(f,'cards.csv',4,html_card)
        f.write(html_end)