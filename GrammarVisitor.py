from antlr4 import *
from Grammar.ProjectLexer import ProjectLexer
from Grammar.ProjectParser import ProjectParser
from Grammar.ProjectListener import ProjectListener
from Grammar.ProjectVisitor import ProjectVisitor

class GrammarVisitor(ProjectVisitor):
    
    def visitExpression(self, ctx: ProjectParser.ExpressionContext):
        # used for debugging
        print("Visit Expression: " + str(ctx.getText()))

        #placeholders
        l_val = 0
        r_val = 0
        val = 0

        # main difference between listener and visitor is visitor must invoke visit to continue
        
        # check for nested expression
        if(ctx.expr != None):
            val = self.visitExpression(ctx.expr)

        # explore nodes
        if(ctx.left != None):
            l_val = self.visitExpression(ctx.left)
        if(ctx.right != None):
            r_val = self.visitExpression(ctx.right)

        # calculate this value
        if(ctx.MULT()):
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
            val = int(str(ctx.ATOM()))
        else:
            # shouldn't get into this statement, unless it's parenthesis
            if(ctx.expr == None):
                print("Issue with visit if checks")

        # return the value from this node
        return val