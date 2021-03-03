import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  
  mat = np.array(list).reshape((3,3))

  calculations={
    'mean':[np.mean(mat,axis=0).tolist(), np.mean(mat,axis=1).tolist(), np.mean(mat).tolist()],
    'variance':[np.var(mat,axis=0).tolist(), np.var(mat,axis=1).tolist(), np.var(mat).tolist()],
    'standard deviation':[np.std(mat,axis=0).tolist(), np.std(mat,axis=1).tolist(), np.std(mat).tolist()],
    'max':[np.max(mat,axis=0).tolist(), np.max(mat,axis=1).tolist(), np.max(mat).tolist()],
    'min':[np.min(mat,axis=0).tolist(), np.min(mat,axis=1).tolist(), np.min(mat).tolist()],
    'sum':[np.sum(mat,axis=0).tolist(), np.sum(mat,axis=1).tolist(), np.sum(mat).tolist()]
  }
  
  return calculations