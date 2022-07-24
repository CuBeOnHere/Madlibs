def madlib():

    adj1 = input("An adjective: ")
    adj2 = input("An adjective: ")
    birdtype = input("A type of bird: ")
    houseroom = input("A room in a house: ")
    verb_pasttense = input("A verb in past tense:")
    verb = input("A verb: ")
    relativename = input("A relative's name: ")
    noun = input('A noun: ')
    liquid = input("A liquid: ")
    ingverb = input("A verb ending in -ing: ")

    madlib = f'It was a {adj1}, cold November day. I woke up to the {adj2} smell of {birdtype} roasting in the {houseroom} downstairs. \
        I {verb_pasttense} down the stairs to see if i could help {verb} the dinner. My mom said, "See if {relativename} needs a fresh {noun}." \
        So I carried a tray of glasses full of {liquid} into the {ingverb} room.'

    print(madlib)
