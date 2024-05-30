def check_brackets(strings):
    results = []

    for s in strings:
        left_stack = []
        result = [' '] * len(s) 
        source_index = 0
        while source_index < len(s):
            char = s[source_index]
            if char == '(':
                left_stack.append(source_index) 
            elif char == ')':
                if left_stack:
                    left_stack.pop()  
                else:
                    result[source_index] = '?'  
            source_index += 1

        while left_stack:
            index = left_stack.pop()
            result[index] = 'x' 

        results.append(''.join(result))  

    return results

# Testcase
input_strings = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

output_strings = check_brackets(input_strings)
for i in range(len(input_strings)):
    print(input_strings[i])
    print(output_strings[i])
