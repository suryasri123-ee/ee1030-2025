import subprocess

def get_points():
    result = subprocess.run(["./generate_points"], capture_output=True, text=True)
    points = []
    for line in result.stdout.strip().split("\n"):
        x, y = map(float, line.split())
        points.append((x, y))
    return points

if __name__ == "__main__":
    pts = get_points()
    print("Points:", pts)

