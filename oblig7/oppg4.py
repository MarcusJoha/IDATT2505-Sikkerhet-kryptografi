
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"

def crack(text):
    sentences = []
    for i in range(0, len(alpha)):
        sentence = ""
        for j in text:
            num = (i+alpha.find(j))%29
            sentence += alpha[num]
        sentences.append(sentence)
    return sentences



if __name__ == "__main__":
    
    msg = "YÆVFBVBVFRÅVBV"
    
    sentences = crack(msg)
    
    i = 0
    for sentence in sentences:
        print(i,":", sentence)
        i += 1
    
# Svar: Hjernen er alene, nøkkel: 12