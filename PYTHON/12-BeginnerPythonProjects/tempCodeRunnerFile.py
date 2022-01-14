rs used
      # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
      print('You have used these letters: ', ' '.join(used_letters))

      # what current word is (ie W - R D)
      word_list = [letter if letter in used_letters else '-' for letter in word]
      print('Current word: ', ' '.join(word_list))

      user_letter = input('Guess a letter: ').upper()
      if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
          word_letters.remove(user_letter)

      elif user_letter in used_letters:
        print('You have already used that character. Please try again.')

      else:
        print('Inval