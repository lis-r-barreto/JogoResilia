def jogar():
    imprimir_imagem_abertura()
    imprimir_mensagem_abertura()

    personagem = int(input('\033[47;1;30m' + """Para começar o jogo, escolha seu personagem:

    [1] - Carmen Sandiego. Ela é uma ladra mestre e fundadora e líder da Villainous International League of Evil (codinome V.I.L.E.).

    [2] - Zack. Ele é agente da ACME, fala mais de 20 idiomas, é muito bom em ciências e engenharia e tem ótima memória fotográfica.

    [3] - Ivy. Ela é agente da ACME, é teimosa, determinada e muito atlética. Ela também é muito protetora com seu irmão mais novo, Zack.\n""" + '\033[0;0m'))

    if (personagem == 1):
        imprimir_sobre_carmen()
    elif (personagem == 2):
        imprimir_sobre_zack()
    elif (personagem ==3):
        imprimir_sobre_ivy()
    else:
        print("Escolha inválida! Tente novamente.")
    local = int(input('\033[47;1;30m' + """Onde devemos iniciar nossa busca? Digite o número correspondente:
            
                        [1] - As Pirâmides de Gizé
            
            
                        [2] - A Esfinge
            
            
                        [3] - O Templo de Abul Simbel\n""" + '\033[0;0m'))

    if (local == 1):
        mostrar_piramides()
        enigma_1 = int(input('\033[46;1;30m' + """Se o filho de Quéops é filho do pai do meu filho, o que eu sou de Quéops?
                                1 - Filho de Quéops
                                2 - Pai de Queóps
                                3 - Avô de Quéops
                                4 - Quéops\n""" + '\033[0;0m'))
        if (enigma_1 == 1):
            mostrar_pergaminho()
        else:
            mostrar_derrota()
    elif (local == 2):
        mostrar_esfinge()
        enigma_2 = int(input('\033[46;1;30m' + """Há dois dias eu tinha 25 anos de idade, mas no ano que vem farei 28.Em que dia nasci?
                              1 - 30 de dezembro
                              2 - 31 de dezembro
                              3 - 1º de janeiro
                              4 - 29 de fevereiro\n""" + '\033[0;0m'))
        if (enigma_2 == 2):
            mostrar_pergaminho()
        else:
            mostrar_derrota()
    elif (local == 3):
        mostrar_templos()
        enigma_3 = int(input('\033[46;1;30m' + """Se 3 gatos matam 3 ratos em 3 minutos, quanto tempo levam 100 gatos para matar 100 ratos?
                             1 - 9 minutos
                             2 - 10 minutos
                             3 - 3 minutos
                             4 - 100 minutos\n""" + '\033[0;0m'))
        if (enigma_3 == 3):
            templo = int(input('\033[47;1;30m' + """Escolha o templo:
                                1 - [Ramsés II]
                                2 - [Nefertari]\n""" + '\033[0;0m'))
            if (templo == 1):
                mostrar_derrota()
            elif (templo == 2):
                enigma_4 = int(input('\033[46;1;30m' + """No templo de Nefertari haviam 4 relíquias. Entraram 2 ladrões e 
                cada um levou uma relíquia. Quantas relíquias ficaram?
                1 - 2 relíquias
                2 - 3 relíquias
                3 - 4 relíquias
                4 - 6 relíquias\n""" + '\033[0;0m'))
                if (enigma_4 == 4):
                    mostrar_fragmento_pergaminho()
                else:
                    mostrar_derrota()
            else:
                print("Local inválido! Tente novamente.")
    else:
        print("Local inválido! Tente novamente.")


def imprimir_imagem_abertura():
    print('\033[43;1;30m' + """          

                   _
                   __ -
               /     __   \ 
                 /   _ -    |
             | '  | (_)  |                        _L/L
                |  __  /   /                    _LT/l_L_
               \ \  __  /                     _LLl/L_T_lL_
                   -      _T/L              _LT|L/_|__L_|_L_
                        _Ll/l_L_          _TL|_T/_L_|__T__|_l_
                      _TLl/T_l|_L_      _LL|_Tl/_|__l___L__L_|L_
                    _LT_L/L_|_L_l_L_  _'|_|_|T/_L_l__T _ l__|__|L_
                  _Tl_L|/_|__|_|__T _LlT_|_Ll/_l_ _|__[ ]__|__|_l_L_
       jjs_ ___ _LT_l_l/|__|__l_T _T_L|_|_|l/___|_ _|__l__|__|__|_T_l_  ___ _
               . ";;:;.;;:;.;;;;_Ll_|__|_l_/__|___l__|__|___l__L_|_l_LL_
                 .  .:::.:::..:::.";;;;:;;:.;.;;;;,;;:,;;;.;:,;;,;::;:".'
                     . ,::.:::.:..:.: ::.::::;..:,:::,::::.::::.:;:.:..
                        . .:.:::.:::.:::: .::.::. :::.::::..::..:.::. . .
                          . ::.:.: :. .:::  ::::.::.:::.::...:. .:::. .
                              .:. ..   . ::.. .: ::. ::::.:: ::::::.   .
                              .  :.         .. :::.::: ::.::::. ::. .
                                . .           .:. :.. :::. ::..: :.
                    nn_r   nn_r   .              :  .:::.:: ::..:  .
                   /l(\   /l)\      nn_r          . ::. :. : : ..
                   `'"``  ``"``    /\(\              . . .:. . : .
                                   ' "``                  . :. .
                                                           .   .
                                                              .\n""" + '\033[0;0m')

def imprimir_mensagem_abertura():
    print(('\033[47;1;30m' + """            
Nossa aventura no Egito Antigo acompanha os dois irmãos que são agentes da ACME, Zack e Ivy,
em busca de Carmen Sandiego, uma antiga detetive da agência que, entediada com as missões, decide passar
para o outro lado, fundando a V.I.L.E. e reunindo ladrões do mundo inteiro cujo objetivo é roubar itens
raros e preciosos de diferentes países ao redor do globo. 

Por meio de pistas deixadas por Carmen, Zack e Ivy tentam encontrá-la antes que ela possa concluir seus
planos de roubar mais um artefato valioso, a Relíquia Antiga que pertencia à Rainha Ankhesenamon.\n""" + '\033[0;0m'))


def imprimir_sobre_carmen():
    print('\033[43;1;30m' + """Você escolheu a personagem Carmen Sandiego!

No Egito Antigo, a ladra super famosa Carmen Sandiego encontra-se novamente em uma missão quase impossível!
Ela precisa encontrar o Papiro do Faraó Tutankhamun, para que seja possível desvendar a localização da 
Relíquia Antiga que pertencia à Rainha Ankhesenamon. A primeira tarefa de Carmen foi bastante difícil.
Com tantos locais para buscar o papiro, ela teve que traçar estratégias e buscar informações históricas
que indicassem possíveis locais onde ele poderia estar guardado. Após uma grande busca, ficou acertado que
os três possíveis locais seriam: As Pirâmides de Gizé, A Esfinge de Gizé e O Templo de Abu Simbel. 
Carmen sabe que os agentes Zack e Ivy a estão perseguindo e que qualquer passo em falso resultará na perda da missão.
Por isso, cada escolha deve ser muito bem pensada!\n""" + '\033[0;0m')


def imprimir_sobre_zack():
    print('\033[43;1;30m' + """Você escolheu o personagem Zack!
    
No Egito Antigo, o agente Zack encontra-se novamente em uma missão quase impossível: 
localizar a ladra super famosa Carmen Sandiego. Ele precisa encontrar o Papiro do Faraó Tutankhamun, 
para que seja possível desvendar a localização da Relíquia Antiga que pertencia à Rainha Ankhesenamon 
(esposa de Tutankhamun) e impedir que Carmen Sandiego a capture. A primeira tarefa dos nossos agentes 
foi bastante difícil. Com tantos locais para buscar o papiro, eles tiveram que traçar estratégias e 
buscar informações históricas que indicassem possíveis locais onde ele poderia estar guardado. Após 
uma grande busca, ficou acertado que os três possíveis locais seriam: As Pirâmides de Gizé, A Esfinge
de Gizé e O Templo de Abu Simbel. Zack e Ivy sabem que perseguir a superladra Carmen Sandiego não é uma
tarefa fácil e que qualquer passo em falso resultará na perda da missão. Por isso, cada escolha deve 
ser muito bem pensada!\n""" + '\033[0;0m')


def imprimir_sobre_ivy():
    print('\033[43;1;30m' + """Você escolheu a personagem Ivy! 

No Egito Antigo, a agente Ivy encontra-se novamente em uma missão quase
impossível: localizar a ladra super famosa Carmen Sandiego. Ela precisa encontrar
o Papiro do Faraó Tutankhamun, para que seja possível desvendar a localização da Relíquia
Antiga que pertencia à Rainha Ankhesenamon (esposa de Tutankhamun) e impedir que Carmen Sandiego
a capture. A primeira tarefa dos nossos agentes foi bastante difícil. Com tantos locais para buscar
o papiro, eles tiveram que traçar estratégias e buscar informações históricas que indicassem possíveis
locais onde ele poderia estar guardado. Após uma grande busca, ficou acertado que os três possíveis locais
seriam: As Pirâmides de Gizé, A Esfinge de Gizé e O Templo de Abu Simbel. Zack e Ivy sabem que perseguir a 
superladra Carmen Sandiego não é uma tarefa fácil e que qualquer passo em falso resultará na perda da missão.
Por isso, cada escolha deve ser muito bem pensada!\n""" + '\033[0;0m')


def mostrar_esfinge():
    print('\033[43;1;30m' + """
                   ___
                 ."///".
                /|<> <>!\ 
               /-|  ^  !-\ 
              /-- \_=_/ --\ 
              )---| W |---(
             /-\--| W |--/-\ 
            (_-_--|_-_|--___)
           (-___  -_-- _-- -_)
           )-_ _--_ _ ___--__|
           (___ --__  __ __--(
          /-_  / __ -_ -__  \_\ 
         _>/  -- /|___| _ \ -_ )
        /--  _ - _/ _ \>\ -  -- \ 
       ( / / /   > |~l \   \ \ \_)
    jjs| |-' | |/  ''''  \| |   |_|
       L_|_|_|_/         L_L_|_l_)\n""" + '\033[0;0m')

def mostrar_piramides():
    print('\033[43;1;30m' + """
                                           _L/L
                                         _LT/l_L_
                                       _LLl/L_T_lL_
                   _T/L              _LT|L/_|__L_|_L_
                 _Ll/l_L_          _TL|_T/_L_|__T__|_l_
               _TLl/T_l|_L_      _LL|_Tl/_|__l___L__L_|L_
             _LT_L/L_|_L_l_L_  _'|_|_|T/_L_l__T _ l__|__|L_
           _Tl_L|/_|__|_|__T _LlT_|_Ll/_l_ _|__[ ]__|__|_l_L_
    jjs_ _LT_l_l/|__|__l_T _T_L|_|_|l/___|__ | _l__|_ |__|_T_L_  __

                           nn_r   nn_r                 __
                     __   /l(\   /l)\      nn_r
               __                         /\(\    __\n""" + '\033[0;0m')



def mostrar_templos():
    print('\033[43;1;30m' + """
     ][][][][][]                                    [][][][][][
     |^^^^^|                                            |^^^^^|
     |^^^^^|                                   |\_/|    |^^^^^|
     |^^^^^|  .::Z::.         .   .            | | |    |^^^^^|
     |^^^^^|  :'^ ^':           . *            (=|=)    |^^^^^|
     |^^^^^|  ::)^(::         .   .  (         |\^/|    |^^^^^|
     |^^^^^| /''\ /''\       ( *). ) )(        | ' |    |^^^^^|
     |^^^^^| | / @ \ |       )( ( )(( )        )\ /(    |^^^^^|
     |^^^^^| ||);;;(||      ( ( )((() )       /  |  \   |^^^^^|
     |^^^^^__|||   |||__    _) )() ( (_       |  @  |   |^^^^^|
     |^^^^^|'-'|   |`-'     \[@]T@S[@]/       |  |  |   |^^^^^|
     |^^^^^|   | | |         |,-~~\  |        | / \ |   |^^^^^|
     |^^^^^|   | | |        /_ (   \ _\       | | | |   |^^^^^|
     |^^^^^|   | | |       |    |\\ \  |      | | | |   |^^^^^|
     |^^^^^|   |/|\|        \\/_]_]\\\/       |_|_|_|   |^^^^^|
     |^^^^^|    |||           ))))((((       (_______`\ |^^^^^|
     |^^^^^|    |||           [][][][]      [�][�][�][�]|^^^^^|
     |^^^^^|____'''_________[][][][][][]___/L@L@L@L@L@L@\^^^^^|
     |^^^^^|____________________________________________|^^^^^|
     |^^^^^|____________________________________________|^^^^^|
     |^^^^^|____________________________________________|^^^^^|
     :][:][:]_____(______________________________)______[:][:][:
     )))))))))    )(                             )(    (((((((((
     ))))))))))) (||)                           (||) (((((((((((\n""" + '\033[0;0m')

def mostrar_pergaminho():

    print('\033[45;1;30m' + """
         .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--.
        / .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \ 
        \ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/ / 
         \/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /
         / /\/ /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /\/ /\ 
        / /\ \/`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\ \/\ \ 
        \ \/\ \                                                    /\ \/ /
         \/ /\ \              Você venceu o jogo!!!                / /\/ /
         / /\/ /                                                   \ \/ /\ 
        / /\ \/            O pergaminho foi encontrado!            \ \/\ \ 
        \ \/\ \                                                    /\ \/ /
         \/ /\ \                                                  / /\/ /
         / /\/ /                                                  \ \/ /\ 
        / /\ \/                                                    \ \/\ \ 
        \ \/\ \.--..--..--..--..--..--..--..--..--..--..--..--..--./\ \/ /
         \/ /\/ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ /\/ /
         / /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\ 
        / /\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \ 
        \ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
         `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\n""" + '\033[0;0m')

def mostrar_derrota():
    print('\033[45;1;30m' + """
         .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--.
        / .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \ 
        \ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/ / 
         \/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /
         / /\/ /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /\/ /\ 
        / /\ \/`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\ \/\ \ 
        \ \/\ \                                                    /\ \/ /
         \/ /\ \                Não foi dessa vez!!!                / /\/ /
         / /\/ /                                                   \ \/ /\ 
        / /\ \/                  Tente novamente!                  \ \/\ \ 
        \ \/\ \                                                    /\ \/ /
         \/ /\ \                                                  / /\/ /
         / /\/ /                                                  \ \/ /\ 
        / /\ \/                                                    \ \/\ \ 
        \ \/\ \.--..--..--..--..--..--..--..--..--..--..--..--..--./\ \/ /
         \/ /\/ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ /\/ /
         / /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\ 
        / /\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \ 
        \ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
         `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\n""" + '\033[0;0m')

jogar()


nova_rodada = int(input('\033[45;1;30m' + """Deseja jogar novamente?
    [1] - Sim
    [2] - Não\n""" + '\033[0;0m'))

if (nova_rodada == 1):
    jogar()
else:
    print('\033[45;1;30m' + "Espero te ver em breve! Até mais!" + '\033[0;0m')