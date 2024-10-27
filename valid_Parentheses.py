def is_valid(s):
    """ returns True if the string is formated correctly such that all {[( have ending brackets and that they are in the correct order
        input s: string (comibnation of {}[]())
    """
    stack = []
    paired = {"}":"{", "]":"[", ")":"("}

    for char in s:
        if char in paired:
            if stack and stack[-1] == paired[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    
    return not stack
