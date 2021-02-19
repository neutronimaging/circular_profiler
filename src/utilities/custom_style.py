from IPython.core.display import HTML


def style():
    css_file = 'src/utilities/custom_nb_styling.css'
    return HTML(open(css_file, "r").read())
