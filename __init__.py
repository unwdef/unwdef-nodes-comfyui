from .unwdef_nodes.nodes_lora import *
from .unwdef_nodes.nodes_text import *

NODE_CLASS_MAPPINGS = {
    "RandomizeLoras": RandomizeLoras,
    "RandomizeLorasStack": RandomizeLorasStack,
    "RandomTextFromMultiline": RandomTextFromMultiline,
    "TextMultilineWithVariables" : TextMultilineWithVariables,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RandomizeLoras": "Randomize LoRAs",
    "RandomizeLorasStack": "Randomize LoRAs (Stack)",
    "RandomTextFromMultiline": "Random Text From Multiline",
    "TextMultilineWithVariables": "Text Multiline with Variables",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]