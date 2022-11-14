from antlr4 import *
from Grammar.ProjectLexer import ProjectLexer
from Grammar.ProjectParser import ProjectParser
from Grammar.ProjectVisitor import ProjectVisitor

class UnexpectedError(Exception):
    pass

class EquationVisitor(ProjectVisitor):

    # Step 1: 
    # Visit a parse tree produced by ProjectParser#equation.
    def visitEquation(self, ctx:ProjectParser.EquationContext):
        result = self.visitEquationChildren(ctx)
        return result

    # Step 1.5:
    # Visit the children of a parse tree produced by ProjectParser#equation.
    def visitEquationChildren(self, node):
        # Since we know equation only has 1 child just get it
        c = node.getChild(0)
        result = str(c.accept(self))
        
        if(isValidInt(result)):
            result = int(result)
        elif(isValidFloat(result)):
            result = float(result)

        return result


    # Step 2:
    # Visit a parse tree produced by ProjectParser#sum.
    def visitSum(self, ctx:ProjectParser.SumContext):
        result = self.visitSumChildren(ctx)
        return result

    # Step 2.5:
    # Visit children of a parse tree produced by ProjectParser#sum.
    def visitSumChildren(self, node):
        result = None
        sign = None
        n = node.getChildCount()
        for i in range(n):
            # get child then visit them
            c = node.getChild(i)
            childResult = str(c.accept(self))

            # We know at this point the value we have is a int, float, str
            # try guessing the value and going with the first valid option
            if(isValidInt(childResult)):
                childResult = int(childResult)
            elif(isValidFloat(childResult)):
                childResult = float(childResult)

            # if result is none just set it to the first value we found
            if(result == None):
                result = childResult
            # if sign is none then the current child should be a sign operator
            elif(sign == None):
                sign = childResult
            else:
                # find what the sign is and apply it to result and childResult
                if(sign == "+"):
                    result = result + childResult
                elif(sign == "-"):
                    result = result - childResult
                else:
                    # Catch any signs that shouldn't be present
                    raise UnexpectedError("Addition/Subtraction sign was value other than '+', '-'")
                # reset sign value so we know it's next
                sign = None
        print(result)
        return result

    # Step 3:
    # Visit a parse tree produced by ProjectParser#factor.
    def visitFactor(self, ctx:ProjectParser.FactorContext):
        result = self.visitFactorChildren(ctx)
        return result

    # Step 3.5
    # functions identically to sum
    # Visit children of a parse tree produced by ProjectParser#factor.
    def visitFactorChildren(self, node):
        result = None
        sign = None
        n = node.getChildCount()
        for i in range(n):
            c = node.getChild(i)
            childResult = str(c.accept(self))
            
            if(isValidInt(childResult)):
                childResult = int(childResult)
            elif(isValidFloat(childResult)):
                childResult = float(childResult)

            if(result == None):
                result = childResult
            elif(sign == None):
                sign = childResult
            else:
                if(sign == "*"):
                    result = result * childResult
                elif(sign == "/"):
                    result = result / childResult
                elif(sign == "%"):
                    result = result % childResult
                else:
                    UnexpectedError("Multiplication/Division/Modulo sign was value other than '*', '/', '%'")
                sign = None

        print(result)
        return result

    # Step 4
    # This step will either return an ATOM or VAR if the equation is done
    # Or another equation if there is some nested in paranthesis
    # Visit a parse tree produced by ProjectParser#val.
    def visitVal(self, ctx:ProjectParser.ValContext):
        # is variable
        if(ctx.VAR()):
            pass
        # is atom value
        elif(ctx.ATOM()):
            return ctx.ATOM()
        # is equation so continue
        else:
            return self.visitValChildren(ctx)
    
    # Step 4.5 
    # nested equation
    # Visit the children of a parse tree produced by ProjectParser#val.
    def visitValChildren(self, node):
        # since we know the only time this is called is when Val = '(' sum ')' just get value of sum
        c = node.getChild(1)
        result = str(c.accept(self))
        
        if(isValidInt(result)):
            result = int(result)
        elif(isValidFloat(result)):
            result = float(result)

        return result

    # This will get the '*' operator
    # Visit a parse tree produced by ProjectParser#mult.
    def visitMult(self, ctx:ProjectParser.MultContext):
        return ctx.getText()

    # This will get the '/' operator
    # Visit a parse tree produced by ProjectParser#div.
    def visitDiv(self, ctx:ProjectParser.DivContext):
        return ctx.getText()

    
    # This will get the '%' operator
    # Visit a parse tree produced by ProjectParser#mod.
    def visitMod(self, ctx:ProjectParser.ModContext):
        return ctx.getText()

    # This will get the '+' operator
    # Visit a parse tree produced by ProjectParser#add.
    def visitAdd(self, ctx:ProjectParser.AddContext):
        return ctx.getText()

    # This will get the '-' operator
    # Visit a parse tree produced by ProjectParser#sub.
    def visitSub(self, ctx:ProjectParser.SubContext):
        return ctx.getText()

def isValidInt(string: str):
    try:
        int(string)
        return True
    except:
        return False

def isValidFloat(string: str):
    try:
        float(string)
        return True
    except:
        return False