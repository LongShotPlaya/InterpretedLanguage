Grammar
Make sure to follow your strokes with commas (like you would use semicolons in most programming languages) in order to proceed to the next line. If you don't, following lines will be ignored (but still error-checked). The only other major thing is that I didn't get around to making numerical strokes work, so you'll only really be able to do things through a few built-in function calls. The strokes you can use are:

swim(arg1 [, arg2]*) -- works very similarly to "print" in Python
classify(lit) -- gets the type of a literal
speak([prompt]) -- just "input()" from Python, but with an optional prompt to give the user before collecting input
reverse(str) -- takes an input string and returns it reversed
repeat(str, count) -- takes an input string and returns it repeated "count" times
blah(lit) -- casts a literal to the "blah" data type
number(lit) -- casts a literal to the "number" data type
mathynum(lit) -- casts a literal to the "mathynum" data type
by(arg1, arg2) -- multiplies two terms together
Keep in mind that the strokes don't actually pay too much attention to how many arguments you pass in, so for strokes which don't take an infinite number of parameters, extras will just be ignored (but still error-checked).

Data Types
blah -- String
booboo -- Boolean
yea -- True
nay -- False
mathynum -- Float
number -- Integer
weapon -- Function