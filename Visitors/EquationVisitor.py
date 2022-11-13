from antlr4 import *
from Grammar.ProjectLexer import ProjectLexer
from Grammar.ProjectParser import ProjectParser
from Grammar.ProjectVisitor import ProjectVisitor

class UnexpectedError(Exception):
    pass

class EquationVisitor(ProjectVisitor):

    # Visit a parse tree produced by ProjectParser#equation.
    def visitEquation(self, ctx:ProjectParser.EquationContext):
        result = self.visitEquationChildren(ctx)
        return result

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


    # Visit a parse tree produced by ProjectParser#equation.
    def visitSum(self, ctx:ProjectParser.SumContext):
        result = self.visitSumChildren(ctx)
        return result

    # Visit children of a parse tree produced by ProjectParser#equation.
    def visitSumChildren(self, node):
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
                if(sign == "+"):
                    result = result + childResult
                elif(sign == "-"):
                    result = result - childResult
                else:
                    raise UnexpectedError("Addition/Subtraction sign was value other than '+', '-'")
                sign = None

        return result

    # Visit a parse tree produced by ProjectParser#factor.
    def visitFactor(self, ctx:ProjectParser.FactorContext):
        result = self.visitFactorChildren(ctx)
        return result

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

        return result

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

    # Visit a parse tree produced by ProjectParser#mult.
    def visitMult(self, ctx:ProjectParser.MultContext):
        return ctx.getText()


    # Visit a parse tree produced by ProjectParser#div.
    def visitDiv(self, ctx:ProjectParser.DivContext):
        return ctx.getText()


    # Visit a parse tree produced by ProjectParser#mod.
    def visitMod(self, ctx:ProjectParser.ModContext):
        return ctx.getText()


    # Visit a parse tree produced by ProjectParser#add.
    def visitAdd(self, ctx:ProjectParser.AddContext):
        return ctx.getText()


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