# Task 1

Here is a text description of [How Stars Age](http://bit.ly/1TyWglh), written using the ten hundred most common words (e.g. the [Up-Goer Five](http://splasho.com/upgoer5/) Challenge).

```
Stars burn a very light type of air that is packed very tight in the middle of the star. The tiny pieces of the air join to form a slightly heavier type of air that can't burn in the star without the middle being much hotter and tighter.

After a long time, all the very light air in the middle is used up. Then the star gets much hotter and tighter in the middle, so it can burn the slightly heavier air. It also also gets much bigger and cooler outside. But it is still so hot it will burn up any close-in worlds.

The sun is a star and will do this after a very long time. It will get so big that it will burn our world all up. This will not happen for at least ten hundred hundred hundred hundred years, so we don't have to worry about it now.

Long after that, a star like the sun will burn up all the slightly heavier air, too. Then it will become very tiny and hot and white, but will be so tiny it won't be able to keep its worlds warm. It will keep cooling off over a very very long time. The worlds that are left will be all ice.

But stars that are heavier can go on to burn heavier and heavier things, until finally they make the biggest flash we know. That is their end.
```

Write a program to count word usage in the text above.  Have this program print out, in decreasing order (most common to least common) the 10 most common words and the count of each word used. As always, your program should contain a `main` loop and an `ifmain` statement, and it should be formatted correctly.  You should use a *standard* dictionary as part of your function(s) to accomplish this task (see Task 2, where you'll use a slightly different type of dictionary).

# Task 2

There are several special types of dictionaries, including [ordereddict](https://docs.python.org/2/library/collections.html#collections.OrderedDict), [defaultdict](https://docs.python.org/2/library/collections.html#collections.defaultdict), and [Counter](https://docs.python.org/2/library/collections.html#collections.Counter).  In fact, [Counter](https://docs.python.org/2/library/collections.html#collections.Counter) is built expressly for tasks similar to the one that I've laid out, above.

Using [Counter](https://docs.python.org/2/library/collections.html#collections.Counter) from the `collections` module, write a program to count word usage in the same text as above.  Have this program print out, in decreasing order (most common to least common) the 10 most common words and the count of each word used. As always, your program should contain a `main` loop and an `ifmain` statement, and it should be formatted correctly.

# Task 3

Here are the same data from ExaML that you've seen before, although they are a little cleaner this time:

ExaML_info.T6\tLikelihood of best tree:\t-82924194.67
ExaML_info.T5\tLikelihood of best tree:\t-82924194.71
ExaML_info.T9\tLikelihood of best tree:\t-82924194.73
ExaML_info.T7\tLikelihood of best tree:\t-82924252.98
ExaML_info.T2\tLikelihood of best tree:\t-82924253.01
ExaML_info.T1\tLikelihood of best tree:\t-82924354.95
ExaML_info.T8\tLikelihood of best tree:\t-82924354.98
ExaML_info.T15\tLikelihood of best tree:\t-82924366.58
ExaML_info.T0\tLikelihood of best tree:\t-82924366.59
ExaML_info.T4\tLikelihood of best tree:\t-82924397.48
ExaML_info.T16\tLikelihood of best tree:\t-82924424.87
ExaML_info.T3\tLikelihood of best tree:\t-82924424.89
ExaML_info.T14\tLikelihood of best tree:\t-82924426.52
ExaML_info.T12\tLikelihood of best tree:\t-82924426.53
ExaML_info.T13\tLikelihood of best tree:\t-82924426.54
ExaML_info.T19\tLikelihood of best tree:\t-82924465.57
ExaML_info.T17\tLikelihood of best tree:\t-82924707.69
ExaML_info.T10\tLikelihood of best tree:\t-82925366.65
ExaML_info.T18\tLikelihood of best tree:\t-82925393.89
ExaML_info.T11\tLikelihood of best tree:\t-82925447.6

Write a program that processess these data to create a dictionary that maps the ExaML run name (e.g. ExaML_info.T6 as the `key`) to the ExaML log-likelihood value (e.g. -82924194.67 as the `value`). Use this function or a function that calls this function to prettily print the run name followed by the log-likelihood value in two column format to the screen like so:

ExaML_info.T6   -82924194.67
ExaML_info.T5   -82924194.71

Also write a function that sorts the log-likelihood values and helps us determine which run name maximizes the -log likelihood value (e.g. the run name having the value closest to zero). Also output the name of this "best" run to the screen.
