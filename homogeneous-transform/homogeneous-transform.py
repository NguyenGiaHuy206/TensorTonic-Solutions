import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here
    T = np.asarray(T, dtype=float)
    points = np.asarray(points, dtype=float)
    single_point = points.ndim == 1
    if single_point:
        points = points.reshape(1, 3)

    ones = np.ones((points.shape[0], 1))
    points_h = np.hstack([points, ones])
    transformed_h = (T @ points_h.T).T
    transformed = transformed_h[:, :3]

    if single_point:
        return transformed[0].tolist()

    return transformed.tolist()
    pass