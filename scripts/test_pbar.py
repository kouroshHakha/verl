from verl.trainer.ppo.ray_trainer import ProgressBar    
import time

with ProgressBar(200, max_event_length=15) as pbar:
    for epoch in range(1, 3):
        for step in range(1, 51):
            pbar.update(step, epoch, "Generating responses ...")
            time.sleep(0.5)
            # Your code here
            pbar.update(step, epoch, "Computing loss ...", increment=True)
            time.sleep(0.1)
