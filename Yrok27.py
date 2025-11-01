from ursina import * 
from ursina.color import orange
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina() # підключаємо вікно ігри
player = FirstPersonController(
    model="sphere",
    color=color.orange,
    scale=(1,2,1),
    texture="brick",
    texture_scale=(1024,1024),
    position=(0,5,0),
    speed = 10,
    mouse_sensitivity = Vec2(40,40), # Чутливість мишки (X,Y)
    gravity = 0.2 ,
    jump_height = 5, # висота стрибка
    jump_duration = 10, # тривалість стрибка 
    collider = "box", # форма зіткнення
    height = 2, # висота камери 
    camera_pivot_y=0.5 # зміщення камери вгору/вниз
)
ground = Entity(model="plane",scale=50,texture="grass",texture_scale=(50,50),collider="box")
Monetka = Entity(model="sphere",scale=(1,2,1),color=color.yellow,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)))
wall = Entity(model="cube",scale=(50,10,1),color=color.red,collider="box",position=(0,1,25),texture="brick",texture_scale=(50,10))
wall = Entity(model="cube",scale=(50,10,1),color=color.red,collider="box",position=(0,1,-25),texture="brick",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,50),color=color.red,collider="box",position=(25,1,0),texture="brick",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,50),color=color.red,collider="box",position=(-25,1,0),texture="brick",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(random.uniform(5,20),10,1),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
wall = Entity(model="cube",scale=(1,10,random.uniform(5,20)),color=color.red,collider="box",position=(random.uniform(-25,25),1,random.uniform(-25,25)),texture="grass",texture_scale=(50,10))
Sky()
score = 0
score_text = Text(text=f"Монет: {score}", position=(-0.85, 0.45), scale=2, color=color.black)

def update():
    global score
    if distance(player.position, Monetka.position) < 2:
        score += 1
        score_text.text = f"Монет: {score}"
        Monetka.position = (random.uniform(-20,20), 1, random.uniform(-20,20))

app.run() # запуск гри

