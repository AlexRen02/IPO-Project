TEMPORARY BRIEF RUNDOWN OF PROJECT
This project was created with the intentions of downloading stock market IPO data from the internet and organizing all of them in one collective chart. We are pulling data from Marketwatch.com and Nasdaw.com.
Currently, this chart will include closing, open, low, and high prices of the first day the stock was released.  In the future, this chart will be expanded upon to include more statistics as well as in-depth analysis on the data.

RESOURCES
Because the historical quotes of these IPOs are stored as an image on Market Watch, we will be converting the image to a text.  To accomplish this, we are using Google Tesseract, an OCR engine with support for unicode and can recognize characters of over 100 languages. In addition, we are also using Python Pillow to handle processing images from a url.
The data for the historical quotes are actually stored in the url themselves but in reverse order.  We could have simply done this project entirely with parsing strings but we took this chance to learn how to utilize and learn more about Optical Character Recognition(OCR) libraries as well as handling urls.

FUTURE
We have plans to expand this project into a website that will be a compilation of past IPOS and will automatically update with new entries into the market.  Even more features will include listing upcoming IPOs to keep visitors updated and technical analysis to better inform visitors on what they are seeing.
