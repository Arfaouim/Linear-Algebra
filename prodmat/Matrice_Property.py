from tkinter import*
import numpy as np

m1=np.loadtxt('test.txt')
m2=np.loadtxt('test1.txt')

def one():
    one1=Label(text=m1,font=40,fg='red',bg='black')
    one1.place(relx=0.11, rely=0.99, anchor=SW)
def two():
    onedisplay=Label(text=m2,font=40,fg='red',bg='black')
    onedisplay.place(relx=0.33, rely=0.99, anchor=SW)





def produit():
    print(np.dot(m1,m2))
    answer = np.dot(m1,m2)# faire apparaitre le resultat a l'aide label sur l'app
    answerdisplay = Label(text=answer,font=40,fg='red',bg='black')
    answerdisplay.place(relx=0.60, rely=0.99, anchor=SW)
def dim():
    print(m1.shape)
    print(m2.shape)
    print('dimension est  ',np.dot(m1,m2).shape)
    answer_2 ='Dimension(m1*m2)est  ',np.dot(m1,m2).shape# faire apparaitre le resultat a l'aide label sur l'app
    answer_2display = Label(bg='red',fg='white',text=answer_2,font=20)
    answer_2display.place(relx=0.00, rely=0.68, anchor=SW)
def help():
    answer_3display = Label(bg='red',fg='white',text='Pour plus d''info =https://fr.wikipedia.org/wiki/Produit_matriciel ')
    answer_3display.place(relx=0.00, rely=0.76, anchor=SW)

root=Tk()
root.title("Produit Matricielle 0.1")
root.geometry("350x400")


label_1= Label(text='                ici partie!!                ',bg='pink',fg='white',font=20)
label_1.place(relx=0.20, rely=0.80, anchor=SW)

button_0=Button(root,text='Lire M1',font=30,relief=RAISED,bg="red",fg="white",bd='5',cursor='spider',command=one)
button_0.pack(fill=X)

button_00=Button(root,text='Lire M2',font=30,relief=RAISED,bg="grey",fg="navy",bd='5',cursor='star',command=two)
button_00.pack(fill=X)



button_1=Button(root,text='Calcul',font=30,relief=RAISED,bg="navy",fg="white",bd='5',cursor='pirate',command=produit)
button_1.pack(fill=X)

button_2=Button(root,text='Dimension',font=30,relief=RAISED,bg="green",fg="navy",bd='5',cursor='heart',command=dim)
button_2.pack(fill=X)

button_3=Button(root,text='Help',font=30,relief=RAISED,bg="pink",fg="black",bd='5',cursor='dotbox',command=help)
button_3.pack(fill=X)
button_4=Button(root,text='Exit',font=30,relief=RAISED,bg="yellow",fg="black",bd='5',cursor='mouse',command=root.destroy)
button_4.pack(fill=X)

root.mainloop()
