mots = ['eddard', 'catelyn', 'robb', 'sansa', 'arya', 'brandon',
'rickon', 'theon', 'rorbert', 'cersei', 'tywin', 'jaime',
'tyrion', 'shae', 'bronn', 'lancel', 'joffrey', 'sandor',
'varys', 'renly', 'a' ]


def mots_lettre_position (liste, lettre, position) :
    tab_res = []
    position = position - 1
    for i in range (0, len(liste)):
        try:
            gotdata = liste[i][position]
        except IndexError:
            gotdata = 'null'

        if gotdata == lettre:
            tab_res.append(liste[i])
    return tab_res 


print(mots_lettre_position(mots, "a", 2))