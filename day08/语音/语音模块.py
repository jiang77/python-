from win32com.client import constants
import os
import win32com.client
import pythoncom

class SpeechRecognition:
    def _init_(self, wordsToAdd):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.listener = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
        self.context = self.lister.CreatRecoContext()
        self.grammar = self.context.CreatRecoGrammar()
        self.grammar.DictationSetState(0)
        self.wordRule = self.grammar.Rules.ADD("wordRule",constants.SRATopLevel+constants.SRADynamic, 0)
        self.wordRule.Clear()
        [self.wordRule.InitialState.AddWordTransition(None, word) for word in wordsToAdd]
        self,grammar.Rules.Commit()
        self.grammar.CmcSetRuleState("wordsRule", 1)
        self,grammar.Rules.Commit()
        self.eventHandler = ContextEvents(self.context)
        self.say("Started successfully")
    def say(self, phrase):
        self.speaker.Speak(phrase)
class ContextEvents(win32com.client.getevents("SAPI.SpSharedRecoContext")):
    def OnRecognition(self, StreamNumber, StreamPosition, RecognitionType, Result):
        newResult = win32com.client.Dispatch(Result)
        print("说：", newResult.PhraseInfo.GetText())
        if s == "记事本":
            os.system("txt")


if __name__ == '__mian__':
    wordsToAdd = ["关机", "取消关机", "记事本", "图画板", "写字板", "设置","关闭记事本"]
    SpeechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.pumnWaitingMessages()