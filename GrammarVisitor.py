from antlr4 import *
from Grammar.ProjectLexer import ProjectLexer
from Grammar.ProjectParser import ProjectParser
from Grammar.ProjectVisitor import ProjectVisitor

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

class UnexpectedError(Exception):
    pass

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

    def visitAssign(self, ctx:ProjectParser.AssignContext):
        result = AssignVisitor().visitAssign(ctx)

        if(self.debugging):
            print("Assign '" + str(ctx.getText()) + "':")
            print(result)

        return result

class AssignVisitor(ProjectVisitor):

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
        if str(l_val) in varDict.keys(): 
            val = varDict[str(l_val)]

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
            val = { "Address" :id(r_val), "Value" : r_val, "Type" : value_type, "Lifetime" : "", "Scope" : ""}
            varDict[str(l_val)] = val

        return val

    def visitId(self, ctx: ProjectParser.IdContext):
        return ctx.VAR()
    
    
    def visitAssign_val(self, ctx: ProjectParser.Assign_valContext):
        if(ctx == None):
            return None

        if(ctx.VAR()):
            assign_val = varDict.get(str(ctx.VAR()))
            
            if(assign_val == None):
                raise NameError("name '" + str(ctx.VAR()) + "' is not defined")

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

        return val

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
            var = varDict.get(str(ctx.VAR()))
            
            if(var == None):
                raise NameError("name '" + str(ctx.VAR()) + "' is not defined")

            assign_val = var.get("Value")

            if(var.get("Type") == type(int)):
                assign_val = int(assign_val)
            elif(var.get("Type") == type(float)):
                assign_val = float(assign_val)    

            return assign_val
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
