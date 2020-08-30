import turtle

# screen settings
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)
screen.bgcolor('black')
screen.delay(0)
# turtle settings
leo = turtle.Turtle()
leo.pensize(4)
leo.speed(1)
leo.setpos(-WIDTH // 6, HEIGHT // 6)
leo.color('gold')
# l-system settings
gens = 5
axiom = 'F++F++F'
chr_1, rule_1 = 'F', 'F-F++F-F'
step = 600
angle = 60


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else chr for chr in axiom]) # <-----


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


for gen in range(gens):
    turtle.pencolor('white')
    turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
    turtle.clear()
    turtle.write(f'generation: {gen}', align="left", font=("Arial", 60, "normal"))

    leo.setheading(0)
    leo.goto(-WIDTH // 6, HEIGHT // 6)
    leo.clear()

    length = step / pow(3, gen)
    for chr in axiom:
        if chr == chr_1:
            leo.forward(length)
        elif chr == '+':
            leo.right(angle)
        elif chr == '-':
            leo.left(angle)

    axiom = apply_rules(axiom)

screen.exitonclick()
