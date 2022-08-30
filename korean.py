from PIL import Image, ImageDraw, ImageFont

#이미지로 출력할 글자 및 폰트 지정
draw_text='''기운내 오미선
할수 있어'''
font = ImageFont.truetype("/home/pi/printing-house/font/D2Coding-Ver1.3.2-20180524-ligature.ttf",25)

#이미지 사이즈 지정
text_width = 100*3
text_height = 500

#이미지 객체 생성
canvas = Image.new('RGB', (text_width, text_height), "white")

#가운데에 그리기
draw = ImageDraw.Draw(canvas)
w, h = font.getsize(draw_text)
#w, h = font.getbbox(draw_text)
#w, h = font.getlength(draw_text)
print(w)
print(h)
draw.text(((text_width-w)/2.0,(text_height-h)/2.0), draw_text, 'black', font)
#draw.text(((150),(250)), draw_text, 'black', font)

#png로 저장 및 출력해서 보기
canvas.save('1'+'.png',"PNG")

#canvas.show()

