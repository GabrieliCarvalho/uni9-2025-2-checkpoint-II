

from canais import WhatsApp, Telegram, Facebook, Instagram, ICanal
from mensagens import MensagemTexto, MensagemVideo, MensagemFoto, MensagemArquivo


from typing import List

def rodar_demonstracao():
    """Função que roda todos os testes pré-definidos."""
    
    print("=" * 40)
    print("### INICIANDO DEMONSTRAÇÃO AUTOMÁTICA (TESTE) ###")
    print("=" * 40 + "\n")


    canal_whatsapp = WhatsApp()
    canal_telegram = Telegram()
    canal_facebook = Facebook()
    canal_instagram = Instagram()


    msg_texto = MensagemTexto("Olá! Este é o checkpoint II de POO.")
    msg_foto = MensagemFoto("Foto da equipe!", "equipe.jpg")
    msg_video = MensagemVideo("Tutorial de Python", "tutorial.mp4", "video/mp4", 300)
    msg_arquivo = MensagemArquivo("Documento de Requisitos", "requisitos.pdf", "application/pdf")

    # A. WhatsApp
    canal_whatsapp.enviar(msg_texto, "+5511999998888")

    # B. Telegram
    canal_telegram.enviar(msg_video, "@usuario_telegram")
    
    # C. Facebook
    canal_facebook.enviar(msg_foto, "usuario.facebook.123")

    # D. Instagram
    canal_instagram.enviar(msg_arquivo, "outro.user.insta")
    
    print("\n### FIM DA DEMONSTRAÇÃO AUTOMÁTICA ###")
    print("=" * 40 + "\n")



def menu_interativo():
    """Função que mostra um menu para o usuário escolher o que enviar."""
    
    print("=" * 40)
    print("### INICIANDO MODO INTERATIVO ###")
    print("=" * 40 + "\n")

    canais = {
        "1": WhatsApp(),
        "2": Telegram(),
        "3": Facebook(),
        "4": Instagram()
    }

    while True:

        print("Para qual canal você quer enviar mensagem?")
        print("  1: WhatsApp")
        print("  2: Telegram")
        print("  3: Facebook")
        print("  4: Instagram")
        print("  0: Sair")
        
        escolha_canal = input("Escolha o canal (0 para Sair): ")

        if escolha_canal == "0":
            print("\nObrigado por usar o sistema! Saindo...")
            break
        
        if escolha_canal not in canais:
            print("\nOpção inválida! Tente novamente.\n")
            continue
        

        canal_selecionado = canais[escolha_canal]
        

        destinatario = input(f"Digite o destinatário para {canal_selecionado.__class__.__name__}: ")

        print("\nQual tipo de mensagem?")
        print("  1: Texto")
        print("  2: Foto")
        print("  3: Vídeo")
        print("  4: Arquivo")
        
        escolha_tipo = input("Escolha o tipo de mensagem: ")
        texto_base = input("Digite o texto principal da mensagem: ")
        
        mensagem_para_enviar = None


        if escolha_tipo == "1":
            mensagem_para_enviar = MensagemTexto(texto_base)
        elif escolha_tipo == "2":

            mensagem_para_enviar = MensagemFoto(texto_base, "foto_interativa.jpg")
        elif escolha_tipo == "3":
            mensagem_para_enviar = MensagemVideo(texto_base, "video_interativo.mp4", "video/mp4", 60)
        elif escolha_tipo == "4":
            mensagem_para_enviar = MensagemArquivo(texto_base, "documento_interativo.pdf", "app/pdf")
        else:
            print("\nTipo inválido. Enviando como texto simples.")
            mensagem_para_enviar = MensagemTexto(texto_base)
            

        try:
            canal_selecionado.enviar(mensagem_para_enviar, destinatario)
            print("--- Mensagem enviada com sucesso! --- \n")
        except Exception as e:
            print(f"Erro ao enviar: {e}\n")



if __name__ == "__main__":

    rodar_demonstracao()
    

    input("... Pressione ENTER para continuar para o Menu Interativo ...")
    

    menu_interativo()
