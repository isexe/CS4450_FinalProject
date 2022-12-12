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

## Resources

1. <https://github.com/antlr/antlr4/blob/master/doc/index.md>
2. <https://tomassetti.me/listeners-and-visitors/>
3. <https://tomassetti.me/antlr-mega-tutorial/#chapter11>
4. <https://www2.southeastern.edu/Academics/Faculty/kyang/2018/Summer/CMPS401/ClassNotes/CMPS401ClassNotesChap03.pdf>
5. <https://stackoverflow.com/questions/9726620/how-can-i-differentiate-between-reserved-words-and-variables-using-antlr>
6. <https://stackoverflow.com/questions/34368305/antlr-calculator-with-negative-numbers-support>
 

## Enviornment and set up

1. Requirements
	* The Java sdk version we used was 19.0.1
	* The antlr version we used was 4.11.1
	* The python3 version we used was 3.9.13
	* The antlr4.runtime version was 4.6.6

2. Parser Set up
    * Java SDK + Antlr library
	* Python3 + Antlr4.runtime
	* Aliases/Commands required for building language
        * The Aliases were needed for the parser to fild the required antlr files on our devices
            * Those aliases being something like: 
        * The command for building the parser language was [antlr4 -Dlanguage=Python3 -visitor Project.g4 -o Grammar]
        * The command for running our language ofter building it was [python3 Project.py --debugging=True] with the added debugging we used for our tests
            * Although since our testing phase is over the command would jst be [python3 Project.py]

3. Miscelaneous Information
	* In the construction of our parser, we used visitors instead of listeners
	* python file layout
	* debugging flag

## Checkpoints and Deliverables

Should discuss what was required, how it was achieved, etc

1. Deliverable #1: Arithmetic/Assignment Operators and Variable defenitions
	* Arithmetic Operators
	* Variables Operators
	* Assignment definitions

2. Deliverable #2: if/else Blocks and Conditional Statements
	* if/else Blocks
	* Conditional Statements

3. Deliverables #3: for/while Loops and comments
	* for Loops
        * 
    * while Loops
        * Programming the while loops wasn't all that complicated. It mostly consisted of relatively the same logic behind if statement grammar visitor code, only this time the code block would repeat unless the conditional statement was false.
	* Comments
        * 

4. Deliverables #4: Function Definitions and Calls
	* Function Implementations
	* Function Calls

5. Parse tree images
    * Deliverable #1 had a 
    * Deliverable #2 had a 
    * Deliverable #3 had a 
    * Deliverable #4 had a 