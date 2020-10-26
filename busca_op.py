import re

def busca_par(text):
    oc = []
    res = ""
    f=0
    tx=text
    while f<len(tx):
        f = tx.find("Operação",f)
        if f == -1:
            break
        
        tx = tx[f:]
        #print(name)
        name = re.compile(r'[ .,!:;"\n]').split(tx)

        j=1
        res = ""
        while (j < len(name) and name[j].istitle()):
            res +=' '+name[j]
            j+=1
        if len(res) > 3:
            if res[0] == ' ':
                res = "Operação"+res
            if res not in oc: oc.append(res)
        f+=8
                
    #print(oc)
    return oc

def busca_op(t):
    r = []
    for x in t:
        
        aux = busca_par(x)
        for i in aux:
            if i not in r: r.append(i)

    return ";".join(r)
      

##test = ["A primeira fase da Operação Sangria, deflagrada no dia 30 de junho, resultou na prisão de 8 pessoas, incluindo a secretária de Saúde da época, Simone Papaiz. O governador Wilson Lima foi alvo de mandado de busca e apreensão por suspeita de envolvimento em esquema de compra de respiradores.",
##       "A Operação é desdobramento da Operação Placebo, que investiga corrupção em contratos públicos do Executivo fluminense."]
##
##
##a = busca_op(test)
