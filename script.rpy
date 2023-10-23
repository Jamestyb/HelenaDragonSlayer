# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Helena", color = "#c71b00")
define c = Character ("Cavaleiro", color="#424ef5")
define N = Character("Narrador")
define d = Character ("desconhecido", color = "#6669")





# The game starts here.

label start:
   

    scene bg inicio with dissolve
    

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
        
        c 'Foi … você que derrotou esse dragão … sozinha?'

        menu:
            "Sim, eu que o derrotei.": 
                h 'Sim, eu que o derrotei.'
                jump eu_derrotei

            "Não, eu só acordei aqui.": 
                h 'Não, eu só acordei aqui.'
                jump acordou

            "Eu não sei... estava desacordada.":
                h 'Eu não sei... estava desacordada.'
                jump desacordada
            

    label eu_derrotei:
        c "Isso é impressionante… Deixe-me ajudar, tenha calma!"

        'O cavaleiro se aproximou do cadáver do réptil'

        'Subindo pela asa e a ajudando a descer, sua espada continuou cravada nas costas do animal'
        
        "Os cavaleiros que chegaram ao redor olharam para ti com uma feição de espanto"

        " Certa admiração pelo tamanho de seu feito"

        "(Plateia aplaudindo)"

        jump continueTwo
    


    label acordou:
        c "Ah… que estranho, mas você está bem? Venha, eu te ajudo."
        " O cavaleiro se aproximou do cadáver do réptil"
        " Subindo pela asa e a ajudando a descer, sua espada continuou cravada nas costas do animal. "
        "Os cavaleiros  ao redor olharam para ti com certo susto pela sua resposta, sussurravam entre si enquanto a encaravam curiosos."
        jump continueTwo
    

    label desacordada:
        c "Você só.. acordou ai? será que o Arcano te escolheu?"
        jump ChooseTres
    return






label ChooseTres:
    menu:
        "O “Arcano” me escolheu? ":
            h "O 'Arcano' me escolheu?"
            jump continueFour

        " Como assim o “Arcano”? ":
            h "Como assim o 'Arcano'"
            jump continueFour
        "Eu acho que sim, eu acho… ":
            h "Eu acho que sim, eu acho..."
            jump continueFour



label continueTwo:
    c "(em tom entusiasmado) Isso! é bem capaz que um poder maravilhoso protege a sua alma! "

    "(Plateia aplaudindo )"

    "Os cavaleiros ao redor passaram a aplaudir e comemorar. rapidamente, o cavaleiro que antes fez a pergunta"

    "correu em direção ao corpo do réptil, ajudando você para descer do corpo do mesmo"

    "sua espada, ficou cravada nas costas do animal"
return


label continueFour:
    "O cavaleiro continua a te guiar até um cavalo que usava uma armadura semelhante à que o cavaleiro usava"

    "Ele te ajudou a subir e em seguida subiu segurando as rédeas do animal, ele se virou para ti"
    
    "com um belo sorriso exposto no rosto."

    c "Vai ficar tudo bem, se segure."


    "(Galopar de um cavalo )"

    "O animal passa a galopar rapidamente, sacudindo para os lados. Instintivamente você se segura no cavaleiro, que se concentrava no caminho. "

    "Toda trajetória ambos ficavam em silêncio, dava para ouvir somente os cascos do cavalo golpeando os diversos solos adiante. "

    "Passou cerca 40 minutos até você conseguir ver construções humanas feitas a pedregulho e pequenas sustentações de madeiras, aparentemente os arredores eram pastos onde animais caminhavam,"
    "mas não havia nenhum, somente cercados e poucas pessoas caminhando ao redor. "
    "Logo mais a frente, uma muralha feita de pedregulho que se estendia até onde sua vista não alcançava mais, havia torres dispersas sobre as muralhas."
    c "Seja bem-vinda a capital do reino de Luskov."

    "Os portões estavam abertos e com dois guardas de cada lado, com a aproximação do cavaleiro ambos se afastaram e deram espaço dizendo “Tai, Comandante!” Dentro do reino"
    "era surpreendente de bonito, uma entrada direta para uma fonte d'água com uma estátua com o guerreiro Luskov, um ogro que uniu todas as raças em um único reino"

    "cessando as guerras para se defenderem dos dragões que assolavam todos. O cavalo parou na puxada das rédeas, e então você desceu."

    c "Bem… Acho que não me apresentei devidamente. Me chamo Idhun, Comandante Idhun."
    c "Vou notificar os demais de sua presença, fique por aqui enquanto isso, não vou demorar muito"
    c "fique à vontade para explorar envolta, só não vá muito longe. "

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
            jump luskFive


    label luskOne:
            "Você se aproxima da árvore e se senta escorada no tronco, era reconfortante, mesmo com o rasgo em seu peito pela falta da família, afinal, dragões são considerados criaturas pacíficas que só lutam caso ameaçadas"

            " porque iria ocorrer um ataque coordenado novamente? eram duvidas sem respostas"
            "que só levariam a mais luto e falta de aceitação, duvidas porem que nao deveriam ser deixadas de lado"
            " um Elfo negro estava sentado pouco proximo, tambem escorado na mesma arvore, ele lia um livro de capa marrom"
            "a capa dizia “Encantos e Magias” era de certa forma curioso."

            label luskOneChoose:
                menu:
                    " Esse livro… o que ele conta?":
                        jump luskOneChoosen
                    "Observar em silêncio":
                        jump luskOneChoosenSix
                    return

    label luskOneChoosenFive
        "O Elfo virou suas atenções para você, seus olhos eram castanhos claro semelhante ao dourado" 
        "com a expressão confusa porém atenciosa, ele fechou a capa rapidamente e a fitou, consultando em sua rápida memória para formular uma resposta."
        d "h! ele se trata de contos antigos, magias que os elfos utilizavam no começo do reino, é bem interessante"
        d "mas não parece de entretenimento, e sim de ensinos, mas eu não sou apto a magia."



    label luskOneChoosenSix
        "O Elfo virou suas atenções para você, seus olhos eram castanhos claro semelhante ao dourado" 
        "com a expressão confusa porém atenciosa, ele fechou a capa rapidamente e a fitou, consultando em sua rápida memória para formular uma resposta."
        d "h! ele se trata de contos antigos, magias que os elfos utilizavam no começo do reino, é bem interessante"
        d "mas não parece de entretenimento, e sim de ensinos, mas eu não sou apto a magia."

        
    label luskOneChoosenSeven
        d "Claro, pode ficar com ele se quiser, eu não tenho nenhuma utilidade, e o encontrei no chão largado"
    label luskOneChoosenEight
        d "Talvez eu consiga aprender algo com ele, o comandante acredita que consigo"



    label luskOneChoosenOitoEsete
        "O garoto entregou o livro a você, apenas agradecimentos sinceros poderiam ser trocados pelo livro, mas o rapaz não parecia estar tão interessado em nenhuma “moeda de troca"

return


 
