
import aspose.slides as slides

# Create a new presentation
with slides.Presentation() as pres:
    # Get reference of slides
    slds = pres.slides

    # Loop through layout slides
    for i in range(len(pres.layout_slides)):
        # Add an empty slide to the slides collection
        slds.add_empty_slide(pres.layout_slides[i])
        
    # Do some work on the newly added slide

    # Save the PPTX file to the Disk
    pres.save("PPTs/presentation.ppt", slides.export.SaveFormat.PPTX)
