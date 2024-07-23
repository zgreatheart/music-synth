from .log import get_logger
log = get_logger(__name__)
log.info("Begin Diffusion imports.")
import torch
from diffusers import StableDiffusionPipeline

model_id2 = "riffusion/riffusion-model-v1"
log.info("Initializing diffusion model.")
pipe2 = StableDiffusionPipeline.from_pretrained(model_id2, torch_dtype=torch.float16)
log.info("Model initialized.")

if torch.cuda.is_available():
    pipe2 = pipe2.to("cuda")
    log.info("Model moved to GPU.")
else:
    log.info("GPU not available. Using Mac processor.")
    pipe2 = pipe2.to("mps")

if __name__ == '__main__':
    log.info('Init complete.')
