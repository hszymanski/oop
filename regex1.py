#!/usr/bin/env python
# skrypt wyswietla liste kont pocztowych o okreslonej domenie

import re

lista = "mnbvc@xyz.pl, fghjkl30@po.com, ghjkl8@br.cz, edcrfv100@qw.ty, tgbyhnujm56@gmial.com, yhnujm@ert.pl, okmijn@wp.pl, abc@xyz.com, qwerty@wp.pl, qwerty@abc.com, zxc@wp.pl, asdf45@gmail.com, qazwsx12@zxc.com, poiu@gmail.com, mnbvcx67@wp.pl"

wzor = re.compile(r"[a-zA-Z0-9._-]+@[gmail.com]{9}")
wynik = re.findall(wzor, lista)
print "Lista kont pocztowych z domena 'gmail.com':", len(wynik)
for wynik in wynik:
    print wynik
