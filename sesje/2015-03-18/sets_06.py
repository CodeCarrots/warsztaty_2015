from stop_words import ALL_STOP_WORDS


page_content = '''
This page is devoted to various tips and tricks that help improve the performance of your Python programs. Wherever the information comes from someone else, I've tried to identify the source.

Python has changed in some significant ways since I first wrote my "fast python" page in about 1996, which means that some of the orderings will have changed. I migrated it to the Python wiki in hopes others will help maintain it.

You should always test these tips with your application and the specific version of the Python implementation you intend to use and not just blindly accept that one method is faster than another. See the profiling section for more details.

Also new since this was originally written are packages like Cython, Pyrex, Psyco, Weave, Shed Skin and PyInline, which can dramatically improve your application's performance by making it easier to push performance-critical code into C or machine language.
'''


def is_stopword(word, stopwords_set):
    '''Checks whenever a `word` is a so-called `stop-word`.
    '''
    pass


separated_phrases = split_into_phrases(page_content)


# oczyszczamy zachowując kolejność
clean_words = []
for phrase in separated_phrases:
    pass
print(clean_words)


# oczyszczamy nie zachowując kolejności
unordered_clean_words = diff_sets(separated_phrases, ALL_STOP_WORDS)
print(unordered_clean_words)
