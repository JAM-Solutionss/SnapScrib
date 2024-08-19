from llama_summarizer import Llama_Summarizer
from summarizer_interface import Summarizer

summarizer = {
    "llama": Llama_Summarizer
}

def get_summarizer(summarizer_model: str=None) -> Summarizer:
    """
    Get a summarizer instance based on the specified model.

    Args:
        summarizer_model (str, optional): The name of the summarizer model to use. If not provided, the default "llama" model will be used.

    Returns:
        Summarizer: An instance of the specified summarizer model.

    Raises:
        ValueError: If the specified summarizer model is not recognized.
    """

    if summarizer_model is None:
        return summarizer["llama"]
    elif summarizer_model in summarizer:
        return summarizer[summarizer_model]
    else:
        raise ValueError(f"Unknown summarizer model: {summarizer_model}")