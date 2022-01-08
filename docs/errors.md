
# ERORES

.\scraping.py:6: GuessedAtParserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if 
you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 6 of the file .\scraping.py. To get rid of this warning, pass the additional argument 'features="lxml"' to the BeautifulSoup constructor.  

  soup = BeautifulSoup(content, 'html')

Traceback (most recent call last):
  File ".\scraping.py", line 9, in <module>
    name = videos.find_all('a').text
  File "C:\Users\Andres\AppData\Local\Programs\Python\Python38\lib\site-packages\bs4\element.py", line 2253, in __getattr__
    raise AttributeError(
AttributeError: ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?

**COMENTARIO** NO Se si estan traqueados en git, o registrados.
