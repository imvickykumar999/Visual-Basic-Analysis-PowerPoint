
import aspose.slides as slides

# Load a presentation
with slides.Presentation("PPTs/presentation.ppt") as presentation:
    
    # Check if presentation contains VBA Project
    if presentation.vba_project is not None:
        
        # Print each module
        for module in presentation.vba_project.modules:
            print(module.name)
            print(module.source_code)
    else:
        print('Presentation does NOT contains VBA Project')
