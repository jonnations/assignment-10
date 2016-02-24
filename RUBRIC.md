## Task 1

Write a program to count word usage in the given text.  Have this program print out, in decreasing order (most common to least common) the 10 most common words and the count of each word used. As always, your program should contain a `main` loop and an `ifmain` statement, and it should be formatted correctly.  You should use a *standard* dictionary as part of your function(s) to accomplish this task (see Task 2, where you'll use a slightly different type of dictionary).

- [ ] Program is correctly formatted (0.5 pt)
- [ ] Program includes `main()` function and "ifmain" statement (0.5 pt)
- [ ] Program uses a dictionary to correctly count words in the text and returns correct words and their counts for the 10 most common words (4 pts.)

## Task 2

Using [Counter](https://docs.python.org/2/library/collections.html#collections.Counter) from the `collections` module, write a program to count word usage in the same text as above.  Have this program print out, in decreasing order (most common to least common) the 10 most common words and the count of each word used. As always, your program should contain a `main` loop and an `ifmain` statement, and it should be formatted correctly.

- [ ] Program is correctly formatted (0.5 pt)
- [ ] Program includes `main()` function and "ifmain" statement (0.5 pt)
- [ ] Program uses a `Counter` to correctly count words in the text and returns correct words and their counts for the 10 most common words (4 pts.)

## Task 3

Write a program that processess the given data to create a dictionary that maps the ExaML run name (e.g. ExaML_info.T6 as the `key`) to the ExaML log-likelihood value (e.g. -82924194.67 as the `value`). Use this function or a function that calls this function to prettily print the run name followed by the log-likelihood value in two column format to the screen.  Also include a function that sorts the log-likelihood values and helps us determine which run name minimizes the negative log likelihood value (e.g. the run name having the LL value closest to zero). Also output the name of this "best" run to the screen.

- [ ] Program is correctly formatted (0.5 pt)
- [ ] Program includes `main()` function and "ifmain" statement (0.5 pt)
- [ ] Program prints run name/LL in two column format and correctly sorts and reports the "best" ML result (4 pts.)
