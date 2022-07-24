def is_correct_bracket(text):
    flag = True
    m = [] 
    while flag:
        text = list(text)
        txet = text[:]
        text = text[0:-1]
        txet.pop(0)
        sym = ''
        print(text)
        print(txet)
        l = []
   
        for i in range(len(text)):
            sym = text[i] + txet[i]                    
            l.append(sym)
        print(l)    
        for i in range(0, len(l)):
            if l[i] == '((':
                l[i] = '('
            elif l[i] == '))':
                l[i] = ')'
        n = len(l)        
        for i in range(n - 1):
            for j in range(n - i - 1):
                if l[j] != '()' and l[j + 1] == '()':                  
                    l[j], l[j + 1] = l[j + 1], l[j]
                if l[j] != ')(' and l[j + 1] == ')(': 
                    l[j], l[j + 1] = l[j + 1], l[j]                    
               
                
        print(len(l))   
        
        print(l)
        z = '()'
        s = ')('
        while z in l: l.remove(z)
        
        #while s in l: l.remove(s)                

        print(l)
        
        if len(l) % 2 == 0:
            return True
        else:
            return False
        '''text = "".join(l)
        print(text)
        if len(l) == 1 or len(text) == 0:
            break
    if len(l) == 1:
        return False'''
    
            
txt = input()

print(is_correct_bracket(txt))