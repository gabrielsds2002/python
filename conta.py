kWh = float(input('qual a quantitade de kWh consumida? '))
instalacao = input('digite o tipo de instalação que você quer, R para residências, I para indústrias e C para comércios.')
valor = 0

if instalacao == "R" or "r":
    (kWh > 500)
    valor = kWh*0.65
elif instalacao == "R" or "r":
        valor = kWh*0.40

elif instalacao == "I" or "i":
    (kWh > 1000)
    valor = kWh*0.60
        
elif instalacao == "I" or "i":
    valor = kWh*0.55
           
elif instalacao == "C" or "c":
    (kWh > 5000)
    valor = kWh*0.60
            
elif instalacao == "C" or "c":
    valor = kWh*0.60
if(instalacao == "R" or instalacao == "r" or instalacao == "C" or instalacao == "c" or instalacao == "I" or instalacao == "i"):                        
    print("O valor da sua conta é de R$%.2f"%(valor))
else:
    print("conta invalida")
    
    
                        
                        
                   
                        
        








