# bible-scraper
 scrape specific chapters of the bible and output to txt as a list

 replace "book" and "chapter" variables with the book name and chapter number *AS A STRING*
 Note: Books such as "John 2" will require the "2" to be assigned to the "booknum" var

 for instance
 book = "John"
 chapter = "1"
 booknum = ""

 as of now there arent really any error checks so if you enter a value that doesnt exist you will feel the wrath.

 But as long as the book and chapters you are looking for exist youshouldnt run into anyproblems

 this will output the entire first chapter of John 2 as a txt file named John1.txt

if you want the output to save as a string rather than a list, assign "as_array" to false

 after changing the variables you just need to run bible_scraper.py

 and that's it.

 definitely more you can do with it if you tweak the link, but i will add more features in the future such as comand line arguments, and change the translation. All can be done manually but i plan to make it more dynamic
