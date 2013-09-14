Pic-helper
==========

This repository is a collection of utility python scripts.

Description
---

It can assist to classify all file which produced by camera to the main four folder.

* **JPG** folder store JPEG files.
* **PNG** folder store PNG files.
* **RAW** folder store CR2 or NEF files.
* **MOV** folder store MOV, AVI files.

And it also can assist to pick out favorite photo or RAW to the Favorite_Pic folder.

Current content
---

 * **Pic_classify.py**

	Classify all files to main four folder.

 * **Pic_selector.py**

	Input image serial number to pick out favorite photo.

 * **RAW_selector.py**

	Input RAW serial number to pick favorite RAW.

Usage
---

* **For Windows User**
		
	**Need to install [Python interpreter] (http://www.python.org/getit/)**

	Copy these three python scripts to the folder which you want to classify.
	
	First run **Pic_classify.py** and all photo will be classified, and 
	
	switch to the \JPG or \RAW folder to run **Pic_selector.py** or **RAW_selector.py** to choose favorite photo.
	
	**OR**
	
	Just download the executable files I have wrapped.
	
	Download link at: https://mega.co.nz/#!hc1QxBaY!GN27zGD2X66aMCkEtU3SuErxuqAKJnEow1svSbvkZdw
	
	**This method does not require python intepreter.**
		

* **For OS X/Linux User**

	Copy these three python scripts to the folder which you want to classify.
	
	Use terminal and switch to the folder then type `$ python Pic_classify.py` photo will be classified.
	
	If you want to pick favorite photo just switch to the /JPG folder then type `$ python Pic_selector.py`
	
	or even pick favorite RAW files switch to the /RAW folder then type `$ python RAW_selector`.


Currently supported camera photo
----

* **Canon & Nikon DSLR**

* **Nikon Coolpix**

* **iPhone**

Author
------
John Lin. Email: ireri339@gmail.com


Copyright ©
-----
The MIT License (MIT)

Copyright (c) 2013 LIN CHE WEI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
