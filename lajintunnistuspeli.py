import subprocess  # image opening
from PIL import Image  # image opening
import random  # name randomization

# varmista että kysyttyä ei kysytä uudestaan
objektit = {"lahko Petromyzoniformes, nahkiaiskalat, laji nahkiainen": ["1A", "1B"],
"lahko Anguilliformes, ankeriaskalat, laji ankerias": ["2A", "2B"],
"lahko Clupeiformes, sillikalat, laji silakka": ["3A", "3B"],
"lahko Clupeiformes, sillikalat, laji kilohaili": ["4A", "4B"],
"lahko Cypriniformes, karppikalat, laji lahna": ["5A", "5B"],
"lahko Cypriniformes, karppikalat, laji salakka": ["6A", "6B"],
"lahko Cypriniformes, karppikalat, laji mutu": ["7A", "7B"],
"lahko Cypriniformes, karppikalat, laji särki": ["8A", "8B"],
"lahko Esociformes, haukikalat, laji hauki": ["9A", "9B"],
"lahko Osmeriformes, kuorekalat, laji kuore": ["10A", "10B"],
"lahko Salmoniformes, lohikalat, laji muikku": ["11A", "11B"],
"lahko Salmoniformes, lohikalat, laji siika": ["12A", "12B"],
"lahko Salmoniformes, lohikalat, laji kirjolohi": ["13A", "13B"],
"lahko Salmoniformes, lohikalat, laji lohi": ["14A", "14B"],
"lahko salmoniformes, lohikalat, laji taimen": ["15A", "15B"],
"lahko Gadiformes, turskakalat, laji turska": ["16A", "16B"],
"lahko Gadiformes, turskakalat, laji made": ["17A", "17B"],
"lahko Gasterosteiformes, piikkikalat, laji kolmipiikki": ["18A", "18B"],
"lahko Scorpaeniformes, simppukalat, laji kivisimppu": ["19A", "19B"],
"lahko Perciformes, ahvenkalat, laji kiiski": ["20A", "20B"],
"lahko Perciformes, ahvenkalat, laji ahven": ["21A", "21B"],
"lahko Perciformes, ahvenkalat, laji kuha": ["22A", "22B"],
"lahko Pleuronectiformes, kampelakalat, laji piikkikampela": ["23A", "23B"],
"lahko Pleuronectiformes, kampelakalat, laji kampela tai itämerenkampela": ["24A", "24B"],
"lahko Caudata, pyrstösammakot, laji manteri": ["25A", "25B"],
"lahko Anura, sammakot, laji rupikonna": ["26A", "26B"],
"lahko Anura, sammakot, laji ruskosammakko": ["27A", "27B"],
"lahko Testudines, kilpikonnat": ["28A", "28B"],
"lahko Crocodylia, krokotiilieläimet": ["29A", "29B"],
"lahko Squamata, suomumatelijat, laji sisilisko": ["30A", "30B"],
"lahko Squamata, suomumatelijat, laji rantakäärme": ["31A", "31B"],
"lahko Squamata, suomumatelijat, laji kyy": ["32A", "32B"],
"lahko Anseriformes, sorsalinnut, laji kyhmyjoutsen": ["33A", "33B"],
"lahko Anseriformes, sorsalinnut, laji laulujoutsen": ["34A", "34B"],
"lahko Anseriformes, sorsalinnut, laji merihanhi": ["35A", "35B"],
"lahko Anseriformes, sorsalinnut, laji valkoposkihanhi": ["36A", "36B"],
"lahko Anseriformes, sorsalinnut, laji tavi": ["37A", "37B"],
"lahko Anseriformes, sorsalinnut, laji sinisorsa": ["38A", "38B"],
"lahko Anseriformes, sorsalinnut, laji tukkasotka": ["39A", "39B"],
"lahko Anseriformes, sorsalinnut, laji haahka": ["40A", "40B"],
"lahko Anseriformes, sorsalinnut, laji alli": ["41A", "41B"],
"lahko Anseriformes, sorsalinnut, laji telkkä": ["42A", "42B"],
"lahko Anseriformes, sorsalinnut, laji isokoskelo": ["43A", "43B"],
"lahko Galliformes, kanalinnut, laji pyy": ["44A", "44B"],
"lahko Galliformes, kanalinnut, laji teeri": ["45A", "45B"],
"lahko Galliformes, kanalinnut, laji metso": ["46A", "46B"],
"lahko Galliformes, kanalinnut, laji fasaani": ["47A", "47B"],
"lahko Podicipediformes, uikkulinnut, laji silkkiuikku": ["48A", "48B"],
"lahko Pelecaniformes, pelikaanilinnut, laji merimetso": ["49A", "49B"],
"lahko Ciconiiformes, haikaralinnut, laji harmaahaikara": ["50A", "50B"],
"lahko Accipitriformes, päiväpetolinnut, laji merikotka": ["51A", "51B"],
"lahko Accipitriformes, päiväpetolinnut, laji kanahaukka": ["52A", "52B"],
"lahko Accipitriformes, päiväpetolinnut, laji varpushaukka": ["53A", "53B"],
"lahko Accipitriformes, päiväpetolinnut, laji hiirihaukka": ["54A", "54B"],
"lahko Accipitriformes, päiväpetolinnut, laji maakotka": ["55A", "55B"],
"lahko Falconiformes, jalohaukkalinnut, laji tuulihaukka": ["56A", "56B"],
"lahko Falconiformes, jalohaukkalinnut, laji muuttohaukka": ["57A", "57B"],
"lahko Gruiformes, kurkilinnut, laji nokikana": ["58A", "58B"],
"lahko Gruiformes, kurkilinnut, laji kurki": ["59A", "59B"],
"lahko Charadriiformes, rantalinnut, laji meriharakka": ["60A", "60B"],
"lahko Charadriiformes, rantalinnut, laji töyhtöhyyppä": ["61A", "61B"],
"lahko Charadriiformes, rantalinnut, laji suokukko": ["62A", "62B"],
"lahko Charadriiformes, rantalinnut, laji taivaanvuohi": ["63A", "63B"],
"lahko Charadriiformes, rantalinnut, laji isokuovi": ["64A", "64B"],
"lahko Charadriiformes, rantalinnut, laji rantasipi": ["65A", "65B"],
"lahko Charadriiformes, rantalinnut, laji naurulokki": ["66A", "66B"],
"lahko Charadriiformes, rantalinnut, laji kalalokki": ["67A", "67B"],
"lahko Charadriiformes, rantalinnut, laji selkälokki": ["68A", "68B"],
"lahko Charadriiformes, rantalinnut, laji harmaalokki": ["69A", "69B"],
"lahko Charadriiformes, rantalinnut, laji räyskä": ["70A", "70B"],
"lahko Charadriiformes, rantalinnut, laji kalatiira": ["71A", "71B"],
"lahko Columbiformes, kyyhkylinnut, laji kesykyyhky": ["72A", "72B"],
"lahko Columbiformes, kyyhkylinnut, laji sepelkyyhky": ["73A", "73B"],
"lahko Cuculiformes, käkilinnut, laji käki": ["74A", "74B"],
"lahko Strigiformes, pöllölinnut, laji huuhkaja": ["75A", "75B"],
"lahko Strigiformes, pöllölinnut, laji helmipöllö": ["76A", "76B"],
"lahko Apodiformes, kiitäjälinnut, laji tervapääsky": ["77A", "77B"],
"lahko Piciformes, tikkalinnut, laji palokärki": ["78A", "78B"],
"lahko Piciformes, tikkalinnut, laji käpytikka": ["79A", "79B"],
"lahko Piciformes, tikkalinnut, laji valkoselkätikka": ["80A", "80B"],
"lahko Passeriformes, varpuslinnut, laji kiuru": ["81A", "81B"],
"lahko Passeriformes, varpuslinnut, laji haarapääsky": ["82A", "82B"],
"lahko Passeriformes, varpuslinnut, laji räystäspääsky": ["83A", "83B"],
"lahko Passeriformes, varpuslinnut, laji metsäkirvinen": ["84A", "84B"],
"lahko Passeriformes, varpuslinnut, laji västäräkki": ["85A", "85B"],
"lahko Passeriformes, varpuslinnut, laji tilhi": ["86A", "86B"],
"lahko Passeriformes, varpuslinnut, laji mustarastas": ["87A", "87B"],
"lahko Passeriformes, varpuslinnut, laji räkättirastas": ["88A", "88B"],
"lahko Passeriformes, varpuslinnut, laji laulurastas": ["89A", "89B"],
"lahko Passeriformes, varpuslinnut, laji pajulintu": ["90A", "90B"],
"lahko Passeriformes, varpuslinnut, laji hippiäinen": ["91A", "91B"],
"lahko Passeriformes, varpuslinnut, laji punarinta": ["92A", "92B"],
"lahko Passeriformes, varpuslinnut, laji satakieli": ["93A", "93B"],
"lahko Passeriformes, varpuslinnut, laji kivitasku": ["94A", "94B"],
"lahko Passeriformes, varpuslinnut, laji harmaasieppo": ["95A", "95B"],
"lahko Passeriformes, varpuslinnut, laji kirjosieppo": ["96A", "96B"],
"lahko Passeriformes, varpuslinnut, laji hömötiainen": ["97A", "97B"],
"lahko Passeriformes, varpuslinnut, laji sinitiainen": ["98A", "98B"],
"lahko Passeriformes, varpuslinnut, laji talitiainen": ["99A", "99B"],
"lahko Passeriformes, varpuslinnut, laji närhi": ["100A", "100B"],
"lahko Passeriformes, varpuslinnut, laji harakka": ["101A", "101B"],
"lahko Passeriformes, varpuslinnut, laji naakka": ["102A", "102B"],
"lahko Passeriformes, varpuslinnut, laji varis": ["103A", "103B"],
"lahko Passeriformes, varpuslinnut, laji korppi": ["104A", "104B"],
"lahko Passeriformes, varpuslinnut, laji kottarainen": ["105A", "105B"],
"lahko Passeriformes, varpuslinnut, laji varpunen": ["106A", "106B"],
"lahko Passeriformes, varpuslinnut, laji peippo": ["107A", "107B"],
"lahko Passeriformes, varpuslinnut, laji viherpeippo": ["108A", "108B"],
"lahko Passeriformes, varpuslinnut, laji vihervarpunen": ["109A", "109B"],
"lahko Passeriformes, varpuslinnut, laji pikkukäpulintu": ["110A", "110B"],
"lahko Passeriformes, varpuslinnut, laji punatulkku": ["111A", "111B"],
"lahko Passeriformes, varpuslinnut, laji keltasirkku": ["112A", "112B"],
"lahko Primates, kädelliset, laji ihminen": ["113A", "113B"],
"lahko Primates, kädelliset, laji simpanssi": ["114A", "114B"],
"lahko Lagomorpha, jäniseläimet, laji rusakko": ["115A", "115B"],
"lahko Lagomorpha, jäniseläimet, laji metsäjänis": ["116A", "116B"],
"lahko Rodentia, jyrsijät, laji peltomyyrä": ["117A", "117B"],
"lahko Rodentia, jyrsijät, laji metsämyyrä": ["118A", "118B"],
"lahko Rodentia, jyrsijät, laji piisami": ["119A", "119B"],
"lahko Rodentia, jyrsijät, laji rotta": ["120A", "120B"],
"lahko Rodentia, jyrsijät, laji kotihiiri": ["121A", "121B"],
"lahko Rodentia, jyrsijät, laji orava": ["122A", "122B"],
"lahko Rodentia, jyrsijät, laji liito-orava": ["123A", "123B"],
"lahko Insectivora, hyönteissyöjät, laji siili": ["124A", "124B"],
"lahko Insectivora, hyönteissyöjät, laji metsäpäästäinen": ["125A", "125B"],
"lahko Artiodactyla, sorkkaeläimet, laji villisika": ["126A", "126B"],
"lahko Artiodactyla, sorkkaeläimet, laji kirahvi": ["127A", "127B"],
"lahko Artiodactyla, sorkkaeläimet, laji hirvi": ["128A", "128B"],
"lahko Artiodactyla, sorkkaeläimet, laji metsäpeura": ["129A", "129B"],
"lahko Artiodactyla, sorkkaeläimet, laji poro": ["130A", "130B"],
"lahko Artiodactyla, sorkkaeläimet, laji nauta": ["131A", "131B"],
"lahko Artiodactyla, sorkkaeläimet, laji vuohi": ["132A", "132B"],
"lahko Artiodactyla, sorkkaeläimet, laji mufloni": ["133A", "133B"],
"lahko Chiroptera, lepakot, laji pohjanlepakko": ["134A", "134B"],
"lahko Perissodactyla, kavioeläimet, laji hevonen": ["135A", "135B"],
"lahko Carnivora, petoeläimet, laji leijona": ["136A", "136B"],
"lahko Carnivora, petoeläimet, laji tiikeri": ["137A", "137B"],
"lahko Carnivora, petoeläimet, laji ilves": ["138A", "138B"],
"lahko Carnivora, petoeläimet, laji villikissa": ["139A", "139B"],
"lahko Carnivora, petoeläimet, laji susi": ["140A", "140B"],
"lahko Carnivora, petoeläimet, laji koira": ["141A", "141B"],
"lahko Carnivora, petoeläimet, laji naali": ["142A", "142B"],
"lahko Carnivora, petoeläimet, laji kettu": ["143A", "143B"],
"lahko Carnivora, petoeläimet, laji supikoira": ["144A", "144B"],
"lahko Carnivora, petoeläimet, laji isopanda": ["145A", "145B"],
"lahko Carnivora, petoeläimet, laji karhu": ["146A", "146B"],
"lahko Carnivora, petoeläimet, laji jääkarhu": ["147A", "147B"],
"lahko Carnivora, petoeläimet, laji saukko": ["148A", "148B"],
"lahko Carnivora, petoeläimet, laji ahma": ["149A", "149B"],
"lahko Carnivora, petoeläimet, laji näätä": ["150A", "150B"],
"lahko Carnivora, petoeläimet, laji mäyrä": ["151A", "1501B"],
"lahko Carnivora, petoeläimet, laji kärppä": ["152A", "152B"],
"lahko Carnivora, petoeläimet, laji minkki": ["153A", "153B"],
"lahko Carnivora, petoeläimet, laji norppa": ["154A", "154B"],
"lahko Carnivora, petoeläimet, laji halli": ["155A", "155B"]}

while True:
    length = len(objektit)
    if length == 0:
        break

    x = random.choice(list(objektit.keys()))  # alkuosa
    y = objektit[x]  # kala joka ui # loppuosa
    y2 = random.choice(y)  # 1A etc

    # image location
    loc = "C:/Users/Veera/Lajintunnistuspeli/" + str(y2) + ".jpg"  # muuta osoite pelatessasi eri koneella
    # print(loc)  # hide
    # print(objektit)  # hide

    # open image
    im = Image.open(loc)
    im.show()

    # close the image if answer correct
    vastaus = input("Tunnista: " + "\n")
    subprocess.run(['taskkill', '/f', '/im', "Microsoft.Photos.exe"], stderr=False, stdout=False)

    # Väärin:
    if vastaus != x:
        print("Voisit vielä hieman opiskella. Oikea vastaus olisi ollut: " + x + "\n")

    # Oikein:
    if vastaus == x:
        z = "Fantastista!"
        d = "Huikeaa!"
        e = "Upeaa!"
        t = "Oikein!"
        o = "Oletpa taitava!"
        p = "Hienoa!"
        h = "Fiksua menoa!"
        s = "Jippii!"
        u = "Kivasti meni tällä kertaa. Otetaanpa astetta hankalampi seuraavaksi."
        g = "Oivaa aivotyöskentelyä."
        q = "Einstein kääntyy haudassaan kateudesta."
        n = "Bonustehtävä: Nimeä kyseisen lajin elinympäristö, pääravinnonlähde ja suurin uhka yksilön ja lajin " \
            "olemassaololle."
        print(random.choice([z, d, e, t, o, p, h, s, u, g, q, n]) + "\n")
        idx = y.index(y2)
        y.pop(idx)
        if len(y) == 0:
            del objektit[x]

input("Onnitteluni. Tunnistit kaikki. Pidä yllä hyvää työtä.")
