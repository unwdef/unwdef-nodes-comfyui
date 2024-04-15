import random
import json

class RandomTextFromMultiline:
    def __init__(self):
      pass

    @classmethod
    def INPUT_TYPES(cls):
        inputs = {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "lines_count": ("INT", {"default": 1, "min": 1, "max": 0xffffffffffffffff}),
                "delimiter": ("STRING", { "multiline": False, "default": ", " }),
                "text": ("STRING", { "multiline": True, "default": "" }),
            }
        }

        return inputs

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    FUNCTION = "random_text_from_multiline"
    CATEGORY = "unwdef/text"

    def random_text_from_multiline(self, seed, lines_count, delimiter, text): 
        if seed is not None:
            random.seed(seed)  # For reproducibility

        # Split the text into separate lines
        lines = text.splitlines()

        # If lines_count is greater than the number of available lines, adjust it
        lines_count = min(lines_count, len(lines))

        # Select random unique lines
        selected_lines = random.sample(lines, lines_count)

        # Join the selected lines with the delimiter
        result = delimiter.join(selected_lines)

        return (result, )
    
class TextMultilineWithVariables:
    def __init__(self):
      pass

    @classmethod
    def INPUT_TYPES(cls):
        inputs = {
            "required": {
                "text": ("STRING", { "multiline": True, "default": "picture of !var_1 in the style of !var_2" }),
            }
        }

        inputs["optional"] = {
            "var_1": ("STRING", { "multiline": False, "default": "", "forceInput": True }),
            "var_2": ("STRING", { "multiline": False, "default": "", "forceInput": True }),
            "var_3": ("STRING", { "multiline": False, "default": "", "forceInput": True }),
            "var_4": ("STRING", { "multiline": False, "default": "", "forceInput": True }),
            "var_5": ("STRING", { "multiline": False, "default": "", "forceInput": True }),
        }

        return inputs

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    FUNCTION = "variable_text_multiline"
    CATEGORY = "unwdef/text"

    def variable_text_multiline(self, text=None, var_1=None, var_2=None, var_3=None, var_4=None, var_5=None): 
        if text == None: 
            return ("", )
        
        # Create a dictionary to map placeholders to their corresponding variables
        replacements = {
            '!var_1': var_1 if var_1 is not None else '',
            '!var_2': var_2 if var_2 is not None else '',
            '!var_3': var_3 if var_3 is not None else '',
            '!var_4': var_4 if var_4 is not None else '',
            '!var_5': var_5 if var_5 is not None else ''
        }     

        # Replace each placeholder in the text with its corresponding value from the dictionary
        for key, value in replacements.items():
            text = text.replace(key, value)

        return (text, )