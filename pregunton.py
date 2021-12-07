import subprocess
print("hola que tal?")
entrada=input();

if entrada=="bien":
 print("encantado")
 print("dame un numero")
 num=input()
 print("gracias")
 print("su numero es: "+ num)
 print("quieres se mi amigo")
else:
 print("no te molesto entonces")

print("quiere ver sus contenedores de docker?")
respuesta=input()
if respuesta=="si":
 print("estos son sus procesos de docker")
 subprocess.run(["docker","ps"])  

