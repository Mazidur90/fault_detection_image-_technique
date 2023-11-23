import playfunction as pf

Speed = 100


def main():

    pf.playNote("C4", "quarter", Speed, "sine")
    #pf.sleep(pf.durationDictionary["full"])
    pf.playNote("D4", "quarter", Speed, "sine")
    pf.playNote("E4", "quarter", Speed, "sine")
    pf.playNote("F4", "quarter", Speed, "sine")
    pf.playNote("G4", "quarter", Speed, "sine")
    pf.playNote("A4", "quarter", Speed, "sine")
    pf.playNote("B4", "quarter", Speed, "sine")
    pf.playNote("C5", "quarter", Speed, "sine")

    #pf.playNote(NOTE, DURATION, SPEED, FUNCTION)


if __name__ == '__main__':
    main()