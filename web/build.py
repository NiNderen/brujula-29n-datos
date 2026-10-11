import json
sd='/tmp/claude-0/-home-claude/479ce1ff-60ce-5b7c-8544-8a861ad2eae0/scratchpad/'
d=json.load(open(sd+'data.json'))
P=[{"id":"psoe","n":"PSOE","full":"Partido Socialista Obrero Español","c1":"#D90F2B","c2":"#F2394C","ink":"#FFFFFF"},
{"id":"pp","n":"PP","full":"Partido Popular","c1":"#0868C9","c2":"#1C8AF0","ink":"#FFFFFF"},
{"id":"vox","n":"VOX","full":"Vox","c1":"#55B91F","c2":"#A6E34F","ink":"#0D1F05"},
{"id":"sumar","n":"SUMAR","full":"Sumar","c1":"#D4006F","c2":"#F0399A","ink":"#FFFFFF"},
{"id":"podemos","n":"PODEMOS","full":"Podemos","c1":"#6A25B0","c2":"#9B54E8","ink":"#FFFFFF"},
{"id":"erc","n":"ERC","full":"Esquerra Republicana de Catalunya","c1":"#FFA400","c2":"#FFD15C","ink":"#2B1A00","reg":["CT"]},
{"id":"junts","n":"JUNTS","full":"Junts per Catalunya","c1":"#00B8A9","c2":"#5CEBDD","ink":"#03302C","reg":["CT"]},
{"id":"bildu","n":"EH BILDU","full":"EH Bildu","c1":"#B9CF00","c2":"#E6F54A","ink":"#232B00","reg":["PV","NA"]},
{"id":"pnv","n":"PNV","full":"Partido Nacionalista Vasco","c1":"#00833F","c2":"#1FB566","ink":"#FFFFFF","reg":["PV"]},
{"id":"bng","n":"BNG","full":"Bloque Nacionalista Galego","c1":"#4DBDEB","c2":"#9BE0FF","ink":"#03283A","reg":["GA"]},
{"id":"cc","n":"CC","full":"Coalición Canaria","c1":"#FFD21F","c2":"#FFE978","ink":"#2B2400","reg":["CN"]},
{"id":"upn","n":"UPN","full":"Unión del Pueblo Navarro","c1":"#19378C","c2":"#3D63CC","ink":"#FFFFFF","reg":["NA"]}]
R=[["AN","Andalucía"],["AR","Aragón"],["AS","Asturias"],["IB","Baleares"],["CN","Canarias"],["CB","Cantabria"],["CM","Castilla-La Mancha"],["CL","Castilla y León"],["CT","Cataluña"],["CE","Ceuta"],["VC","C. Valenciana"],["EX","Extremadura"],["GA","Galicia"],["RI","La Rioja"],["MD","Madrid"],["ML","Melilla"],["MC","Murcia"],["NA","Navarra"],["PV","País Vasco"]]
seed=json.load(open('../feed.json'))
t=open('tpl.html').read()
for k,v in [("__Q__",d['Q']),("__BAND__",d['BAND']),("__FAM__",d['FAM']),("__AX__",d['AX']),("__PARTIES__",P),("__REGIONS__",R),("__SEED__",seed)]:
    t=t.replace(k,json.dumps(v,ensure_ascii=False).replace("</","<\\/"))
open('index.html','w').write(t)
