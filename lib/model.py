from .log import get_logger
log = get_logger(__name__)
log.info("Begin Diffusion imports.")
import torch
from diffusers import StableDiffusionPipeline

model_id2 = "riffusion/riffusion-model-v1"
log.info("Initializing diffusion model.")
pipe2 = StableDiffusionPipeline.from_pretrained(model_id2, torch_dtype=torch.float16)
log.info("Model initialized.")
pipe2 = pipe2.to("cuda")
