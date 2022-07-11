# import entire module
import modules.module_weight_converter #modules is the module folder
# import a function from a module
from modules.module_print import hey
print(modules.module_weight_converter.kg_to_lbs(70))
print(hey("Riz"))