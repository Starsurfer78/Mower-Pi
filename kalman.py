# kalman.py

class KalmanFilter:
    def __init__(self, q, r, x0, p0):
        self.q = q
        self.r = r
        self.x = x0
        self.p = p0

    def update(self, measurement):
        # Vorhersage-Phase
        x_pred = self.x
        p_pred = self.p + self.q

        # Update-Phase
        k = p_pred / (p_pred + self.r)
        self.x = x_pred + k * (measurement - x_pred)
        self.p = (1 - k) * p_pred