
ufs = {"Acre":"AC",
"Alagoas":"AL",
"Amapá":"AP",
"Amazonas":"AM",
"Bahia":"BA",
"Ceará":"CE",
"Distrito Federal":"DF",
"Espírito Santo":"ES",
"Goiás":"GO",
"Maranhão":"MA",
"Mato Grosso": "MT",
"Mato Grosso do Sul":"MS",
"Minas Gerais":"MG",
"Pará": "PA",
"Paraíba": "PB",
"Paraná": "PR",
"Pernambuco": "PE",
"Piauí": "PI",
"Rio de Janeiro": "RJ",
"Rio Grande do Norte": "RN",
"Rio Grande do Sul": "RS",
"Rondônia": "RO",
"Roraima": "RR",
"Santa Catarina": "SC",
"São Paulo": "SP",
"Sergipe": "SE",
"Tocantins": "TO"}



def busca_uf_par(text):
    res = []
    for x in ufs:
        f = text.find(x)
        if f != -1:
            #name = re.split(r'\W+', text[f:-len(x)])
            name = text[f:(f+len(x))]
            #print(name)
            res.append(ufs[name])
    if not res:
        for x in ufs.values():
            f = text.find(x)
            try:
                if f != -1 and (f == 0 or (text[f-1] in [' ','('])) and (text[f+2] in [' ',')',',','.']):
                    name = text[f:(f+len(x))]
                    #print(name)
                    res.append(name)
            except IndexError:
                print("Oops")
            
    return res
    
def busca_ufs(t):
    r, r2 = [], []    
    for x in t:
        r = busca_uf_par(x)
        for i in r:
            if i not in r2: r2.append(i)
    #print(r2)
    return r2   
    


#a = ["A etapa no Rio Grande do Norte. foi feita em dezembro.", "lalala, no Paraná, l."]
#print(busca_ufs(a))
    
