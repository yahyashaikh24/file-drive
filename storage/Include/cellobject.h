import os
import comtypes.client
from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image, ImageFont, ImageDraw

mimes = ['msword','msword','vnd.openxmlformats-officedocument.wordprocessingml.document','vnd.openxmlformats-officedocument.wordprocessingml.template','vnd.ms-word.document.macroEnabled.12','vnd.ms-word.template.macroEnabled.12','vnd.ms-excel','vnd.ms-excel','vnd.ms-excel','vnd.openxmlformats-officedocument.spreadsheetml.sheet','vnd.openxmlformats-officedocument.spreadsheetml.template','vnd.ms-excel.sheet.macroEnabled.12','vnd.ms-excel.template.macroEnabled.12','vnd.ms-excel.addin.macroEnabled.12','vnd.ms-excel.sheet.binary.macroEnabled.12','vnd.ms-powerpoint','vnd.ms-powerpoint','vnd.ms-powe