import itertools

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

kombinatsiyalar = list(itertools.product(list1, list2))
print(kombinatsiyalar)
```

Kodni ishlatish uchun quyidagicha:

1. `import itertools` satrida `itertools` modulini import qilish uchun foydalanamiz.
2. `list1` va `list2` deygarliklarida ikkita ro'yxat yaratamiz.
3. `itertools.product` funksiyasini chaqiramiz, unga `list1` va `list2` ro'yxatlari beramiz.
4. Natijani `kombinatsiyalar` deygarligiga saqlaymiz.
5. Natijani `print` funksiyasidan foydalanib chiqaramiz.
