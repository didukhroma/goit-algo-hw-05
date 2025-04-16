import timeit
from pathlib import Path

from task_3 import kmp_search, boyer_moore_search, rabin_karp_search

article_1_path = Path(__file__).parent/"task_3"/"test_article_1.txt"
article_2_path = Path(__file__).parent/"task_3"/"test_article_2.txt"

with article_1_path.open('r',encoding="utf-8") as file:
    article_1 = file.read() 

with article_2_path.open('r',encoding="utf-8") as file:
    article_2 = file.read() 

searching_queries = ["структури даних", "неіснуючий підрядок", ]

def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=1000)


for query in searching_queries:
    print(f"Query: {query}")
    print(f"KMP: {measure_time(kmp_search, article_1, query)}")
    print(f"BM: {measure_time(boyer_moore_search, article_1, query)}")
    print(f"RK: {measure_time(rabin_karp_search, article_1, query)}")
    print("\n")
