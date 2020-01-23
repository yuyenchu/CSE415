def is_multiple_of_3(n):
    return n%3==0
## Return True if n is a multiple of 3; False otherwise.

## pre: m > 0, m is an integer
def next_prime(m):
    n=m+1
    while (True):
        for i in range(2,n):
            if (n % i) == 0:
                n+=1
                break
        else:
            return n 
##  Return an integer p that is prime, and such that
##  p > m, and there does not exist any n, with n > m
##  and n < p such that n is prime. In other words, return
##  the next prime number after m.

import wordscraper as ws
import math
url = "http://courses.cs.washington.edu/courses/cse415/20wi/desc.html"
def empirical_probabilities(url):
    html_bytes=ws.fetch(url)
    word_list = ws.html_bytes_to_word_list(html_bytes)
    count_dict = ws.make_word_count_dict(word_list)
    for key in count_dict:
          count_dict[key] = 1.0 - math.exp(-(count_dict[key]+1))
    return count_dict
##  Return a dictionary whose keys are words in a reference vocabulary,
##  and whose values are PROBABILITIES of those words, based on the
##  number of occurrences on the webpage at the given URL.
