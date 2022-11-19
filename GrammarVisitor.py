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

# "stack" that variables are stored ion
# instead of having dict of dict,
# should create a class for variables at some point
varDict = {}

class UnexpectedError(Exception):
    pass

class GrammarVisitor(ProjectVisitor):
    def __init__(self, debugging = False):
        self.debugging = debugging
    
    # Visit a parse tree produced by ProjectParser#code.
    # Next Node is Line
    def visitCode(self, ctx:ProjectParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#line.
    # Next Node is Statement
    def visitLine(self, ctx:ProjectParser.LineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#block.
    def visitBlock(self, ctx: ProjectParser.BlockContext):
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

    def visitIfElseBlock(self, ctx: ProjectParser.IfElseBlockContext):
        result = IfElseBlock().visitIfElseBlock(ctx)

        if(self.debugging):
            print("IfElseStatement:\t" + str(result))
        
        print(varDict)

        return result

class AssignVisitor(ProjectVisitor):

    # Visit a parse tree produced by ProjectParser#assign.
    def visitAssign(self, ctx: ProjectParser.AssignContext):
        if(ctx == None):
            return None

        #placeholders
        val = None
        value_type = None

        l_val = self.visitId(ctx.left)
        r_val = self.visitAssign_val(ctx.right)

        if(type(r_val) is dict):
            # r_val is a variable passed in, need to handle it
            # for now just set r_val to value of variable
            r_val = r_val.get("Value")

        if(r_val == None or r_val == "None"):
            r_val = None
        else:
            r_val = str(r_val)
            if(isValidInt(r_val)):
                r_val = int(r_val)
            elif(isValidFloat(r_val)):
                r_val = float(r_val)
            elif(isValidBool(r_val)):
                if(r_val == "True"):
                    r_val = True
                else:
                    r_val = False
            else:
                r_val = str(r_val)

        # check if variable already defined
        if str(l_val) in varDict.keys(): 
            val = varDict[str(l_val)]

        # if the variable is previously defined
        if(val != None):
            op = ""
            try:
                if(ctx.PLU_EQU()):
                    op = "+="
                    if val['Type'] == str:
                        val['Value'] = val['Value'][:-1]
                        r_val = r_val[1:]
                    val['Value'] += r_val
                elif(ctx.MIN_EQU()):
                    op = "-="
                    val["Value"] -= r_val
                elif(ctx.MULT_EQU()):
                    op = "*="
                    tmp = val["Value"]
                    if(type(tmp) is str and type(r_val) is int):
                        quote = tmp[0]
                        tmp = tmp[1:-1]
                        tmp = tmp * r_val
                        val["Value"] = quote + tmp + quote
                    elif(type(tmp) is int and type(r_val) is str):
                        quote = r_val[0]
                        r_val = r_val[1:-1]
                        r_val = r_val * tmp
                        val["Value"] = quote + r_val + quote
                    else:
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
                raise TypeError(errMsg)
        else:
            val = { "Address" :id(r_val), "Value" : r_val, "Type" : type(r_val), "Lifetime" : "", "Scope" : ""}
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
            elif(isValidBool(val)):
                if(val == "True"):
                    val = True
                else:
                    val = False
            elif(val == "None"):
                val = None
            else:
                val = str(val)
        elif(ctx.logicExpr() != None):
            return LogicVisitor().visitLogicExpr(ctx.logicExpr())  
        elif(ctx.equation() != None):
            return EquationVisitor().visitEquation(ctx.equation())
        else:
            raise UnexpectedError("Assigned value isn't an atom, equation, or logic expression")

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
        result = c.accept(self)
        
        if(result != None):
            result = str(result)
            if(isValidInt(result)):
                result = int(result)
            elif(isValidFloat(result)):
                result = float(result)

        return result


    # Step 2:
    # Visit a parse tree produced by ProjectParser#eqFourthOrder.
    def visitEqFourthOrder(self, ctx:ProjectParser.EqFourthOrderContext):
        result = self.visitEqFourthOrderChildren(ctx)
        return result

    # Step 2.5:
    # Visit children of a parse tree produced by ProjectParser#eqFourthOrder.
    def visitEqFourthOrderChildren(self, node):
        result = None
        sign = None
        n = node.getChildCount()
        for i in range(n):
            # get child then visit them
            c = node.getChild(i)
            childResult = c.accept(self)

            # We know at this point the value we have is a int, float, str
            # try guessing the value and going with the first valid option
            if(childResult != None):
                childResult = str(childResult)
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
                try:
                    # find what the sign is and apply it to result and childResult
                    if(sign == "+"):
                        if(type(result) is str and type(childResult) is str):
                            result = result[:-1]
                            childResult = childResult[1:]
                        result = result + childResult
                    elif(sign == "-"):
                        result = result - childResult
                    else:
                        # Catch any signs that shouldn't be present
                        raise UnexpectedError("Addition/Subtraction sign was value other than '+', '-'")
                    # reset sign value so we know it's next
                    
                except:
                    raise TypeError("unsupported operand type(s) for " + str(sign) + ": '" + type(result) + "' and '" + type(str) + "'")
                    
                sign = None
        return result

    # Step 3:
    # Visit a parse tree produced by ProjectParser#eqThirdOrder.
    def visitEqThirdOrder(self, ctx:ProjectParser.EqThirdOrderContext):
        result = self.visitEqThirdOrderChildren(ctx)
        return result

    # Step 3.5
    # functions identically to sum
    # Visit children of a parse tree produced by ProjectParser#eqThirdOrder.
    def visitEqThirdOrderChildren(self, node):
        result = None
        sign = None
        n = node.getChildCount()
        for i in range(n):
            c = node.getChild(i)
            childResult = c.accept(self)
            
            if(childResult != None):
                childResult = str(childResult)
                if(isValidInt(childResult)):
                    childResult = int(childResult)
                elif(isValidFloat(childResult)):
                    childResult = float(childResult)

            if(result == None):
                result = childResult
            elif(sign == None):
                sign = childResult
            else:
                try:
                    if(sign == "*"):
                        if(type(result) is str and type(childResult) is int):
                            quote = result[0]
                            result = result[1:-1]
                            result = result * childResult
                            result = quote + result + quote
                        elif(type(result) is int and type(childResult) is str):
                            quote = childResult[0]
                            childResult = childResult[1:-1]
                            result = result * childResult
                            result = quote + result + quote
                        else:
                            result = result * childResult
                    elif(sign == "/"):
                        result = result / childResult
                    elif(sign == "%"):
                        result = result % childResult
                    else:
                        raise UnexpectedError("Multiplication/Division/Modulo sign was value other than '*', '/', '%'")
                except:
                    raise TypeError("unsupported operand type(s) for " + str(sign) + ": '" + type(result) + "' and '" + type(str) + "'")
                
                sign = None

        return result

    # Step 4:
    # Visit a parse tree produced by ProjectParser#eqSecondOrder.
    def visitEqSecondOrder(self, ctx: ProjectParser.EqSecondOrderContext):
        result = self.visitEqSecondOrderChildren(ctx)
        return result

    # Step 4.5
    # functions identically to other orders of operations
    # Visit children of a parse tree produced by ProjectParser#eqSecondOrder.
    def visitEqSecondOrderChildren(self, node):
        result = None
        sign = None
        n = node.getChildCount()
        for i in range(n):
            c = node.getChild(i)
            childResult = c.accept(self)
            
            if(childResult != None):
                childResult = str(childResult)
                if(isValidInt(childResult)):
                    childResult = int(childResult)
                elif(isValidFloat(childResult)):
                    childResult = float(childResult)

            if(result == None):
                result = childResult
            elif(sign == None):
                sign = childResult
            else:
                try:
                    if(sign == "**"):
                        result = result ** childResult
                    elif(sign == "//"):
                        result = result // childResult
                    else:
                        raise UnexpectedError("Power/Square sign was value other than '**', '//'")
                except:
                    raise TypeError("unsupported operand type(s) for " + str(sign) + ": '" + type(result) + "' and '" + type(str) + "'")
                
                sign = None

        return result

    # Step 5
    # This step will either return an ATOM or VAR if the equation is done
    # Or another equation if there is some nested in paranthesis
    # Visit a parse tree produced by ProjectParser#val.
    def visitEqFirstOrder(self, ctx: ProjectParser.EqFirstOrderContext):
        
        result = None

        if(ctx.para != None):
            result = self.visitEqFourthOrder(ctx.para)
        elif(ctx.terminal != None):
            result = self.visitEqVal(ctx.terminal)

        if(result != None):
            result = str(result)
            if(isValidInt(result)):
                result = int(result)
            elif(isValidFloat(result)):
                result = float(result)

        if(ctx.sign != None):
            if(ctx.sign.text == "-"):
                try:
                    result = -result
                except:
                    raise TypeError("bad operand type for unary -: " + type(result))
            elif(ctx.sign.text == "+"):
                try:
                    result = +result
                except:
                    raise TypeError("bad operand type for unary +: " + type(result))

        return result

    def visitEqVal(self, ctx: ProjectParser.EqValContext):
        result = None
        # is variable
        if(ctx.VAR()):
            var = varDict.get(str(ctx.VAR()))
            
            if(var == None):
                raise NameError("name '" + str(ctx.VAR()) + "' is not defined")

            result = var.get("Value")

            # should be stored as it's proper type
            # if(var.get("Type") == type(int)):
            #     result = int(result)
            # elif(var.get("Type") == type(float)):
            #     result = float(result)
            
        # is atom value
        elif(ctx.ATOM()):
            result = ctx.ATOM()

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

    # This will get the '**' operator
    # Visit a parse tree produced by ProjectParser#expon.
    def visitExpon(self, ctx: ProjectParser.ExponContext):
        return ctx.getText()

    # This will get the '//' operator  
    # Visit a parse tree produced by ProjectParser#Sqrt.
    def visitSqrt(self, ctx: ProjectParser.SqrtContext):
        return ctx.getText()

class IfElseBlock(ProjectVisitor):
    # This ctx is the parent of all the ifelseblock code, has statement and code sections
    # need to visit children
    # start with if then go through each block
    # break if one returns true
    def visitIfElseBlock(self, ctx: ProjectParser.IfElseBlockContext):
        result = self.visitIfElseBlockChildren(ctx)
        return result

    # Visit the children of a parse tree produced by ProjectParser#equation.
    def visitIfElseBlockChildren(self, node):
        result = None
        n = node.getChildCount()

        for i in range(n):
            if not self.shouldVisitNextChild(node, result):
                return result
            
            c = node.getChild(i)
            result = c.accept(self)

            print("childresult" + str(result))
        
            if(result != None):
                if(str(result) == "True"):
                    result = True
                elif(str(result) == "False"):
                    result = False
                
                if(result):
                    break

        return result

    # Need to visit children
    # if child(logicExpr) and if true, visit child(ifElseCode)
    # need to return the value from logicExpr
    def visitIfStatement(self, ctx: ProjectParser.IfStatementContext):
        ctxLogic = ctx.logicExpr()
        ctxCode = ctx.ifElseCode()

        result = None
        logVal = self.visitLogicExpr(ctxLogic)

        if(logVal != None):
            if(str(logVal) == "True"):
                logVal = True
            elif(str(logVal) == "False"):
                logVal = False

        if(logVal):
            result = self.visitIfElseCode(ctxCode)

        return logVal

    def visitElifStatement(self, ctx: ProjectParser.ElifStatementContext):
        ctxLogic = ctx.logicExpr()
        ctxCode = ctx.ifElseCode()

        result = None
        logVal = self.visitLogicExpr(ctxLogic)

        #make result bool

        if(logVal != None):
            if(str(logVal) == "True"):
                logVal = True
            elif(str(logVal) == "False"):
                logVal = False

        if(logVal):
            result = self.visitIfElseCode(ctxCode)

        return logVal

    def visitElseStatement(self, ctx: ProjectParser.ElseStatementContext):
        ctxCode = ctx.ifElseCode()
        self.visitIfElseCode(ctxCode)
        return None

    def visitIfElseCode(self, ctx: ProjectParser.IfElseCodeContext):
        n = ctx.getChildCount()
        result = None

        for i in range(n):
            c = ctx.getChild(i)

            result = GrammarVisitor().visit(c)
        
        return result

    def visitLogicExpr(self, ctx: ProjectParser.LogicExprContext):
        print("LogExpr:\t" + ctx.getText())
        result = LogicVisitor().visitLogicExpr(ctx)
        print("Result:\t" + str(result))
        return result
    
class LogicVisitor(ProjectVisitor):

    def visitLogicExpr(self, ctx: ProjectParser.LogicExprContext):
        result = self.visitLogicExprChildren(ctx)
        return result

    # need to handle the results from the children nodes
    def visitLogicExprChildren(self, node):
        result = None
        sign = None
        result_arr = []
        and_flag = False
        or_flag = False
        n = node.getChildCount()
        for i in range(n):
            if not self.shouldVisitNextChild(node, result):
                return result

            c = node.getChild(i)
            childResult = c.accept(self)

            if(childResult != None):
                childResult = str(childResult)
                if(isValidInt(childResult)):
                    childResult = int(childResult)
                elif(isValidFloat(childResult)):
                    childResult = float(childResult)
                elif(childResult == "and"):
                    and_flag = True
                    continue
                elif(childResult == "or"):
                    or_flag = True
                    continue
                elif(childResult == "False" or childResult == "True"):
                    result_arr.append(childResult)
                    # print(result_arr)
                    if(len(result_arr) > 2):
                        result_arr.pop(0)
                    if(and_flag):
                        if("False" in result_arr):
                            result = False
                        else:
                            result = True
                    elif(or_flag):
                        if("True" in result_arr):
                            result = True
                        else:
                            result = False
                
                    and_flag = False
                    or_flag = False
                        

            # if result is none just set it to the first value we found
            if(result == None):
                result = childResult
            # if sign is none then the current child should be a sign operator
            elif(sign == None):
                sign = childResult
            else:
                try:
                    if sign == "==":
                        result = (result == childResult)
                    elif sign == "!=":
                        result = (result != childResult)
                    elif sign == ">=":
                        result = (result >= childResult)
                    elif sign == ">":
                        result = (result > childResult)
                    elif sign == "<=":
                        result = (result <= childResult)
                    elif sign == "<":
                        result = (result < childResult)
                    else:
                        UnexpectedError("Comparison was not valid")
                except:
                    raise TypeError("unsupported operand type(s) for " + str(sign) + ": '" + type(result) + "' and '" + type(childResult) + "'")

                result_arr.append(str(result))
                sign = None

        return result

    def visitLogicConj(self, ctx: ProjectParser.LogicConjContext):
        # print("LogCong:\t" + ctx.getText())
        result = ctx.getText()
        return result
    
    def visitLogicVal(self, ctx: ProjectParser.LogicValContext):
        result = None
        if(ctx.VAR()):
            result = varDict.get(str(ctx.VAR()))
            if(result == None):
                raise NameError("name '" + str(ctx.VAR()) + "' is not defined")
        elif(ctx.ATOM()):
            result = ctx.ATOM()
        elif(ctx.equation() != None):
            result = EquationVisitor().visitEquation(ctx.equation())

        # print("LogVal:\t" + ctx.getText() + " = " + str(result))
        # print("LogVal:\t" + ctx.getText())

        return result

    def visitLogicOp(self, ctx:ProjectParser.LogicOpContext):
        # print("LogOp:\t" + ctx.getText())
        result = ctx.getText()
        return result

# tr;y converting it to int, if fail not int
def isValidInt(string):
    try:
        int(str(string))
        return True
    except:
        return False

# try converting it to float, if fail not float
def isValidFloat(string):
    try:
        float(str(string))
        return True
    except:
        return False

# check for True or False
def isValidBool(string):
    if str(string) == "True" or str(string) == "False":
        return True
    else:
        return False

# check for quotes at front and back
def isValidString(string):
    if str(string)[0] == '"' and str(string)[-1] == '"':
        return True
    elif str(string)[0] == "'" and str(string)[-1] == "'":
        return True
    else:
        return False
