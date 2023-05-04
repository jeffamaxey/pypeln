import pypeln as pl
from tqdm import tqdm
import time

total = 300_000


def f(x):
    i = len(range(500_000))
    return x * 2


stage = range(total)
stage = pl.process.map(f, stage, workers=8, maxsize=2000)
stage = tqdm(stage, total=total, desc="pipeline")

pl.process.run(stage)
