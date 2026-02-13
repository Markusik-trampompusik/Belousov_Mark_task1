print('Что надеть?!')

temperature = input('Температура в диапазоне между +20С и +30С ')

if temperature == 'да':
    rain_value = input('Есть осадки? ')
    if rain_value == 'да':
        print('Одень майку/футболку, шорты + дождевик/зонт ')
    elif rain_value == 'нет':
        print('Одень майку/футболку, шорты')

elif temperature == 'нет':
    temperature = input('Температура выше 0С? ')
    if temperature == 'нет':
        print('Одень пуховик')
    elif temperature == 'да':
        rain_value = input('Есть осадки? ')
        if rain_value == 'нет':
            print('Одень пальто, джинсы + шарф')
        elif rain_value == 'да':
            type_rain = input('Осадки сильные? ')
            if type_rain == 'нет':
                print('Одень пальто/легкую куртку + дождевик')
            elif type_rain == 'да':
                print('Одень пальто/легкую куртку + резиновые сапоги, зонт. А, вообще, лучше сидеть дома в такую погоду')
