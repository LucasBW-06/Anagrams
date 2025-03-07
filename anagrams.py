def count_anagrams(array): # função que conta a quantidade de anagramas numa lista
    aux = [''.join(sorted(list(i))) for i in array] # faz uma lista auxiliar das palavras da lista array com suas letras ordenadas alfabéticamente
    return max([aux.count(i) for i in aux]) # faz uma lista da quantidade de vezes que cada elemento da lista aux aparece na lista aux e retorna o maior número

num = int(input()) # recebe N número inteiro
words = [input() for _ in range(num)] # recebe lista de N strings

eq_word_n = count_anagrams(words) # conta a quantidade de anagramas
print(eq_word_n)