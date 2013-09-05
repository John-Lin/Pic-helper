Pic-helper
==========

This repository is a collection of utility python scripts.

Description
---

It can assist to classify all image files to main four folder.

* **JPG** folder store JPEG files.
* **PNG** folder store PNG files.
* **RAW** folder store CR2 or NEF files.
* **MOV** folder store video files.

And it also can assist to pick favorite pictures or RAW to the Favorite_Pic folder.

Current content
---

 * **Pic_classify.py**

	Classify all files to main four folder

 * **Pic_selector.py**

	Input image serial number to pick favorite pictures.

 * **RAW_selector.py**

	Input RAW serial number to pick favorite RAW

Usage
---

* **For Windows**
		
	**Need to install [Python interpreter] (http://www.python.org/getit/)**

	Then copy these 3 python scripts to the folder which you want to classify.
	
	First run **Pic_classify.py** and all image will be classified.
	
	Switching to JPG or RAW folder to run **Pic_selector.py** or **RAW_selector.py** to choose favorite pictures.
	
	**OR**
	
	Just download the executable files I have wrapped.
	
	Download link at: https://mega.co.nz/#!hc1QxBaY!GN27zGD2X66aMCkEtU3SuErxuqAKJnEow1svSbvkZdw
	
	**This method does not require python intepreter.**
		

* **For OS X/Linux**

	Copy these 3 python scripts to the folder which you want to classify.
	
	Use terminal and switch to the folder then type `$ python Pic_classify.py` it will be classified.
	
	If you want to pick favorite pictures just switch to /JPG folder type `$ python Pic_selector.py`.
	
	RAW files `$ python RAW_selector` and so on.


Currently supports camera pictures
----

* All DSLR **Canon** & **Nikon**

* **Nikon Coolpix**

* **iPhone**

Author
------
John Lin. Email: ireri339@gmail.com
