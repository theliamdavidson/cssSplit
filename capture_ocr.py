import cv2 as cv
import pytesseract
from PIL import Image
import logging
from random import randint

def capture_from_image():
    cap = cv.VideoCapture(0)
    while cap.isOpened():
        
        ret, frame = cap.read()
        if ret is False:
            return(ret)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
   
        cap.release()
        cv.destroyAllWindows()
        return gray

def capture_decoder():#cd():
    '''
        Will return a value in the form of [string, string].
        The return when a value isn't found is ["vessel not found", "0.00"]
    '''
    logging.basicConfig(filename="blankoutput.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
    logger = logging.getLogger()
    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    searching_for_text = True
    iterator = 0
    capture_decoder_return = ["vessel not found", "0.00"]
    while searching_for_text:
        img1 = capture_from_image()
        if img1 is False:
            return("Camera is not detected")
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'    
        try:
            text = pytesseract.image_to_string(Image.fromarray(img1))
        except:
            text = "Camera may be disconnected"
        logger.info(text)
        
        split_txt = text.split("\n")
        
        #return(split_txt)
        matchespi = [match for match in split_txt if "PI" in match]
        matchespi += [match for match in split_txt if "Pi" in match]
        matchespi += [match for match in split_txt if "Pl" in match]
        matchespi += [match for match in split_txt if "P1" in match]
        matchespi += [match for match in split_txt if "PL" in match]
        matchesvf = [match for match in split_txt if "Vol Flow" in match]
        array_lengthpi = len(matchespi)
        array_lengthvf = len(matchesvf)

        if (array_lengthvf > 0) or (array_lengthpi > 0):
            if array_lengthvf > 0:
                for items in matchesvf:
                    matches = items.split()
                name = "VF"
                array_lengthvf = len(matches)
                #if array_lengthvf >= 5:
                    #logging.debug("long vascular flow input", matchesvf, "end of the long input")
            elif array_lengthpi > 0:
                for items in matchespi:
                    matches = items.split()
                array_lengthpi = len(matches)
                name = "PI"
                #if array_lengthpi >= 3:
                    #logging.debug("long pulsatility index input", matchespi, "end of the long input")
            for items in matches:
                try:
                    float(items)
                    capture_decoder_return = [name, items]
                except:
                    print()
            return(capture_decoder_return)
        else:
            if iterator <= 2:
                iterator += 1
                print(text)
                print(iterator)
            else:
                return(["vessel not found", "0.00"])            
            # thinking about changing how the blank return is formatted
        

def cd():
    '''
        Debug version of the ocr program, without the overhead required from the main program
        Will return a value in the form of [string, string].
    '''
    names =[ "PI", "VF" ]
    will_loop = randint(0,1)
    return([names[will_loop],str(randint(1, 450)/4.5)])
    

if __name__ == "__main__":
    while True:
        return_val = capture_decoder()
        #logging.info
        print("return_val = ", return_val)