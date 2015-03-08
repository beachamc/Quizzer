# Quizzer
a command line quizzing application to help with studying.

This is a quick tool I made up to help quiz myself for a class.

to run, just use `python driver.py` from the root directory.

Questions are put in text files in the /Quizzes folder in .txt files.

The format for a question is:

```
{
	Question goes here.
	answer on newline
	other answer on new line
	correct answer marked with number sign #
	any number of answers are fine
}
```

The script determines between true/false, fill in the blank, and multiple choice automatically.

```
{
	True statement here.
	True #
	False
}
```

Once you have the quizzes in the folder, you can select all by typing `all` or select them from the list as comma separated values.

This quizzer has a learning mode which automatically adds back in the questions you get incorrect so that you can learn them quicker. Just select `y` when prompted for learning mode.

