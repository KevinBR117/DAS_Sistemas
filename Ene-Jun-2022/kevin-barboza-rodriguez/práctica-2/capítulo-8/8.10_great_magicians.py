def show_magicians(magician_names):
    for name in magician_names:
        msg = name.title()
        print(msg)

def make_great(magician_names):
    for i in range(0,len(magician_names)):
        magician_names[i] = "the great " + magician_names[i].title()  
        
magician_names = ['melchor', 'gaspar', 'blatazar']

make_great(magician_names)
show_magicians(magician_names)