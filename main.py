def jogar():
    imprimir_imagem_abertura()
    imprimir_mensagem_abertura()

    local = int(input('\033[47;1;30m' + """Onde devemos iniciar nossa busca? Digite o número correspondente:
            
                        1 - [As Pirâmides]
            
            
                        2 - [A Esfinge]
            
            
                        3 - [O Templo]\n""" + '\033[0;0m'))

    if (local == 1):
        mostrar_piramides()
        enigma_1 = int(input('\033[46;1;30m' + """Se o filho de Quéops é filho do pai do meu filho, o que eu sou de Quéops?
                                1 - Filho de Quéops
                                2 - Pai de Queóps
                                3 - Avô de Quéops
                                4 - Quéops\n""" + '\033[0;0m'))
        if (enigma_1 == 1):
            mostrar_fragmento_pergaminho()
        else:
            print("Você perdeu!")
    elif (local == 2):
        mostrar_esfinge()
        enigma_2 = int(input('\033[46;1;30m' + """Há dois dias eu tinha 25 anos de idade, mas no ano que vem farei 28.Em que dia nasci?
                              1 - 30 de dezembro
                              2 - 31 de dezembro
                              3 - 1º de janeiro
                              4 - 29 de fevereiro\n""" + '\033[0;0m'))
        if (enigma_2 == 2):
            mostrar_fragmento_pergaminho()
        else:
            print("Você perdeu!")
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
                print("Você perdeu")
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
                    print("Você perdeu!")
            else:
                print("Local inválido! Tente novamente.")
    else:
        print("Local inválido! Tente novamente.")


def imprimir_imagem_abertura():
    print('\033[43;1;30m' + """
   _____          _____                       _   _                                              ______           _   _           
  / ____|        / ____|                     | | (_)                                            |  ____|         (_) | |          
 | |            | (___     __ _   _ __     __| |  _    ___    __ _    ___      _ __     ___     | |__      __ _   _  | |_    ___  
 | |             \___ \   / _` | | '_ \   / _` | | |  / _ \  / _` |  / _ \    | '_ \   / _ \    |  __|    / _` | | | | __|  / _ \ 
 | |____   _     ____) | | (_| | | | | | | (_| | | | |  __/ | (_| | | (_) |   | | | | | (_) |   | |____  | (_| | | | | |_  | (_) |
  \_____| (_)   |_____/   \__,_| |_| |_|  \__,_| |_|  \___|  \__, |  \___/    |_| |_|  \___/    |______|  \__, | |_|  \__|  \___/ 
                                                              __/ |                                        __/ |                  
                                                             |___/                                        |___/                   

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

            No Egito Antigo, a ladra super famosa Carmen Sandiego encontra-se novamente em uma missão quase impossível!

            Ela precisa encontrar os fragmentos do Papiro do Faraó Tutankhamun, para que seja possível desvendar 
            a localização da Relíquia Antiga que pertencia à Rainha Ankhesenamon (esposa de Tutankhamun).

            A primeira tarefa de Carmen foi bastante difícil. Com tantos locais para buscar os fragmentos ela teve 
            que traçar estratégias e buscar informações históricas que indicassem possíveis locais onde esses fragmentos 
            estariam guardados.
            
            Após uma grande busca, ficou acertado que os três possíveis locais seriam: 
            As Pirâmides de Gizé, A Esfinge de Gizé e O Templo de Abu Simbel.

            Carmen sabe que os agentes Zack e Ivy a estão perseguindo e que qualquer passo em falso resultará
            na perda da missão. Por isso, cada escolha deve ser muito bem pensada!\n""" + '\033[0;0m'))

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

def mostrar_fragmento_pergaminho():

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
        / /\ \/     O fragmento de pergaminho foi recuperado!!!    \ \/\ \ 
        \ \/\ \                                                    /\ \/ /
         \/ /\ \                       📜                         / /\/ /
         / /\/ /                                                  \ \/ /\ 
        / /\ \/                                                    \ \/\ \ 
        \ \/\ \.--..--..--..--..--..--..--..--..--..--..--..--..--./\ \/ /
         \/ /\/ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ /\/ /
         / /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\ 
        / /\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \ 
        \ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
         `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\n""" + '\033[0;0m')

jogar()