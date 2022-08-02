from typing import List

from test_framework import generic_test

import functools

def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    '''
    play options:
        2 pts = safety 
        3 pts = field goal 
        7 pts = touchdown  
    
    example 1: 
    input: final_score = 12 

    output: 4 ( the # of combinations)
    - 6 safeties 
    - 3 safeties and 2 field goals 
    - 1 safeties, 1 field goals, and 1 touchdown
    - 4 field goals 

    top down dp approach 
    start off with s (lowest) as the first play, fill it up till reach yield, if not switch options

    play_table = [] # len is yield // 2

    only safety => [12, 10, 8, 6, 4, 2]
    
    decide b/w including field goals or not => [9, 6, 3, 0]


    [2, 3, 7]

    [6, ]
    '''
    # print(individual_play_scores)
    # table_length = final_score // 2 

    # for play in individual_play_scores:
    #     for i in range(table_length):
    @functools.lru_cache(None)

    def score_helper(index, score):  
        if score == 0: 
           return 1 

        if index == n:
         return 0 
        with_score, without_score = 0, 0
        if individual_play_scores[index] <= score: # score of 5 and play score is 10
            with_score = score_helper(index, score - individual_play_scores[index])
       
        without_score = score_helper(index + 1, score)
        return with_score + without_score
    n = len(individual_play_scores)
    return score_helper(0, final_score)




#   n = len(plays)
#   return score_helper(0, m)

# def final_score_combinations(m, plays):

#   @functools.lru_cache(None)
#   def score_helper(index, score):  
#     if score == 0: 
#       return 1 

#     if index == n:
#       return 0 
#     with_score, without_score = 0, 0
#     if plays[index] <= score: # score of 5 and play score is 10
#       with_score = score_helper(index, score - plays[index])
#     without_score = score_helper(index + 1, score)
#     return with_score + without_score

#   n = len(plays)
#   return score_helper(0, m)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
