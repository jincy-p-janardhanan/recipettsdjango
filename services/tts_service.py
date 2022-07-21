from gtts import gTTS
from base.models import RecipeInstruction
from pydub import AudioSegment
import os

def getRecipeAudio(recipe_instructions, user_id = 0, language = 'en'):
    
    for i in recipe_instructions:
        myobj = gTTS(text=i.instruction, lang=language, slow=False)
        myobj.save('media/%d_%d_%d.mp3' % (user_id, i.r_id_id, i.seq_no))

    recipe_audio = AudioSegment.from_file('media/%d_%d_1.mp3' % (user_id, i.r_id_id), 'mp3')
    try:
        os.remove('media/%d_%d_1.mp3' % (user_id, i.r_id_id))
    except:
        print('media/%d_%d_1.mp3 not deleted.' % (user_id, i.r_id_id))

    recipe_instructions = recipe_instructions[1:]

    for i in recipe_instructions:

        instruction = AudioSegment.from_file('media/%d_%d_%d.mp3' % (user_id, i.r_id_id, i.seq_no), 'mp3')

        hours, minutes, seconds = [int(x) for x in i.time_stamp.split(':')]
        milliseconds = (seconds + minutes*60 + hours*3600) * 1000
        silence = AudioSegment.silent(duration=milliseconds)
        recipe_audio += silence + instruction
        try:
            os.remove('media/%d_%d_%d.mp3' % (user_id, i.r_id_id, i.seq_no))
        except:
            print('media/%d_%d_%d.mp3' % (user_id, i.r_id_id, i.seq_no))

    recipe_audio.export("media/recipe_%d.mp3"%(i.r_id_id))

    return "recipe_%d.mp3"%(i.r_id_id)

