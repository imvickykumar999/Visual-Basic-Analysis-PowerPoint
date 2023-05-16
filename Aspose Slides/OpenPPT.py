
import aspose.slides as slides

# Open presentation
with slides.Presentation("presentation.ppt") as presentation:
    
    # Access the default slide
    slide = presentation.slides[0]
    
    # Save the presentation
    presentation.save("presentation_0.ppt", slides.export.SaveFormat.PPT)
