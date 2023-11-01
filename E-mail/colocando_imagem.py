import aspose.words as aw

# Load the license
wordAddPicture = aw.License()
wordAddPicture.set_license("/Program Files/M-Files/23.10.13060.5/Bin/anycpu/Aspose.Total.lic")

# Load Word document
AddImagesToWordDOC =aw.Document("CheckList_Diário_Life_T.docx")

# Instantiate DocumentBuilder object
imageWriter = aw.DocumentBuilder(AddImagesToWordDOC)

# Move to last paragraph
imageWriter.move_to(AddImagesToWordDOC.last_section.body.last_paragraph)

# Insert the image
imageAsLinkToFile = imageWriter.insert_image("SampleImage.jpg")

# Save As DOCX
AddImagesToWordDOC.save("output.docx")

print ("Image added successfully to the Word document")