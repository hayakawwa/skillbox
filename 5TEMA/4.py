place = int(input('Введите место в списке поступающих: '))
summ = int(input('Введите количество баллов за экзамены: '))

if place <= 10 and summ >= 290:
    print('Поздравляем, вы поступили!') 
    print('Бонусом вам будет начисляться стипендия.')
elif place <= 10 and summ < 290:
    print('Поздравляем, вы поступили!')
    print('Но вам не хватило баллов для стипендии.')
elif place > 10:
    print('К сожалению, вы не поступили.')
    