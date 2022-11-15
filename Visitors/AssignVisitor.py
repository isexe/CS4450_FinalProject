from antlr4 import *
from Grammar.ProjectLexer import ProjectLexer
from Grammar.ProjectParser import ProjectParser
from Grammar.ProjectVisitor import ProjectVisitor

from Visitors.EquationVisitor import EquationVisitor

class UnexpectedError(Exception):
    pass

class AssignVisitor(ProjectVisitor):

    # Visit a parse tree produced by ProjectParser#assign.
    def visitAssign(self, ctx:ProjectParser.AssignContext):
        print(ctx.getText())
        return self.visitAssignChildren(ctx)


    def visitAssignChildren(self, node):
        result = self.defaultResult()
        n = node.getChildCount()
        for i in range(n):
            if not self.shouldVisitNextChild(node, result):
                return result

            c = node.getChild(i)
            childResult = c.accept(self)
            result = self.aggregateResult(result, childResult)

        return result
    
    # Visit a parse tree produced by ProjectParser#id.
    def visitId(self, ctx:ProjectParser.IdContext):
        print(ctx.VAR())
        return str(ctx.VAR())

    # Visit a parse tree produced by ProjectParser#assign_val.
    def visitAssign_val(self, ctx:ProjectParser.Assign_valContext):
        if(ctx.VAR()):
            pass
        elif(ctx.ATOM()):
            pass
        else:
            return EquationVisitor().visitEquation(ctx)

# dictionary = {
#     "myVar" : {
#                 "Address" : "...",
#                 "Value" : "Hello Word",
#                 "Type" : "str",
#                 "Lifetime" : "...",
#                 "Scope" : "..."
#             },
#     "myVar2" : {
#                 "Address" : "",
#                 "Value" : "",
#                 "Type" : "",
#                 "Lifetime" : "",
#                 "Scope" : ""
#             },
# }

##! Example statment
# myVar2 = myVar

#! BEGIN - visitAssign(ctx)

# l_val = str(self.visitId(ctx.left))
##! BEGIN - visitId(ctx)
# return ctx.VAR()
##! END - visitId(ctx)


# if(l_val in dict) 
#   val = (dict where key == l_val)
# else 
#   create variable and insert into dictionary (name/key == l_val)


# r_val = self.visitAssign_val(ctx.right)
##! BEGIN - visitAssign_val(ctx)
    # if(ctx.VAR()):
        # assign_val = (dictionary entry with key == ctx.VAR())
        # if not found raise error
        # else return assign_val
    # elif(ctx.ATOM()):
        # assign_val = check if int, float, or string(ctx.ATOM())
        # return assign_val
    # elif(ctx.equation != None):
        # return EquationVisitor.visitEquation(ctx.equation)
    # else:
        # shouldn't ever get into this block
##! END - visitAssign_val(ctx)
# if r_val is variable, set val.Value = r_val.Value, val.Type = r_val.Type
# elif r_val is int,float, string, set val.Value = r_val, val.Type = typeof(r_val)

#! END - visitAssign(ctx)

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