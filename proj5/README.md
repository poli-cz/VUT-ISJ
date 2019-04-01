Definujte funkci gen_quiz, která bude moci být volána se 4 parametry:
qpool - seznam dvojic otázka a seznam odpovědí
libovolný počet indexů do seznamu qpool
altcodes - sekvence, přes kterou lze projít konstrukcí for a která vrací řetězce, jež se mají ve výsledku předřadit (spolu s ': ') před každou z odpovědí
quiz - vstupní podoba kvízu ve formě seznamu dvojic otázka a seznam formátovaných odpovědí.

Pokud bude některý z indexů do seznamu qpool mimo rozsah, nebo nastane jiná chyba při zpracování konkrétního indexu, má se vypsat:
Ignoring index <číslo> - <text výjimky>
(poněkud nesmyslně na standardní výstup, nikoliv na standardní chybový výstup, aby fungoval doctest)

Pokud bude sekvence altcodes kratší než seznam možných odpovědí v některém ze seznamů, dá se do výsledného kvízu pouze daný počet (lze využít konstrukci zip(altcodes, answers)). Defaultně jsou odpovědi označovány písmeny a je maximálně 6 možných odpovědí, tedy altcodes = 'ABCDEF')

Pokud není zadána vstupní podoba kvízu, vytvoří se nový kvíz s položkami podle definovaných indexů. Defaultní hodnota je tedy prázdný kvíz.
