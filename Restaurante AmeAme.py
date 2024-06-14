from tkinter import *
import random
import time
from tkinter import filedialog,messagebox

def salidaPrincipal():
    ventana.destroy()

Title = ("arial black", 30)
Subtitle = ("Cambria", 15)

ventana = Tk()
ventana.geometry("800x700")
ventana.title("RESTAURANTE")
ventana.config(bg="#FF9933")


tituloPrincipal = Label( text="Restaurante AmeAme", font=Title, fg="#202020", bg="#FF9933")
tituloPrincipal.pack()

subPrincipal = Label( bd=5, text="BIENVENIDOS", font=Subtitle, fg="#202020", bg="#FF9933")
subPrincipal.pack()


def menu():
    ventanaMenu = Toplevel()
    ventanaMenu.config(bg="#202020")
    ventanaMenu.title("Menu")
    ventanaMenu.geometry("1260x650")

    def texto():
        textoText.delete(1.0, END)
        x = random.randint(1, 10000)
        noText = "No" + str(x)
        fecha = time.strftime("%d-%m-%y")
        textoText.insert(END, "Ayuda.." + noText + "\t\t\t\t Fecha:" + fecha + "\n")
        textoText.insert(END, "************************************************************************\n")
        textoText.insert(END, "Instrucciones \t\t\t Para ordenar usted debe:\n")
        textoText.insert(END, "¡BIENVENIDO! "+ "\n")
        textoText.insert(END, "Haga click sobre el check para desbloquear la funcion y "+"\n" +
                         "digitar las unidades que desea consumir")
        textoText.insert(END, "\n\n")
        textoText.insert(END, "************************************************************************\n\n")
        textoText.insert(END, "Le deseamos lo mejor\t\t\t"+ "\n")

    def borrar():
        textoText.delete(1.0, END)
        txtAsado.set("0")
        txtMilanesa.set("0")
        txtPure.set("0")
        txtEnsalada.set("0")
        txtPapas.set("0")
        txtPollo.set("0")
        txtPastas.set("0")
        txtArroz.set("0")
        txtPizza.set("0")


        txtPepsi.set("0")
        txtCoca.set("0")
        txtFanta.set("0")
        txtSprite.set("0")
        txtAguaS.set("0")
        txtAgua.set("0")
        txtAndes.set("0")
        txtQuilmes.set("0")
        txtVino.set("0")

        
        textAsado.config(state=DISABLED)
        textMilanesa.config(state=DISABLED)
        textPure.config(state=DISABLED)
        textEnsalada.config(state=DISABLED)
        textPapas.config(state=DISABLED)
        textPollo.config(state=DISABLED)
        textPastas.config(state=DISABLED)
        textArroz.config(state=DISABLED)
        textPizza.config(state=DISABLED)

    
        textPepsi.config(state=DISABLED)
        textPepsi.config(state=DISABLED)
        textFanta.config(state=DISABLED)
        textSprite.config(state=DISABLED)
        textAguaS.config(state=DISABLED)
        textAgua.config(state=DISABLED)
        textAndes.config(state=DISABLED)
        textQuilmes.config(state=DISABLED)
        textVino.config(state=DISABLED)


        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)
        var18.set(0)

        global varcostocomida, varcostobebidas, total
        varcostocomida=0
        varcostobebidas=0
        total=0

        entryCostoComida.config(state=NORMAL)
        entryCostoComida.delete(0, END)
        entryCostoComida.insert(0, varcostocomida)
        entryCostoComida.config(state=DISABLED)

        entryCostoBebidas.config(state=NORMAL)
        entryCostoBebidas.delete(0, END)
        entryCostoBebidas.insert(0, varcostobebidas)
        entryCostoBebidas.config(state=DISABLED)

        entryTotal.config(state=NORMAL)
        entryTotal.delete(0, END)
        entryTotal.insert(0, total)
        entryTotal.config(state=DISABLED)

    def salirMenu():
        ventanaMenu.destroy()

    def totalFinal():
        global varcostocomida, varcostobebidas, total
        t_asado = int(textAsado.get()) 
        t_milanesa = int(textMilanesa.get())
        t_pure = int(textPure.get())
        t_ensalada = int(textEnsalada.get())
        t_papas = int(textPapas.get())
        t_pollo = int(textPollo.get())
        t_pastas = int(textPastas.get())
        t_arroz = int(textArroz.get())
        t_pizza = int(textPizza.get())
        varcostocomida = (t_asado * 1000) + (t_milanesa * 700) + (t_pure * 500) + (t_ensalada * 750) + (t_papas * 1500) + (t_pollo * 800) + (t_pastas * 1100) + (t_arroz * 600) + (t_pizza * 1500)
        entryCostoComida.config(state=NORMAL)
        entryCostoComida.delete(0, END)
        entryCostoComida.insert(0, varcostocomida)
        entryCostoComida.config(state=DISABLED)

        t_pepsi = int(textPepsi.get())
        t_coca = int(textCocaCola.get())
        t_fanta = int(textFanta.get())
        t_sprite = int(textSprite.get())
        t_aguaS = int(textAguaS.get())
        t_agua = int(textAgua.get())
        t_andes = int(textAndes.get())
        t_quilmes = int(textQuilmes.get())
        t_vino = int(textVino.get())
        varcostobebidas = (t_pepsi * 600) + (t_coca * 600) + (t_fanta * 600) + (t_sprite * 600) + (t_aguaS * 500) + (
                    t_agua * 500) + (t_andes * 800) + (t_quilmes * 800) + (t_vino * 800)
        entryCostoBebidas.config(state=NORMAL)
        entryCostoBebidas.delete(0, END)
        entryCostoBebidas.insert(0, varcostobebidas)
        entryCostoBebidas.config(state=DISABLED)

        total = varcostocomida + varcostobebidas
        entryTotal.config(state=NORMAL)
        entryTotal.delete(0, END)
        entryTotal.insert(0, total)
        entryTotal.config(state=DISABLED)

    def asado(): 
        if var1.get() == 1:
            textAsado.config(state=NORMAL)
            textAsado.delete(0, END)
            textAsado.focus()
        else: 
            textAsado.config(state=DISABLED)
            txtAsado.set("0")

    def milanesa():
        if var2.get() == 1:
            textMilanesa.config(state=NORMAL)
            textMilanesa.delete(0, END)
            textMilanesa.focus()
        else:
            textMilanesa.config(state=DISABLED)
            txtMilanesa.set("0")

    def pure():
        if var3.get() == 1:
            textPure.config(state=NORMAL)
            textPure.delete(0, END)
            textPure.focus()
        else:
            textPure.config(state=DISABLED)
            txtPure.set("0")

    def ensalada():
        if var4.get() == 1:
            textEnsalada.config(state=NORMAL)
            textEnsalada.delete(0, END)
            textEnsalada.focus()
        else:
            textEnsalada.config(state=DISABLED)
            txtEnsalada.set("0")

    def papas():
        if var5.get() == 1:
            textPapas.config(state=NORMAL)
            textPapas.delete(0, END)
            textPapas.focus()
        else:
            textPapas.config(state=DISABLED)
            txtPapas.set("0")

    def pollo():
        if var6.get() == 1:
            textPollo.config(state=NORMAL)
            textPollo.delete(0, END)
            textPollo.focus()
        else:
            textPollo.config(state=DISABLED)
            txtPollo.set("0")

    def pastas():
        if var7.get() == 1:
            textPastas.config(state=NORMAL)
            textPastas.delete(0, END)
            textPastas.focus()
        else:
            textPastas.config(state=DISABLED)
            txtPastas.set("0")

    def arroz():
        if var8.get() == 1:
            textArroz.config(state=NORMAL)
            textArroz.delete(0, END)
            textArroz.focus()
        else:
            textArroz.config(state=DISABLED)
            txtArroz.set("0")

    def pizza():
        if var9.get() == 1:
            textPizza.config(state=NORMAL)
            textPizza.delete(0, END)
            textPizza.focus()
        else:
            textPizza.config(state=DISABLED)
            txtPizza.set("0")


    def pepsi():
        if var10.get() == 1:
            textPepsi.config(state=NORMAL)
            textPepsi.delete(0, END)
            textPepsi.focus()
        else:
            textPepsi.config(state=DISABLED)
            txtPepsi.set("0")

    def coca():
        if var11.get() == 1:
            textCocaCola.config(state=NORMAL)
            textCocaCola.delete(0, END)
            textCocaCola.focus()
        else:
            textCocaCola.config(state=DISABLED)
            txtCoca.set("0")

    def fanta():
        if var12.get() == 1:
            textFanta.config(state=NORMAL)
            textFanta.delete(0, END)
            textFanta.focus()
        else:
            textFanta.config(state=DISABLED)
            txtFanta.set("0")

    def sprite():
        if var13.get() == 1:
            textSprite.config(state=NORMAL)
            textSprite.delete(0, END)
            textSprite.focus()
        else:
            textSprite.config(state=DISABLED)
            txtSprite.set("0")

    def aguaS():
        if var14.get() == 1:
            textAguaS.config(state=NORMAL)
            textAguaS.delete(0, END)
            textAguaS.focus()
        else:
            textAguaS.config(state=DISABLED)
            txtAguaS.set("0")

    def agua():
        if var15.get() == 1:
            textAgua.config(state=NORMAL)
            textAgua.delete(0, END)
            textAgua.focus()
        else:
            textAgua.config(state=DISABLED)
            txtAgua.set("0")

    def andes():
        if var16.get() == 1:
            textAndes.config(state=NORMAL)
            textAndes.delete(0, END)
            textAndes.focus()
        else:
            textAndes.config(state=DISABLED)
            txtAndes.set("0")

    def quilmes():
        if var17.get() == 1:
            textQuilmes.config(state=NORMAL)
            textQuilmes.delete(0, END)
            textQuilmes.focus()
        else:
            textQuilmes.config(state=DISABLED)
            txtQuilmes.set("0")

    def vino():
        if var18.get() == 1:
            textVino.config(state=NORMAL)
            textVino.delete(0, END)
            textVino.focus()
        else:
         textVino.config(state=DISABLED)
         txtVino.set("0")
         textVino.focus()


    marcoSuperior = Frame(ventanaMenu, bd=5, relief=RIDGE, bg="#FF9933")
    marcoSuperior.pack(side=TOP)

    tituloMenu = Label(marcoSuperior, text="ORDENE AQUI", font=Title, fg="black", bg="#FF8000", width=53)
    tituloMenu.grid(row=0, column=0)


    marcoMenu = Frame(ventanaMenu, bd=10, relief=RIDGE, bg="#FF8000")
    marcoMenu.pack(side=LEFT)

    marcoCosto = Frame(marcoMenu, bd=2, relief=RIDGE, bg="#FF8000")
    marcoCosto.pack(side=BOTTOM)

    marcoComida = LabelFrame(marcoMenu, text="Platos", bd=5, font=Subtitle, fg="white", relief=RIDGE, bg="#202020")
    marcoComida.pack(side=LEFT)

    marcoBebidas = LabelFrame(marcoMenu, text="Bebidas", bd=5, font=Subtitle, fg="white", relief=RIDGE, bg="#202020")
    marcoBebidas.pack(side=LEFT)


    ladoDerecho = Frame(marcoMenu, bd=5, relief=RIDGE, bg="#202020")
    ladoDerecho.pack(side=RIGHT)
    marcoTexto = Frame(ladoDerecho, bd=5, relief=RIDGE, bg="#202020")
    marcoTexto.pack()
    marcoBoton = Frame(ladoDerecho, bd=5, relief=RIDGE, bg="#202020")
    marcoBoton.pack()


    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    var16 = IntVar()
    var17 = IntVar()
    var18 = IntVar()


    txtAsado = StringVar()
    txtAsado.set("0")
    txtMilanesa = StringVar()
    txtMilanesa.set("0")
    txtPure = StringVar()
    txtPure.set("0")
    txtEnsalada = StringVar()
    txtEnsalada.set("0")
    txtPapas = StringVar()
    txtPapas.set("0")
    txtPollo = StringVar()
    txtPollo.set("0")
    txtPastas = StringVar()
    txtPastas.set("0")
    txtArroz = StringVar()
    txtArroz.set("0")
    txtPizza = StringVar()
    txtPizza.set("0")


    txtPepsi = StringVar()
    txtPepsi.set("0")
    txtCoca = StringVar()
    txtCoca.set("0")
    txtFanta = StringVar()
    txtFanta.set("0")
    txtSprite = StringVar()
    txtSprite.set("0")
    txtAguaS = StringVar()
    txtAguaS.set("0")
    txtAgua = StringVar()
    txtAgua.set("0")
    txtAndes = StringVar()
    txtAndes.set("0")
    txtQuilmes = StringVar()
    txtQuilmes.set("0")
    txtVino = StringVar()
    txtVino.set("0")


    varcostocomida = StringVar()

    Asado = Checkbutton(marcoComida, text="Asado----$1000", font=Subtitle, onvalue=1, offvalue=0, variable=var1,
                        command=asado)
    Asado.grid(row=0, column=0, sticky=W)
    Milanesa = Checkbutton(marcoComida, text="Milanesa--$700", font=Subtitle, onvalue=1, offvalue=0, variable=var2,
                           command=milanesa)
    Milanesa.grid(row=1, column=0, sticky=W)
    Pure = Checkbutton(marcoComida, text="Pure-------$500", font=Subtitle, onvalue=1, offvalue=0, variable=var3,
                       command=pure)
    Pure.grid(row=2, column=0, sticky=W)
    Ensalada = Checkbutton(marcoComida, text="Ensalada-$750", font=Subtitle, onvalue=1, offvalue=0, variable=var4,
                           command=ensalada)
    Ensalada.grid(row=3, column=0, sticky=W)
    PapasFritas = Checkbutton(marcoComida, text="Papas\nFritas----$1500", font=Subtitle, onvalue=1, offvalue=0,
                              variable=var5, command=papas)
    PapasFritas.grid(row=4, column=0, sticky=W)
    Pollo = Checkbutton(marcoComida, text="Pollo-------$800", font=Subtitle, onvalue=1, offvalue=0, variable=var6,
                        command=pollo)
    Pollo.grid(row=5, column=0, sticky=W)
    Pastas = Checkbutton(marcoComida, text="Pastas----$1100", font=Subtitle, onvalue=1, offvalue=0, variable=var7,
                         command=pastas)
    Pastas.grid(row=6, column=0, sticky=W)
    Arroz = Checkbutton(marcoComida, text="Arroz------$600", font=Subtitle, onvalue=1, offvalue=0, variable=var8,
                        command=arroz)
    Arroz.grid(row=7, column=0, sticky=W)
    Pizza = Checkbutton(marcoComida, text="Pizza-----$1500", font=Subtitle, onvalue=1, offvalue=0, variable=var9,
                        command=pizza)
    Pizza.grid(row=8, column=0, sticky=W)

    textAsado = Entry(marcoComida, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtAsado)
    textAsado.grid(row=0, column=1)
    textMilanesa = Entry(marcoComida, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtMilanesa)
    textMilanesa.grid(row=1, column=1)
    textPure = Entry(marcoComida, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtPure)
    textPure.grid(row=2, column=1)
    textEnsalada = Entry(marcoComida, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtEnsalada)
    textEnsalada.grid(row=3, column=1)
    textPapas = Entry(marcoComida, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtPapas)
    textPapas.grid(row=4, column=1)
    textPollo = Entry(marcoComida, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtPollo)
    textPollo.grid(row=5, column=1)
    textPastas = Entry(marcoComida, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtPastas)
    textPastas.grid(row=6, column=1)
    textArroz = Entry(marcoComida, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtArroz)
    textArroz.grid(row=7, column=1)
    textPizza = Entry(marcoComida, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtPizza)
    textPizza.grid(row=8, column=1)


    Pepsi = Checkbutton(marcoBebidas, text="Pepsi---------$600", font=Subtitle, onvalue=1, offvalue=0, variable=var10,
                        command=pepsi)
    Pepsi.grid(row=0, column=0, sticky=W)
    CocaCola = Checkbutton(marcoBebidas, text="Coca-Cola---$600", font=Subtitle, onvalue=1, offvalue=0, variable=var11,
                           command=coca)
    CocaCola.grid(row=1, column=0, sticky=W)
    Fanta = Checkbutton(marcoBebidas, text="Fanta---------$600", font=Subtitle, onvalue=1, offvalue=0, variable=var12,
                        command=fanta)
    Fanta.grid(row=2, column=0, sticky=W)
    Sprite = Checkbutton(marcoBebidas, text="Sprite--------$600", font=Subtitle, onvalue=1, offvalue=0, variable=var13,
                         command=sprite)
    Sprite.grid(row=3, column=0, sticky=W)
    AguaS = Checkbutton(marcoBebidas, text="Agua\nSaborizada-$500", font=Subtitle, onvalue=1, offvalue=0,
                        variable=var14, command=aguaS)
    AguaS.grid(row=4, column=0, sticky=W)
    Agua = Checkbutton(marcoBebidas, text="Agua---------$500", font=Subtitle, onvalue=1, offvalue=0, variable=var15,
                       command=agua)
    Agua.grid(row=5, column=0, sticky=W)
    Andes = Checkbutton(marcoBebidas, text="Andes--------$800", font=Subtitle, onvalue=1, offvalue=0, variable=var16,
                        command=andes)
    Andes.grid(row=6, column=0, sticky=W)
    Quilmes = Checkbutton(marcoBebidas, text="Quilmes------$800", font=Subtitle, onvalue=1, offvalue=0, variable=var17,
                          command=quilmes)
    Quilmes.grid(row=7, column=0, sticky=W)
    Vino = Checkbutton(marcoBebidas, text="Vino----------$800", font=Subtitle, onvalue=1, offvalue=0, variable=var18,
                       command=vino)
    Vino.grid(row=8, column=0, sticky=W)

    textPepsi = Entry(marcoBebidas, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtPepsi)
    textPepsi.grid(row=0, column=1)
    textCocaCola = Entry(marcoBebidas, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtCoca)
    textCocaCola.grid(row=1, column=1)
    textFanta = Entry(marcoBebidas, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtFanta)
    textFanta.grid(row=2, column=1)
    textSprite = Entry(marcoBebidas, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtSprite)
    textSprite.grid(row=3, column=1)
    textAguaS = Entry(marcoBebidas, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtAguaS)
    textAguaS.grid(row=4, column=1)
    textAgua = Entry(marcoBebidas, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtAgua)
    textAgua.grid(row=5, column=1)
    textAndes = Entry(marcoBebidas, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtAndes)
    textAndes.grid(row=6, column=1)
    textQuilmes = Entry(marcoBebidas, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtQuilmes)
    textQuilmes.grid(row=7, column=1)
    textVino = Entry(marcoBebidas, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtVino)
    textVino.grid(row=8, column=1)


    costoComida = Label(marcoCosto, text="Total de comida $", font=Subtitle, bd=10, bg="#FF9933", fg="white")
    costoComida.grid(row=0, column=0)
    entryCostoComida = Entry(marcoCosto, font=Subtitle, bd=5, width=14, state="readonly")
    entryCostoComida.grid(row=0, column=1, padx=5)

    costoBebidas = Label(marcoCosto, text="Total Bebidas $", font=Subtitle, bd=10, bg="#FF9933", fg="white")
    costoBebidas.grid(row=1, column=0)
    entryCostoBebidas = Entry(marcoCosto, font=Subtitle, bd=5, width=14, state="readonly")
    entryCostoBebidas.grid(row=1, column=1, padx=5)

    costoTotal = Label(marcoCosto, text="Total $", font=Subtitle, bd=10, bg="#FF9933", fg="white")
    costoTotal.grid(row=2, column=0)
    entryTotal = Entry(marcoCosto, font=Subtitle, bd=5, width=14, state="readonly")
    entryTotal.grid(row=2, column=1, padx=5)


    textoText = Text(marcoTexto, font=("arial", 12, "bold"), bd=3, width=48, height=12)
    textoText.grid(row=0, column=0)

    botonTotal = Button(marcoBoton, text="Total", font=Subtitle, fg="white", bg="#202020", bd=4, padx=5, command=totalFinal)
    botonTotal.grid(row=0,column=0)

    botonTexto = Button(marcoBoton, text="Ayuda", font=Subtitle, fg="white", bg="#202020", bd=4, padx=5, command=texto)
    botonTexto.grid(row=0, column=1)


    botonBorrar = Button(marcoBoton, text="Borrar", font=Subtitle, fg="white", bg="#202020", bd=4, padx=5, command=borrar)
    botonBorrar.grid(row=0, column=3)

    botonSalida = Button(marcoBoton, text="Salir", font=Subtitle, fg="white", bg="#202020", bd=4, padx=5, command=salirMenu)
    botonSalida.grid(row=0, column=4)

menuBoton = Button(ventana, font=Subtitle, text="Ordenar", command=menu, height="2", width="20")
menuBoton.config(bd=2, bg="#202020", fg="white")
menuBoton.pack()
menuBoton.place(x=200, y=300)


salir = Button(ventana, font=Subtitle, text="Salir", command=salidaPrincipal, width="20", height="2")
salir.config(bd=2, bg="#202020", fg="white")
salir.pack()
salir.place(x=200, y=400)

ventana.mainloop()




