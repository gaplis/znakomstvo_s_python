import model
import view

def run():
    model.init(view.get_value(), view.get_value(), view.get_value())
    view.view_data(model.calculation())