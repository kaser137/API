# Bitly URL shortener

This project allows to get access to the bit.ly API .Creates a console tool that shortens links. 
Counts transitions. If you input URL, it returns shorten link, if you input shorten link, 
it returns sum of transitions this link.

### How to install

You should register on the Bitly.com, then you have to get GENERIC ACCESS TOKEN
(it looks like: 17c09e20ad155405123ac1977542fecf00231da7), then, in project directory, 
you must create file: .env, for storage value of gotten token, and write in this file: 
BITLY_TOKEN={value of your token}(for example:17c09e20ad155405123ac1977542fecf00231da7).

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
For running program, you have to type in terminal from project directory:
```
py(or python) main.py [URL or shorten link]
```
### Project Goals

This code was written for educational purposes as part of an online course 
for web developers at [dvmn.org](https://dvmn.org/).
