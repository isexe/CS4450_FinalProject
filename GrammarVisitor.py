from antlr4 import *
from Grammar.ProjectLexer import ProjectLexer
from Grammar.ProjectParser import ProjectParser
from Grammar.ProjectListener import ProjectListener
from Grammar.ProjectVisitor import ProjectVisitor

class GrammarVisitor(ProjectVisitor):
    
    def visitExpression(self, ctx: ProjectParser.ExpressionContext):
        if(ctx == None):
            return None

        # used for debugging/printing tree
        tab = '    '
        tab = (ctx.depth()-1) * tab
        print(tab + str(ctx.getText()))

        #placeholders
        l_val = None
        r_val = None
        val = None

        # main difference between listener and visitor is visitor must invoke visit to continue
        
        # check for nested expression
        if(ctx.expr != None):
            val = self.visitExpression(ctx.expr)

        # explore nodes
        l_val = self.visitExpression(ctx.left)
        r_val = self.visitExpression(ctx.right)

        # calculate this value
        if(ctx.EXPON()):
            val = l_val ** r_val
        elif(ctx.MULT()):
            val = l_val * r_val
        elif(ctx.DIV()):
            val = l_val / r_val
        elif(ctx.MOD()):
            val = l_val % r_val
        elif(ctx.ADD()):
            val = l_val + r_val
        elif(ctx.SUB()):
            val = l_val - r_val
        elif(ctx.ATOM()):
            # if at terminal convert ATOM to valid value
            val = str(ctx.ATOM())
            if(isValidInt(val)):
                val = int(val)
            elif(isValidFloat(val)):
                val = float(val)
            else:
                val = str(val)
        else:
            # shouldn't get into this statement, unless it's parenthesis
            if(ctx.expr == None):
                print("ERROR: Visit didn't match any expected value.")

        # return the value from this node
        return val

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