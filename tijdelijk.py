Prijzen={"aardbei":"3","vanille":"4","chocolade":"5"}
aanbieding=Prijzen["aardbei"]
reclame_tekst=f"Vandaag in de aanbieding: aardbei-ijs, 1liter-slechts €2.40"
reclame_tekst2=reclame_tekst[:63]
reclame_tekst3=reclame_tekst2.upper()
reclame_tekst4=reclame_tekst3.split()
for el in reclame_tekst4:
    if len(el)>4:
        print(el.upper())
    else:
        print(el.lower())
