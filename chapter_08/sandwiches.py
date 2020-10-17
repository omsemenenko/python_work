def sandwiches(*componets):
    print("\nNext components in your sandwiche:")
    for componet in componets:
        print(componet)

sandwiches('first')
sandwiches('first', 'second')
sandwiches('first', 'second', 'third')
