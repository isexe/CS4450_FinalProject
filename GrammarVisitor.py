from antlr4 import *
from Grammar.ProjectLexer import ProjectLexer
from Grammar.ProjectParser import ProjectParser
from Grammar.ProjectVisitor import ProjectVisitor

from Visitors.EquationVisitor import EquationVisitor
from Visitors.AssignVisitor import AssignVisitor

sampleDict = {
  "myVar" : {
              "Address" : "",
              "Value" : "",
              "Type" : "",
              "Lifetime" : "",
              "Scope" : ""
            }
}

class GrammarVisitor(ProjectVisitor):
    def __init__(self, debugging = False):
        self.debugging = debugging
    
    # Visit a parse tree produced by ProjectParser#code.
    # Next Node is Lines
    def visitCode(self, ctx:ProjectParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#lines.
    # Next Node is Statement
    def visitLines(self, ctx:ProjectParser.LinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#statement.
    # Will direct to visit parse rule
    # i.e. 1 + 1 will go to visitEquation next
    def visitStatement(self, ctx:ProjectParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#equation.
    def visitEquation(self, ctx:ProjectParser.EquationContext):
        result = EquationVisitor().visitEquation(ctx)

        # used to debug
        if(self.debugging):
            print("Equation:\n" + ctx.getText() + " = " + str(result))

        return result

    # Visit a parse tree produced by ProjectParser#assign.
    def visitAssign(self, ctx: ProjectParser.AssignContext):
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
        """if(ctx != None):
            val = self.visitExpression(ctx)
        
        val = None
        l_val = self.visitId(ctx)"""

        r_val = self.visitAssign_val(r_val)

        if l_val in sampleDict: 
            val = sampleDict[l_val]
        else:
            #create variable and insert into dict where key = l_val
            if r_val == None :
                value_type = "None"
            if isValidInt(r_val):
                value_type = "Int"
            elif isValidFloat(r_val):
                value_type = "Float"
            elif isValidBool(r_val): 
                value_type = "Bool"
            else:
                value_type = "String"

            sampleDict[str(l_val)] = { "Address" : "", "Value" : r_val, "Type" : value_type, "Lifetime" : "", "Scope" : ""}
            print(sampleDict[str(l_val)])


    def visitId(self, ctx: ProjectParser.EquationContext):
        return ctx.VAR()
    
    
    def visitAssign_val(self, ctx: ProjectParser.EquationContext):
        if(ctx == None):
            return ctx
        if(ctx.VAR()):
            assign_val = sampleDict[ctx.VAR()]
            #if not found raise Error
            return assign_val
        elif(ctx.ATOM()):
            val = str(ctx.ATOM())
            if(isValidInt(val)):
                val = int(val)
            elif(isValidFloat(val)):
                val = float(val)
            else:
                val = str(val)
        elif(ctx.equation != None):
            return EquationVisitor.visitEquation(ctx.equation)
            #print("need to find and import eq visitor, will need to pull from github")
        else:
            print("something is very wrong")
        
        #ill implement this later
        # if r_val is variable 
        #     val.Value = r_val.Value
        #     val.Type = r_val.Type
        # elif r_val is int, float, or string 
        #     val = r_val
        #     val.type = typeof(r_val)

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

def isValidBool(string: str):
    if string == "True" or string == "False":
        return True
    else:
        return False
