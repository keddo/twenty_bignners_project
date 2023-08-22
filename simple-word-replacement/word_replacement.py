def replace_word():
    # Sentnce
    strg = "HI guys, I am Kedo, HI HI HI HI"
    
    print(f"Here is the sentence: {strg}")
    # Prompt the user the word to be replaced and replacement
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word to replacement: ")
    print(strg.replace(word_to_replace, word_replacement))