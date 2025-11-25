import turtle

def koch_snowflake(t, length, level):
    """
    Малює один бік сніжинки Коха рекурсивно.
    t: об'єкт turtle
    length: довжина лінії
    level: рівень рекурсії
    """
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, level-1)
        t.left(60)
        koch_snowflake(t, length, level-1)
        t.right(120)
        koch_snowflake(t, length, level-1)
        t.left(60)
        koch_snowflake(t, length, level-1)

def draw_snowflake(length, level):
    """
    Малює повну сніжинку Коха (трикутник).
    """
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-length/2, length/3)  # центруємо фрактал
    t.pendown()
    
    for _ in range(3):
        koch_snowflake(t, length, level)
        t.right(120)
    
    turtle.done()

def main():
    try:
        level = int(input("Введіть рівень рекурсії (ціле число >=0): "))
        if level < 0:
            raise ValueError
    except ValueError:
        print("Помилка: введіть коректне ціле число >=0")
        return
    
    length = 300  # довжина сторони сніжинки
    draw_snowflake(length, level)

if __name__ == "__main__":
    main()
