import time
import pyautogui

def minimize_vscode_and_open_chrome():
    # Aguarda 5 segundos
    time.sleep(5)

    # Simula o atalho de teclado para minimizar a janela do VS Code
    pyautogui.hotkey('win', 'down')
    time.sleep(5)

    # Pressiona a tecla do Windows para abrir o menu Iniciar
    pyautogui.press('win')

    # Aguarda um momento para o menu Iniciar abrir
    time.sleep(5)

    # Digita "Google Chrome" no menu Iniciar
    pyautogui.typewrite('Google Chrome')
    time.sleep(5)
    pyautogui.hotkey('win', 'up')
    
    time.sleep(5)

    # Pressiona Enter para abrir o Google Chrome
    pyautogui.press('enter')
    time.sleep(10)

    # Digita "gmail.com" na barra de endereço do Google Chrome
    pyautogui.typewrite('gmail.com')
    pyautogui.press('enter')
    time.sleep(12)
    
    # Loop para repetir a ação 10 vezes
    for _ in range(10):
        # Clica no botão "Escrever" para abrir a barra de e-mail
        pyautogui.click(x=83, y=188, duration=3)  
        time.sleep(5)
        
        # Digita os endereços de e-mail no campo "Para"
        destinatarios = ['concei', 'eduarda', 'carina', 'vasco', 'scout', 'daniela', 'hello', 'marcela']
        for destinatario in destinatarios:
            pyautogui.typewrite(destinatario)
            time.sleep(1)
            pyautogui.press('enter')  # Pressiona Enter para separar os destinatários
            time.sleep(1)

        pyautogui.click(x=1303, y=686, duration=3)
        pyautogui.typewrite('Jonathan Silva Desenvolvedor Full-Stack')

        pyautogui.click(x=1199, y=1060, duration=3)
        time.sleep(2)

        pyautogui.mouseDown(button='right', x=196, y=219)
        pyautogui.dragTo(514, 471, duration=2, button='right')
        pyautogui.mouseUp(button='right')

        # Copia o texto selecionado
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)

        # Clica no local onde deseja colar o texto
        pyautogui.click(x=1405, y=584, duration=3)
        time.sleep(2)

        # Cole o texto copiado
        pyautogui.hotkey('ctrl', 'v')

        pyautogui.click(x=1449, y=1011, duration=3)
        time.sleep(2)
        pyautogui.click(x=580, y=433, duration=3)
        file1_location = (580, 433)  # Exemplo de coordenadas do primeiro arquivo
        file2_location = (673, 288)  # Exemplo de coordenadas do segundo arquivo
        pyautogui.keyDown('ctrl')
        time.sleep(1)
        pyautogui.click(file2_location)
        time.sleep(1)
        pyautogui.keyUp('ctrl')

        pyautogui.click(x=1193, y=695, duration=3)

        pyautogui.click(x=1287, y=1009, duration=3)

if __name__ == "__main__":
    minimize_vscode_and_open_chrome()
