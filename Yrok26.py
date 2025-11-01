# from ursina import * 
# import random 
# app = Ursina()
# gravets = Entity(model="cube",color=color.red,position=(0,0,0),scale=(1,1,1))
# monetka = Entity(model="sphere",color=color.orange,position=(3,4,3),scale=(0.5,0.5,0.5))
# ochky = 0
# tekst_ochok = Text(text=f"очки {ochky}",position=(-0.85,0.45),scale=2)
# def update():
#     speed = 2
#     if held_keys["shift"]:
#         speed=10
#     if held_keys["w"]:
#         gravets.z+=speed*time.dt
#     if held_keys["s"]:
#         gravets.z-=speed*time.dt
#     if held_keys["d"]:
#         gravets.x+=speed*time.dt
#     if held_keys["a"]:
#         gravets.x-=speed*time.dt
#     if held_keys["up arrow"]:
#         gravets.y+=speed*time.dt
#     if held_keys["down arrow"]:
#         gravets.y-=speed*time.dt
#     vidstan = distance(gravets.position,monetka.position)
#     if vidstan<1:
#         collect()
# def collect():
#     global ochky
#     ochky+=1
#     monetka.position = (random.randint(-4,4),random.randint(-4,4),random.randint(-4,4))
#     tekst_ochok.text = f"очки {ochky}"
# app.run()

from  ursina import * 
import random 
app = Ursina()

gravets = Entity(model="cube",color=color.green,position=(0,0,0),scale=(0.4,0.4,0.4))
obj1 = Entity(model="cube",color=color.blue,position=(2,4,1),scale=(3,1,1))
obj2 = Entity(model="cube",color=color.blue,position=(3,2,3),scale=(3,1,1))
obj3 = Entity(model="cube",color=color.blue,position=(4,1,5),scale=(3,1,1))
monetka = Entity(model="sphere",color=color.orange,position=(3,2,1),scale=(0.5,0.5,0.5))
ochky = 0
tekst_ochok = Text(text=f"очки {ochky}",position=(-0.85,0.45),scale=2)

def update():
    speed = 2
    if held_keys["shift"]:
        speed=10
    if held_keys["w"]:
        gravets.z+=speed*time.dt
    if held_keys["s"]:
        gravets.z-=speed*time.dt
    if held_keys["d"]:
        gravets.x+=speed*time.dt
    if held_keys["a"]:
        gravets.x-=speed*time.dt
    if held_keys["up arrow"]:
        gravets.y+=speed*time.dt
    if held_keys["down arrow"]:
        gravets.y-=speed*time.dt

    vidstan = distance(gravets.position,monetka.position)
    vidstan2 = distance(gravets.position,obj1.position)
    vidstan3 = distance(gravets.position,obj2.position)
    vidstan4 = distance(gravets.position,obj3.position)
    print(vidstan2)
    # print(vidstan3)
    # print(vidstan4)
    if vidstan<1:
        collect()
    if vidstan2  <1: #vidstan3 or vidstan4
        udar()
    if vidstan3  <1: #vidstan3 or vidstan4
        udar()
    if vidstan4  <1: #vidstan3 or vidstan4
        udar()
def udar():
    global ochky
    ochky-=1
    obj1.position = (random.uniform(-4,4),random.uniform(-4,4),random.uniform(-4,4))
    obj2.position = (random.uniform(-4,4),random.uniform(-4,4),random.uniform(-4,4))
    obj3.position = (random.uniform(-4,4),random.uniform(-4,4),random.uniform(-4,4))
    tekst_ochok.text = f"очки {ochky}"
def collect():
    global ochky
    ochky+=1
    monetka.position = (random.uniform(-4,4),random.uniform(-4,4),random.uniform(-4,4))
    tekst_ochok.text = f"очки {ochky}"
# camera.position = (0, 15, -15)
# camera.rotation_x=45
app.run()
