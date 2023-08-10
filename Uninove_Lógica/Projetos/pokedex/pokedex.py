import requests
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

#FFFFFF
col0 = '#FFFFFF'
col1 = '#444466'

janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=col0)

ttk.Separator(janela,orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=272)

style = ttk.Style(janela)
style.theme_use('clam')

#frame pokemon
frame_pokemon = Frame(janela,width=550,height=290,relief='flat')
frame_pokemon.grid(row=1,column=0)

#name
poke_name = Label(frame_pokemon,text='Jorge',relief='flat',anchor=CENTER,font=('Fixedsys 20'),bg=col0,fg=col1)
poke_name.place(x=12,y=15)

#category
poke_categ = Label(frame_pokemon,text='Jorge',relief='flat',anchor=CENTER,font=('Ivy 10 bold'),bg=col0,fg=col1)
poke_categ.place(x=12,y=50)

#id
poke_id = Label(frame_pokemon,text='#1010',relief='flat',anchor=CENTER,font=('Ivy 10 bold'),bg=col0,fg=col1)
poke_id.place(x=12,y=75)

#image pokemon
image_pokemon = Image.open('Projetos/pokedex/images/TheRock.png')
image_pokemon = image_pokemon.resize((238,238))
image_pokemon = ImageTk.PhotoImage(image_pokemon)

poke_image = Label(frame_pokemon,image=image_pokemon,text='Jorge',relief='flat',bg=col0,fg=col1)
poke_image.place(x=12,y=50)

poke_categ.lift()
poke_id.lift()

#status
poke_status = Label(janela,text='Status',relief='flat',anchor=CENTER,font=('Verdana 20'),bg=col0,fg=col1)
poke_status.place(x=15,y=310)

#hp
poke_hp = Label(janela,text='HP:2000',relief='flat',anchor=CENTER,font=('Verdana 10'),bg=col0,fg=col1)
poke_hp.place(x=15,y=360)

#attack
poke_attack = Label(janela,text='Ataque:1000',relief='flat',anchor=CENTER,font=('Verdana 10'),bg=col0,fg=col1)
poke_attack.place(x=15,y=380)

#defense
poke_defense = Label(janela,text='Defesa:3000',relief='flat',anchor=CENTER,font=('Verdana 10'),bg=col0,fg=col1)
poke_defense.place(x=15,y=400)

#speed
poke_speed = Label(janela,text='Velocidade:3000',relief='flat',anchor=CENTER,font=('Verdana 10'),bg=col0,fg=col1)
poke_speed.place(x=15,y=420)

#total
poke_speed = Label(janela,text='Total:Infinito',relief='flat',anchor=CENTER,font=('Verdana 15'),bg=col0,fg=col1)
poke_speed.place(x=15,y=460)

#ability
poke_status = Label(janela,text='Habilidades',relief='flat',anchor=CENTER,font=('Verdana 20'),bg=col0,fg=col1)
poke_status.place(x=300,y=310)

#ability1
poke_ability1 = Label(janela,text='Choque Veloz e Furioso',relief='flat',anchor=CENTER,font=('Verdana 10'),bg=col0,fg=col1)
poke_ability1.place(x=300,y=360)

#ability2
poke_ability2 = Label(janela,text='Pedrada',relief='flat',anchor=CENTER,font=('Verdana 10'),bg=col0,fg=col1)
poke_ability2.place(x=300,y=380)

#ability3
poke_ability3 = Label(janela,text='Sombrancelha',relief='flat',anchor=CENTER,font=('Verdana 10'),bg=col0,fg=col1)
poke_ability3.place(x=300,y=400)

#create buttons for pokemons
image_pokemon_min = Image.open('Projetos/pokedex/images/TheRock_min.png')
image_pokemon_min = image_pokemon_min.resize((40,40))
image_pokemon_min = ImageTk.PhotoImage(image_pokemon_min)

poke_image_min = Button(janela,image=image_pokemon_min,text='Jorge',relief='flat',overrelief=RIDGE,anchor=NW,compound=LEFT,padx=5,bg=col0,fg=col1)
poke_image_min.place(x=375,y=66)



janela.mainloop()
def get_ability(poke):
    for i in poke['abilities']:
        print(i['ability']['name'])



def main():
    api = 'https://pokeapi.co/api/v2/pokemon/pikachu'
    res = requests.get(api)
    poke = res.json()
    get_ability(poke)
    pass

#if __name__ == '__main__':
    #main()