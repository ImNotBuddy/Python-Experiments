import PyPDF2
import os

dirname = os.path.dirname(__file__)

pdfFolder = os.path.join(dirname, 'PDF')
outputFolder = os.path.join(dirname, 'Output')

def pdfToText(fileName):
  target = os.path.join(pdfFolder, f"{fileName}.pdf")

  with open(target, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    pdf_text = ""
    
    for page in reader.pages:
      pdf_text += page.extract_text()
        
    file.close()
  
  return pdf_text

def saveText(textToSave, outputFileName):
  target = os.path.join(outputFolder, f"{outputFileName}.txt")
  with open(target, "w") as file:
    file.write(textToSave)
    file.close()

def main():
  try:
    fileName = str(input("Please enter the PDF file name that is in the PDF folder: "))
    outputFileName = str(input("Please enter what you would like the output file saved as: "))

    textToSave = pdfToText(fileName)
    saveText(textToSave, outputFileName)

    print(f"\nSuccess, extracted the text from the pdf file {fileName}.pdf to {outputFileName}.txt!")
  except Exception as e:
    print("\nAn error has occured whilst executing the program: " + str(e))

  unused = input("\nPress enter to exit or close the window")


if __name__ == "__main__":
  main()