import tkinter as tk
import random

# === Clicker Game ===
def iniciar_clicker():
    janela = tk.Toplevel()
    janela.title("Clicker Game")
    janela.geometry("300x200")
    contador = tk.IntVar(value=0)
    tempo = tk.IntVar(value=10)

    def clicar():
        if tempo.get() > 0:
            contador.set(contador.get() + 1)

    def atualizar_tempo():
        if tempo.get() > 0:
            tempo.set(tempo.get() - 1)
            janela.after(1000, atualizar_tempo)
        else:
            botao.config(state="disabled")
            tk.Label(janela, text=f"⏱️ Você clicou {contador.get()} vezes!").pack(pady=10)

    tk.Label(janela, text="Clique o máximo que puder em 10 segundos!").pack(pady=10)
    botao = tk.Button(janela, text="CLIQUE!", font=("Arial", 16), command=clicar)
    botao.pack(pady=10)
    tk.Label(janela, textvariable=tempo).pack()
    atualizar_tempo()

# === Quiz ISCZN ===
def iniciar_quiz():
    perguntas = [
        ("Qual linguagem estamos usando?", "Python"),
        ("Quantos segundos tem 1 minuto?", "60"),
        ("Qual planeta é conhecido como planeta vermelho?", "Marte")
    ]
    janela = tk.Toplevel()
    janela.title("Quiz ISCZN")
    janela.geometry("400x200")

    pontuacao = tk.IntVar(value=0)
    indice = tk.IntVar(value=0)

    pergunta_label = tk.Label(janela, text="")
    pergunta_label.pack(pady=10)
    resposta_entry = tk.Entry(janela)
    resposta_entry.pack()

    def verificar():
        resposta = resposta_entry.get().strip().lower()
        correta = perguntas[indice.get()][1].lower()
        if resposta == correta:
            pontuacao.set(pontuacao.get() + 1)
        resposta_entry.delete(0, tk.END)
        indice.set(indice.get() + 1)
        if indice.get() < len(perguntas):
            pergunta_label.config(text=perguntas[indice.get()][0])
        else:
            pergunta_label.config(text=f"Fim do quiz! Pontuação: {pontuacao.get()}")
            resposta_entry.pack_forget()
            botao_verificar.pack_forget()

    botao_verificar = tk.Button(janela, text="Responder", command=verificar)
    botao_verificar.pack(pady=10)
    pergunta_label.config(text=perguntas[indice.get()][0])

# === Snake Game ===
class SnakeGame:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Snake - ISCZN Arcade")
        self.window.resizable(False, False)
        self.canvas = tk.Canvas(self.window, width=400, height=400, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100)]
        self.direction = "Right"
        self.food = None
        self.score = 0
        self.running = True

        self.canvas.focus_set()
        self.canvas.bind("<Up>", lambda e: self.set_direction("Up"))
        self.canvas.bind("<Down>", lambda e: self.set_direction("Down"))
        self.canvas.bind("<Left>", lambda e: self.set_direction("Left"))
        self.canvas.bind("<Right>", lambda e: self.set_direction("Right"))

        self.spawn_food()
        self.update()

    def set_direction(self, new_dir):
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_dir != opposites.get(self.direction):
            self.direction = new_dir

    def spawn_food(self):
        while True:
            x = random.randint(0, 19) * 20
            y = random.randint(0, 19) * 20
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def update(self):
        if not self.running:
            return

        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= 20
        elif self.direction == "Down":
            head_y += 20
        elif self.direction == "Left":
            head_x -= 20
        elif self.direction == "Right":
            head_x += 20

        new_head = (head_x, head_y)

        if (head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400 or new_head in self.snake):
            self.running = False
            self.canvas.create_text(200, 200, text=f"Game Over\nScore: {self.score}", fill="white", font=("Arial", 16))
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.spawn_food()
        else:
            self.snake.pop()

        self.draw()
        self.window.after(100, self.update)

    def draw(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+20, y+20, fill="green")
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx+20, fy+20, fill="red")
        self.canvas.create_text(40, 10, text=f"Score: {self.score}", fill="white", font=("Arial", 12))

# === Menu Principal ===
def abrir_menu():
    root = tk.Tk()
    root.title("ISCZN Games Arcade")
    root.geometry("400x350")

    tk.Label(root, text="🎮 ISCZN Games Arcade 🎮", font=("Arial", 18)).pack(pady=20)
    tk.Button(root, text="Clicker Game", width=25, command=iniciar_clicker).pack(pady=5)
    tk.Button(root, text="Quiz ISCZN", width=25, command=iniciar_quiz).pack(pady=5)
    tk.Button(root, text="Snake", width=25, command=SnakeGame).pack(pady=5)
    tk.Button(root, text="Sair", width=25, command=root.quit).pack(pady=20)

    root.mainloop()

abrir_menu()