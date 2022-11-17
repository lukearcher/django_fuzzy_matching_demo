# fuzzy matching imports
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# overall matching score
def get_fuzz_ratio(name1, name2):
    return fuzz.ratio(name1,name2)

# partial score
def get_fuzz_partial_ratio(name1, name2):
    return fuzz.partial_ratio(name1,name2)

# token score
def get_fuzz_token_sort_ratio(name1, name2):
    return fuzz.token_sort_ratio(name1,name2)

def return_fuzzy_message(name1, name2):

    # return the fuzzy matching scores
    fuzzy_score = get_fuzz_ratio(name1, name2)
    partial_score = get_fuzz_partial_ratio(name1, name2)
    token_score = get_fuzz_token_sort_ratio(name1, name2)

    # create the result string
    result_message = 'Fuzzy matching results:<br>Fuzzy Score: ' + str(fuzzy_score) + '<br>Partial Score: ' + str(partial_score) + '<br>Token Score: ' + str(token_score) + '<br>'

    return result_message
