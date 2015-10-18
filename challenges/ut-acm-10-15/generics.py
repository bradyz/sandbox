def array(s):
    if not s:
        return True
    if len(s) >= 2 and s[0] == "[" and s[1] == "]":
        return array(s[2:])
    return False


def valid(s):
    if not s:
        return False
    if s[0] in "< > [ ]":
        return False
    for i in range(len(s)):
        if s[i] in "> ]":
            return False
        if s[i] == "<":
            if ">" in s:
                t = s[i+1: s.rfind(">")].split(",")
                if not t:
                    return False
                for v in t:
                    if not valid(v):
                        return False
                return array(s[s.rfind(">")+1:])
            return False
        if s[i] == "[":
            return array(s[i:])
    return True

for _ in range(int(input())):
    if valid(input()):
        print("CORRECT")
    else:
        print("INCORRECT")
