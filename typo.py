import re
from collections import Counter

# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import string

# def words(text): return re.findall(r'\w+', text.lower())

import sqlite3

class TyphoCorrection:
    def __init__(self):
        conn = sqlite3.connect('KBBI.db')
        # print("Opened database successfully");

        self.word_list = []

        cursor = conn.execute("SELECT katakunci from datakata")
        for row in cursor:
            self.word_list.append(row[0][:-1])
            # print(str(row[0]) + ' - ' + row[1])

        # print("Operation done successfully");
        conn.close()

        self.WORDS = Counter(self.word_list)

    def P(self, word): 
        "Probability of `word`."
        N=sum(self.WORDS.values())
        return self.WORDS[word] / N

    def correction(self, word): 
        "Most probable spelling correction for word."
        return max(self.candidates(word), key=self.P)

    def candidates(self, word): 
        "Generate possible spelling corrections for word."
        return (self.known([word]) or self.known(self.edits1(word)) or [word])

    def known(self, words): 
        "The subset of `words` that appear in the dictionary of WORDS."
        return set(w for w in words if w in self.WORDS)

    def edits1(self, word):
        "All edits that are one edit away from `word`."
        letters    = 'abcdefghijklmnopqrstuvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def ocr(self,image_name):
        # load the example image and convert it to grayscale
        image = cv2.imread(image_name)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # check to see if we should apply thresholding to preprocess the
        # image
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # write the grayscale image to disk as a temporary file so we can
        # apply OCR to it
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)

        # load the image as a PIL/Pillow image, apply OCR, and then delete
        # the temporary file
        text = pytesseract.image_to_string(Image.open(filename), lang="ind")
        os.remove(filename)

        # show the output images
        # cv2.imshow("Image", image)
        # cv2.imshow("Output", gray)
        s = text.split()
        # print(known(edits(s)))
        # print(word_list.count('zone'))
        res = "Koreksi : <br>"
        table = str.maketrans({key: None for key in string.punctuation})

        for i in s :
            stripped = i.translate(table).lower()
            res += i + ':' + self.correction(stripped) + ' <br>'

        return res