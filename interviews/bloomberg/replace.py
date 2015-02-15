# Replace Description:
# Given a string, character to replace, and character to sub
# Return a new string which subbed in characters


def sub_letter(a_str, to_r, to_s):
    arr = list(a_str)
    for i in range(len(arr)):
        if arr[i] == to_r:
            arr[i] = to_s
    return "".join(arr)


if __name__ == "__main__":
    a_string = "brady"
    b_string = sub_letter(a_string, "b", "g")
    print(a_string)
    print(b_string)
