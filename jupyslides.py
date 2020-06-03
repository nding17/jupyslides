import ipywidgets as widgets
import os
import natsort 
from IPython.display import Image

class jupyslides:

  def __init__(self, 
               slides_path,
               default_width=720,
               height_to_width_ratio=810/1080):

    self._default_width = default_width
    self._default_height = default_width*height_to_width_ratio
    self._slides = self._read_slides(slides_path)

  def _read_slides(self, slides_path):

    slide_names = [sn for sn in os.listdir(slides_path) if any(map(str.isdigit, sn))]

    try:
      slide_names_sorted = natsort.natsorted(slide_names, reverse=False)
    except ValueError as e:
      print(f'Error: {e}, please make sure the images have numbers to indicate the order')
      raise

    slides = [Image(filename=f'{slides_path}/{slide_name}', 
                    width=self._default_width,
                    height=self._default_height) \
              for slide_name in slide_names_sorted]

    return slides 

  def _current_slide(self,
                     zoom, 
                     page):

    current_slide = self._slides[page-1]
    current_slide.width = self._default_width*zoom
    current_slide.height = self._default_height*zoom
    return current_slide

  def slideshow(self,
                min_zoom=0.6,
                max_zoom=2,
                step_zoom=0.2):

    return widgets.interact(self._current_slide, 
                            page=widgets.IntSlider(min=1, 
                                                   max=len(self._slides), 
                                                   step=1),
                            zoom=widgets.FloatSlider(value=1, 
                                                     min=min_zoom, 
                                                     max=max_zoom, 
                                                     step=step_zoom))