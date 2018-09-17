i = [0.1,0.6,0.4,0.7,0.2]
b = [0.3,0.8]
c = [0.3,0.8,0.4]
d = [0.3,0.6,0.4,0.5]

def T_function(x,y):
    cnt = []
    alpha = y[0]
    beta = y[1]
    for no in x:
        if no>=alpha:
            a = 0
        elif no>=beta:
            a = 1
        elif no<(no<=beta):
            a = (no - alpha) / (beta - alpha)
        cnt.append(a)
    return cnt

def L_function(x,y):
    cnt = []
    alpha = y[0]
    beta = y[1]
    for no in x:
        if no<=alpha:
            a = 1
        elif no>beta:
            a = 0
        elif alpha<(no<=beta):
            a = (beta - no) / (beta - alpha)
        cnt.append(a)
    return cnt

def Tringular_function(x,y):
    cnt = []
    alpha = y[0]
    beta = y[1]
    zeta = y[2]
    for no in x:
        if no<=alpha:
            a = 0
        elif no>zeta:
            a = 0
        elif no<(no<=beta):
            a = (no-alpha) / (beta - alpha)
        elif beta<(no<=zeta):
            a = (zeta-no) / (zeta-beta)
        cnt.append(a)
    return cnt

def Pie_function(x,y):
    cnt = []
    alpha = y[0]
    beta = y[1]
    zeta = y[2]
    eta = y[3]
    for no in x:
        if no<=alpha:
            a = 0
        elif no>eta:
            a = 0
        elif no<(no<=beta):
            a = (no-alpha) / (beta - alpha)
        elif beta<(no<=zeta):
            a = 1
        elif zeta<(no<=eta):
            a = (eta-no)/(eta-zeta)
        cnt.append(a)
    return cnt

def Zadeh_function(x,y):
    cnt = []
    alpha = y[0]
    beta = y[1]
    zeta = y[2]
    for no in x:
        if no<=alpha:
            a = 0
        elif no>zeta:
            a = 0
        elif no<(no<=beta):
            a = (2*((no-alpha) / (beta - alpha))**2)
        elif beta<(no<=zeta):
            a = 1-(2*((zeta-no) / (zeta-beta))**2)
        cnt.append(a)
    return cnt




print('T_function :',T_function(i,b))
print('L_function :',L_function(i,b))
print('Tringular_function :',Tringular_function(i,c))
print('Pie_function :',Pie_function(i,d))
print('Zadeh_function :',Zadeh_function(i,c))

