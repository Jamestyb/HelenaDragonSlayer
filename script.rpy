# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Helena", color = "#c71b00")
define c = Character ("Cavaleiro", color="#424ef5")
define N = Character("Narrador")
define d = Character ("desconhecido", color = "#6669")

image helena normal = "helenaNormal.png"
image helena treino = "helenaTreino.png"
image cavaleiro = "cavaleiro.png"


# The game starts here.

label start:

    scene reino with dissolve
    

    "Você se chama Helena, uma moça de 28 anos, que cresceu trabalhando em um vilarejo afastado da capital do seu reino."
    
    "Cuidava de plantas para vendê-las à nobreza  da capital, seu marido Marcus e seu filho Lucius ajudavam em carregá-las para o rei."

    "De repente, em um entardecer tranquilo todo vilarejo foi incendiado, por conta de um ataque de vários dragões cuspidores de fogos."

    "Você entrou em sua casa que já estava cercada de chamas, sua família deitada sobre a cama, soterrada de escombros."

    "Madeiras em labaredas se intensificaram a cada segundo que perdia analisando a situação."

    "Você sem pensar duas vezes mais, avança na direção de ambos, antes de se aproximar, o teto cai sobre eles juntos."

    "Em seguida, a pata de um enorme dragão pisa sobre ambos, afundando eles sobre a terra."

    "Tal dragão era de uma cor vermelha bem forte, suas asas espalharam brasas que se ampliaram ao ambiente com rapidez, ele a fitou, e encarou em silêncio. "

    "Aos pés de Helena, a espada de seu marido, você a segura e se levanta em uma posição torta de combate."
    


    menu:
        'Atacar o dragão': 
            jump Atacar_o_dragão
        "Ficar na defensiva": 
            jump Ficar_na_defensiva



    label Atacar_o_dragão:
        'Você aperta firmemente o cabo de sua arma, sem pensar duas vezes, corre na direção do dragão '

        'Porém de surpresa, a cauda do réptil se desloca quebrando algumas madeiras da residência no processo'

        'Chegando a um impacto grosseiro e firme em seu corpo, que é atirado para uma das pilastras do local'

        'Você fica inconsciente, tudo que se lembra era de tudo ficar vermelho, como se estivesse rodeado de chamas que não te machucaram'


        'Enfim você desperta, com o sol raiando em seu rosto, reparando ao redor, todo vilarejo com destruído, com fumaças brancas em alguns pontos espalhados'


        'Olhando abaixo, o dragão que matou sua família, estava morto, com a sua espada cravada nas costas dele'

        'As asas com vários cortes falhos espalhados e ao corpo do réptil sangue escorria. Um cavaleiro montado a um cavalo negro surge'

        ' Usava uma armadura preta, e um cabelo loiro, ele se aproxima espantado com a cena na sua frente'

        'O mesmo ficou reparando por uns instantes em um silêncio, engolindo o seco, ele pergunta a você'
        jump continue
    return





    label Ficar_na_defensiva:
        'Você se posiciona, segurando a espada com firmeza e encarando o réptil nos olhos, porém, um ataque surpresa em meio ao fogo pelo seu inimigo é realizado'

        'A cauda dele se desloca quebrando as madeiras da residência no processo, e logo chega a um impacto grosseiro e firme em seu corpo'

        'Que é atirado para uma das pilastras do local, você fica inconsciente, tudo que se lembra era de tudo ficar vermelho, como se estivesse rodeado de chamas que não te machucaram'

        'Enfim você desperta, com o sol raiando em seu rosto, reparando ao redor, todo vilarejo com destruído'

        ' Com fumaças brancas em alguns pontos espalhados, olhando abaixo, o dragão que matou sua família, estava morto, com a sua espada cravada nas costas dele'

        'As asas com vários cortes falhos espalhados e ao corpo do réptil sangue escorria. Um cavaleiro montado a um cavalo negro surge, usava uma armadura preta'

        'E um cabelo loiro, ele se aproxima espantado com a cena na sua frente. O mesmo ficou reparando por uns instantes em um silêncio, engolindo o seco, ele pergunta a você'
        jump continue
    return

   
    

    label continue:
        show cavaleiro at right
        with dissolve
        c 'Foi … você que derrotou esse dragão … sozinha?'
        hide cavaleiro
        menu:
            "Sim, eu que o derrotei.": 
               show helena normal at left
               with dissolve
               h 'Sim, eu que o derrotei'
               hide helena normal
               jump eu_derrotei

            "Não, eu só acordei aqui.": 
               show helena normal at left
               with dissolve
               h 'Não, eu só acordei aqui.'
               hide helena normal
               jump acordou

            "Eu não sei... estava desacordada.":
               show helena normal at left
               with dissolve
               h 'Eu não sei... estava desacordada.'
               hide helena normal
               jump desacordada
            

    label eu_derrotei:
        show cavaleiro at right
        with dissolve
        c "Isso é impressionante… Deixe-me ajudar, tenha calma!"
        hide cavaleiro
        'O cavaleiro se aproximou do cadáver do réptil'

        'Subindo pela asa e a ajudando a descer, sua espada continuou cravada nas costas do animal'
        
        "Os cavaleiros que chegaram ao redor olharam para ti com uma feição de espanto"

        " Certa admiração pelo tamanho de seu feito"

        "(Plateia aplaudindo)"

        jump continueTwo
    return


    label acordou:
        show cavaleiro at right
        with dissolve
        c "Ah… que estranho, mas você está bem? Venha, eu te ajudo."
        hide cavaleiro
        " O cavaleiro se aproximou do cadáver do réptil"
        " Subindo pela asa e a ajudando a descer, sua espada continuou cravada nas costas do animal. "
        "Os cavaleiros  ao redor olharam para ti com certo susto pela sua resposta, sussurravam entre si enquanto a encaravam curiosos."
        jump continueTwo
    return

    label desacordada:
    show cavaleiro at right
    with dissolve
    c "Você só.. acordou ai? será que o Arcano te escolheu?"
    hide cavaleiro
    jump ChooseTres
    return






label ChooseTres:
    menu:
        "O “Arcano” me escolheu? ":
            show helena normal at left
            with dissolve
            h "O 'Arcano' me escolheu?"
            hide helena normal
            jump continueFour

        " Como assim o “Arcano”? ":
            show helena normal at left
            with dissolve
            h "Como assim o 'Arcano'"
            hide helena normal
            jump continueFour
        "Eu acho que sim, eu acho… ":
            show helena normal at left
            with dissolve
            h "Eu acho que sim, eu acho..."
            hide helena normal
            jump continueFour
return


label continueTwo:
    show cavaleiro at right
    with dissolve
    c "(em tom entusiasmado) Isso! é bem capaz que um poder maravilhoso protege a sua alma! "
    hide cavaleiro
    "(Plateia aplaudindo )"

    "Os cavaleiros ao redor passaram a aplaudir e comemorar. rapidamente, o cavaleiro que antes fez a pergunta"

    "correu em direção ao corpo do réptil, ajudando você para descer do corpo do mesmo"

    "sua espada, ficou cravada nas costas do animal"
    jump continueFour
return


label continueFour:
    "O cavaleiro continua a te guiar até um cavalo que usava uma armadura semelhante à que o cavaleiro usava"

    "Ele te ajudou a subir e em seguida subiu segurando as rédeas do animal, ele se virou para ti"
    
    "com um belo sorriso exposto no rosto."
    show cavaleiro at right
    with dissolve
    c "Vai ficar tudo bem, se segure."
    hide cavaleiro

    "(Galopar de um cavalo )"

    "O animal passa a galopar rapidamente, sacudindo para os lados. Instintivamente você se segura no cavaleiro, que se concentrava no caminho. "

    "Toda trajetória ambos ficavam em silêncio, dava para ouvir somente os cascos do cavalo golpeando os diversos solos adiante. "

    "Passou cerca 40 minutos até você conseguir ver construções humanas feitas a pedregulho e pequenas sustentações de madeiras, aparentemente os arredores eram pastos onde animais caminhavam,"
    "mas não havia nenhum, somente cercados e poucas pessoas caminhando ao redor. "
    "Logo mais a frente, uma muralha feita de pedregulho que se estendia até onde sua vista não alcançava mais, havia torres dispersas sobre as muralhas."
    show cavaleiro at right
    with dissolve
    c "Seja bem-vinda a capital do reino de Luskov."
    hide cavaleiro

    "Os portões estavam abertos e com dois guardas de cada lado, com a aproximação do cavaleiro ambos se afastaram e deram espaço dizendo “Tai, Comandante!” Dentro do reino"
    "era surpreendente de bonito, uma entrada direta para uma fonte d'água com uma estátua com o guerreiro Luskov, um ogro que uniu todas as raças em um único reino"

    "cessando as guerras para se defenderem dos dragões que assolavam todos. O cavalo parou na puxada das rédeas, e então você desceu."
    show cavaleiro at right
    with dissolve
    c "Bem… Acho que não me apresentei devidamente. Me chamo Idhun, Comandante Idhun."
    c "Vou notificar os demais de sua presença, fique por aqui enquanto isso, não vou demorar muito"
    c "fique à vontade para explorar envolta, só não vá muito longe. "
    hide cavaleiro
    "( Galopar do cavalo curto logo some )"

    "Você observa o arredor, um pouco perdida com sua situação, afinal todos eram desconhecidos, você não tinha muitas opções a não ser esperar pacientemente. "
    "Apesar de que, o ambiente não  parecia nada hostil, havia crianças correndo e brincando, e por se tratar da capital de seu reino"
    "poucos elfos, ogros e até mesmo fadas com traços animalescos apareciam, bem diferentes um dos outros"
    "todos nem davam muita importância, você estava muito bem disfarçada entre os demais. Além da fonte de Luskov"
    "tinha uma lojinha de carroça a madeira, com uma moça atendendo algumas crianças"
    "uma árvore próxima a carroça dando uma fuga da luz quente que o sol emitia.  Poucas opções se abrirão a você ao atender sua curiosidade."

    label luskovv:
    menu:
        " Aguardar o Cavalheiro abaixo da sombra da árvore  ":
            jump luskOne

        "  Observar os produtos da lojinha  ":
            jump luskTwo
        "se-sentar a beira da fonte ":
            jump luskFour
        "Ir mais a fundo do reino":
            jump luskThree


    label luskOne:
            "Você se aproxima da árvore e se senta escorada no tronco, era reconfortante, mesmo com o rasgo em seu peito pela falta da família, afinal, dragões são considerados criaturas pacíficas que só lutam caso ameaçadas"

            " porque iria ocorrer um ataque coordenado novamente? eram duvidas sem respostas"
            "que só levariam a mais luto e falta de aceitação, duvidas porem que nao deveriam ser deixadas de lado"
            " um Elfo negro estava sentado pouco proximo, tambem escorado na mesma arvore, ele lia um livro de capa marrom"
            "a capa dizia “Encantos e Magias” era de certa forma curioso."

            label luskOneChoose:
            menu:
                "Eu adoraria aprender, posso vê-lo?":
                    jump luskOneChoosenSeven
                "Talvez eu consiga aprender algo com ele, o comandante acredita que consigo":
                    jump luskOneChoosenSix
            return

    label luskOneChoosenFive:
    d "Claro, pode ficar com ele se quiser, eu não tenho nenhuma utilidade, e o encontrei no chão largado." 


    label luskOneChoosenSix:
        d "O comandante a conhece?? nossa, se isso vai ajudar você e o comandante, por favor, fique! Não se preocupe, não fará falta."
        jump luskOneChoosenOitoEsete

    label luskOneChoosenSeven:
        d "Claro, pode ficar com ele se quiser, eu não tenho nenhuma utilidade, e o encontrei no chão largado"
        jump luskOneChoosenOitoEsete




    label luskOneChoosenOitoEsete:
        show livro at center
        "O garoto entregou o livro a você, apenas agradecimentos sinceros poderiam ser trocados pelo livro, mas o rapaz não parecia estar tão interessado em nenhuma 'moeda de troca'. "
        "O livro é bem longo, mas a introdução conta detalhes interessantes. A escrita é a seguinte"
        "'A Mana é a essência presente na vida, tudo ao seu redor possui mana percorrendo seu espírito de ser ou não ser. As consideradas raças superiores'"
        "'Ou até mesmo o rio que percorre toda natureza possui um espírito ou alma, um grão de areia da praia possui um pequeno espírito'"
        "'que é feito à base da mana. Ou seja, existe uma ordem natural entre a natureza e tudo que tem origem dela. Com isso em mente, com uma energia invisível percorrendo a sua alma'"
        "'As raças superiores passaram a manipular essa energia espiritual e desenvolvê-la para suas magias e feitiços. Desta maneira'"
        "'As espécies inteligentes foram capazes de desenvolver magias através da energia de nosso espírito.'"
        show helena normal at left
        h "Uau, parece meio… impossível"
        hide helena normal
    return


    label luskTwo:
        "Você se aproxima de uma lojinha de carroça, feita com várias tábuas de madeiras, inclusive as rodas era feitas de madeira."
        "Existiam dois pequenos andares que não tapam a visão da atendente. Os andares apresentavam conteúdos diferentes"
        " você infelizmente não tinha moedas para uma compra, mas uma olhada não fazia mal a ninguém."
        "A cultura de seu vilarejo era mórbida, sem muitas coisas a venda além de refeições e materiais de construções. A lojinha a sua frente possuía várias flores no segundo andar"
        "Até mesmo algumas bem semelhantes às que você vendiam com sua família."
        "No andar de cima existiam alguns colares, bem diferentes entre si, com pedras coloridas e alguns símbolos, como as asas de uma fada"
        "presas de um ogro, entre outros símbolos que representam as espécies adversas que existem no reino de Luskov."
    return

    label luskThree:
        show livro at center
        "Você caminha mais a frente, olhando o arredor. as residências são coladas umas nas outras, bem altas com paredes grossas e extensas."
        "A maioria das casas eram feitas de pedregulho e completadas com pilastras e pisos de madeira, durante sua breve explorada, é possível notar várias criaturas caminhando, as raças superiores."
        "Tais raças são as que vivem no reino e participam como um dos reis, o reino de Luskov possui 5 reis"
        "sendo eles um de cada raça superior, e pelo seu caminho"
        "você pode notar um Ogro que media cerca de 2 metros de altura, sua pele era verde"
    return
