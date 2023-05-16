
import PPT_Fun as ppt

save_path = 'static/Collection.pptx'

ppt.set_title(0, save_path)
ppt.bullet_level(1, save_path)
ppt.change_fonts(2, save_path)
ppt.set_image(3, save_path)
ppt.shape_steps(4, save_path)
ppt.set_tables(5, save_path)
ppt.extract_code(save_path)
