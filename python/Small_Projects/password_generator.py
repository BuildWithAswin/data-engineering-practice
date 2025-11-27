import string, random
_sysrand = random.SystemRandom()

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True,use_punctuation=True, avoid_ambigious=True):
    if length < 6:
        raise ValueError("Length must be greater than 6")
    pools = []
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_digits:
        pools.append(string.digits)
    if use_punctuation:
        pools.append('!@#$%&*()=+[]{};<>?')
    if avoid_ambigious:
        ambiguous = ['I', 'l', '0', 'o']
        pools = [''.join(ch for ch in pool if ch not in ambiguous) for pool in pools]
    if not pools:
        raise ValueError("At lease one character type must be enabled")
    
    pass_chars = [_sysrand.choice(pool) for pool in pools]
    full_chars = ''.join(pools) 
    remaining = length - len (pass_chars)
    if remaining > 0:
        pass_chars += [_sysrand.choice(full_chars) for _ in range(remaining)]
        _sysrand.shuffle(pass_chars)
        return ''.join(pass_chars)
    

print(generate_password(length=12))