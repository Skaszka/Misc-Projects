#!/usr/bin/env python3

# Twitter @SkaszkaCodes
# Github @Skaszka
# 2019/09/09
# Done for shits and giggles and to make myself use python 3 since python 2.7 is being deprecated
# Also actually use functions again finally

import sys
import socket
import _thread
from collections import OrderedDict
import time
import random
import hashlib, struct
import math

alethio_intro = ("",
"                              M: MN8MMM=7MMMMM  8                              ",
"                            DIMMI:,  N8MMM ,:=$8M:D                            ",
"                         ,7I~     :$+     77:      ~$M                         ",
"                      NO:   I $MMMOI       ?ZMMM? +   ,=O                      ",
"                   DO:  $,MM,  NNMMNMZ$?ZZMMMMMM  :MM 8   I7                   ",
"                 8I  8=M8 +NM++ 8  ,=  N     DD:MOMM= NM I  ?Z                 ",
"               O+   MD MMM N~M    N+  8 M  N  D ~  N +MM MM   ?Z               ",
"             8I =$M,DM    ~M7Z N 7IM ?Z:M   ?  $ =N,   M=M8 M   +Z,            ",
"            O   M MMM  NO ?  M  ? MM:I8MN MZ N 7~MI ~  7  ,MO M   Z            ",
"          DI :M 8M +   8N :: Z8 Z    8      + = I ~  7DM  :  M?IMZ ,I          ",
"         O  =M:M       ~Z,  ~  M8~7:   7   ~?:DD   +      :M$8 O Z  ,I         ",
"        Z =M+ZD     $  7   ?MZ:? D7MM8MZM8MMOO  :~M  = ~ M$D? ::N+8$  I        ",
"       $ NM 8:+  O    M NM7~ 7MM8  ?N$   MN:  NMMM  =MN  ~ D 7  ,+N NI ?       ",
"      I DM M=  $IM $ : NO OMMZ7:+MMMOZ, ~IOMMM~O,$MM= IM + 7,8 N   M NI I      ",
"     I MM 7, , Z$  M,M$ MMD8IMMZ$?, :     MN?+ZOMMM+MMMM,M+,8M:M    $ M+ $     ",
"    7 ~M O:   M~    ~ ?MNM NNM , :        7Z,Z,= DOM MMM, :$ ? Z   M $,Z  Z    ",
"   I: NZM:  O    N : MO8 MO7 M  ?               I  +$MOM87 :~M   M    O$  ~    ",
"   ?  N,8M,  =IN =O MMZ?$NI   MD     =   MM:D  7     D7~DMD ~  MMN  =,M D+ I   ",
"  8  M,M    DI   ?MMMMMZ=  ~7 MM ,       MMO =    $$  =?NDM8 =   $M :, D I :D  ",
"  ?  M7=M=MM,=+:8 MM=M7     $   M  ~=: ~MMM            7?NOMO N~   O=  I=$, I  ",
" 8, M,M~8   O  M:M?8=7,          M      MM      :     ? ?7:NO=+NMM $    N ~ ~M ",
" Z ?M~I  $?M+= 7 M= O: = : :  ,D :8    ,MM      + :    , +8$7M 7  :Z8$  8 M7 O ",
" ?  DN:M  ,7  M:DM~M?~D +         I8  ,?MD         D    ,?+$~Z:7? 8MN+N  OM  Z ",
",= 8$M M ,NM  ? M$,$=     N       :7M +MM~ M      8 O     ~O+8: 8   M    ZI  + ",
"N: M=M =MM,   ? MM OZ  ?    D    MMMM$ MM NMM,    N       7+ +M I     ODNM ?  M",
"I  M:Z  MM    Z Z$M :    ~     = OMM MM MM87=  ?        : ?  $M +  ,I: N M M  M",
"M IM,$ 7 MMMM~7=NDMZZZ,N7         DMNMMNMMMO=,:  =        +,M8M ?  7MNDN N    +",
"MMMM~Z       :? MMMZ8=,$DN,         MMMMMOMM: O8OI  :N7DMM$OMMM    N$+,, M M8:M",
"MMMM=M+:+7MI: M$MMM$+8::~=I7D O  , 8N M=8M~+OMMMNMM8Z$$$I?ODMMM ,  IDM8O$M MMMM",
",MMM=M  ,  =: M?MMOOI~:Z ,O,?~=+DMMD :+  DMZ~MMMMMMMMM:O??8NMMOMM D O O  MMMMM ",
" MMMMMNMM,O 7 MMMM MNO:,:$ D  OMMM$~,M8M  MM ?    ZDDMMMM7$ODDMMMN    8D MMMMM ",
" MMMMM~  ,  N =MNM ~88~N  ?,MMMMD    MM$+  MM  =  8 O  =DZ$O,MMM?M+N    ZMMMDM ",
" MMMMMM~  +M N MDMM:MMDZ7  MMMN      O +    D?~:?  78MMMMO  7MMMM     MMMNM8NM ",
":~MMMMM,NMMM,?88MOM$ M8OMMMMM,      M     M   ,    8:+I$8D $MNM   NMNOM:NMNIN? ",
",$MMMMMM  ~ M,  ZNMM  MMMMM$DO$  MMIN     D,~M , ,MNI7NDN MM O, D      MZM$ZM  ",
" :MDNMMMZMM, M 8MN8ZMD~IMM,=:,?~  ,            Z   ==OM :DM$77 M MM MMI=M8?DM  ",
" ,NMD8MMM :      ?8?~M=, MM8  ~   ,     :    ,  :  NMM7==M=IDN :DM7  ~ZM~~$M   ",
"   MNMMMMM    NO N =Z7NM7~,MMM++?8:I,,=    :     MNM,,NMO+$~  +~, N,:MZ$ =M8N  ",
"  M8MMO8MMM:M?8IM+M MM$,M8I?IMMMMOI??:~   ,  7MMM8$7DMMI$M+  =  ,MI~M=M=:NOM+Z,",
" MZM MN7OMMM~N, 8 8=I,OMD7MMZ,, :MMMMMM MMMMMM?+=DZMD$DM= ?$ NI  ,7M7M?:ZM~7IM ",
"  M?O:MM7DMMMI  :M  87M=IM778MMM8M=       , +MDMM87MDMM  M   M  +M=MI ~MM?ZMMM ",
"  IMMMMMM?=MM8MMIMMM  M  M=DMZMOONMMMMMMMMMMMMN78MM:  ~M M ?  MMN~M  ?MMM7DM   ",
"    MMMMMM$=$M8M7NMMIM M :M: =7NMMMMMZ:  DMMMMMM   ,    N:+= ,N7=M::?MM$MMM    ",
"         MO$DMM7M$=M M ~ ?+    M MNMZNM7MZ?~ 8  ,?N ~MM~I8M7O=M: ,ZM==$        ",
"          8MN$?:MN$MZNM   M M~,M  88=7DDM8 OM: Z ,O8M  ,,INM,M7+ ?M$N,         ",
"            NMOI++MD~M8?,M~M M M =M = ,MM   :  MM =  M:~MD,MNO IZ8M            ",
"               DD7+:MMO7MN$=8,M +M  M   I      O , ?=MM ZMI7 =D?               ",
"                 MO7=D$MM==MMDMM7+~~M,:~M:M=:M??MMM7,$MM   :Z~                 ",
"                    NZ=~O+MMM, ~NMMMMMI?MMMMN$:,=DMM:+  ,IO                    ",
"                       DZ?+,$ 7MMMMMMNN7MMMMMMMI D  ,=7D                       ",
"                          ODZ7?~ :,?88Z,8O?     =+I88                          ",
"                                MMDZO$$7IZO8D88                                ",
"",
"           The alethiometer/His Dark Materials series belongs to Philip Pullman",
"             Text sourced from https://preview.tinyurl.com/archive-alethiometer",
"      This is a non-commercial, fair use, just-for-fun project by @SkaszkaCodes",
"",
"===============================================================================",
"",
"Enter 'Help' to for a guide to interpreting alethiometer symbols.",
"",
"Otherwise, enter three symbols for your question, separated by commas.",
"",
"===============================================================================",
"")

alethio_guide = ("",
"Each symbol has one primary meaning and a range of subsidiary meanings, which is potentially infinite. However, the subsidiary meanings are all related by association to the primary meaning.\n", 
"So, for instance, the sun symbolizes (1) day, because it is during the day that we see the sun. It also symbolizes (2) authority, because the sun is the most powerful thing in the sky. Another meaning is (3) truth, because by the sun's light we can see the true forms of things. The sun range continues:",
"(4) kingship (or political authority of any kind), because the king is the sun around whom the court or the state revolves;\n(5) a particular king or leader (in the context of a query to the alethiometer, it will be obvious which one is meant);\n(6) Phoebus Apollo, and thus rationality and the intellect, as opposed to the baser emotions;\n(7) archery (Apollo's bow and arrows) and thence\n(8) the power of administering punishment at a distance, including\n(9) plague;\n(10) the creative arts (through Apollo's patronage of the nine Muses);\n(11) the laurel (through Apollo's love for Daphne), and thence\n(12) honor, prizes, fame, through Apollo's awarding of the laurel wreath;\n(13) divination and prophecy (through the Delphic Oracle);\n(14) pastoral husbandry (Apollo's flocks and herds), and thence\n(15) a particular farm, and thence\n(16) a particular beast;\n(17) homosexual love (Apollo's love for Hyacinthus);\n(18) gold...\n",
"And so on, infinitely. No one has ever reached the end of a symbol range, even though some have been explored to the depth of a thousand or more meanings.\n",
"Each symbol is thus capable of expressing a multitude of ideas, but each subsidiary meaning carries with it some quality of the primary one, even when it may appear to coincide with a meaning in another range. For example, the meaning `sea` appears both as number seven in the dolphin's range and number four in the anchor's, but it signifies different things in each. In the dolphin range, it means 'the sea as wide, nourishing home,' and in the anchor range, 'the sea as danger and unpredictability.' A skillful reading of the alethiometer would have to take into account not only the meaning itself, wherever it comes within the range, but also the significance lent it by the range itself.",
"",)

symbol_dict = OrderedDict([('HOURGLASS',('Time','Death, change ...')),
('SUN',('Day','Authority, truth ...')),
('ALPHA AND OMEGA',('Finality','Process, inevitability ...')),
('MARIONETTE',('Obedience','Submission, grace ...')),
('SERPENT',('Evil','Guile, natural wisdom ...')),
('CAULDRON',('Alchemy','Craft, achieved wisdom ...')),
('ANCHOR',('Hope','Steadfastness, prevention ...')),
('HELMET',('War','Protection, narrow vision ...')),
('BEEHIVE',('Productive work','Sweetness, light ...')),
('MOON',('Chastity','Mystery, the uncanny ...')),
('MADONNA',('Motherhood','The feminine, worship ...')),
('APPLE',('Sin','Knowledge, vanity ...')),
('BIRD',('The soul (the dæmon)','Spring, marriage ...')),
('BREAD',('Nourishment','Christ, sacrifice ...')),
('ANT',('Mechanical work','Diligence, tedium ...')),
('BULL',('Earth','Power, honesty ...')),
('CANDLE',('Fire','Faith, learning ...')),
('CORNUCOPIA',('Wealth','Autumn, hospitality ...')),
('CHAMELEON',('Air','Greed, patience ...')),
('THUNDERBOLT',('Inspiration','Fate, chance ...')),
('DOLPHIN',('Water','Resurrection, succor ...')),
('WALLED GARDEN',('Nature','Innocence, order ...')),
('GLOBE',('Politics','Sovereignty, fame ...')),
('SWORD',('Justice','Fortitude, the Church ...')),
('GRIFFIN',('Treasure','Watchfulness, courage ...')),
('HORSE',('Europe','Journeys, fidelity ...')),
('CAMEL',('Asia','Summer, perseverance ...')),
('ELEPHANT',('Africa','Charity, continence ...')),
('CROCODILE',('America','Rapacity, enterprise ...')),
('BABY',('The future','Malleability, helplessness ...')),
('COMPASS',('Measurement','Mathematics, science ...')),
('LUTE',('Poetry','Rhetoric, philosophy ...')),
('TREE',('Firmness','Shelter, fertility ...')),
('WILD MAN',('Wild man','The masculine, lust ...')),
('OWL',('Night','Winter, fear ...'))
])

def list_digest(strings):
        # credit: https://security.stackexchange.com/a/163640
    hash = hashlib.sha1()
    for s in strings:
        hash.update(struct.pack("I", len(s.encode())))
        hash.update(s.encode())
    return hash.hexdigest()

def returnRandomNumbers(input_symbols, addr):
# reasoning here:
# 1. Asking the same question repeatedly should give you the same answer.
# 2. However, the same symbols might describe a different question for different people, 
#    or on different days. So use broad time seed AND ip seed... or just broad time if
#    running locally.
        list = set()
        ticks = int(math.ceil(time.time() / 100000.0)) * 100000
                # ticks should change roughly every day: 100000 seconds is 1.157 days
        
        random_list = [str(ticks), str(addr[0])]   # time, ip address...
        random_list.extend(input_symbols)       # symbols they submitted
        random_seed = list_digest(random_list)
        
        random.seed ( random_seed )
        amt_symbols = random.randint(2,8)
        
        for i in range(amt_symbols):
                list.add(random.randint(0,len(symbol_dict)-1))
        
        return list

def returnSymbols(input_symbols, addr):
        output_symbols = []
        
        if not len(input_symbols) == 3 or not len(set(input_symbols)) == 3:
                output_symbols.append("fail")
                return output_symbols
                
        log_string = str(addr) + "\t"
        
        temp_log = ""
        for entry in input_symbols:
                temp_log += entry.strip().upper() + ". "
                if entry.strip().upper() not in symbol_dict:
                        output_symbols.append("fail")
                        return output_symbols
        output_nums = returnRandomNumbers(input_symbols, addr)        
                
        log_string += "{:<45}".format(temp_log) + "\t"
        
        temp_symbols = list(symbol_dict)
        for i in output_nums:
                symbol = temp_symbols[i]
                log_string += symbol.upper() + ". "
                output_symbols.append("\t " + "{:<16}".format(symbol) + "\t " + "{:<20}".format(symbol_dict[symbol][0]) + "\t " + symbol_dict[symbol][1] + "\n")
        
        print(log_string)
        return output_symbols

#SEND text + "\n"

def serve_client(conn,addr):
        for entry in alethio_intro:
                msg = entry + "\n"
                conn.send(msg.encode()) 
        
        while True:
                conn.send("> ".encode())
                
                data = conn.recv(1024)
                if not data:
                        break
                data = data.decode().strip().lower()
                
                if "help" in data[0:5]:
                        print(str(addr) + "\t\tHelp")
                        for entry in alethio_guide:
                                msg = entry + "\n"
                                conn.send(msg.encode())
                        conn.send("LIST OF\n".encode())
                        conn.send( ("{:<16}".format("SYMBOLS") + " \t" + "{:<20}".format("PRIMARY MEANING") + " \t" + "ADDITIONAL MEANINGS" + "\n").encode())
                        conn.send("-------------------------------------------------------------------------------\n".encode())
                        for key in symbol_dict:
                                conn.send( ("{:<16}".format(key) + "\t" + "{:<20}".format(symbol_dict[key][0]) + "\t" + symbol_dict[key][1] + "\n").encode() )
                        conn.send("\n".encode())
                else: # assume symbols... for now
                        input_symbols = data.split(",")
                        answer = returnSymbols(input_symbols, addr)
                        if "fail" in answer[0]:
                                conn.send("Could not understand symbols. Did you send exactly three unique symbols?\n".encode()) 
                                print(str(addr) + "\t\tSymbols not understood")
                        else:
                                conn.send("The alethiometer needle pointed at the following symbols:\n".encode())
                                conn.send( ("\t" + "{:<16}".format("SYMBOL") + " \t" + "{:<20}".format("PRIMARY MEANING") + " \t" + "ADDITIONAL MEANINGS" + "\n").encode())
                                for entry in answer:
                                        conn.send(entry.encode())
                
                conn.send("\n===============================================================================\n\n".encode())
                
        conn.close()
        
def serve_alethio(HOST, PORT):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen()
        
        print("\n                              The alethiometer/His Dark Materials series belongs to Philip Pullman")
        print("                                Text sourced from https://preview.tinyurl.com/archive-alethiometer")
        print("                         This is a non-commercial, fair use, just-for-fun project by @SkaszkaCodes")

        print("\nNow running alethiometer server on port " + str(PORT) + "...\n")
        
        print("IP \t\t\t" + "{:<45}".format("QUESTION")+"\tANSWER")
        print("--------------------------------------------------------------------------------------------------")

        try:
                while True:
                        conn, addr = s.accept()
                        _thread.start_new_thread(serve_client,(conn,addr))
                
        except KeyboardInterrupt:
                print("\n\nShutting down alethiometer server...\n")
                s.close()
                exit(0)
                
        except Exception as e:
                print("\n\nError:" + str(e))
                print("Shutting down alethiometer server...\n")
                s.close()
                exit(1)

if __name__== "__main__":

        if len(sys.argv) < 2:
                print("Expects 'local' or 'full' as a command line argument, where local runs on 127.0.0.1, and full runs on all interfaces")
                exit()
        
        if str(sys.argv[1]) == "full":
                HOST = "" # make HOST "" to accept connections on all interfaces
        elif str(sys.argv[1]) == "local":
                HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        else: 
                print("Expects 'local' or 'full' as a command line argument, where local runs on 127.0.0.1, and full runs on all interfaces")
                exit()
        
        PORT = 47375    
                
        serve_alethio(HOST, PORT)
        