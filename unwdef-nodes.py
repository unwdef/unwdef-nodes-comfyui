import random
from nodes import LoraLoader
import folder_paths

class RandomizeLoras:
    def __init__(self):
      pass

    @classmethod
    def INPUT_TYPES(cls):
        loras = ["None"] + folder_paths.get_filename_list("loras")
        inputs = {
            "required": {
                "model": ("MODEL",),
                "clip": ("CLIP", ),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "max_random": ("INT", {"default": 10, "min": 1, "max": 10}),
            }
        }
        for i in range(1, 11):
            inputs["required"][f"lora_{i}"] = (loras,)
            inputs["required"][f"min_str_{i}"] = ("FLOAT", {"default": 0.5, "min": -10.0, "max": 10.0, "step": 0.01})
            inputs["required"][f"max_str_{i}"] = ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01})

        return inputs
  
    RETURN_TYPES = ("MODEL", "CLIP", "STRING")
    RETURN_NAMES = ("model", "clip", "chosen loras")
    FUNCTION = "load_lora"
    CATEGORY = "unwdef"

    def load_lora(self, model, clip, seed, max_random, **kwargs):      
        if seed is not None:
          random.seed(seed)  # For reproducibility

        # Initialize list to hold lora configurations
        lora_configs = []

        # Dynamically extract lora configurations from kwargs
        for i in range(1, 11): 
            lora_name = kwargs.get(f"lora_{i}")
            min_str = kwargs.get(f"min_str_{i}")
            max_str = kwargs.get(f"max_str_{i}")

            if lora_name != "None":
                lora_configs.append({"name": lora_name, "min_str": min_str, "max_str": max_str})

        # Initialize the string to hold chosen loras and values
        chosen_str = ""

        # Check if no loras are selected
        if len(lora_configs) == 0:
            return (model, clip, chosen_str)
        
        # Adjust max_random
        if (max_random > len(lora_configs)):
            max_random = len(lora_configs)

        # Randomly choose some of these loras
        chosen_loras = random.sample(lora_configs, random.randint(1, max_random))

        for lora in chosen_loras:
            # Randomly determine a value between min_str and max_str
            strength = random.uniform(lora['min_str'], lora['max_str'])

            # Apply changes to model and clip
            model, clip = LoraLoader().load_lora(model, clip, lora['name'], strength, strength)

            # Append the current lora and its value to the string
            chosen_str += f"<lora:{lora['name'].split('.')[0]}:{strength:.2f}>, "

        # Find the last occurrence of the comma to remove it
        last_comma_index = chosen_str.rfind(',')
        # Slice the string to remove the last comma and everything after it
        if last_comma_index != -1:
            chosen_str = chosen_str[:last_comma_index]
            
        return (model, clip, chosen_str)
  

NODE_CLASS_MAPPINGS = {
    "RandomizeLoras": RandomizeLoras
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RandomizeLoras": "Randomize LoRAs"
}