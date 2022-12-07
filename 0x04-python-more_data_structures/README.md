If Guido van Rossum, the author of the programming language Python, had got his will, this chapter would have been missing in our tutorial. In his article from May 2005 "All Things Pythonic: The fate of reduce() in Python 3000", he gives his reasons for dropping lambda, map(), filter() and reduce(). He expected resistance from the Lisp and the scheme "folks". What he didn't anticipate was the rigidity of this opposition. Enough that Guido van Rossum wrote hardly a year later: "After so many attempts to come up with an alternative for lambda, perhaps we should admit defeat. I've not had the time to follow the most recent rounds, but I propose that we keep lambda, so as to stop wasting everybody's talent and time on an impossible quest." We can see the result: lambda, map() and filter() are still part of core Python. Only reduce() had to go; it moved into the module functools.

His reasoning for dropping them is like this:

There is an equally powerful alternative to lambda, filter, map and reduce, i.e. list comprehension
List comprehension( is more evident and easier to understand
Having both list comprehension and "Filter, map, reduce and lambda" is transgressing the Python motto "There should be one obvious way to solve a problem"
