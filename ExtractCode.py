
# https://python-pptx.readthedocs.io/en/latest/user/quickstart.html
# pip install python-pptx
from pptx import Presentation

path_to_presentation = 'PPTs/PlayFair Ciphertext Encryption.pptx'
prs = Presentation(path_to_presentation)
text_runs = []

for slide in prs.slides:
    for shape in slide.shapes:
        print(shape.textframe.paragraphs)
    print()
        # if not shape.has_textframe:
        #     continue
        # for paragraph in shape.textframe.paragraphs:
        #     for run in paragraph.runs:
        #         text_runs.append(run.text)

