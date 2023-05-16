
# pip install aspose.slides
import aspose.slides as slides

# Create a new presentation
with slides.Presentation() as presentation:
    
    # Access the default slide
    slide = presentation.slides[0]
    
    # Save the presentation
    presentation.save("presentation.ppt", slides.export.SaveFormat.PPTX)
