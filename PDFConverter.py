from xhtml2pdf import pisa             # import python module

# Define your data
outputFilename = "test.pdf"
outputDirectory = "C:\\Users\\Circle\\PycharmProjects\\TemplateDocsGenerator\\GeneratedPDF\\"
#TODO make a config file where user can set all their variables
# Utility function
def GenerateFilePath(outputFilename):

    return outputDirectory+outputFilename

def convertHtmlToPdf(sourceHtml,outputFilename):
    # open output file for writing (truncated binary)
    resultFile = open(GenerateFilePath(outputFilename), "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            sourceHtml,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

    # close output file
    resultFile.close()                 # close output file

    # return True on success and False on errors
    return pisaStatus.err