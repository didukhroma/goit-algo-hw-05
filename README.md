# goit-algo-hw-05

## Порівняльний аналіз алгоритмів пошуку підрядка

### Таблиця результатів

| Algorithm Name | Query: "структури даних" | Query: "неіснуючий підрядок" |
| -------------- | ------------------------ | ---------------------------- |
| KMP            | 0.09741570003097877      | 2.4243659999920055           |
| BM             | 0.027663899993058294     | 0.4257542999694124           |
| RK             | 0.2234018999733962       | 4.615626499988139            |

Висновок:
Boyer-Moore найшвидший алгоритм для пошуку підрядка у великих текстах, особливо коли збігів небагато (або їх нема).

KMP працює добре, коли є підрядок, але витрачає більше часу при відсутності збігів.

Rabin-Karp — найменш ефективний. Він швидкий для кількох підрядків (завдяки хешам), але через колізії та перевірки працює повільно, особливо без збігів.
