# Capstone project 

## Introduction

The goal is to count the number of times a given author appears in a
bibliography stored in a spreadsheet.

We can't use bash commands, like `cut`and `wc`, because the author field in
file in the spreadsheet uses commas to separate names in multi-author papers.

> Take a look to the spreadsheet with `cat` or `head -5` to sneak peak into
> the spreadsheet

## Solution

The author with more papers is 'Bengio' at 261 counts.

## Challenges

-Why the "O'Reilly" has double quotes while 'McClelland' has single quotes?
-Modify the script to solve ties, i.e. when several authors have the same
number of publications. You could defensive programming here: 
    -make a new test case with just two rows from the biblio with one author papers. 
    -modify the bash script to trun both test cases.
    -modify the python script until you get both names for the tie.
