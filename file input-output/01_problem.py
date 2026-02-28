with open("poem.txt") as f:
    content=f.read()
    if("twinkle"  in content ):
        print("the word twinkle is present in text")
    else:
        print("the word twinkle is not present in text")
      