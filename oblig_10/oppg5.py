

def rsa_cryptate(m, e, n):
    return (m ** e) % n

def rsa_decrypt(c, d, n):
    return (c ** d) % n

def valid(x,y, key):
    if x == rsa_decrypt(y, key[0], key[1]):
        return "Valid"
    else:
        return "Not valid"
    
def msg_attack(signature_1, signature_2, n):
    return (signature_1[0]*signature_2[0])%n, (signature_1[1]*signature_2[1])%n

if __name__ == '__main__':
    
    n = 437
    b = 13
    p = 23
    q = 19
    a = 61

    bob_public_key = [b,n]
    bob_priv_key = [a,n]
    
    alice_public_key = [283, 731]
    alice_priv_key = [19, 731]
    
    # 1)
    print("1)")
    print(valid(78,394, bob_public_key)) # valid
    print(valid(123,289, bob_public_key)) # valid
    
    
    # 3)
    valid_msg = msg_attack([38,171], [97,337], n)
    
    print(f"\n3)\nValid msg: {valid_msg}\nSjekker om den er valid:")
    print(valid(valid_msg[0], valid_msg[1], bob_public_key)) # valid
    
    
    # 4)
    print("\n4)\nSignerer og krypterer melding 109 som sendes til Bob\nBob sjekker at den er fra Alice\n")
    alice_signature = rsa_decrypt(109, alice_priv_key[0], alice_priv_key[1])
    
    bob_crypt = [rsa_cryptate(109, bob_public_key[0], bob_public_key[1]), 
           rsa_cryptate(alice_signature, bob_public_key[0], bob_public_key[1])]
    
    print(f"Kryptert melding til bob {bob_crypt}")
    
    bob_decrypt = [rsa_decrypt(bob_crypt[0], bob_priv_key[0], bob_priv_key[1]), rsa_decrypt(bob_crypt[1], bob_priv_key[0], bob_priv_key[1])]
    
    print(f"Dekryptert melding som bob mottar {bob_decrypt}")

    print("Validert med Alice sin public key: ", valid(bob_decrypt[0], bob_decrypt[1], alice_public_key))    