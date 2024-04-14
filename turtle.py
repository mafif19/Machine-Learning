import turtle

# Membuat jendela untuk menggambar
window = turtle.Screen()
window.title("Contoh Menggunakan Turtle")

# Membuat objek turtle
pen = turtle.Turtle()

# Menggambar sebuah pola sederhana
pen.color("blue")
pen.begin_fill()
for _ in range(4):
    pen.forward(100)
    pen.right(90)
pen.end_fill()

# Menutup jendela saat di-klik
window.mainloop()
