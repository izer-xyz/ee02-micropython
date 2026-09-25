from ee02 import Ee02

print("Hello EE02.")

display = Ee02()
display.begin()
display.set_rotation(1)
display.print_text(50, 50, "Partial update demo")
display.draw_rect(50, 120, 150, 60, display.BLACK)
display.display()
