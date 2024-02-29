# Висновки

## Порівняння алгоритмів DFS і BFS для знаходження шляхів у графі

- **DFS (Depth-First Search)**:
  - Використовує стратегію "глибини", тобто спочатку обходить усі вершини одного дерева, а потім переходить до наступного. 
  - Здійснює глибокий пошук, проникаючи якомога глибше в граф перед тим, як повернутися назад.
  - Шляхи, які знаходить DFS, можуть бути довшими, оскільки алгоритм не обов'язково шукає найкоротший шлях.

- **BFS (Breadth-First Search)**:
  - Використовує стратегію "ширини", тобто спочатку обходить всі вершини на одному рівні, а потім переходить на наступний рівень.
  - Здійснює пошук шляхів, починаючи з найближчих вершин і просуваючись далі від них.
  - Зазвичай знаходить найкоротший шлях до кожної вершини.

## Різниця в отриманих шляхах

- **DFS**:
  - DFS може знайти шлях, який може бути довшим за найкоротший, оскільки він шукає глибоко в графі, перевіряючи всі можливі ребра перед тим, як повернутися назад.
  - Через це, шляхи, знайдені DFS, можуть бути неоптимальними з точки зору мінімальної довжини.

- **BFS**:
  - BFS, натомість, зазвичай знаходить найкоротший шлях до кожної вершини, оскільки він спочатку досліджує всі можливі шляхи з поточної вершини перед тим, як перейти до наступної.
  - Це робить BFS більш ефективним для пошуку найкоротших шляхів у графі.

## Висновок

- Для пошуку найкоротших шляхів у графі краще використовувати алгоритм BFS, оскільки він зазвичай знаходить оптимальніші шляхи у порівнянні з DFS.
- Однак DFS може бути корисним, коли не потрібно знаходити найкоротший шлях, або коли важливо дослідити глибокі гілки графа.

## Висновок

Для аналізу графа лондонського метрополітену були використані алгоритми пошуку шляху у глибину (DFS) та у ширину (BFS). Обидва алгоритми були успішно застосовані для знаходження шляхів між двома вказаними станціями - "Acton Town" і "Aldgate East".

Загальна кількість вузлів та ребер у графі була виведена для контролю. Граф був візуалізований для візуального розуміння структури мережі лондонського метрополітену.

-------

DFS та BFS знайшли різні шляхи між вказаними станціями. Це може бути зумовлено різними стратегіями обходу графа. Зазвичай DFS вибирає глибший шлях, тоді як BFS шукає найкоротший шлях. У нашому випадку це відображається у вигляді різних маршрутів між початковою та кінцевою станціями.

DFS може дати більш довгий шлях, оскільки він глибше проникає в граф перед тим, як повертатися назад, тоді як BFS спочатку досліджує всі сусідні вузли на поточному рівні, що часто призводить до знаходження коротших шляхів.

Порівняли результати роботи обох алгоритмів для даного графа, що показало різницю у знайдених шляхах. Враховуючи особливості кожного алгоритму, DFS та BFS знаходять різні маршрути залежно від того, яку стратегію обходу вони використовують.
