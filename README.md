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

And it also can assist to pick favorite photo or RAW to the Favorite_Pic folder.

Current content
---

 * **Pic_classify.py**

	Classify all files to main four folder.

 * **Pic_selector.py**

	Input image serial number to pick favorite photo.

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
