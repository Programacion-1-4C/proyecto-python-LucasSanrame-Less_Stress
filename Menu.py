import webbrowser
def Menu1():
    webbrowser.open("https://www.friv.com/")
    True
def Menu2():
    webbrowser.open("https://poki.com/es?campaign=14722916619&adgroup=128255170260&extensionid=&targetid=aud-1419837974820:kwd-4005696664&location=1000126&matchtype=e&network=g&device=c&devicemodel=&creative=547316785669&keyword=friv&placement=&target=&gclid=CjwKCAjw6raYBhB7EiwABge5Kg8nw2u8oKG5Txi1m8AvY10nYESkhXShXGRo0WCAMPSoHGvI8CeiEBoC568QAvD_BwE")
    True
def batalla_naval():
    import BatallaNaval
def Criminals():
    import The_Criminals
print("Bienvenido")
print("¿Quiere ingresar en el menu de juegos de Less Stress?")
bienvenida = input("--")
universal = ()
if bienvenida == "si":
    print("¿A que juego quiere entrar?")
    print("En juego disponibles, estan:")
    print("1-La batalla naval")
    print("2-Criminales")
    print("Tambien podemos recomendarte otros menus de juegos")
    print("3-Friv")
    print("4-Poki Games")
    eleccion_de_juego = input("--")
    if eleccion_de_juego == "1":
        batalla_naval()
    if eleccion_de_juego == "2":
        Criminals()
    if eleccion_de_juego == "3":
        Menu1()
    if eleccion_de_juego == "4":
        Menu2()
else:
    print("Gracias por usar Less Stress")