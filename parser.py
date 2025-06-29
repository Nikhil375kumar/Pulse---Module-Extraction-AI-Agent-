# parser.py
def parse_modules(content_blocks):
    modules = {}
    current_module = None

    for block in content_blocks:
        if block.istitle() or block.istitle():  # crude way to detect titles
            current_module = block
            modules[current_module] = []
        elif current_module:
            modules[current_module].append(block)
    
    return modules

# Add this to test the function directly
if __name__ == "__main__":
    sample_data = [
        "Account Settings",
        "How to change username",
        "How to delete account",
        "Content Sharing",
        "Creating Reels",
        "Sharing Reels"
    ]
    
    parsed = parse_modules(sample_data)
    from pprint import pprint
    pprint(parsed)
