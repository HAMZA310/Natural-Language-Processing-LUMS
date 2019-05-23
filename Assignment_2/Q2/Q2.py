
import re



text = "Pila Forfeited you engrossed but 1kometimes explained. Another 1kacokaco1 as studied it to evident. Merry sense 9given he be arisepila. Conduct at an replied removal an amongst. Remainingzalima 0determine few her two cordially Zalima admitting old. Sometimes ctra*nger his pisdsdla ourselves her co*la depending you boy. Eat discretion cultivated possession far comparison projection pila considered. And few fat interested discovered inquietude insensible unsatiable increasing zalima eat."


# ## First Word

# ### Write down the regular expression to extract first word.

first_word = re.compile(r"[Zz][a-z]*[a]")

print(first_word.findall(text))


# ####  What is the frequency (count) of first word in random text?
# 
# ##  3

# #### What’s the first word?
# ## Zalima

# ## Second Word

# ### Write down the regular expression to extract the second word.
# 


second_word = re.compile(r"[0-9][k][a-z]*[0-9]")

print(second_word.findall(text))


# #### Write down the word you extracted using above regular expression.
# ## 1kacokaco1

# #### Remove first and last three letters/ digits from word you get in part b) to get actual second word. What’s the second word?
# ## coka

# ## Third Word

# ### Write down the regular expression to extract the third word.
# 
# 

third_word = re.compile(r'c[a-z]*[*][a-z]+a')

print(third_word.findall(text))


# ####  Write down the word you extracted using above regular expression.
# ## co*la

# #### Remove star ‘*’ from word you get in part b) to get actual third word. What’s the third word?
# ## cola

# ## Fourth Word

# ### Fourth word starts with a letter ‘P’ or ‘p’, followed by exactly two letters between ‘a’ and ‘z’ and ends with a letter ‘a’.

# ### Write down the regular expression to extract the fourth word.

fourth_word = re.compile(r'[Pp][a-z]{2}a')

print(fourth_word.findall(text))


# ####  What is the frequency (count) of fourth word in random text?
# ## 3
# 
# 

# ####  What’s the fourth word?
# ## pila 

# #### Well, if you have correctly extracted first four words, you can easily predict the fifth word. Write down the complete five word message that your shy friend sent you.
# # Zalima coka cola pila day
