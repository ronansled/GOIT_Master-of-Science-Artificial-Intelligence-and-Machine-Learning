import turtle


def draw_pythagoras_tree(t, length, level):
    if level == 0:
        return

    t.forward(length)

    t.left(45)
    draw_pythagoras_tree(t, length * 0.7, level - 1)

    t.right(90)
    draw_pythagoras_tree(t, length * 0.7, level - 1)

    t.left(45)
    t.backward(length)


def main():
    print("Чим більший рівень — тим складніший фрактал.")
    level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.title("Фрактал: Дерево Піфагора")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()

    draw_pythagoras_tree(t, 100, level)

    screen.mainloop()


if __name__ == "__main__":
    main()
