from validaciones import validar_sn
from gestionPasajeros import login_cliente
from gestionReservas import cancelar_reserva


#Lista asociada a palabras de cancelacion.
cancelar = ["cancelar", "baja", "parar", "eliminar", "anular"]
 
modificar=["cambiar","modificar","agregar"]



def interpretar_intencion(mensaje):
   while True:

      mensaje = mensaje.lower()
      


      for palabra in cancelar:

         if palabra in mensaje:

            print("¿Quiere cancelar una reserva?")
            opcion= validar_sn()
            if opcion == "si":
               print("Para cancelar una reserva debe entrar como USUARIO.")
               pasajero = login_cliente()
               cancelar_reserva(pasajero)
              
            else:
               print("Lo siento, no te entendi bien, puedes volver a repetir tu consulta")
      break
      
      
  
      

print("Hola soy Tina el bot de AIRES AIRLINES \n ¿En que te puedo ayudar hoy? \n")
mensaje= input("Ingrese consulta:")
interpretar_intencion(mensaje)

            
            


         
   
   

