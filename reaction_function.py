from koneroj import *
reaction_function = writable_concept("Reaction function")
reaction_function.parts["Definition"].desplay += r""" The reaction function of a firm is a function which maps the quantity firm A will produce for each expected quantity of firm B. 
$$ f(\text{quantity firm A expects firm B to produce}) =\text{ quantity firm A will produce} $$
"""
reaction_function.write_module_doc()    
