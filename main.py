from metro import *

test = Metro(setup_environment=True)
test.set_language("UKR")

dist, path = test.find_path("Академгородок", "Хрещатик")

test.print_path(dist, path)
