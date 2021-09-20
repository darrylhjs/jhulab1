


# Program for infix, prefix and postfix inter-conversion
##### 605.202 Lab 1: Choice 2
##### Submission by Darryl Hwang Jun Siang
---

This programme is written for the inter-conversion of infix, prefix and postfix notations. 

Please read the following instructions for the correct usage of the programme.

#### Running Instructions

1. Run 'main.py' in terminal.
```
$ python main.py
```

2. Enter the file name of the input file (see instructions below for formatting of input file).
```
Hello there! Please read README.txt before running this programme! 
Please enter the INPUT file name: example.txt
```
3. Enter the desired file name of the output file.
```
Please enter desired OUTPUT file name: output.txt
```
4. Allow program to run - an update is given after each string is processed.
```
Input 1: Done! 
 
Input 2: Done! 
 
Input 3: Done! 
```

5. Once completed, the following line should appear:
```
Done! Please check the output file, 'output.txt', for outputs!
```
6. Check output file for the converted output strings.
---
#### Formatting of input file

+ The input file should be a **.txt** file.
+ Each input should be written in a **single line**, with a space between each of the following elements.

+ **Notation number**
  + Use the notation number to indicate the type of notation for the input and output.
  + The legend for the notiation number is in following table:

| Notation number | Represented notation |
| ------ | ----------- |
| 0 | Infix |
| 1 | Prefix |
| 2 | Postfix |

+ **String**
  ++ Only use alphabets (e.g. A B C a b c) as operands.
  ++ Only include valid operands (+ - * / ^).
 
+ The following is the syntax for a line of input string:

```
[input-type][output-type] [string]
```

For example:
```
02 A/B+C^(D+E) # Convert infix to postfix
12 +^*AB/CD+EFG # Convert prefix to postfix
```
---
#### Output file
+ The output file will be created in the same directory as the program. 
+ Each output will include **(1) the input string** and **(2) the output string in the desired notation**.
---
#### Errors & Troubleshooting
+ Errors will be displayed in the OUTPUT file and the console.
+ Refer to the ERROR messages for troubleshooting/








