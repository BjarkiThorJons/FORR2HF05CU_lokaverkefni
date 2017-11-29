vopn={"brons sverð":{"value":4,"verd":200,"tegund":"sverð"}
    ,"járn sverð":{"value":8,"verd":1000,"tegund":"sverð"}
    ,"járn öxi":{"value":10,"verd":1200,"tegund":"öxi"}
    ,"mithril brynja":{"value":60,"verd":70000,"tegund":"brynja"}
    ,"járn brynja":{"value":4,"verd":750,"tegund":"brynja"}}
for x in vopn:
    v=vopn[x]
    if v["tegund"]=="sverð" or v["tegund"]=="öxi":
        print(x,"dmg:",v["value"],"verð:",v["verd"],"tegund:",v["tegund"])
    else:
        print(x,"block:", v["value"],"verð:",v["verd"],"tegund:",v["tegund"])
kaupa=input("Veldu það sem þú vilt kaupa ")
peningur=int(input("peningur "))
inv={}
for x in vopn:
    v=vopn[x]
    if x==kaupa:
        if peningur>=v["verd"]:
            peningur-=v["verd"]
            inv[x]=v
print(peningur)
print(inv)