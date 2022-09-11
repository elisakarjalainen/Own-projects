import random

objektit = {"sininen": ["antroposeeni", "biodiversiteetti", "biosfääri", "ekologia", "ekosysteemi", "ekosysteemipalvelut", "fossiiliset polttoaineet", "ilmastonmuutos", "joukkosukupuutto", "kestävä kehitys", "teollistuminen", "väestöräjähdys", "ympäristöekologia", "abioottinen", "bioindikaattori", "bioottinen", "ekolokero", "ilmentäjälaji", "kapea-alainen laji", "laaja-alainen laji", "levinneisyys", "minimitekijä", "sietoisuus", "sopeutuminen", "tasalämpöinen", "vaihtolämpöinen", "ympäristöresurssi"],
            "keltainen": ["ekologinen käytävä", "eksponentiaalinen kasvu", "ikäpyramidi", "kannanvaihtelu", "kuolevuus", "lajinsisäinen kilpailu", "logistinen kasvukäyrä", "metapopulaatio", "muuttoliike", "populaatio", "ravintospesialisti", "reviiri", "syntyvyys", "tiheydensäätely", "ympäristön kantokyky", "ympäristön vastuu", "biomassa", "ehdollinen mutualismi", "ehdoton mutualismi", "eliöyhteisö", "hajottaja", "kilpailu", "koevoluutio", "laidunnus", "lajienvälinen kilpailu", "loinen", "mutualismi", "peto", "pöytävieras", "saalistus", "symbioosi", "syrjäyttävä kilpailu"],
            "oranssi": ["aineiden kierto", "avainlaji", "biomassa", "biomi", "bruttoperustuotanto", "ekologinen pyramidi", "ekologinen tehokkuus", "ekosysteemi", "eloton luonto", "eliöyhteisö", "epäorgaaninen aine", "hajottaja", "jatkotuotanto", "kuluttaja", "nettoperustuotanto", "ohivirtaava energia", "omavarainen", "orgaaninen aine", "perustuotanto", "ravintoketju", "ravintoverkko", "trofiataso", "tuottaja", "ekologinen käytävä", "hallittu hoitamattomuus", "kaupunkiekosysteemi", "kaupunkiekologia", "kaupunkilaji", "kaupunkisuunnittelu", "reunavaikutus", "valosaaste", "viheralue"],
            "ruskea": ["fossiilinen polttoaine", "ilmastonmuutos", "hiilen kierto", "hiilen lyhytaikainen varasto", "hiilen pitkäaikainen varasto", "hiilidioksidi", "hiilijalanjälki", "hiilinielu", "kasvihuoneilmiö", "kasvihuonekaasu", "kasvukausi", "lämpösäteily", "metaani", "vesihöyry", "CFC-yhdisteet", "halonit", "hiukkassäteily", "ionisoimaton säteily", "ionisoiva säteily", "otsonikerros", "radioaktiivinen aine", "sähkömagneettinen säteily", "UV-säteily"],
            "pinkki": ["abioottinen typensidonta", "bioliginen typensidonta", "biologinen hapenkulutus", "denitrifikaatio", "fosforin kierto", "fossiiliset polttoaineet", "hajakuormitus", "happikato", "jätevedenpuhdistus", "pistekuormitus", "rehevöityminen", "sisäinen kuormitus", "suolavesipulssi", "syanobakteeri", "typenkierto", "bioindikaattori", "happamoituminen", "happamuus", "harsuuntuminen", "hiilihappo", "hiilidioksidi", "jäkäläautio", "kaukokulkeutuminen", "kriittinen kuormitus", "kuivalaskeuma", "märkälaskeuma", "rikkidioksidi", "typen oksidi", "DDT", "dioksiini", "elohopea", "kadmium", "kertyminen", "lyijy", "mikromuovi", "orgaaninen ympäristömyrkky", "PCB", "raskasmetalli", "rikastuminen", "supermyrkky", "ympäristömyrkky", "öljy"],
            "vihreä": ["biodiversiteetti", "biopolttoaine", "ekosysteemien monimuotoisuus", "endeeminen laji", "joukkosukupuutto", "koralliriutta", "kosteikko", "lajimonimuotoisuus", "lajinsisäinen monimuotoisuus", "mangrovemetsä", "sattuma", "sukupuuttovelka", "trooppinen metsä", "uhanalaisuusluokitus", "vieraslaji", "ekologinen askelkivi", "ekologinen käytävä", "ekosysteemipalvelu", "eläintarha", "geenipankki", "kansallispuisto", "kasvitieteellinen puutarha", "luonnonpuisto", "monimuotoisuuskeskus", "rauhoittaminen", "sateenvarjolaji", "siemenpankki", "suojelualue", "suojeluohjelma", "ekologinen jalanjälki", "ekologinen kapasiteetti", "ekologinen kestävyys", "ekologinen selkäreppu", "ekososiaalinen sivistys", "ekotehokkuus", "factor-4", "kestävä kehitys", "kiertotalous", "kohtuutalous", "MIPS", "tuotteen elinkaari", "ylikulutuspäivä", "ympäristömerkki"]}

deleted = {"sininen": [], "keltainen": [], "oranssi": [], "ruskea": [], "pinkki": [], "vihreä": []}

print("(C) Elisa Karjalainen 2020" + "\n")

while True:
    x = input("Anna väri: ")
    while x not in objektit:
        x = input("Väriä ei tunnistettu. Tarkista kirjoitusasu peliohjeesta. Anna väri: ")

    y = objektit[x]
    l = len(y)
    f = deleted[x]

    if l == 0:
        u = {x: f}
        objektit.update(u)
        y = objektit[x]
        deleted[x] = []
        f = deleted[x]

    r = random.choice(y)
    print("Selitettävä sana: " + r + "\n")

    z = y.index(r)
    del objektit[x][z]

    f.append(r)
    # print(f)
    # print(y)