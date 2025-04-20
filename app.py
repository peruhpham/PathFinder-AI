import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
from maze_solver import MazeSolver
from simpleai.search import astar
from constants import MAP, M, N, W
from map_utils import generate_maze_image
import time

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.dem = 0
        self.old_start_x = -1  # Khởi tạo tọa độ điểm bắt đầu cũ
        self.old_start_y = -1
        self.old_goal_x = -1   # Khởi tạo tọa độ điểm kết thúc cũ
        self.old_goal_y = -1
        self.title('Tìm đường trong mê cung')
        self.image_tk = ImageTk.PhotoImage(generate_maze_image())
        self.cvs_me_cung = tk.Canvas(self, width=N * W, height=M * W)
        self.cvs_me_cung.create_image(0, 0, anchor=tk.NW, image=self.image_tk)
        self.cvs_me_cung.grid(row=0, column=0)
        self.cvs_me_cung.bind("<Button-1>", self.handle_mouse_click)
        # Reset and instructions
        self.setup_menu()

    def setup_menu(self):
        lbl_menu = tk.LabelFrame(self)
        btn_reset = tk.Button(lbl_menu, text='Reset', command=self.reset)
        btn_reset.grid(row=0, column=0)
        lbl_menu.grid(row=0, column=1)

    def handle_mouse_click(self, event):
        """
        Xử lý sự kiện khi người dùng nhấp chuột vào mê cung.
        """
        px, py = event.x, event.y
        x, y = px // W, py // W

        if self.dem == 0:  # Chọn điểm bắt đầu
            if MAP[y][x] == '#':
                return
            MAP[y][x] = 'o'

            # Xóa điểm bắt đầu cũ nếu có
            if self.old_start_x != -1:
                MAP[self.old_start_y][self.old_start_x] = ' '
                self.cvs_me_cung.create_oval(
                    self.old_start_x * W + 2, self.old_start_y * W + 2,
                    (self.old_start_x + 1) * W - 2, (self.old_start_y + 1) * W - 2,
                    outline='#FFFFFF', fill='#FFFFFF'
                )

            # Vẽ điểm bắt đầu mới
            self.cvs_me_cung.create_oval(
                x * W + 2, y * W + 2, 
                (x + 1) * W - 2, (y + 1) * W - 2,
                outline='#BF8725', fill='#BF8725'
            )
            self.old_start_x, self.old_start_y = x, y
            self.dem += 1

        elif self.dem == 1:  # Chọn điểm kết thúc
            if MAP[y][x] == '#':
                return
            MAP[y][x] = 'x'

            # Xóa điểm kết thúc cũ nếu có
            if self.old_goal_x != -1:
                MAP[self.old_goal_y][self.old_goal_x] = ' '
                self.cvs_me_cung.create_rectangle(
                    self.old_goal_x * W + 2, self.old_goal_y * W + 2,
                    (self.old_goal_x + 1) * W - 2, (self.old_goal_y + 1) * W - 2,
                    outline='#FFFFFF', fill='#FFFFFF'
                )

            # Vẽ điểm kết thúc mới
            self.cvs_me_cung.create_rectangle(
                x * W + 2, y * W + 2,
                (x + 1) * W - 2, (y + 1) * W - 2,
                outline='#BF8725', fill='#BF8725'
            )
            self.old_goal_x, self.old_goal_y = x, y
            self.dem += 1

            # Chạy thuật toán tìm đường
            problem = MazeSolver(MAP)
            result = astar(problem, graph_search=True)
            path = [x[1] for x in result.path()]

            # Hiển thị đường đi
            for i in range(len(path)):
                px, py = path[i]
                self.cvs_me_cung.create_rectangle(
                    px * W + 2, py * W + 2, 
                    (px + 1) * W - 2, (py + 1) * W - 2,
                    outline='#817821', fill='#817821'
                )
                time.sleep(0.5)
                self.cvs_me_cung.update()
            messagebox.showinfo('Result', 'Success')

    def reset(self):
        """
        Đặt lại trạng thái của mê cung.
        """
        self.cvs_me_cung.delete(tk.ALL)
        self.cvs_me_cung.create_image(0, 0, anchor=tk.NW, image=self.image_tk)
        self.dem = 0

        for x in range(M):
            for y in range(N):
                if MAP[x][y] in ('o', 'x'):
                    MAP[x][y] = ' '

