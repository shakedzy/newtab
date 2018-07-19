# New Tab Extension for Chrome

![screenshot](desc/screenshot.png)

## Installation:
* Extract all files to any directory
* In Chrome, go to [`chrome://extensions`](chrome://extensions)
* Enable _Developer Mode_
* Click _Load Unpacked_ and choose the directory you placed the files in

## Creating custom tabs:
Follow the instructions below and use the `create.py` script.


**Note:** The script used requires Python 3.x

### Configuring links:
Two CSV files are used required (you can also have just one): `chips.csv` and 
`cards.csv`, where Chips are the small links at the top and Cards are the big ones 
underneath them (see screen-shot above).

Both CSV files have the same syntax: `name,url`. For example:
``` 
HBO,http://www.hbo.com
Netflix,http://www.netflix.com
``` 

### Configuring images:
The script automatically look for an image named `img/[name].png`, where `[name]`
is the name defined in the CSV file (lowered-case and with no spaces, so for `HBO`
it will look for an image named `img/hbo.png` and for `Big Query` it will look
for `img/bigquery.png`). If no such image is found, then no image will be used for 
Chips, and a colored square with the first letter will be used for Cards (see the
rightmost card on the second row in the screen-shot).

**Defining alternative images:** You can specify an alternative image file instead
of the one looked for by default. To do so, add the image file-name as a third
column in the CSV file. For example, to define an alternative image for `Netflix`:
``` 
HBO,http://www.hbo.com
Netflix,http://www.netflix.com,nfx.jpg
``` 
This will make the script use the file `img/nfx.jpg`.

Note that all images are always stored in the `img/` directory.

### Running the script:
Assuming the files were placed in: `~/newtab/`, run:
```
cd ~/newtab
python3 create.py
``` 
There's no need to reinstall the extension.