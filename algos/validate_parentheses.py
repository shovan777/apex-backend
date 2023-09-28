"""Tring to valdiate parentheses."""


def validate_parentheses(par_string):
    couples = ["()", "{}", "[]"]
    while par_string:
        prev_len = len(par_string)
        for couple in couples:
            par_string = par_string.replace(couple, "")
        final_length = len(par_string)
        if final_length == prev_len:
            break
    if len(par_string) > 0:
        return False
    return True


inp_string = "{[]()"
print(validate_parentheses(inp_string))
