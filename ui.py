from tkinter import *
from system import center_window, setup_maze
from maze import generate_solveable
from menu import menu
import os

grid_size = menu()
cell_size = 620 // grid_size
start_x = (720 - 620) // 2
start_y = (720 - 620) // 2

maze = generate_solveable(grid_size)
total_life = 15
selected_rect = None
clicked = {"rect": None}

w = Tk()

w.title("Maze")
w.resizable(False, False)
w.geometry("720x720")

c = Canvas(w, width=720, height=720, background="darkgrey", highlightbackground="grey", highlightthickness=10)
c.pack()

lives = {}
lives_shadow = {}
lives_inside = {}

for i in range(total_life):
    lives_shadow[i] = c.create_rectangle(
        100 + i*35, 680, 125 + i*35, 705,
        fill="black",
        outline="black",
        width=2,
    )
    lives[i] = c.create_rectangle(
        95 + i*35, 675, 120 + i*35, 700,
        fill="pink",
        outline="red",
        width=2,
    )
    lives_inside[i] = c.create_rectangle(
        100 + i*35, 685, 115 + i*35, 690,
        fill="red",
        outline="black",
        width=2,
    )

rects = {}
rects, selected_rect, end = setup_maze(grid_size, start_x, start_y, cell_size, c, maze, rects)

def erase_square(event):
    global total_life
    global selected_rect
    global clicked
    
    x, y = event.x, event.y
        
    right = (
        x > selected_rect["coords"][2] and
        x < selected_rect["coords"][2] + cell_size and
        y > selected_rect["coords"][1] and
        y < selected_rect["coords"][3]
    )

    left = (
        x < selected_rect["coords"][0] and
        x > selected_rect["coords"][0] - cell_size and
        y > selected_rect["coords"][1] and
        y < selected_rect["coords"][3]
    )

    down = (
        y > selected_rect["coords"][3] and
        y < selected_rect["coords"][3] + cell_size and
        x > selected_rect["coords"][0] and
        x < selected_rect["coords"][2]
    )

    up = (
        y < selected_rect["coords"][1] and
        y > selected_rect["coords"][1] - cell_size and
        x > selected_rect["coords"][0] and
        x < selected_rect["coords"][2]
    )

    adjacent = False

    directions = [right, left, down, up]
    if directions.count(True) == 1:
        adjacent = True
    else:
        adjacent=False
        
    print(adjacent)
        
    for rect_id, (x1, y1, x2, y2, secure) in rects.items():
        if x1 <= x <= x2 and y1 <= y <= y2 and adjacent:
            if secure:
                if clicked["rect"]:
                    c.delete(clicked["rect"])
                    
                if rects[rect_id] == end:
                    endgame("win")
                    
                c.delete(rect_id)
                rec = c.create_rectangle(
                    x1, y1, x2, y2,
                    fill="white",
                    outline="darkblue",
                    width=2,
                )
                rects[rec] = (x1, y1, x2, y2, True)
                del rects[rect_id]
                selected_rect = {
                    "coords": (x1, y1, x2, y2),
                    "secure": True
                }
                s_rect =  c.create_rectangle(
                    x1, y1, x2, y2,
                    fill="cyan",
                    outline="darkblue",
                    width=2,
                )
                clicked["rect"] = s_rect
                break
            
            
            else: 
                rect_id = c.create_rectangle(
                    x1, y1, x2, y2,
                    fill="red",
                    outline="black",
                    width=2,
                )
                
                total_life -= 1
                c.delete(lives[total_life])
                c.delete(lives_shadow[total_life])
                c.delete(lives_inside[total_life])
                del lives[total_life]
                del lives_shadow[total_life]
                del lives_inside[total_life]
                
                if total_life <= 0:
                    endgame("lose")
                    

def restart_game(endgame_canvas):
    endgame_canvas.destroy()
    w.destroy()
    os.system(f'python "{__file__}"')

def endgame(result):
    c.destroy()
    endgame_c = Canvas(w, width=720, height=720, background="black", highlightbackground="grey")
    endgame_c.pack()
    
    if result == "lose":
        endgame_c.create_text(720//2, 720//2, text="GAME OVER", fill="white", font=("Purisa", 75))
    else:
        endgame_c.create_text(720//2, 720//2, text="YOU WON!!!", fill="white", font=("Purisa", 75))
        
    restart_btn = Button(w, text="Restart", font=("Purisa", 20), command=lambda: restart_game(endgame_c))
    restart_btn.place(x=310, y=500)


c.bind("<Button-1>", erase_square)
center_window(w)

w.mainloop()
