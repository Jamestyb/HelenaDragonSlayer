# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Helena", color = "#c71b00")
define c = Character ("Cavaleiro", color="#424ef5")
define N = Character("Narrador")





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


return

