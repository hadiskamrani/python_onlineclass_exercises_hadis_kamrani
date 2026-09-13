sen = int(input("sene khood ra vared konid "))
janr = input("janr morede alaghe khood ra vared konid ")
emtiyaz = float(input("hadeaghal emtiyaz ghabele ghabool ra vared konid "))
Films = [{"name":"The Roocki","hadeaghal sen mojaz":14,"janr":"dram","emtiyaz":8},
 {"name": "dexter" , "hadeaghal sen mojaz":16,"janr" : "tarsnak" , "emtiyaz" : 9},
 {"name": "Love,Rose" , "hadeaghal sen mojaz":13,"janr" : "asheghane" , "emtiyaz" : 7},
{"name": "Ted Lasso" , "hadeaghal sen mojaz":12,"janr" : "comedy" , "emtiyaz" : 9},
 {"name": "This is Us" , "hadeaghal sen mojaz":15,"janr" : "dram" , "emtiyaz" : 8}]
for film in Films:
    if film["hadeaghal sen mojaz"] > sen and janr == film["janr"] and emtiyaz >= film["emtiyaz"] :
        print(film["name"])
        break
    else:
        print("filme monasebi peida nashood")
        break