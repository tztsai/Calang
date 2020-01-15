# A small but powerful calculator

Run "python calc.py" to start the program.

In this calculator, there are five types of values: Number, Symbol, List, Range and Function.
Every evaluation will return a value of one of these four types.  

## Demo

<iframe height=498 width=510 src="CalcDemo.mp4">  

Check the file "__builtins.py" to see the available builtin operations and functions.  

## Features

- Evaluation of simple arithmetic expressions  
    **Examples**: 1+3, 0.5*2, -8^(4-2), 147 % 43 (modular arithmetic), 52 // 17 (integer division),
    8 & 3 (bitwise "and" operation), 1e10 \* 3e-5 (supports scientific notation)
- History  
    Use keyword **'** to represent the result of the last calculation.  
    Use keyword **'\<n>** to represent the result of the \<n>th calculation.  
    Use keyword **"** to represent the second last result.  
    Use keyword **ENV** to let the calculator print all variable bindings in the global environment.
- Multiline expression  
    Use **\\** at the end of the line to indicate that the expression continues in the next line.  
- Omit displaying result  
    Use **;** at the end of the line.  
- Complex numbers  
    The keyword **I** represents the imaginary number "i" in mathematics.  
  
    **Examples**:
  - (3+4I)*(2-6I)
  - z:=3+4I  
    [real(z), imag(z), angle(z), abs(z), conj(z)]  
- Evaluation of boolean expressions  
    Return 1 if the result is true, otherwise return 0  
    **Examples**: 3 > 2, 2 = 2, x = y xor x = z, x > 0 and x < 2, not (a or b) = (not a and not b)
- Definition and evaluation of variables  
    A legitimate variable name begins with a letter and only contains digits, letters, underscores and '?'
    (only used at the end of the name of a function that does a judgement).
    **Syntax**: \<var> := \<exp>  
    **Examples**: x := 1, g := x > 2, c := x if x > 2 else 0
- Symbol  
    A symbol is represented by an underscore '_' followed by a legitimate variable name.  
    **Examples**: _x, _y, _angle
- Definition and evaluation of functions  
  
    **Examples**:  
  - f(x, y) := 2x + y
  - f(3, 2) = 8
  - cot(x) := 1/tan(x)  
  - fact(n) := 1 if n=0 else n*fact(n-1)
  - d(f) := {x} (f(x+0.0001)-f(x))/0.0001;  
    newton(f, x) := {update: {x} x - f(x)/d(f)(x)} \  
    x if abs(f(x)) \< 0.0001 else newton(f, update(x));  
    newton(sin, 3)  (return: 3.1416)
- Lambda expression (anonymous function)  
    A lambda expression directly evaluates to a function, whose parameters are inside the brace and function body is the expression after the braces.  
    **Syntax**: {\<par1>, \<par2>, ...} \<exp>  
  
    **Examples**:
  - fact := {n} 1 if n=0 else n*fact(n-1)
  - compose := {f, g} {x} f(g(x))
- Conditional expression  
    **Syntax 1**: \<exp1> if \<cond> else \<exp2>  
    (if \<cond> holds then the expression is evaluated as \<exp1>, otherwise as \<exp2>)  
  
    **Examples**:  
  - step(x) := 0 if x<0 else 1
  - ramp(x) := 0 if x<0 else x  
  - rect(x) := 0 if x<-1 else 1 if x<=1 else 0  

  **Syntax 2**: cases \<exp1>, \<cond1>; \<exp2>, \<cond2>; ... ; \<expElse> (note that for the lase expression there is no condition to examine)  
  
  **Examples**:  
  - max(x, y, z) := cases x, x > y and x > z; y, y > z; z
- Local environment  
    **Syntax**: {\<par1>: \<val1>, \<par2>: \<val2>, ...} \<exp>  
    In fact, it is identical to **({\<par1>, \<par2>, ...} \<exp>)(\<val1>, \<val2>, ...)**.  
  
    **Examples**:  
  - {exp: a_very_long_expression} sqrt(exp) + exp + exp^2
  - binomial(n, m) := 1 if (n=0 or m=0 or m=n) else {b1:binomial(n-1, m-1), b2:binomial(n-1,   m)} b1 + b2  
- List  
    **Syntax**: [\<exp1>, \<exp2>, ...]  
    The keyword **in** can examine whether an element is contained in a list.  
    The operation **+** can concatenate two lists together (you should not apply the **+** operation on a number and a list).  
  
    **Examples**:
  - l := [1, 2, 3]
    3 in l
  - [1, 2]+[3, 4]
  - sum([1, 2, 3, 4]) (the "sum" function returns the sum of all elements of a list)  
  - sum([[1, 2], [3, 4]]) (since we can concatenate two lists by "+", the "sum" function will concatenate all lists in the list) (return: [1, 2, 3, 4])
- List subscription  
    **Syntax 1**: \<list>@\<index>  
    You can use either an integer, a list or a range as the index of the list. When using a list or a range, you will get a sub-list containing the elements whose indices lie in this range.  
    **Syntax 2**: \<list>[\<i1>, \<i2>, ..., \<in>]  
    This syntax is equivalent to sequentially subscripting \<list> by \<i1>, \<i2>, ...  
    **Note**: The advantage of the **@** symbol is that it is actually an operation, so the expression on its right is evaluated first. Thus, you are allowed to evaluate expressions like **l@s**, **l@[1, 2, 5]**, etc. Its disadvantage is that you are unable to slice the list till its end.  
  
    **Examples**:  
  - [1, 2, 3]@1
  - [1, 2][-1] (a negative index means counting from the end of the list) (return: 2)
  - [1, 2, 3]@(1~2) (return: [2, 3])
  - [1, 2, 3, 4, 5]@[i for i in range(5) if i%2] (return: 2, 4)
  - m := [[1, 2, 3], [3, 4, 5]]
    m[0, 1] (return: 2)
- List slicing  
    **Syntax**: \<list>[\<start>:\<end>(:\<step>)]
    This syntax is identical to the list slicing syntax in python.
    The second colon can be omitted, when \<step> is 1 as default.
    When \<start> is omitted, it is set to 0; when \<end> is omitted, it is set to the end of the list.  
  
    **Examples**:  
  - l := [1, 2, 3, 4, 5]  
    [l[1:], l[:3], l[:], l[:2:-1], l[::2]] (return: [[2, 3, 4, 5], [1, 2, 3], [1, 2, 3, 4, 5], [5, 4], [1, 3, 5]])
- Range  
    A range is a different type from list. A value of type "range" is an instance of the python class range.  
    There are two ways to generate a "range" type value: by using the symbol "\~" or by the builtin function "range".  
    The expression "a\~b" evaluates to a range including all integers from a to b.  
    The "range" function, however, is identical to the python function "range", which excludes the second argument from the range. Besides, you can use a third argument in the function "range" to specify the step of the range.  
    If a range is used as the index of a list, a sub-list containing elements whose indices lies in this range will be returned.  
  
    **Examples**:
  - r := 1~4  
    list(r) (converts a range to a list, return: [1, 2, 3, 4])
  - sum([i^2 for i in 1~10])
  - r := range(1, 4), list(r) (return: [1, 2, 3])
  - r := range(9, 1, -2) (return: [9, 7, 5, 3])
- List comprehension  
    Use the same syntax as in python: [\<exp> for \<arg1> in \<range1> if \<cond1> for \<arg2> in \<range2> if \<cond2> ...]  
    Note that \<range> does not necessarily have to be a range type value - it can also be a list.  
  
    **Examples**:
  - [i for i in range(4) if i%2] (return: [1, 3])
  - m := [[1, 2, 3],[3, 4, 5],[5, 6, 7]]  
    m@[range(2), [i for i in [0, 1, 2] if i%2]] (return: [[2],[4]])
  - [i\*j for i in range(10) if i%3 for j in range(10) if i+j>6]
  - sum([i^2 for i in 1~10])
  - differentiate_polynomial(coeff_list) := let {l:coeff_list} [l@i * i for i in range(len(l)) if i > 0]
- Comment  
    Use **#** to comment.
- Load files  
    Use the keyword "load" appended by a sequence of file names (located in "modules") to load these files. You can use "ENV" after the loading to check what definitions have been appended.  
    The calculator will run through the loaded file and load its definitions into the current environment. However, the current evaluation history will not be affected.  
    The loading command has two extra options: verbose and test. To turn on the verbose option, add "-v" in your command; to turn on the test option, add "-t" in your command. The testing process will be explained in the next section.  
  
    **Examples**:
  - load ../examples/merge_sort examples/btree
  - 12  
    load somefile  
    ' (return: 12)
  - load la -t
  - load scinums -v
- Create modules and testing  
    If you want to write a module by yourself, create a file inside the "modules" directory and write your definitions in it. To test your module, add the expected value after an expression as a comment. Besides, to better organize your module, you can separate your definitions and tests; if you add a line of comment: "#TEST" and put tour tests below it, the calculator will not run these tests when you load without the test option.  
  
    **An example of a module**:
  - (Inside a module "sample")  
    f(x) := x^2 + 2*x + 1;  
    const := sqrt(2) - 1;  
    \#TEST  
    f(const)  # 2
  - (In the calculator)  
    load sample -t (it will tell you tests have been passed)  
    const (return 0.4142)
- Import python modules
    Use the keyword "import" appended by a sequence of python module names (located in "pymodules") to import the definitions in these modules. To create such an importable module, you must create a python file in the "pymodules" directory and apply a variable "definitions" bound to a dict object, containing the definitions you want to export (the main program will only import "definitions" in this file). This feature is used to empower calculator with python functions and powerful python modules like numpy and sympy.  
  
    **Example**:
  - import gauss_jordan

You can find more examples in the "examples" folder.  
