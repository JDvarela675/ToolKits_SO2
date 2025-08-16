# Developer
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import os
import subprocess
import time
from tkinter import scrolledtext

#crear ventana y estilo de esta misma

v0=Tk()
v0.title("ToolKits Para Linux version 2.0")
v0.geometry("1000x500+200+200")
v0.configure(bg="lavender") # definir otro color mas tarde




def clean():
            destino.set('')
            cuerpo.set('')
            asunto.set('')


#funciones

def SendMail():
               ck2=str(check2.get())
               if (ck2=="" or ck2=="0"):
                                        print("Sending Email NOW...")
                                        d=str(destino.get())
                                        a=str(asunto.get())
                                        c=str(cuerpo.get())
                                        enc="#!/bin/bash"
                                        e="echo"
                                        tab=" "
                                        cd='"'
                                        b="|"
                                        comando="mail -s"
                                        
                                        cadena1=(str(e)+''+str(tab)+''+str(cd)+''+str(c)+''+str(cd)+''+str(tab)+''+str(b)+''+str(tab)+''+str(comando)+''+str(tab)+''+str(cd)+''+str(a)+''+str(cd)+''+str(tab)+''+str(d))
                                        os.system("sudo chmod -R 777 /home/sandoval/send.sh")
                                        pf=open("/home/sandoval/send.sh","w")
                                        pf.write(enc)
                                        pf.write("\n")
                                        pf.write(cadena1)
                                        pf.write("\n")
                                        pf.close()

                                        time.sleep(0.1)

                                        #ejecutar el script
                                        os.system("sudo /./home/sandoval/send.sh")
                                        clean()
                                        messagebox.showinfo("INFO",message="Correo Enviado Con Exito")
               if (ck2=="1"):
                             print("Sending Email NOW...")
                             d=str(destino.get())
                             a=str(asunto.get())
                             c=str(cuerpo.get())
                             enc="#!/bin/bash"
                             e=" echo "
                             tab=" "
                             cd='"'
                             b="|"
                             comando=" | mail -s"
                             #-------------------------------- Variable provisional -----------------------
                             ruta="cd /home/sandoval/Backups"
                             v='file=$(ls -l | tail -nl | cut -d " " -f9)'
                             ad="uuencode $file $file > /tmp/out.mail"
                             ap=" < /tmp/out.mail"
                             llavei="{"
                             llavef="}"
                             apc=" cat /tmp/out.mail"
                             cadena0=(str(e)+''+str(cd)+''+str(c)+''+str(cd))
                             cadena1=(str(comando)+''+str(tab)+''+str(cd)+''+str(a)+''+str(cd)+''+str(tab)+''+str(d))
                             os.system("sudo chmod -R 777 /home/sandoval/send2.sh")
                             pf=open("/home/sandoval/send2.sh","w")
                             pf.write(enc)
                             pf.write("\n")
                             pf.write(ruta)
                             pf.write("\n")
                             pf.write(v)
                             pf.write("\n")
                             pf.write(ad)
                             pf.write("\n")
                             pf.write(llavei)
                             pf.write("\n")
                             pf.write(cadena0)
                             pf.write("\n")
                             pf.write(apc)
                             pf.write("\n")
                             pf.write(llavef)
                             pf.write(cadena1)
                             pf.write("\n")
                             pf.close()
                             time.sleep(0.1)

                             #ejecutar el script
                             os.system("sudo /./home/sandoval/send2.sh")
                             clean()
                             messagebox.showinfo("INFO",message="Correo Enviado Con Exito")



            
def EvaluarCheck1():
                    print("Listar Respaldo")
                    ck1=str(check1.get())
                    
                    if(ck1=="1"):
                                os.system("sudo ls -l /home/sandoval/Backups > infobak.txt")
                                valor1=subprocess.check_output("cat /home/sandoval/infobak.txt",shell=True)
                                area1=scrolledtext.ScrolledText(v0,width=80,height=15,bg="#F8F8FF", fg="black")
                                area1.place(x=10,y=220)
                                area1.insert(END,valor1)

                    if(ck1=="0"):
                                messagebox.showinfo("INFO",message="Casilla Vacia")
                                  



def EvaluarCheck2():
                    print("Adjuntar Respaldo....")



def CrearBK():
               os.system("sudo /./home/sandoval/backupsunah.sh")
               messagebox.showinfo("INFO",message="Respaldo Creado con Exito")



def EvaluarComboMenu():
                        print("Menu de Opciones ...")
                        cb=str(combomenu.get())

                        if(cb=="Firewall"):
                                           v2=Toplevel()
                                           v2.title("Configuracion de Firewall")
                                           v2.geometry("800x400+200+200")
                                           v2.configure(bg="lavender")
                                           #tipo de textos
                                           text_t=font.Font(family="Arial",size=18)
                                           text_p=font.Font(family="Arial",size=12)

                                           def EvaluarRadio2():# aqui se van a agregar las opcioens de ver puertos agregar o elimianr puertos dependiendoi que eligan con los radiobutton
                                                               print("pruebas")
                                                               vinet2=inetfire.get()

                                                               if(vinet2==2):
                                                                             print("eliminar puertos")
                                                                             global puerto2,protocolo2
                                                                             puerto2=StringVar()
                                                                             protocolo2=StringVar()

                                                                             def Eliminar_Puerto():
                                                                                 print("Se elimino Puerto")
                                                                                 pu=str(puerto2.get())
                                                                                 pro=str(protocolo2.get())
                                                                                 enc="#!/bin/bash"
                                                                                 abi="sudo ufw enable"
                                                                                 e="sudo ufw delete allow "
                                                                                 p="/"
                                                                                 if pro:
                                                                                        fila1=(str(e)+''+str(pu)+''+str(p)+''+str(pro))
                                                                                 else:
                                                                                      fila1 = (str(e)+''+str(pu))

                                                                                      
                                                                                 #Eliminar puertos metodo mas facil :)
                                                                                    
                                                                                 #os.system("sudo chmod -R 777 /home/sandoval/deletepuerto.sh")# dar permisos
                                                                                 os.system(abi)
                                                                                 os.system(fila1)
                                                                                 #pf=open("/home/sandoval/deletepuerto.sh","w")
                                                                                 #pf.write(enc)
                                                                                 #pf.write("\n")
                                                                                 #pf.write(abi)
                                                                                 #pf.write("\n")
                                                                                 #pf.write(fila1)
                                                                                 #time.sleep(0.1)# ya esta solo hay que probarlo
                                                                                 #os.system("sudo /./home/sandoval/deletepuerto.sh")
                                                                                 #clean()
                                                                                 messagebox.showinfo("INFO",message="Se a eliminado el puerto exitosamente ")
                                                                                 


                                                                             label_puerto2=Label(v2,text="Puerto a eliminar:",font=text_p,bg="lavender",fg="black").place(x=310,y=100)
                                                                             label_proto2=Label(v2,text="Ingrese su protocolo:",font=text_p,bg="lavender",fg="black").place(x=310,y=190)
                                
                                                                             #variables
                                                                             txt_puerto2=Entry(v2,textvariable=puerto2,width=25).place(x=550,y=100)
                                                                             txt_proto2=Entry(v2,textvariable=protocolo2,width=25).place(x=550,y=190)
                                                                             btn_eliminarPuerto=Button(v2,text="Eliminar",command=Eliminar_Puerto).place(x=330,y=260)# boton que llevara a cabo la funcion
                                                                             
                                                                             

                                                               

                                                               if(vinet2==3):
                                                                             print("mostrar puertos") #Nota ver si se sale rentable activar el firebase antes de mostrar los datos
                                                                             os.system("sudo ufw enable")
                                                                             os.system("sudo ufw status numbered > /home/sandoval/puertos.txt")
                                                                             # se lee el archivo donde esta los puertos
                                                                             valor1 = subprocess.check_output("cat puertos.txt", shell=True, text=True)
                                                                             # Crear área de texto para mostrar el resultado
                                                                             area1 = scrolledtext.ScrolledText(v2, width=60, height=15,bg="#F8F8FF", fg="black")
                                                                             area1.place(x=210, y=100)
                                                                             area1.insert(END, valor1)

                                                               

                                                               if(vinet2==1): #Agregar puerto
                                                                             global puerto,protocolo
                                                                             puerto=StringVar()
                                                                             protocolo=StringVar()


                                                                             def Agregar_Puerto():
                                                                                 print("se agrego puerto")
                                                                                 pu=str(puerto.get())
                                                                                 pro=str(protocolo.get())
                                                                                 enc="#!/bin/bash"
                                                                                 abi="sudo ufw enable"
                                                                                 permiso="sudo ufw allow "
                                                                                 p="/"
                                                                                 if pro:
                                                                                        fila1=(str(permiso)+''+str(pu)+''+str(p)+''+str(pro))
                                                                                 else:
                                                                                      fila1 = (str(permiso)+''+str(pu))
                                                                                      
                                                                                 fila1=(str(permiso)+''+str(pu)+''+str(p)+str(pro))

                                                                                 #ejecutar el script para agregar puertos(lo comentariado era una prueba se opto mejor este metodo)
                                                                                 os.system(abi)
                                                                                 os.system(fila1)
                                                                                 #os.system("sudo chmod -R 777 /home/sandoval/addPuerto.sh")# dar permisos
                                                                                 #pf=open("/home/sandoval/addPuerto.sh","w")
                                                                                 #pf.write(enc)
                                                                                 #pf.write("\n")
                                                                                 #pf.write(abi)
                                                                                 #pf.write("\n")
                                                                                 #pf.write(fila1)
                                                                                 #time.sleep(0.1)# ya esta solo hay que probarlo
                                                                                 #os.system("sudo /./home/sandoval/addPuerto.sh")
                                                                                 #clean()
                                                                                 messagebox.showinfo("INFO",message="Se a agregado puerto exitosamente ")

                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 

                                                                             
                                                                             label_puerto=Label(v2,text="Puerto que desea agregar:",font=text_p,bg="lavender",fg="black").place(x=310,y=100)
                                                                             label_proto=Label(v2,text="Ingrese el protocolo:",font=text_p,bg="lavender",fg="black").place(x=310,y=190)
                                
                                                                             #variables
                                                                             txt_puerto=Entry(v2,textvariable=puerto,width=25).place(x=550,y=100)
                                                                             txt_proto=Entry(v2,textvariable=protocolo,width=25).place(x=550,y=190)
                                                                             btn_agregarPuerto=Button(v2,text="Agregar",command=Agregar_Puerto).place(x=330,y=260)# boton que llevara a cabo la funcion

                                                                            
                                                                             
                                                                             
                                                               

                                                               





                                           
                                           #labels
                                                                        
                                           label_t=Label(v2,text="Configuracion de firewall",font=text_t,bg="lavender",fg="black").place(x=100,y=5)
                                           label_inet=Label(v2,text="Menu de Puertos",font=text_t,bg="lavender",fg="black").place(x=20,y=50)
                                           global inetfire
                                           style = ttk.Style()
                                           style.configure("Custom.TRadiobutton", background="lavender")
                                           inetfire=IntVar()
                                           r1=ttk.Radiobutton(v2,text="Agregar puerto",variable=inetfire,value=1,command=EvaluarRadio2,style="Custom.TRadiobutton")
                                           r1.place(x=20,y=120)
                                           r2=ttk.Radiobutton(v2,text="Eliminar puerto",variable=inetfire,value=2,command=EvaluarRadio2,style="Custom.TRadiobutton")
                                           r2.place(x=20,y=190)
                                           r3=ttk.Radiobutton(v2,text="Listar puertos",variable=inetfire,value=3,command=EvaluarRadio2,style="Custom.TRadiobutton")
                                           r3.place(x=20,y=260)

                                           v2.mainloop()
                            


                        
                        if(cb=="Configurar_IP"):
                                                v1=Toplevel()
                                                v1.title("Configuracion Protocolo TCP /IPV4")
                                                v1.geometry("700x300+250+250")
                                                v1.configure(bg="lavender")


                                                def EvaluarRadio():
                                                                    vinet=inet.get()
                                                                    if (vinet==1):
                                                                                 global ether,ipaddress,netmask,gateway,dns
                                                                                 ether=StringVar()
                                                                                 ipaddress=StringVar()
                                                                                 netmask=StringVar()
                                                                                 gateway=StringVar()
                                                                                 dns=StringVar()


                                                                                 def inet_static_interface():
                                                                                     e=str(ether.get())
                                                                                     ip=str(ipaddress.get())
                                                                                     n=str(netmask.get())
                                                                                     gw=str(gateway.get())
                                                                                     ds=str(dns.get())
                                                                                     tipo="static"
                                                                                     #constantes
                                                                                     linea1="auto lo"
                                                                                     linea2="iface lo inet loopback"
                                                                                     linea3="auto "
                                                                                     linea3_A=(str(linea3)+''+str(e)) #choose
                                                                                     linea4a="iface "
                                                                                     linea4b="inet "
                                                                                     linea4_A=(str(linea4a)+''+str(e)+''+str(linea4b)+''+str(tipo)) #choose
                                                                                     linea5="address "
                                                                                     linea5_A=(str(linea5)+''+str(ip)) #choose
                                                                                     linea6="netmask "
                                                                                     linea6_A=(str(linea6)+''+str(n)) #choose
                                                                                     linea7="gateway "
                                                                                     linea7_A=(str(linea7)+''+str(gw)) #choose
                                                                                     linea8="dns-nameservers "
                                                                                     linea8_A=(str(linea8)+''+str(ds)) #choose

                                                                                     os.system("sudo chmod -R 777 /etc/network/interfaces")
                                                                                     os.system("sudo echo 1 > /etc/network/interfaces")
                                                                                     pf=open("/etc/network/interfaces","w")
                                                                                     pf.write(linea1)
                                                                                     pf.write("\n")
                                                                                     pf.write(linea2)
                                                                                     pf.write("\n")
                                                                                     pf.write(linea3_A)
                                                                                     pf.write("\n")
                                                                                     pf.write(linea4_A)
                                                                                     pf.write("\n")
                                                                                     pf.write(linea5_A)
                                                                                     pf.write("\n")
                                                                                     pf.write(linea6_A)
                                                                                     pf.write("\n")
                                                                                     pf.write(linea7_A)
                                                                                     pf.write("\n")
                                                                                     pf.write(linea8_A)
                                                                                     pf.write("\n")
                                                                                     pf.close()
                                                                                     time.sleep(0.1)
                                                                                     os.system("sudo chmod -R 644 /etc/network/interfaces")
                                                                                     os.system("sudo ifdown enp0s3 && ifup enp0s3")
                                                                                     messagebox.showinfo("INFO",message="Cambios Aplicad en RED")
                                
                                                            
                                                                                 def updateEther():
                                                                                     os.system('lshw -C network | grep "enp0s3" | cut -d " " -f10 > inter.txt')
                                                                                     valor=subprocess.check_output("cat inter.txt",shell=True)
                                                                                     valorf=valor.strip()
                                                                                     ether.set(valorf)


                                                                                

                                                                                 updateEther()
                                                                                 
                                                                                 label_ether=Label(v1,text="Interface Statica:",font=text_p).place(x=20,y=80)
                                                                                 label_ip=Label(v1,text="IP adress: ",font=text_p).place(x=20,y=110)
                                                                                 label_mask=Label(v1,text="NetMask:",font=text_p).place(x=20,y=140)
                                                                                 label_gw=Label(v1,text="Getway:",font=text_p).place(x=20,y=170)
                                                                                 label_dns=Label(v1,text="DNS: ",font=text_p).place(x=20,y=200)
                                                                                 #variables
                                                                               
                                                                                 txt_ether=Entry(v1,textvariable=ether,width=15).place(x=170,y=80)
                                                                                 txt_ip=Entry(v1,textvariable=ipaddress,width=20).place(x=120,y=110)
                                                                                 txt_mask=Entry(v1,textvariable=netmask,width=20).place(x=120,y=140)
                                                                                 txt_gw=Entry(v1,textvariable=gateway,width=20).place(x=120,y=170)
                                                                                 txt_dns=Entry(v1,textvariable=dns,width=20).place(x=120,y=200)

                                                                                 btn_save=Button(v1,text="save",command=inet_static_interface).place(x=120,y=260)
                                                                                 


                                                                                 
                                                                    if (vinet==2):
                                                                                 global ether2
                                                                                 ether2=StringVar()
                                                                                 def updateEther2():
                                                                                     os.system('lshw -C network | grep "enp0s3" | cut -d " " -f10 > inter.txt')
                                                                                     valor=subprocess.check_output("cat inter.txt",shell=True,text=True)
                                                                                     valorf=valor.strip()
                                                                                     ether2.set(valorf)
                                                                                 

                                                                                 
                                                                                 updateEther2()
                                                                                 
                                                                                 def inet_dhcp_interface():
                                                                                     e=str(ether2.get())
                                                                                     tipo="dhcp"
                                                                                     #constantes
                                                                                     linea1="auto lo" #chose
                                                                                     linea2="iface lo inet loopback" #choose
                                                                                     linea3="auto "
                                                                                     linea3_A=(str(linea3)+''+str(e)) #choose
                                                                                     linea4a="iface "
                                                                                     linea4b="inet "
                                                                                     linea4_A=(str(linea4a)+''+str(e)+''+str(linea4b)+''+str(tipo)) #choose
                                                                                     os.system("sudo chmod -R 777 /etc/network/interfaces")
                                                                                     os.system("sudo echo 1 > /etc/network/interfaces")
                                                                                     pf=open("/etc/network/interfaces","w")
                                                                                     pf.write(linea1)
                                                                                     pf.write("\n")
                                                                                     pf.write(linea2)
                                                                                     pf.write("\n")
                                                                                     pf.write(linea3_A)
                                                                                     pf.write("\n")
                                                                                     pf.write(linea4_A)
                                                                                     pf.write("\n")
                                                                                     pf.close()
                                                                                     time.sleep(0.1)
                                                                                     os.system("sudo chmod -R 644 /etc/network/interfaces")
                                                                                     os.system("sudo ifdown enp0s3 && ifup enp0s3")
                                                                                     messagebox.showinfo("INFO",message="Cambios Aplicad en RED")


                                                                        
                                                                                    
                                                                                 label_ether=Label(v1,text="Interface DHCP:",font=text_p).place(x=20,y=100)
                                                                                 txt_ether=Entry(v1,textvariable=ether2,width=15).place(x=150,y=80)
                                                                                 btn_dhcp=Button(v1,text="Activar-DHCP",command=inet_dhcp_interface).place(x=120,y=150)

                                                                    if (vinet==3):
                                                                                 os.system("cat /etc/network/interfaces > infored.txt")
                                                                                 valor1=subprocess.check_output("cat /home/sandoval/infored.txt",shell=True)
                                                                                 area1=scrolledtext.ScrolledText(v1,width=80,height=5)
                                                                                 area1.place(x=10,y=150)
                                                                                 area1.insert(END,valor1)

                                                                                 
                                                                    if (vinet==4):
                                                                                 print("Metodo Netplan")
                                                                                 global netplan
                                                                                 netplan=IntVar()

                                                                                 
                                                                                        

                                                                                 def EvaluarRadioNet():


                                                                                     
                                                                                        net=netplan.get()
                                                                                        if(net==1):
                                                                                            print("ip estatica")
                                                                                            global ether3,ipaddress2,netmask2,gateway2,dns2
                                                                                            ether3=StringVar()
                                                                                            ipaddress2=StringVar()
                                                                                            netmask2=StringVar()
                                                                                            gateway2=StringVar()
                                                                                            dns2=StringVar()


                                                                                            def netplan_static_interface():
                                                                                                                           print("prueba botton")
                                                                                                                           e=str(ether3.get())
                                                                                                                           ip = ipaddress2.get()
                                                                                                                           mask = netmask2.get()
                                                                                                                           gw = gateway2.get()
                                                                                                                           dns = dns2.get()
                                                                                                                           linea1 = "network:"
                                                                                                                           linea2 = "    version: 2"
                                                                                                                           linea3 = "    ethernets:"
                                                                                                                           linea4 = f"        {e}:"
                                                                                                                           linea5 = "            dhcp4: false"
                                                                                                                           linea6 = f"            addresses: [{ip}/{mask}]"
                                                                                                                           linea7 = f"            gateway4: {gw}"
                                                                                                                           linea8 = f"            nameservers:"
                                                                                                                           linea9 = f"                addresses: [{dns}]"
                                                                                                                           
                                                                                                                           os.system("sudo chmod -R 777 /etc/netplan/50-cloud-init.yaml")#damos permisos para escribir
                                                                                                                           os.system("sudo echo 1 > /etc/netplan/50-cloud-init.yaml")#limpiamos el archivo poniendole un 1
                                                                                                                           pf=open("/etc/netplan/50-cloud-init.yaml","w")# mientras miramos como va la movida
                                                                                                                           pf.write(linea1)
                                                                                                                           pf.write("\n")
                                                                                                                           pf.write(linea2)
                                                                                                                           pf.write("\n")
                                                                                                                           pf.write(linea3)
                                                                                                                           pf.write("\n")
                                                                                                                           pf.write(linea4)
                                                                                                                           pf.write("\n")
                                                                                                                           pf.write(linea5)
                                                                                                                           pf.write("\n")
                                                                                                                           pf.write(linea6)
                                                                                                                           pf.write("\n")
                                                                                                                           pf.write(linea7)
                                                                                                                           pf.write("\n")
                                                                                                                           pf.write(linea8)
                                                                                                                           pf.write("\n")
                                                                                                                           pf.write(linea9)
                                                                                                                           pf.close()
                                                                                                                           time.sleep(0.1)
                                                                                                                           os.system("sudo chmod -R 600 /etc/netplan/50-cloud-init.yaml")
                                                                                                                           os.system("sudo netplan apply") #la volvemos statica
                                                                                                                           
                                                                                                                           

                                                                                                                           
                                                                                                                           
                                                                                                                           
                                                                                                                           


                                                                                            def updateEther3(): #solucionar esto despeus si no borrarlo(ya se soluciono)
                                                                                                               os.system('lshw -C network | grep "enp0s3" | cut -d " " -f10 > inter.txt')
                                                                                                               valor=subprocess.check_output("cat inter.txt",shell=True,text=True)
                                                                                                               valorf=valor.strip()
                                                                                                               ether3.set(valorf)


                                                                                

                                                                                            updateEther3()
                                                                                 
                                                                                            label_ether=Label(v1,text="Interface Statica:",font=text_p,bg="lavender",fg="black").place(x=20,y=130)
                                                                                            label_ip=Label(v1,text="Direccion IP: ",font=text_p,bg="lavender",fg="black").place(x=20,y=165)
                                                                                            label_mask=Label(v1,text="NetMask:",font=text_p,bg="lavender",fg="black").place(x=20,y=200)
                                                                                            label_gw=Label(v1,text="Getway:",font=text_p,bg="lavender",fg="black").place(x=20,y=230)
                                                                                            label_dns=Label(v1,text="DNS: ",font=text_p,bg="lavender",fg="black").place(x=20,y=260)
                                                                                            #variables
                                                                               
                                                                                            txt_ether=Entry(v1,textvariable=ether3,width=15).place(x=170,y=130)
                                                                                            txt_ip=Entry(v1,textvariable=ipaddress2,width=20).place(x=155,y=165)
                                                                                            txt_mask=Entry(v1,textvariable=netmask2,width=20).place(x=120,y=200)
                                                                                            txt_gw=Entry(v1,textvariable=gateway2,width=20).place(x=120,y=230)
                                                                                            txt_dns=Entry(v1,textvariable=dns2,width=20).place(x=120,y=260) #borrar hasta aqui en todo caso(ya solucionado)
                                                                                            btn_static=Button(v1,text="Activar IP statica",command=netplan_static_interface).place(x=320,y=250)

                                                                                            
                                                                                            
                                                                                            

                                                                                            
                                                                                        if(net==2):
                                                                                            print("ip dhcp via netplan")
                                                                                            global ether4
                                                                                            ether4=StringVar()

                                                                                            def netplan_dhcp_interface():
                                                                                                                         print("Cambio a dhcp por medio de netplan")
                                                                                                                         e=str(ether4.get())
                                                                                                                         linea1 = "network:"
                                                                                                                         linea2 = "    ethernets:"
                                                                                                                         linea3 = f"        {e}:"
                                                                                                                         linea4 = "            dhcp4: true"
                                                                                                                         linea5 = "    version: 2"
                                                                                                                         os.system("sudo chmod -R 777 /etc/netplan/50-cloud-init.yaml")#damos permisos para escribir
                                                                                                                         os.system("sudo echo 1 > /etc/netplan/50-cloud-init.yaml")#limpiamos el archivo poniendole un 1
                                                                                                                         
                                                                                                                         pf=open("/etc/netplan/50-cloud-init.yaml","w")# mientras miramos como va la movida
                                                                                                                         pf.write(linea1)
                                                                                                                         pf.write("\n")
                                                                                                                         pf.write(linea2)
                                                                                                                         pf.write("\n")
                                                                                                                         pf.write(linea3)
                                                                                                                         pf.write("\n")
                                                                                                                         pf.write(linea4)
                                                                                                                         pf.write("\n")
                                                                                                                         pf.write(linea5)
                                                                                                                         pf.close()
                                                                                                                         time.sleep(0.1)
                                                                                                                         os.system("sudo chmod -R 600 /etc/netplan/50-cloud-init.yaml")#seria volver a permisos 600?
                                                                                                                         os.system("sudo netplan apply") #comando para agregar metodo dhcp via netplan

                                                                                                                         
                                                                                                                         
                                                                                                                         
                                                                                                                         


                                                                                            
                                                                                            def updateEther4():
                                                                                                               os.system('lshw -C network | grep "enp0s3" | cut -d " " -f10 > inter.txt')
                                                                                                               valor=subprocess.check_output("cat inter.txt",shell=True,text=True)
                                                                                                               valorf=valor.strip()
                                                                                                               ether4.set(valorf)
                                                                                 

                                                                                 
                                                                                            updateEther4()
                                                                                            label_ether=Label(v1,text="Interface DHCP:",font=text_p,bg="lavender",fg="black").place(x=20,y=120)
                                                                                            txt_ether=Entry(v1,textvariable=ether4,width=15).place(x=180,y=120)
                                                                                            btn_dhcp=Button(v1,text="Activar-DHCP",command=netplan_dhcp_interface).place(x=120,y=170)
                                                                                            

                                                                                        
                                                                                     
                                                                                 

                                                                                 style = ttk.Style()
                                                                                 style.configure("Custom.TRadiobutton", background="lavender")
                                                                                 r1=ttk.Radiobutton(v1,text="Static",variable=netplan,value=1,command=EvaluarRadioNet,style="Custom.TRadiobutton")
                                                                                 r1.place(x=250,y=80)
                                                                                 r2=ttk.Radiobutton(v1,text="DHCP",variable=netplan,value=2,command=EvaluarRadioNet,style="Custom.TRadiobutton")
                                                                                 r2.place(x=340,y=80)
                                                                                 

                                                                                 



                                                

                                                text_t=font.Font(family="Arial",size=18)
                                                text_p=font.Font(family="Arial",size=12)

                                                label_t=Label(v1,text="Configuracion IPV4",font=text_t,bg="lavender",fg="black").place(x=180,y=5)
                                                label_inet=Label(v1,text="Metodo Red ---->",font=text_p,bg="lavender",fg="black").place(x=20,y=50)
                                                global inet
                                                style = ttk.Style()
                                                style.configure("Custom.TRadiobutton", background="lavender")
                                                
                                                inet=IntVar()
                                                r1=ttk.Radiobutton(v1,text="Static",variable=inet,value=1,command=EvaluarRadio,style="Custom.TRadiobutton")
                                                r1.place(x=180,y=50)
                                                r2=ttk.Radiobutton(v1,text="DHCP",variable=inet,value=2,command=EvaluarRadio,style="Custom.TRadiobutton")
                                                r2.place(x=260,y=50)
                                                r3=ttk.Radiobutton(v1,text="Consultar IP",variable=inet,value=3,command=EvaluarRadio,style="Custom.TRadiobutton")
                                                r3.place(x=330,y=50)
                                                r4=ttk.Radiobutton(v1,text="Netplan",variable=inet,value=4,command=EvaluarRadio,style="Custom.TRadiobutton")
                                                r4.place(x=450,y=50) # vamos a crear otros dos para este metodo r1.1 y r1.2
                                                
                                                


                                                v1.mainloop()

#variables fonts
text1=font.Font(family="Arial",size=18)
text2=font.Font(family="Arial",size=12)

label_t=Label(v0,text="Tollkits for Linux",font=text1,bg="lavender",fg="black").place(x=100,y=5)
label_destino=Label(v0,text="Destinatario :",font=text2,bg="lavender",fg="black").place(x=8,y=70)
label_asunto=Label(v0,text="Asunto: ",font=text2,bg="lavender",fg="black").place(x=8,y=100)
label_cuerpo=Label(v0,text="Cuerpo Correo:",font=text2,bg="lavender",fg="black").place(x=8,y=130)


#variables gobales
global destino,asunto,cuerpo
destino=StringVar()
asunto=StringVar()
cuerpo=StringVar()
txt_destino=Entry(v0,textvariable=destino,width=30).place(x=130,y=70)
txt_asunto=Entry(v0,textvariable=asunto,width=40).place(x=130,y=100)
txt_cuerpo=Entry(v0,textvariable=cuerpo,width=50).place(x=130,y=130)
style = ttk.Style()
style.configure("Custom.TCheckbutton", background="lavender", foreground="black")
global check1
check1=StringVar()
c1=ttk.Checkbutton(v0,text="Listar Respaldos",variable=check1,command=EvaluarCheck1, style="Custom.TCheckbutton")
c1.place(x=290,y=45)
global check2
check2=StringVar()
c2=ttk.Checkbutton(v0,text="Adjuntar Respaldos",variable=check2,command=EvaluarCheck2, style="Custom.TCheckbutton")
c2.place(x=430,y=45)
#combobox
global combomenu
combomenu=StringVar()
cmb1=ttk.Combobox(v0,textvariable=combomenu,values=["Configurar_IP","Listar-Usuarios","Matar Usuarios","Firewall"])
cmb1.place(x=800,y=7)
btn_combo=Button(v0,text="Ejecutar",command=EvaluarComboMenu).place(x=700,y=5)

# botones
btn_enviar=Button(v0,text="Enviar",command=SendMail).place(x=30,y=180)
btn_crearbk=Button(v0,text="CrearRespaldo",command=CrearBK).place(x=100,y=180)


v0.mainloop()

