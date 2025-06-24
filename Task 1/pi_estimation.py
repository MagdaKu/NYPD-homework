import random

def pi_estimation(N, k):
    points_inside = 0
    for i in range(1, N+1):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            points_inside += 1
        if i%k == 0:
            pi_est = (points_inside / i) * 4
            print(f"Iteration {i}: estimation: {round(pi_est, 3)}")
    return (points_inside / N) * 4
        

if __name__ == "__main__":
    pi_est = pi_estimation(N=10000, k=500)
    print(f"Final estimation of pi: {pi_est}")




