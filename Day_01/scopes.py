# 5. Scope: Local vs Global -> Scope determines where variables can be accessed in your code.
# Local Scope:- Variables defined inside a function are local to that function:
"""def my_function():
    local_var = "I'm local"  
    print(local_var)

my_function()  """

# Global Scope :-Variables defined outside functions are global:
"""global_var = "I'm global"  

def access_global():
    print(global_var)  

def another_function():
    print(global_var)  

access_global()      
another_function() """  
