
import re

"""
    APPROACH:
        > Separate forward parenthesis and backward parenthesis in two separate lists 
        using regular expressions. If these lists are of different lengths, Reject. 
        
        > Separate all the parenthesis in a single list using regular expressions. 
        Iterate over the list (containing parenthesis only)
        and find valid match of every forward paren if it exists. 
        If no match or any invalidity is found reject; Accept otherwise.
         
"""


def main():
    string = input('input expression: ')
    if parens_balance(string):
        print('"ACCEPTED". All parenthesis are balanced and properly ordered.')
    else:
        print('"REJECTED". Some parenthesis are "NOT" balanced or properly ordered.')
    

def parens_balance(string):
    find_fwd_parens = re.compile(r"[\(\{]")
    fwd_braks = find_fwd_parens.findall(string)

    find_bkwd_parens = re.compile(r"[\)\}]")
    bkwd_braks = find_bkwd_parens.findall(string)
    
    if (len(fwd_braks) != len(bkwd_braks)): # check 1
        return False
    
    all_braks = re.compile(r"[\(\{\)\}]")
    all_braks = all_braks.findall(string)

    iterations = 0
    for char in all_braks:
        iterations = iterations + 1
        if is_open_bracket(char): # find matches of open braks only
            open_braks = 0 
            for i in range(iterations, len(string)):
                if braks_inconsistant(open_braks):
                    return False
                current_bracket = all_braks[i]
                if open_braks == 0: # Assume current bracket is the valid match if no addtional brak is open. 
                    if valid_match(char) == current_bracket:
                        break 
                if is_open_bracket(current_bracket): 
                    open_braks = open_braks + 1 
                    
                if not is_open_bracket(current_bracket):
                    open_braks = open_braks - 1
                    
                if i == len(all_braks) - 1: # no match was found for this open brak 
                    return False
      
    return True


################ 'Helper Functions below' ################

is_open_bracket = lambda x : x in ['(', '{']
valid_match = lambda x: ')' if x == '(' else '}'
braks_inconsistant = lambda x : True if x < 0 else False ## Inconsistant if more brackets 
														 ## are closed then were opened initially

################ 'Helper Functions above' ################


if __name__ == "__main__":
    main()


