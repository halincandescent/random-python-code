def longestValidParentheses(s: str) -> int:
    listString = []
    for element in s: 
        listString.append(element)
    return listString


s = ")()((()()()((()())()())))(()()()()()())((()((("
print(longestValidParentheses(s))
