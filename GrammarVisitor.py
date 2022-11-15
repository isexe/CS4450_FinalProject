from antlr4 import *
from Grammar.ProjectLexer import ProjectLexer
from Grammar.ProjectParser import ProjectParser
from Grammar.ProjectVisitor import ProjectVisitor

from Visitors.EquationVisitor import EquationVisitor
from Visitors.AssignVisitor import AssignVisitor

sampleDict = {
  "myVar" : {
              "Address" : "",   # ?
              "Value" : "",     # value of var
              "Type" : "",      # type(dict["Value"])
              "Lifetime" : "",  # ?
              "Scope" : ""      # ?
            }
}

# need to serialize this into a json or something else so we can access from other visitors
varDict = {}

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
        # tab = '    '
        # tab = (ctx.depth()-1) * tab
        # print(tab + str(ctx.getText()))

            #placeholders
        val = None
        value_type = None

        l_val = self.visitId(ctx.left)
        r_val = self.visitAssign_val(ctx.right)

        if(type(r_val) is dict):
            # r_val is a variable passed in, need to handle it
            # for now just set r_val to value of variable
            r_val = r_val.get("Value")

        if(r_val == None):
            r_val = None
        else:
            r_val = str(r_val)
            if(isValidInt(r_val)):
                r_val = int(r_val)
            elif(isValidFloat(r_val)):
                r_val = float(r_val)
            elif(isValidBool(r_val)):
                r_val = bool(r_val)
            else:
                r_val = str(r_val)

        # check if variable already defined
        if l_val in varDict: 
            val = varDict[l_val]

        #create variable and insert into dict where key = l_val
        value_type = type(r_val)
        
        # if the variable is previously defined
        if(val != None):
            op = ""
            try:
                if(ctx.PLU_EQU)():
                    op = "+="
                    val['Value'] += r_val
                elif(ctx.MIN_EQU()):
                    op = "-="
                    val["Value"] -= r_val
                elif(ctx.MULT_equ()):
                    op = "*="
                    val["Value"] *= r_val
                elif(ctx.DIV_EQU()):
                    op = "/="
                    val["Value"] /= r_val
                elif(ctx.EQU()):
                    op = "="
                    val["Value"] = r_val

                val["Type"] = type(val["Value"])
            except:
                errMsg = "unsupported operand type(s) for " + op + ": " + str(type(val.get("Value"))) + " and " + str(type(r_val))
                TypeError(errMsg)
        else:
            varDict[str(l_val)] = { "Address" : "", "Value" : r_val, "Type" : value_type, "Lifetime" : "", "Scope" : ""}

        # used for debugging
        print("Variables after '" + str(ctx.getText()) + "' assignment:")
        for key in varDict:
            print(str(key) + ":\t" + str(varDict.get(key)))
        print()

    def visitId(self, ctx: ProjectParser.IdContext):
        return ctx.VAR()
    
    
    def visitAssign_val(self, ctx: ProjectParser.Assign_valContext):
        if(ctx == None):
            return None

        if(ctx.VAR()):
            assign_val = varDict.get(str(ctx.VAR()))
            
            if(assign_val == None):
                # TODO Variable undefined, need to handle
                pass

            return assign_val
        elif(ctx.ATOM()):
            val = str(ctx.ATOM())
            if(isValidInt(val)):
                val = int(val)
            elif(isValidFloat(val)):
                val = float(val)
            else:
                val = str(val)
        elif(ctx.equation() != None):
            return EquationVisitor().visitEquation(ctx.equation())
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

def isValidInt(string):
    try:
        int(str(string))
        return True
    except:
        return False

def isValidFloat(string):
    try:
        float(str(string))
        return True
    except:
        return False

def isValidBool(string):
    if str(string) == "True" or str(string) == "False":
        return True
    else:
        return False
