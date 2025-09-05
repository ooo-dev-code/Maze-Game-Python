
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y-50}")



def setup_maze(grid_size, start_x, start_y, cell_size, c, maze, rects):
    selected_rect = None
    end = None
    for i in range(grid_size):
        for j in range(grid_size):
            x1 = start_x + j * cell_size
            y1 = start_y + i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            
            rect_id = c.create_rectangle(
                x1, y1, x2, y2,
                fill="green" if maze[i][j] == "A" or maze[i][j] == "B" else "grey",
                outline="black",
                width=2,
            )
            
            secure = True
            if maze[i][j] == 0 or maze[i][j] == "A" or maze[i][j] == "B":
                secure = True
            else:
                secure = False
                
            rects[rect_id] = (x1, y1, x2, y2, secure)
            
            if maze[i][j] == "A":
                selected_rect = {
                    "coords": (x1, y1, x2, y2),
                    "secure": secure
                }
                
            if maze[i][j] == "B":
                end = (x1, y1, x2, y2, secure)
                
    return rects, selected_rect, end
