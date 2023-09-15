with open('quotes.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)

author = input('вкажіть автора ')

with open('quotes.txt', 'a', encoding='utf-8') as file:
    file.write(f'({author})')

# asking_for_new_text = input('Хочете додати цитату?(так/ні)').lower()
# authors = [author]
# while asking_for_new_text != 'ні':
#     adding_new_text = input('Введіть цитату')
#     with open('quotes.txt','a',encoding='utf-8') as file:
#         file.write(f'{adding_new_text}')


#     adding_author = input('Введіть автора')

#     authors.append(adding_author)
#     with open('quotes.txt','a',encoding='utf-8') as file:
#         file.write(adding_author)    
#     asking_for_new_text = input('Хочете додати цитату?(так/ні)').lower()
# else:
#     print(f'({authors})')