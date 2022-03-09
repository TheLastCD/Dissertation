import nlpaug.augmenter.char as nac
import nlpaug.augmenter.sentence as nas
import os



import nlpaug.augmenter.word as naw

text = 'The quick brown fox jumped over the lazy dog'
back_translation_aug = naw.BackTranslationAug(
    from_model_name='transformer.wmt19.en-de',
    to_model_name='transformer.wmt19.de-en')
quaback_translation_aug.augment(text)