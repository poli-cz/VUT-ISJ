#!/usr/bin/env python3
def first_with_given_key(the_iterable, key=lambda x: x):
    """
    povinný parametr iterable, odpovídající předanému iterovatelnému objektu (může být i nekonečný)
    nepovinný parametr key, odpovídající funkci, která při volání na položce objektu iterable vrátí hodnotu klíče,
    s defaultní hodnotou identické funkce (tedy vrácení přímo položky, na které je funkce zavolána),
    implementované pomocí konstrukce lambda.

    Funkce aplikuje klíč na položky objektu iterable a vybírá (generuje) pouze ty, jejichž klíč se dosud nevyskytl.

    print(tuple(first_with_given_key([[1],[2,3],[4],[5,6,7],[8,9]], key = len))) vypíše ([1], [2, 3], [5, 6, 7]).
    """
    tmp_key_mem=[]
    for i in range(len(the_iterable)):
        if (key(the_iterable[i]) not in tmp_key_mem):
            yield the_iterable[i]
            tmp_key_mem.append(key(the_iterable[i]))
    del tmp_key_mem
