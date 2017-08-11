    def generar(enviados,recibidos,mail,clave):
        # crea una lista que contiene todos los mensajes ordenados por fecha, en formato str
        # los mensajes se conforman por Fecha, Hora, Emisor, Destinatario, Mensaje.
        lista_todos=[]
        lista_final=[]
        for i in enviados:
            lista_todos.append([i,"e"])
        for i in recibidos:
            lista_todos.append([i,"r"])
        lista_todos2=ordena(lista_todos)
        for i in range(len(lista_todos2)):
            decript=OTP(lista_todos2[i][0][2],clave)
            if lista_todos2[i][1]=="e":
                lista_final.append(ext_fecha(lista_todos2[i][0])+"  "+ ext_hora(lista_todos2[i][0])+"  De: "+mail+"  Para: "+lista_todos2[i][0][0]+" - "+binario_a_string(decript))
            elif lista_todos2[i][1]=="r":
                lista_final.append(ext_fecha(lista_todos2[i][0])+"  "+ ext_hora(lista_todos2[i][0])+"  De: "+lista_todos2[i][0][0]+"  Para: "+mail+" - "+binario_a_string(decript))
        lista_final.reverse()
        return lista_final