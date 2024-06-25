from datetime import datetime

def validate_files(request,field,update = False):
    
    #TODO metodo 1 de poder modificar el request y alterar el campo 'imagen' que envien
    # request._mutable = True
    # if update:
    #     #cuando me envian un string elminado el campo que nos envian, en este caso 'image'
    #     if type(request[field])==str:
    #         del request[field]
    # else:
    #     request[field] = None if type(request[field]) == str else request[field]
    #     request._mutable = False           
    # return request

    #TODO metodo 2 con metodo .copy() y __setitem__  Video 48 de developer.pe
    
    new_request = request.copy()
    
    if update:
        if type(new_request[field])==str:
            new_request.__delitem__(field)
    else:        
        if type(new_request[field])==str:
            new_request.__setitem__(field,None)
    
    return new_request

def formatear_date(date):
    date = datetime.strptime(date, '%d/%m/%Y')
    date = f"{date.year}-{date.month}-{date.day}"
    return date