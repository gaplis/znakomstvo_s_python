import model_mult as mult
import model_sum as sum
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    sum.init(value_a, value_b)
    result = sum.do_it()
    view.view_data(result)