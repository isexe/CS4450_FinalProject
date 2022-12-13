# PoPL Final Project

## Description 

In this project, we are implementing a parser for a language similar to Python using Context-free Grammar (CFG) with ANTLR.

## Our Team

[Insert Team Name Here]

## Members

1. Isaac Sexe (aka. isexe)
2. Ryan Kramer (aka. monkey2987)
3. Devin Hackman (aka. bardfighter)
4. Manas Katta (aka. ManasKatta)

## Programming Language

Python

## GitHub Repository

<https://github.com/isexe/CS4450_FinalProject> 

## Environment and Setup

1. Required Software
	* Java JDK version 19.0.1
	* Antlr version 4.11.1
	* Python3 version 3.9.13
	* Antlr4-Python3-Runtime version 4.6.6

For the software above, it may be okay to use a newer version, but this is the only supported configuration we tested.

2. Antlr Setup

The first part of using Antlr is setting up the general Antlr environment.  Start by installing the [Java JDK](https://www.oracle.com/java/technologies/downloads/).  After installing it ensure its directory is accessible from your system's PATH.  After that, install [Antlr](https://www.antlr.org/download.html) targeted for Python3.  This should be placed in the Java JDK's directory in a folder called lib and the package should be added to your's CLASSPATH variable.  Optionally you can set up these two aliases in Linux:
```
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9.3-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.9.3-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'
```
Or set up two batch files in Windows
```
// create antlr4.bat  
java org.antlr.v4.Tool %* 
// create grun.bat  
java org.antlr.v4.gui.TestRig %*
// need to be stored somewhere in path
```
These are two common commands used while using developing Antlr and should be created if you plan on adding to this project.

The second part of using Antlr is setting up Antlr for the targetted language.  This will be different depending on which language you want to develop in, but since we used python the steps will be included.  First, ensure you have [python3](https://www.python.org/downloads/) installed and it's on your system's PATH.  After that use the pip command to install antlr4 runtime.
```
// install the latest version of runtime
pip install antlr4-python3-runtime
// or install the version used during development
pip install antlr4-python3-runtime=4.6.6
```

At this point, you should be ready to either use or further develop our language.  If you used different versions of the software than what we used you will need to regenerate the Grammar for it to work properly.  Below are some snippets of commands that you might use while working with our Grammar.
```
// generate a new Grammar
antlr4 -visitor <grammar-file>
// generate our Grammar
antlr4 -Dlanguage=Python3 -visitor Project.g4 -o Grammar

// generate a parse tree
grun <grammar-name> <rule-to-test> -gui -tokens
// generate our parse tree
grun Project.g4 code -gui -tokens

// run the generated Grammar
python3 Project.py
// or with the debugging flag
python3 Project.py --debugging=True
// this outputs some generic information that was used during our testing
```

A common issue we encountered while setting up our environments is having conflicting versions of Antlr and Antlr4.Python3.Runtime.  This would allow us to generate a new Grammar, but it would return an error about incorrect serialization version when running the python file.

If you have any other questions or concerns about the installation process please use the [Antlr Mega Tutorial](https://tomassetti.me/antlr-mega-tutorial/).  It's a massive guide about how to install and get started with Antlr and it was very helpful during the development of this project.

## Checkpoints and Deliverables

1. Deliverable #1: Arithmetic/Assignment Operators and Variable definitions

Arithmetic operators support addition, subtraction, multiplication, division, modulo, exponents, square roots, and parenthesis.  It was implemented in the Grammar as a mixture of parser and lexer rules.  The main rule is the equation parser rule.  This rule is laid out so that it naturally follows the orders of operation by having higher precedence operations nested in lower precedence operations.  A visitor was set up to find the left value and right value of an equation and apply the operator to them, it would then return the results.

Variable definitions were implemented as a lexer rule in the Grammar so that they reflected Pythons variable naming conventions.  There wasn't too much independent Python since it was a lexer rule and instead was utilized in the arithmetic operators class and the assignment class.

Assignment operators support equals signs, as well as arithmetic assignments like plus-equals and others.  It was implemented as a mixture of parser and lexer rules.  The main rule is the assign parser rule which is composed of an id, an assignment operator, and an assignment value.  A visitor class called AssignVisitor was implemented to find the id and either create or update a variable to the assign_val and store the result in our variable dictionary called varDict.

2. Deliverable #2: if/else Blocks and Conditional Statements

Conditional statements support logic operators and conjunctions.  It was implemented as a mixture of parser and lexer rules.  The main rule is the logicExpr rule.  This rule is right-recursive and allows for statements that have any amount of conditional statements connected by logical conjunctions.  A visitor class called visitLogicExpr was used to find the logical value of each conditional statement and returns the final result.

If/Else blocks support a single if statement, followed by any number of optional elif statements, followed by an optional else statement.  It was implemented as a mixture of parser and lexer rules.  The main rule is the ifBlseBlock parser rule.  A visitor class called visitIfElseBlock was used to interpret the parse tree.  It would start by interpreting the ifStatement rule, if the logicExpr in it returned true, it would perform the code in the ifElse code block.  If it wasn't true, the visitor would continue to look through the ifElseBlock's children until one of them returns true, meaning it ran its code.  If no statement returns true, the elseStatement is performed.

3. Deliverables #3: for/while Loops and comments

For loops were similiar to while loops in the sense that the actual looping part of the code was relatively easy to implement. The main differences from a while loop were having to implement the range function, which had to be able to handle 1, 2, and 3 parameters to cover all of the different cases and contexts in which the range funciton can be used. We also had to make sure that we were properly defining the loop variable that is in the definintion on the loop.

Programming the while loops wasn't all that complicated. It mostly consisted of relatively the same logic behind if statement Grammar visitor code, only this time the code block would repeat unless the conditional statement was false.

Comments support inline comments only since Python only supports those.  Comments have a lexer rule that states any characters that follow a # are skipped.  Currently, only certain characters such as alphanumerical and popular punctuations are supported so in the future this could be improved to include all possible UTF-8 characters.

4. Deliverables #4: Function Definitions and Calls

In python, functions are stored as variables, so we wanted to keep that implementation the same in our parser. Our function definition function finds all of the parameters in the function defintion passed to it from the user and stores them in an array. It then takes that array and the ctx.FunctionCode and stores that in an object that can then be stored in the variable dictionary, with the key being the name of the function

Our function calls work by getting the object stored in the variable dictionary and making a local copy of it that can be used to turn all of the parameter names into variable themselves that can be used to run the code stored within the function

5. Parse tree images

We've included some images of parse trees generated by grun [here](./Images/).  We tried including an example of a 'simple' and 'complex' tree when applicable for each new function implemented.  If you are having trouble understanding the parse tree or how our Grammar works, these images may help.

## Demo Video

## Helpful Resources

1. <https://github.com/antlr/antlr4/blob/master/doc/index.md>
2. <https://tomassetti.me/listeners-and-visitors/>
3. <https://tomassetti.me/antlr-mega-tutorial/#chapter11>
4. <https://www2.southeastern.edu/Academics/Faculty/kyang/2018/Summer/CMPS401/ClassNotes/CMPS401ClassNotesChap03.pdf>
5. <https://stackoverflow.com/questions/9726620/how-can-i-differentiate-between-reserved-words-and-variables-using-antlr>
6. <https://stackoverflow.com/questions/34368305/antlr-calculator-with-negative-numbers-support>