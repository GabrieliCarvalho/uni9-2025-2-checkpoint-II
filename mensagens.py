from datetime import datetime
from abc import ABC, abstractmethod


class Mensagem(ABC):
    """
    Classe base abstrata para todas as mensagens.
    Define o "contrato" básico de uma mensagem.
    """
    def __init__(self, mensagem: str):

        self._mensagem_base = mensagem
        self._data_envio = datetime.now()
    
    @property
    @abstractmethod
    def conteudo(self) -> str:
        """
        Método abstrato que DEVE ser implementado pelas classes filhas.
        Isso é a base do Polimorfismo: cada mensagem vai se "renderizar"
        de uma forma diferente.
        """
        pass


class MensagemTexto(Mensagem):
    """Implementação concreta para mensagens de texto simples."""
    def __init__(self, mensagem: str):

        super().__init__(mensagem)
    
    @property
    def conteudo(self) -> str:

        return f"[{self._data_envio.strftime('%H:%M')}] {self._mensagem_base}"


class MensagemComArquivo(Mensagem):
    """
    Classe base para mensagens que contêm um arquivo (Foto, Vídeo, Documento).
    Ela herda de Mensagem e adiciona novos atributos e comportamentos.
    """
    def __init__(self, mensagem: str, arquivo: str, formato: str):
        super().__init__(mensagem)
        self._arquivo = arquivo  
        self._formato = formato  
    
    @property
    @abstractmethod
    def conteudo(self) -> str:
        """Força as classes filhas a implementarem este método."""
        pass


class MensagemFoto(MensagemComArquivo):
    """Implementação para mensagens com Foto."""
    def __init__(self, mensagem: str, arquivo: str, formato: str = "image/jpeg"):
        super().__init__(mensagem, arquivo, formato)
    
    @property
    def conteudo(self) -> str:

        return (f"[{self._data_envio.strftime('%H:%M')}] {self._mensagem_base}\n"
                f"\t[FOTO: {self._arquivo} (Formato: {self._formato})]")

class MensagemVideo(MensagemComArquivo):
    """Implementação para mensagens com Vídeo."""
    def __init__(self, mensagem: str, arquivo: str, formato: str, duracao_seg: int):
        super().__init__(mensagem, arquivo, formato)
        self._duracao = duracao_seg  
    
    @property
    def conteudo(self) -> str:

        return (f"[{self._data_envio.strftime('%H:%M')}] {self._mensagem_base}\n"
                f"\t[VIDEO: {self._arquivo} (Formato: {self._formato}, Duração: {self._duracao}s)]")

class MensagemArquivo(MensagemComArquivo):
    """Implementação para mensagens com Arquivo genérico."""
    def __init__(self, mensagem: str, arquivo: str, formato: str):
        super().__init__(mensagem, arquivo, formato)
    
    @property
    def conteudo(self) -> str:

        return (f"[{self._data_envio.strftime('%H:%M')}] {self._mensagem_base}\n"
                f"\t[ARQUIVO: {self._arquivo} (Formato: {self._formato})]")