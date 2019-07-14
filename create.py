import yaml
import os.path

manifest = """{
	"name": "New Tab",
	"version": "1.0",
	"description": "New Tab",
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
  max-width: 1800px;
  font-size: 14px;
}
.card {
  padding-top: 20px;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  background: white;
  transition: 0.3s;
  width: 15%;
  border-radius: 5px;
  height: 90%;
  display: inline-block;
  margin: 20px;
  position: relative;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
  background-color: #d3f3ff
}

.cardimg { 
  border-radius: 5px 5px 0 0;
  max-width: 70%;
  height: 100%;
  max-height: 100px;
  padding-bottom: 5px;
  position: relative;
}

.cardbg {
  position: absolute; 
  width: 100%; 
  height: 100%; 
  top: 0px; 
  left: 0px;
}

.cardletter {
  height: 90px; 
  border-radius: 5px 5px 5px 5px; 
  padding-bottom: 5px; 
  width: 45%; 
  font-size: 75px; 
  color: white;
}

.dropdown {
  position: absolute; 
  right: 0px; 
  top: 0px;
  z-index: 1;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown:hover .dropdownarrow  {
  background-color: #96ffcc;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f1f1f1;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}

.dropdown-content-item {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.container {
  padding-top: 5px;
  padding-bottom: 5px;
  background: #eeeeee;
  height: 100%;
  position: relative;
}

.chip {
  font-size: 12px;
  padding: 0 25px;
  height: 45px;
  line-height: 50px;
  border-radius: 25px;
  background-color: transparent;
  display: inline-block;
  position: relative;
}

.chip-wrapper {
  font-size: 12px;
  height: 45px;
  line-height: 50px;
  border-radius: 25px;
  background-color: #f1f1f1;
  display: inline-block;
  position: relative;
  margin: 20px;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  z-index: 110;
}

.chip-wrapper:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
  background-color: #d3f3ff
}

.chip-wrapper:hover .dropdown-content {
  display: block;
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


def get_color_by_string(s):
    u = sum([ord(c) for c in s.upper()])
    l = sum([ord(c) for c in s.lower()])
    return '#%02X%02X%02X' % (u % 255, l % 255, ord(s[0]) % 255)


def get_image_name(name,alt_image):
    if alt_image is None or not alt_image:
        img_name = "img/" + name.replace(' ','').lower() + '.png'
    else:
        img_name = "img/" + alt_image
    if os.path.isfile(img_name):
        return img_name
    else:
        return None


def html_chip(chip_name, url, image_name, dropdown):
    if image_name is None or not image_name:
        img = ''
    else:
        img = """<img src="{image_name}">""".format(image_name=image_name)
    if not url:
        href = ''
    else:
        href = 'href="{url}"'.format(url=url)
    if dropdown is None or not dropdown:
        dropdown_html = ''
    else:
        dropdown_html = """<div class="dropdown-content" style="top: 45px; line-height: 10px">"""
        for item in dropdown:
            if item == '_':
                dropdown_html += """<hr>"""
            else:
                k = list(item.keys())[0]
                dropdown_html += """\n<a class="dropdown-content-item" href="{url}">{name}</a>""".format(name=k ,url=item[k])
        dropdown_html += """\n</div>"""
    return """<div class="chip-wrapper">{dropdown_html}<a {href}><div class="chip">{img}{chip_name}</div></a></div>""".format(chip_name=chip_name,href=href,img=img,dropdown_html=dropdown_html)


def html_card(card_name, url, image_name, dropdown, idx):
    if card_name is None:
        card_name = '&nbsp;'
        container_additional = 'style="background-color: transparent;"'
    else:
        container_additional = ''
    if image_name is None:
        img_html = """<div class="cardletter" style="background-color: {color}; ">{letter}</div><div style="height: 10px"></div>""".format(letter=card_name[0].upper(), color=get_color_by_string(card_name))
    else:
        img_html = """<img src="{image_name}" class="cardimg">""".format(image_name=image_name)
    if idx is not None:
        z_index = 100 - idx
    else:
        z_index = 0
    if not url:
        href = ''
    else:
        href = 'href="{url}"'.format(url=url)
    if not dropdown:
        dropdown_html = ''
    else:
        dropdown_html = """<div class="dropdown"><img src="img/dropdown.png" class="dropdownarrow"><div class="dropdown-content">"""
        for item in dropdown:
            if item == '_':
                dropdown_html += """<hr>"""
            else:
                k = list(item.keys())[0]
                dropdown_html += """\n<a class="dropdown-content-item" href="{url}">{name}</a>""".format(name=k ,url=item[k])
        dropdown_html += """\n</div></div>"""
    return """<div class="card" style="z-index: {z_index};">
      {dropdown_html}
      <a {href}><img src="img/blank.png" class="cardbg" >{img_html}
      <div class="container" align="center" {container_additional}>
        {card_name} 
      </div></a>
    </div>""".format(card_name=card_name,image_name=image_name,img_html=img_html,href=href,
                     dropdown_html=dropdown_html,z_index=z_index,container_additional=container_additional)


def get_element_name(element):
    name = list(element.keys())
    try:
        name.remove('image')
    except ValueError:
        pass
    try:
        name.remove('more')
    except ValueError:
        pass
    if len(name) > 1:
        raise RuntimeError('Ambiguous name: {}'.format(name))
    else:
        return name[0]


def add_chips_to_file(file):
    filename = 'chips.yml'
    try:
        with open(filename, 'r') as yml:
            data = yaml.safe_load(yml)
            row_length = 8
            i = 0
            for element in data:
                i = i + 1
                alt_img = element.get('image', None)
                name = get_element_name(element)
                image_name = get_image_name(name, alt_img)
                file.write(html_chip(chip_name=name, url=element[name], image_name=image_name,
                                     dropdown=element.get('more', None)))
                if i % row_length == 0 and i > 0:
                    file.write('<br>')
            if not i % row_length == 0:
                file.write('<br>')
    except IOError:
        print("{file} was not found".format(file=filename))
    except Exception as e:
        print('An error occurred while parsing {file}:'.format(file=filename))
        print(e)


def add_cards_to_file(file):
    filename = 'cards.yml'
    try:
        with open(filename, 'r') as yml:
            data = yaml.safe_load(yml)
            row_length = 4 if len(data) <= 16 else 5
            i = 0
            for element in data:
                i = i + 1
                alt_img = element.get('image', None)
                name = get_element_name(element)
                image_name = get_image_name(name, alt_img)
                file.write(html_card(card_name=name, url=element[name], image_name=image_name,
                                     dropdown=element.get('more', None), idx=i))
                if i % row_length == 0 and i > 0:
                    file.write('<br>')
            if i % row_length != 0:
                while i % row_length != 0:
                    i = i + 1
                    file.write(html_card(None, None, 'img/blank.png', {}, idx=None))
                file.write('<br>')
            if not i % row_length == 0:
                file.write('<br>')
    except IOError:
        print("{file} was not found".format(file=filename))
    except Exception as e:
        print('An error occurred while parsing {file}:'.format(file=filename))
        print(e)


if __name__ == '__main__':
    with open('manifest.json','w') as f:
        f.write(manifest)
    with open('style.css','w') as f:
        f.write(css)
    with open('newtab.html','w') as f:
        f.write(html_start)
        add_chips_to_file(f)
        add_cards_to_file(f)
        f.write(html_end)
