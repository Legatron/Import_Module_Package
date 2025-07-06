from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from graphicswithpython import  window, delay, color, midpointcircle

if __name__ == '__main__':
    current_date = datetime.now().strftime("%d.%m.%Y")
    print(f"[{current_date}] Запуск программы")

    calculate_salary()
    get_employees()

    window(600, 550)  # first make window to get output there
    # Midpoint  Circle Line
    midpointcircle(70, 200, 200, "line", color("red"))
    # Midpoint Circle Dash
    midpointcircle(70, 400, 200, "dash", color("green"))
    # Midpoint Circle Dotted
    midpointcircle(70, 200, 400, "dotted", color("white"))
    # Midpoint Circle Solid
    midpointcircle(70, 400, 400, "solid", color("blue"))
    # Midpoint Circle Dash and Normal
    midpointcircle(60, 300, 300, "dottedandline", color("yellow"))
    delay(1000)
    print("Программа завершена")