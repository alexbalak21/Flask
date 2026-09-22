from functools import wraps

# 1. DECORATOR WITH @WRAPS
def with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# 2. DECORATOR WITHOUT @WRAPS
def without_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# --- Testing the difference ---

@with_wraps
def say_hello():
    """Greet the user."""
    pass

@without_wraps
def say_goodbye():
    """Bid farewell."""
    pass

print("With @wraps:")
print(say_hello.__name__)    # Output: say_hello
print(say_hello.__doc__)     # Output: Greet the user.

print("Without @wraps:")
print(say_goodbye.__name__)  # Output: wrapper (Lost identity!)
print(say_goodbye.__doc__)   # Output: None    (Lost documentation!)
