#expression to solve.
expression = "495*843575/931-178/-352667-767751**-679-931+745837--716-16-274--633476*310-337+-534995/404"


list_expression = [] #empty list to append values later on


def append(): #created a function called append (appends to the list)
  idx = 0 #set idx to 0 
  end_idx = 0 # set the end idx to 0
  ops = "+-*/" #operators
  neg = '-' #negative
  while idx < len(expression): #while idx is less than the length of the expression

      if expression[idx] in ("+", "-", "*", "/", "**"): #if expression at idx is +, -, *, /, **
        if expression[idx:idx+2] == "**": #if expression at idx and idx+1 is **
          list_expression.append(expression[idx:idx+2]) #append ** to the list
          idx += 2 #increment idx by 2

          
      
        if idx == 0 and expression[idx] in neg: #if idx is 0 and expression at idx is -
          end_idx = idx +1 #set end_idx to idx +1
          while end_idx < len(expression) and expression[end_idx] not in ops: #while end_idx is less than the length of the expression and expression at end_idx is not in ops
            end_idx += 1 #increment end_idx by 1
          list_expression.append(expression[idx:end_idx]) #append the expression from idx to end_idx to the list
          idx = end_idx #set idx to end_idx
        
        if expression[idx] in neg and expression[idx-1] in ops: #if expression at idx is - and expression at idx-1 is in ops
          end_idx = idx +1 #set end_idx to idx +1
          while end_idx < len(expression) and expression[end_idx] not in ops: #while end_idx is less than the length of the expression and expression at end_idx is not in
            end_idx += 1 #increment end_idx by 1
          list_expression.append(expression[idx:end_idx]) #append the expression from idx to end_idx to the list
          idx = end_idx #set idx to end_idx
  
       
        else:
          list_expression.append(expression[idx]) #append expression at idx to the list
          idx+= 1 #increment idx by 1
      
      else:
        end_idx = idx + 1 #set end_idx to idx +1
        while end_idx < len(expression) and (expression[end_idx].isdigit() or expression[end_idx]=="."):  #while end_idx is less than the length of the expression and expression at end_idx is a digit
          end_idx += 1  #increment end_idx by 1
        list_expression.append(expression[idx:end_idx])  #append the expression from idx to end_idx to the list
        idx = end_idx #set idx to end_idx
  
def operations(a, ops, b): #created a function called operations (takes in 3 parameters), a, b, and operator.
  if ops == "+": #if ops is +
    return a + b #return a + b
  elif ops == "-": #if ops is -
    return a - b  #return a - b
  elif ops == "*": #if ops is *
    return a * b #return a * b
  elif ops == "/": #if ops is /
    return a / b #return a / b
  elif ops == "**": #if ops is **
    return a ** b  #return a ** b

def bedmas(): #created a function called bedmas
  AS = ("+-") #set AS to +- (addition, subtraction)
  DM = ("/*") #set DM to /* (division, multiplication)
  idx = 0  #set idx to 0
  while "**" in list_expression: #while "**" is in the list expression
    if list_expression[idx] == "**": #if list expression at idx is **
      num1 = list_expression[idx - 1] #set num1 to list expression at idx - 1
      num2 = list_expression[idx + 1] #set num2 to list expression at idx + 1
      Sign = list_expression[idx] #set Sign to list expression at idx (in the middle)
  
      list_expression[idx] = operations(float(num1), Sign, float(num2)) #set list expression at idx to the operations function (float(num1), Sign, float(num2))
      del list_expression[idx + 1] #delete list expression at idx + 1
      del list_expression[idx - 1] #delete list expression at idx - 1
      idx -= 1 #decrement idx by 1
    idx += 1 #increment idx by 1

  idx = 0 #set idx to 0
  while "*" in list_expression or "/" in list_expression: #while * or / is in the list expression
    if str(list_expression[idx]) in DM: #if list expression at idx is in DM
      num1 = list_expression[idx - 1] #set num1 to list expression at idx - 1
      num2 = list_expression[idx + 1] #set num2 to list expression at idx + 1
      Sign = list_expression[idx] #set Sign to list expression at idx (in the middle)
    
      list_expression[idx] = operations(float(num1), Sign, float(num2)) 
      del list_expression[idx + 1] #delete list expression at idx + 1
      del list_expression[idx - 1] #delete list expression at idx - 1
      idx -= 1 #decrement idx by 1
    idx += 1 #increment idx by 1
    
  idx = 0 #set idx to 0
  while "+" in list_expression or "-" in list_expression: #while + or - is in the list expression
    if str(list_expression[idx]) in AS: #if list expression at idx is in AS
      num1 = list_expression[idx - 1] #set num1 to list expression at idx - 1
      num2 = list_expression[idx + 1] #set num2 to list expression at idx + 1
      Sign = list_expression[idx] #set Sign to list expression at idx (in the middle)
    
      list_expression[idx] = operations(float(num1), Sign, float(num2))
      del list_expression[idx + 1] #delete list expression at idx + 1
      del list_expression[idx - 1] #delete list expression at idx - 1
      idx -= 1 #decrement idx by 1
    idx += 1 #increment idx by 1
  idx = 0  #set idx to 0  

def main(operations): #created a function called main (takes in 1 parameter), operations.
  append() #call append function
  bedmas() #call bedmas function

main(operations) #call main function with the parameter operations to run the code for equation
  

print("The answer of my calculator is: " + str(list_expression[0]))
print("")
print("The eval of this expression is: " + str(eval(expression)))