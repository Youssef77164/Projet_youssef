import os
from os import listdir
from os.path import isfile, join
import wave
import librosa
import soundfile as sf




#Affiche le fichier présent dans le dossier "Import_Audio et créer une variable dessus"
Audio_to_treat = listdir('Import_Audio')[0]
print("Le fichier audio à traiter se nomme : {}".format(Audio_to_treat))

#---------------------------------------------------------------------------------------------------------

#Import du fichier audio
filename = 'Import_Audio/'+Audio_to_treat
y, sr = librosa.load(filename)


#---------------------------------------------------------------------------------------------------------
#Conversion audio en .WAV + enregistrement + change file source

if ".wav" not in Audio_to_treat :
    sf.write('Import_Audio/{}.wav'.format(Audio_to_treat.replace(".","")), y, sr)
    os.remove('Import_Audio/'+Audio_to_treat)
    Audio_to_treat = listdir('Import_Audio')[0]
    print("Le nouveau fichier audio à traiter se nomme : {}".format(Audio_to_treat))
else : 
    print("Le fichier à traiter se nomme toujours {}".format(Audio_to_treat))
