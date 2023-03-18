text = """Aktuell finden im Erdgeschoss grundlegende Umbaumaßnahmen statt,
sodass die Villa in den Wintermonaten nicht als Kursort zur Verfügung stehen wird.
Die Präsenzkurse weichen daher auf unsere vielseitigen Räume in der Zinnowwald-Grundschule aus.
Generelle Infos zur Villa findet ihr zum Beispiel beim Tagesspiegel."""


suche = input("Welches Wort willst du messen?  ").lower()

txt = text.replace("."," ").replace(","," ").lower().replace("!"," ").replace("?"," ").replace("="," ").replace("+"," ").replace("\n"," ").replace(":"," ").replace(";"," ")
wörter = txt.split(sep=" ")
wörter = list(filter(None, wörter))
def wortanzahlzaehler(wörtchen):
    anzahl = 0
    for wort in wörter:
        if wort == wörtchen:
            anzahl += 1
    return anzahl

#print(wörter)

def wortzaehler(txt):
    wort_anzahl = 1
    for buchstabe in text:
        #print(buchstabe)
        if buchstabe == " ":
            wort_anzahl = wort_anzahl+1
        
    
    #print(text)
    print(str(wort_anzahl)+" Worte")


wortzaehler(text)
print (f"Das Wort {suche} kommt "+str(wortanzahlzaehler(suche))+"-mal vor.")
