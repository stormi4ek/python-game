player = {
    'name': '',
    'armor': 0.95,
    'hp': 100,
    'attack': 5,
    'luck': 10,
    'money': 100000,
    'inventory': []
}

enemies = [
        {
        'name': 'Долор', 
        'hp': 50,
        'attack': 20,
        'script': 'Зачем ты здесь? Ты не сможешь меня победить. Принцесса больше не твоя, а чья - не твоя забота. Уходи, пока можешь.',
        'win': 'Ты - достойный противник, но до принцессы тебе всё равно никогда не добраться.',
        'loss': 'Ха! Я же говорил - тебе меня не одолеть. Уходи и не возвращайся.',
        'reward' : 100
    },
    {
        'name': 'Глоксиния',
        'hp': 75,
        'attack': 25,
        'script': 'Не ожидал меня встретить? Я, если честно, тоже не думала, что здесь окажусь. Но, в этот раз сказали защищать долину на пути к замку. В любом случае,  Ты не пройдёшь!',
        'win': ' ты меня победил. ',
        'loss': 'Могли бы просто побеседовать. Ты же и сам знал, что у тебя не получится меня убить.. Возвращайся как-нибудь, здесь довольно одиноко.',
    'reward' : 150
    },

    {
        'name': 'Монсипет',
        'hp': 100,
        'attack': 35,
        'script': 'Как ты смог добраться до сюда?! Как ты вообще посмел думать, что можешь со мной сражаться? Ты слаб! Принцесса будет наша, а ты уйдёшь ни с чем. .',
        'win': 'Ты меня убил...',
        'loss': 'Прощай..'},
        {'name': 'Дерриер',
        'hp': 150,
        'attack': 50,
        'script': 'Слабак... Я уничтожу тебя.',
        'win': 'Ты меня одолел...',
        'loss': 'Я же говорил что ты ничтожество.',
        'reward' : 200},
       { 'name': 'Эстаросса',
        'hp': 250,
        'attack': 50,
        'script': ' Ты слаб! Уходи .',
        'win': 'Ты меня убил...',
        'loss': 'Прощай..',
        'reward' : 500},
    {'name': 'Зелдрис',
        'hp': 350,
        'attack': 75,
        'script': 'Я сильнее. Я убью тебя',
        'win': 'Ты меня убил...',
        'loss': 'Прощай..',
        'reward' : 750},
        {'name': 'Король демонов',
        'hp': 500,
        'attack': 100,
        'script': 'Как ты смог добраться до сюда?! Как ты вообще посмел думать, что можешь со мной сражаться? Ты слаб! Принцесса будет наша, а ты уйдёшь ни с чем. .',
        'win': 'Ты меня убил...',
        'loss': 'Прощай..',
        'reward' : 1000}
]

items = {1 : {'name' : 'Зелье Удачи',
              'price' : 1500},
        2 : {'name' : 'Пропуск тренировки',
            'price' : 500},
        3 : {'name' : 'Кровь Демона',
             'effects' : '+сила атаки, +хп, ухудшение брони на 10%',
             'price' : 3000},
       4  : {'name' : 'Заповедь Благочестия',
             'effects' : 'Урон увеличивается в 1,5 раза',
             'price' : 10000}, 
       5  :  {'name' : 'Заповедь Любви',
              'effects' : 'Урон противников уменьшается в на 33%',
              'price' : 7500},
}


