import random 
cities1 =  ['абакан', 'азов', 'александров', 'алексин', 'альметьевск', 'анапа', 'ангарск', 'анжеро-судженск', 'апатиты',
          'арзамас', 'армавир', 'арсеньев', 'артем', 'архангельск', 'асбест', 'астрахань', 'ачинск', 'балаково', 'балахна', 'балашиха', 'балашов', 'барнаул', 'батайск', 'белгород', 'белебей', 'белово', 'белогорск',
          'белорецк', 'белореченск', 'бердск', 'березники', 'березовский', 'бийск', 'биробиджан', 'благовещенск', 'бор',
          'борисоглебск', 'боровичи', 'братск', 'брянск', 'бугульма', 'буденновск', 'бузулук', 'буйнакск', 'великие луки', 'великий новгород', 'верхняя пышма', 'видное', 'владивосток', 'владикавказ', 'владимир',
          'волгоград', 'волгодонск', 'волжск', 'волжский', 'вологда', 'вольск', 'воркута', 'воронеж', 'воскресенск',
          'воткинск', 'всеволожск', 'выборг', 'выкса', 'вязьма', 'гатчина', 'геленджик', 'георгиевск', 'глазов', 'горно-алтайск', 'грозный', 'губкин', 'гудермес', 'гуково',
          'гусь-хрустальный', 'дербент', 'дзержинск', 'димитровград', 'дмитров', 'долгопрудный', 'домодедово', 'донской', 'дубна', 'евпатория', 'егорьевск', 'ейск', 'екатеринбург', 'елабуга', 'елец', 'ессентуки', 'железногорск', 'жигулевск', 'жуковский', 'заречный', 'зеленогорск', 'зеленодольск', 'златоуст', 'иваново', 'ивантеевка', 'ижевск', 'избербаш', 'иркутск', 'искитим', 'ишим', 'ишимбай', 'казань', 'калининград', 'калуга', 'каменск-уральский', 'каменск-шахтинский', 'камышин', 'канск', 'каспийск',
          'кемерово', 'керчь', 'кинешма', 'кириши', 'киров', 'кирово-чепецк', 'киселевск', 'кисловодск', 'клин', 'клинцы',
          'ковров', 'когалым', 'коломна', 'комсомольск-на-амуре', 'копейск', 'королев', 'кострома', 'котлас', 'красногорск',
          'краснодар', 'краснокаменск', 'краснокамск', 'краснотурьинск', 'красноярск', 'кропоткин', 'крымск', 'кстово',
          'кузнецк', 'кумертау', 'кунгур', 'курган', 'курск', 'кызыл', 'лабинск', 'лениногорск', 'ленинск-кузнецкий', 'лесосибирск', 'липецк', 'лиски', 'лобня', 'лысьва', 'лыткарино',
          'люберцы', 'магадан', 'магнитогорск', 'майкоп', 'махачкала', 'междуреченск', 'мелеуз', 'миасс', 'минеральные воды',
          'минусинск', 'михайловка', 'михайловск', 'мичуринск', 'москва', 'мурманск', 'муром', 'мытищи', 'набережные челны', 'назарово', 'назрань', 'нальчик', 'наро-фоминск', 'находка', 'невинномысск', 'нерюнгри',
          'нефтекамск', 'нефтеюганск', 'нижневартовск', 'нижнекамск', 'нижний новгород', 'нижний тагил', 'новоалтайск',
          'новокузнецк', 'новокуйбышевск', 'новомосковск', 'новороссийск', 'новосибирск', 'новотроицк', 'новоуральск',
          'новочебоксарск', 'новочеркасск', 'новошахтинск', 'новый уренгой', 'ногинск', 'норильск', 'ноябрьск', 'нягань', 'обнинск', 'одинцово', 'озерск', 'октябрьский', 'омск', 'орел', 'оренбург', 'орехово-зуево', 'орск', 'павлово', 'павловский посад', 'пенза', 'первоуральск', 'пермь', 'петрозаводск', 'петропавловск-камчатский',
          'подольск', 'полевской', 'прокопьевск', 'прохладный', 'псков', 'пушкино', 'пятигорск', 'раменское', 'ревда', 'реутов', 'ржев', 'рославль', 'россошь', 'ростов-на-дону', 'рубцовск', 'рыбинск', 'рязань', 'салават', 'сальск', 'самара', 'санкт-петербург', 'саранск', 'сарапул', 'саратов', 'саров', 'свободный',
          'севастополь', 'северодвинск', 'северск', 'сергиев посад', 'серов', 'серпухов', 'сертолово', 'сибай', 'симферополь',
          'славянск-на-кубани', 'смоленск', 'соликамск', 'солнечногорск', 'сосновый бор', 'сочи', 'ставрополь',
          'старый оскол', 'стерлитамак', 'ступино', 'сургут', 'сызрань', 'сыктывкар', 'таганрог', 'тамбов', 'тверь', 'тимашевск', 'тихвин', 'тихорецк', 'тобольск', 'тольятти', 'томск', 'троицк',
          'туапсе', 'туймазы', 'тула', 'тюмень', 'узловая', 'улан-удэ', 'ульяновск', 'урус-мартан', 'усолье-сибирское', 'уссурийск', 'усть-илимск', 'уфа', 'ухта', 'феодосия', 'фрязино', 'хабаровск', 'ханты-мансийск', 'хасавюрт', 'химки', 'чайковский', 'чапаевск', 'чебоксары', 'челябинск', 'черемхово', 'череповец', 'черкесск', 'черногорск', 'чехов',
          'чистополь', 'чита''шадринск', 'шали', 'шахты', 'шуя', 'щекино', 'щелково', 'электросталь', 'элиста', 'энгельс', 'южно-сахалинск', 'юрга', 'якутск', 'ялта', 'ярославль'] # Это список всех городов РФ в алфавитном порядке
cities2 = list (cities1) 
random.shuffle(cities2) 
bot_answer = cities2.pop ()
print ('БОТ: ' + bot_answer)
print('Вам на букву "' + bot_answer [-1] + '".')
print( )

game_over = False
while not game_over: 
    user_answer = input ('ИГРОК: ') 
    if user_answer.lower() [0] != bot_answer [-1]: 
        print ('Неправильно. город должен начинаться с буквы "' + bot_answer [-1] + '"')
        print()
        continue
    elif user_answer not in  cities1:
        print ('Такого города в России не существует! Попробуйте снова.')
        print()
    elif user_answer not in cities2:
        print ('Такой город уже называли.')
        print()
    else:
        print ('Верно!')
        print ('Мне на букву "' + user_answer[-1] + '".')
        print()
        cities2.remove (user_answer) 

        for candidate in cities2: 
            if candidate.lower()[0] == user_answer[-1]:
                bot_answer = candidate 
                cities2.remove (candidate) 
                print ('БОТ: ' + candidate) 
                print ('Вам на букву "' + candidate [-1] + '".')
                print()
                break
        else:
            game_over = True
            print ('Я больше не знаю городов на букву "' + user_answer[-1] + '". Сдаюсь, вы победили!')