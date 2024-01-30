# Scanner/Scanner.py

def Scanner(s=''):
    exp = input(s)
    if not exp.strip():
        return None
    try:
        return eval(exp)
    except Exception as e:
        error = f"\033[1m\033[38;2;255;122;136m{type(e).__name__}\033[0m"
        print(f"{error}: {e}")
