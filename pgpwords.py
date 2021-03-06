#!/usr/bin/env python3

import sys
import argparse
import secrets

wordlist = { 
    "00": ("aardvark" , "adroitness" ),
    "01": ("absurd"   , "adviser"    ),
    "02": ("accrue"   , "aftermath"  ),
    "03": ("acme"     , "aggregate"  ),
    "04": ("adrift"   , "alkali"     ),
    "05": ("adult"    , "almighty"   ),
    "06": ("afflict"  , "amulet"     ),
    "07": ("ahead"    , "amusement"  ),
    "08": ("aimless"  , "antenna"    ),
    "09": ("algol"    , "applicant"  ),
    "0a": ("allow"    , "apollo"     ),
    "0b": ("alone"    , "armistice"  ),
    "0c": ("ammo"     , "article"    ),
    "0d": ("ancient"  , "asteroid"   ),
    "0e": ("apple"    , "atlantic"   ),
    "0f": ("artist"   , "atmosphere" ),
    "10": ("assume"   , "autopsy"    ),
    "11": ("athens"   , "babylon"    ),
    "12": ("atlas"    , "backwater"  ),
    "13": ("aztec"    , "barbecue"   ),
    "14": ("baboon"   , "belowground"),
    "15": ("backfield", "bifocals"   ),
    "16": ("backward" , "bodyguard"  ),
    "17": ("banjo"    , "bookseller" ),
    "18": ("beaming"  , "borderline" ),
    "19": ("bedlamp"  , "bottomless" ),
    "1a": ("beehive"  , "bradbury"   ),
    "1b": ("beeswax"  , "bravado"    ),
    "1c": ("befriend" , "brazilian"  ),
    "1d": ("belfast"  , "breakaway"  ),
    "1e": ("berserk"  , "burlington" ),
    "1f": ("billiard" , "businessman"),
    "20": ("bison"    , "butterfat"  ),
    "21": ("blackjack", "camelot"    ),
    "22": ("blockade" , "candidate"  ),
    "23": ("blowtorch", "cannonball" ),
    "24": ("bluebird" , "capricorn"  ),
    "25": ("bombast"  , "caravan"    ),
    "26": ("bookshelf", "caretaker"  ),
    "27": ("brackish" , "celebrate"  ),
    "28": ("breadline", "cellulose"  ),
    "29": ("breakup"  , "certify"    ),
    "2a": ("brickyard", "chambermaid"),
    "2b": ("briefcase", "cherokee"   ),
    "2c": ("burbank"  , "chicago"    ),
    "2d": ("button"   , "clergyman"  ),
    "2e": ("buzzard"  , "coherence"  ),
    "2f": ("cement"   , "combustion" ),
    "30": ("chairlift", "commando"   ),
    "31": ("chatter"  , "company"    ),
    "32": ("checkup"  , "component"  ),
    "33": ("chisel"   , "concurrent" ),
    "34": ("choking"  , "confidence" ),
    "35": ("chopper"  , "conformist" ),
    "36": ("christmas", "congregate" ),
    "37": ("clamshell", "consensus"  ),
    "38": ("classic"  , "consulting" ),
    "39": ("classroom", "corporate"  ),
    "3a": ("cleanup"  , "corrosion"  ),
    "3b": ("clockwork", "councilman" ),
    "3c": ("cobra"    , "crossover"  ),
    "3d": ("commence" , "crucifix"   ),
    "3e": ("concert"  , "cumbersome" ),
    "3f": ("cowbell"  , "customer"   ),
    "40": ("crackdown", "dakota"     ),
    "41": ("cranky"   , "decadence"  ),
    "42": ("crowfoot" , "december"   ),
    "43": ("crucial"  , "decimal"    ),
    "44": ("crumpled" , "designing"  ),
    "45": ("crusade"  , "detector"   ),
    "46": ("cubic"    , "detergent"  ),
    "47": ("dashboard", "determine"  ),
    "48": ("deadbolt" , "dictator"   ),
    "49": ("deckhand" , "dinosaur"   ),
    "4a": ("dogsled"  , "direction"  ),
    "4b": ("dragnet"  , "disable"    ),
    "4c": ("drainage" , "disbelief"  ),
    "4d": ("dreadful" , "disruptive" ),
    "4e": ("drifter"  , "distortion" ),
    "4f": ("dropper"  , "document"   ),
    "50": ("drumbeat" , "embezzle"   ),
    "51": ("drunken"  , "enchanting" ),
    "52": ("dupont"   , "enrollment" ),
    "53": ("dwelling" , "enterprise" ),
    "54": ("eating"   , "equation"   ),
    "55": ("edict"    , "equipment"  ),
    "56": ("egghead"  , "escapade"   ),
    "57": ("eightball", "eskimo"     ),
    "58": ("endorse"  , "everyday"   ),
    "59": ("endow"    , "examine"    ),
    "5a": ("enlist"   , "existence"  ),
    "5b": ("erase"    , "exodus"     ),
    "5c": ("escape"   , "fascinate"  ),
    "5d": ("exceed"   , "filament"   ),
    "5e": ("eyeglass" , "finicky"    ),
    "5f": ("eyetooth" , "forever"    ),
    "60": ("facial"   , "fortitude"  ),
    "61": ("fallout"  , "frequency"  ),
    "62": ("flagpole" , "gadgetry"   ),
    "63": ("flatfoot" , "galveston"  ),
    "64": ("flytrap"  , "getaway"    ),
    "65": ("fracture" , "glossary"   ),
    "66": ("framework", "gossamer"   ),
    "67": ("freedom"  , "graduate"   ),
    "68": ("frighten" , "gravity"    ),
    "69": ("gazelle"  , "guitarist"  ),
    "6a": ("geiger"   , "hamburger"  ),
    "6b": ("glitter"  , "hamilton"   ),
    "6c": ("glucose"  , "handiwork"  ),
    "6d": ("goggles"  , "hazardous"  ),
    "6e": ("goldfish" , "headwaters" ),
    "6f": ("gremlin"  , "hemisphere" ),
    "70": ("guidance" , "hesitate"   ),
    "71": ("hamlet"   , "hideaway"   ),
    "72": ("highchair", "holiness"   ),
    "73": ("hockey"   , "hurricane"  ),
    "74": ("indoors"  , "hydraulic"  ),
    "75": ("indulge"  , "impartial"  ),
    "76": ("inverse"  , "impetus"    ),
    "77": ("involve"  , "inception"  ),
    "78": ("island"   , "indigo"     ),
    "79": ("jawbone"  , "inertia"    ),
    "7a": ("keyboard" , "infancy"    ),
    "7b": ("kickoff"  , "inferno"    ),
    "7c": ("kiwi"     , "informant"  ),
    "7d": ("klaxon"   , "insincere"  ),
    "7e": ("locale"   , "insurgent"  ),
    "7f": ("lockup"   , "integrate"  ),
    "80": ("merit"    , "intention"  ),
    "81": ("minnow"   , "inventive"  ),
    "82": ("miser"    , "istanbul"   ),
    "83": ("mohawk"   , "jamaica"    ),
    "84": ("mural"    , "jupiter"    ),
    "85": ("music"    , "leprosy"    ),
    "86": ("necklace" , "letterhead" ),
    "87": ("neptune"  , "liberty"    ),
    "88": ("newborn"  , "maritime"   ),
    "89": ("nightbird", "matchmaker" ),
    "8a": ("oakland"  , "maverick"   ),
    "8b": ("obtuse"   , "medusa"     ),
    "8c": ("offload"  , "megaton"    ),
    "8d": ("optic"    , "microscope" ),
    "8e": ("orca"     , "microwave"  ),
    "8f": ("payday"   , "midsummer"  ),
    "90": ("peachy"   , "millionaire"),
    "91": ("pheasant" , "miracle"    ),
    "92": ("physique" , "misnomer"   ),
    "93": ("playhouse", "molasses"   ),
    "94": ("pluto"    , "molecule"   ),
    "95": ("preclude" , "montana"    ),
    "96": ("prefer"   , "monument"   ),
    "97": ("preshrunk", "mosquito"   ),
    "98": ("printer"  , "narrative"  ),
    "99": ("prowler"  , "nebula"     ),
    "9a": ("pupil"    , "newsletter" ),
    "9b": ("puppy"    , "norwegian"  ),
    "9c": ("python"   , "october"    ),
    "9d": ("quadrant" , "ohio"       ),
    "9e": ("quiver"   , "onlooker"   ),
    "9f": ("quota"    , "opulent"    ),
    "a0": ("ragtime"  , "orlando"    ),
    "a1": ("ratchet"  , "outfielder" ),
    "a2": ("rebirth"  , "pacific"    ),
    "a3": ("reform"   , "pandemic"   ),
    "a4": ("regain"   , "pandora"    ),
    "a5": ("reindeer" , "paperweight"),
    "a6": ("rematch"  , "paragon"    ),
    "a7": ("repay"    , "paragraph"  ),
    "a8": ("retouch"  , "paramount"  ),
    "a9": ("revenge"  , "passenger"  ),
    "aa": ("reward"   , "pedigree"   ),
    "ab": ("rhythm"   , "pegasus"    ),
    "ac": ("ribcage"  , "penetrate"  ),
    "ad": ("ringbolt" , "perceptive" ),
    "ae": ("robust"   , "performance"),
    "af": ("rocker"   , "pharmacy"   ),
    "b0": ("ruffled"  , "phonetic"   ),
    "b1": ("sailboat" , "photograph" ),
    "b2": ("sawdust"  , "pioneer"    ),
    "b3": ("scallion" , "pocketful"  ),
    "b4": ("scenic"   , "politeness" ),
    "b5": ("scorecard", "positive"   ),
    "b6": ("scotland" , "potato"     ),
    "b7": ("seabird"  , "processor"  ),
    "b8": ("select"   , "provincial" ),
    "b9": ("sentence" , "proximate"  ),
    "ba": ("shadow"   , "puberty"    ),
    "bb": ("shamrock" , "publisher"  ),
    "bc": ("showgirl" , "pyramid"    ),
    "bd": ("skullcap" , "quantity"   ),
    "be": ("skydive"  , "racketeer"  ),
    "bf": ("slingshot", "rebellion"  ),
    "c0": ("slowdown" , "recipe"     ),
    "c1": ("snapline" , "recover"    ),
    "c2": ("snapshot" , "repellent"  ),
    "c3": ("snowcap"  , "replica"    ),
    "c4": ("snowslide", "reproduce"  ),
    "c5": ("solo"     , "resistor"   ),
    "c6": ("southward", "responsive" ),
    "c7": ("soybean"  , "retraction" ),
    "c8": ("spaniel"  , "retrieval"  ),
    "c9": ("spearhead", "retrospect" ),
    "ca": ("spellbind", "revenue"    ),
    "cb": ("spheroid" , "revival"    ),
    "cc": ("spigot"   , "revolver"   ),
    "cd": ("spindle"  , "sandalwood" ),
    "ce": ("spyglass" , "sardonic"   ),
    "cf": ("stagehand", "saturday"   ),
    "d0": ("stagnate" , "savagery"   ),
    "d1": ("stairway" , "scavenger"  ),
    "d2": ("standard" , "sensation"  ),
    "d3": ("stapler"  , "sociable"   ),
    "d4": ("steamship", "souvenir"   ),
    "d5": ("sterling" , "specialist" ),
    "d6": ("stockman" , "speculate"  ),
    "d7": ("stopwatch", "stethoscope"),
    "d8": ("stormy"   , "stupendous" ),
    "d9": ("sugar"    , "supportive" ),
    "da": ("surmount" , "surrender"  ),
    "db": ("suspense" , "suspicious" ),
    "dc": ("sweatband", "sympathy"   ),
    "dd": ("swelter"  , "tambourine" ),
    "de": ("tactics"  , "telephone"  ),
    "df": ("talon"    , "therapist"  ),
    "e0": ("tapeworm" , "tobacco"    ),
    "e1": ("tempest"  , "tolerance"  ),
    "e2": ("tiger"    , "tomorrow"   ),
    "e3": ("tissue"   , "torpedo"    ),
    "e4": ("tonic"    , "tradition"  ),
    "e5": ("topmost"  , "travesty"   ),
    "e6": ("tracker"  , "trombonist" ),
    "e7": ("transit"  , "truncated"  ),
    "e8": ("trauma"   , "typewriter" ),
    "e9": ("treadmill", "ultimate"   ),
    "ea": ("trojan"   , "undaunted"  ),
    "eb": ("trouble"  , "underfoot"  ),
    "ec": ("tumor"    , "unicorn"    ),
    "ed": ("tunnel"   , "unify"      ),
    "ee": ("tycoon"   , "universe"   ),
    "ef": ("uncut"    , "unravel"    ),
    "f0": ("unearth"  , "upcoming"   ),
    "f1": ("unwind"   , "vacancy"    ),
    "f2": ("uproot"   , "vagabond"   ),
    "f3": ("upset"    , "vertigo"    ),
    "f4": ("upshot"   , "virginia"   ),
    "f5": ("vapor"    , "visitor"    ),
    "f6": ("village"  , "vocalist"   ),
    "f7": ("virus"    , "voyager"    ),
    "f8": ("vulcan"   , "warranty"   ),
    "f9": ("waffle"   , "waterloo"   ),
    "fa": ("wallet"   , "whimsical"  ),
    "fb": ("watchword", "wichita"    ),
    "fc": ("wayside"  , "wilmington" ),
    "fd": ("willow"   , "wyoming"    ),
    "fe": ("woodlark" , "yesteryear" ),
    "ff": ("zulu"     , "yucatan"    )
}


def reverse_wordlist(wordlist):
    out = {
        "even": {},
        "odd": {}
    }
    for x,ws in wordlist.items():
          out["even"][ws[0]] = x
          out["odd"][ws[1]] = x
    return out

reversed_word_list = reverse_wordlist(wordlist)

def chunks(seq, size):
    return [seq[i:i+size] for i  in range(0, len(seq), size)]

def chunkstring(st, n):
    return list(map(lambda cs: ''.join(cs), chunks(st, 2)))

def hexbytes2words(hexbytes):
    return [ wordlist[b][0 if i%2 == 0 else 1] for i,b in enumerate(hexbytes)]

def hexstring2words(hexs):
    """ Assumed good hex string. Ignore whitespace and non-hex characters"""
    hexstring = ''.join(c for c in hexs.lower() if c in set("0123456789abcdef"))
    bites = chunkstring(hexstring, 2)
    return hexbytes2words(bites)

def formatwords(words):
    colwidth = max([len(w) for w in words])+2
    spaced_words = ["{:{width}}".format(w, width=colwidth) for w in words]
    return "\n".join([" ".join(ws) for ws in chunks(spaced_words, 4)])

def wordstring2hexs(wordstring):
    """KeyError on bad word"""
    words = wordstring.split()
    return [reversed_word_list["even" if i%2==0 else "odd"][w] for i,w in enumerate(words)]


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--gen", nargs='?', const=16, metavar="N", type=int, help="Generate and display an N byte phrase. N=16 by default.")
    parser.add_argument("--towords", metavar="HEXSTRING", help="Accept hex-encoded data and output pgp words. Use - for stdin.")
    parser.add_argument("--tohex",  metavar="WORDS", help="Accept pgp words and output hex-encoded data argument. Use - for stdin.")

    args = parser.parse_args()

    if args.gen:
        data = secrets.token_hex(args.gen)
        print(" ".join(chunkstring(data, 2)))
        print(formatwords(hexstring2words(data)))

    elif args.towords:
        if args.towords == "-":
            data = sys.stdin.read()
        else:
            data = args.towords
        print(formatwords(hexstring2words(data)))

    elif args.tohex:
        if args.tohex == "-":
            data = sys.stdin.read()
        else:
            data = args.tohex
        print(" ".join(wordstring2hexs(data.lower())))
    
    else:
        parser.print_help()

