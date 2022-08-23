import random

# Ao chamar a função um valor de dia, mês e ano no tipo (int) são retornados
# além disso a data gerada é exibida em tela
def gerar_data():
    
    year = random.randint(1925,2022)
    month = random.randint(1,12)

    if(( year % 4) == 0 and (year % 100) != 0 and month == 2):
        day = random.randint(1,29)
    else:
        if((year % 400) == 0):
            day = random.randint(1,29)
        else:
            day = random.randint(1,28)
    
    if(month == 4 or month == 6 or month == 9 or month == 11):
        day = random.randint(1,30)
    else:
        day = random.randint(1,31)
        

    print(str(day)+"/"+str(month)+"/"+str(year))
    
    return(day,month,year)

# ------------------------------------------------------------------------

# Esta função verifica se o ano é bissexto
# os parâmetros são valores do tipo int para
# dia, mês e ano
# No entanto, dia e mês são irrelevantes
def verificar_ano_bissexto(day,month,year):

    if(( year % 4) == 0 and (year % 100) != 0 and month == 2):
        print("Ano bissexto")
    else:
        if((year % 400) == 0):
            print("Ano bissexto")
        else:
            print("Ano não bissexto")

# ------------------------------------------------------------------------

# A função abaixo verifica se uma data é verdadeira, 
# considerando as particularidades de cada mês, inclusive 
# quando se trata de um ano bissexto
def verificar_data(day,month,year):

    ver = True

    if (day > 0 and day < 32):
        if (month > 0 and month < 13):
            if(( year % 4) == 0 and (year % 100) != 0 and month == 2 and day < 30):
                ver = True
                print("Data válida")
            else:
                if((year % 400) == 0 and month == 2 and day < 30):
                    ver = True
                    print("Data válida")
                else:
                    if (month == 2 and day < 29):
                        ver = True
                        print("Data válida")
                    else:
                        if((month == 4 or month == 6 or month == 9 or month == 11) and day < 31):
                            ver = True
                            print("Data válida")
                        else:
                            if((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day < 32):
                                ver = True
                                print("Data válida")
                            else:
                                ver = False
                                print("Data inválida. Esse mês não possui esse dia")
        else:
            ver = False
            print("Data inválida. Mês incorreto.")
    else:
        ver = False
        print("Data inválida. Dia incorreto.")

# ------------------------------------------------------------------------
# Em desenvolvimento.
# A função abaixo deve obter o dia da semana, baseado em
# uma data informada com parâmetro, de acordo com o 
# Calendário Gregoriano - O desafio aqui é popular o calendário

def verificador_dia_semana():


    list_year = []
    first_list = []

    for i in range(0,4):
        first_list.append(i * 28)
    
    list_year.append(tuple(first_list))

    for i in range(0,27):
        if(i < 15):
            for u in range(0,4):
                if((first_list[u] + 1) > 0 and (first_list[u] + 1 ) < 100):
                    first_list[u] = first_list[u]+1
        else:
            if(len(first_list) == 4):
                first_list.remove(99)
            for u in range(0,3):
                first_list[u] = first_list[u]+1
                # if((first_list[u] + 1) > 0 and (first_list[u] + 1 ) < 100):
                #     first_list[u] = first_list[u]+1
        
        print(first_list)
        
    # print(list_year)

    # for i in range(0,28):


    # return day_week
verificador_dia_semana()